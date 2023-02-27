import subprocess
import jinja2
import pdfkit
from datetime import datetime
from ReadFromDb import read_from_db


#
# Prevelo il path assoluto della macchina
#

output = subprocess.check_output(['pwd'])
str_abs = output.decode('utf8', errors='strict').strip() # Path da concatenare alla cartella delle immagini
output = subprocess.check_output(['which','wkhtmltopdf'])
str_wkhtmltopdf = output.decode('utf8', errors='strict').strip() # Path della libreria wkhtmltopdf

azienda = "General_Service" # Selezionatore azienda

#
# Popolo i campi per la creazione del pdf
#

data_nome_pdf = datetime.today().strftime("%Y-%m-%d")
today_date = datetime.today().strftime("%d %b, %Y")
#
# Modificare i path qui sotto con i nomi delle risorse necessarie
#
#
logo=str_abs+"/images/GeneralService_logo_intestato.jpeg"
html_template = str_abs+'/templates/GeneralServiceTemplate.html'

#
# Prelevo da DB le spedizioni
#

# Ottengo una lista in cui ogni elemento è una lista che rappresenta la spedizione
lista_delle_spedizioni=read_from_db() 

# Inizializzo il file html del borderò
newHtmlFile = open('templates/temp.html', 'w')
newHtmlFile.write("""<body>""")
newHtmlFile.close()

# Inizializzo il dictionary di contesto del borderò
context_bord = {}

#
# Genero un PDF per ogni spedizione
#
doc_id=0
for i in lista_delle_spedizioni:
    causale = "Vendita"
    trasporto_a_mezzo = "Vettore"
    vettore = "T.M.S. Unipersonale S.r.l."
    aspetto_beni = "A Vista"
    lettera_di_vettura = i[0]
    mittente_nome = i[1]
    mittente_via = i[2]
    mittente_luogo = i[3]
    destinatario_nome = i[4]
    destinatario_via = i[5]
    destinatario_luogo = i[6]
    contrassegno = i[7]
    annotazioni= i[8]
    numero_colli = i[9]
    peso = i[10]
    ddt=i[11]
    data_inizio_trasporto = i[12]

    # Aggiungo al dictionary i valori di data e autista e logo che vanno agigunti una sola volta
    if(doc_id == 0):
        context_bord['data'] = today_date
        context_bord['autista'] = i[13]
        context_bord['logo'] = logo

    # Aggiungo al dictionary del context del borderò i campi necessari
    context_bord['mitt_'+str(doc_id)] = mittente_nome
    context_bord['dest_'+str(doc_id)] = destinatario_nome
    context_bord['viadest_'+str(doc_id)] = destinatario_via
    context_bord['luogo_'+str(doc_id)] = destinatario_luogo
    context_bord['colli_'+str(doc_id)] = numero_colli
    context_bord['peso_'+str(doc_id)] = peso
    context_bord['contrassegno_'+str(doc_id)] = contrassegno

    # Appendo all' HTML il placeholder
    newHtmlFile = open('templates/temp.html', 'a')
    newHtmlFile.write("""<a>"""+str(mittente_nome)+"""</a>""")
    newHtmlFile.close()

    context = {'logo':logo,'lettera_di_vettura': lettera_di_vettura, 'mittente_nome': mittente_nome, 
                'mittente_via': mittente_via, 'mittente_luogo': mittente_luogo,
                'destinatario_nome':destinatario_nome,'destinatario_via':destinatario_via,
                'destinatario_luogo':destinatario_luogo, 'contrassegno':contrassegno,
                'numero_colli':numero_colli, 'peso':peso, 'data': today_date, 
                'annotazioni':annotazioni, 'DDT':ddt, 'causale':causale,
                'trasporto_a_mezzo':trasporto_a_mezzo, 'vettore':vettore, 'aspetto_beni':aspetto_beni,
                'data_inizio_trasporto':data_inizio_trasporto}

    template_loader = jinja2.FileSystemLoader('/')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(html_template)
    output_text = template.render(context)
    config = pdfkit.configuration(wkhtmltopdf=str_wkhtmltopdf)
    output_pdf = str_abs+'/output/'+str(data_nome_pdf)+'_'+str(lettera_di_vettura)+'.pdf'
    options={"enable-local-file-access": ""}
    pdfkit.from_string(output_text, output_pdf, configuration=config, options=options)
    doc_id+=1

newHtmlFile = open('templates/temp.html', 'a')
newHtmlFile.write("""</body>""")
newHtmlFile.close()

print(context_bord)