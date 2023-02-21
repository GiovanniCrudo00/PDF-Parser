import subprocess
import jinja2
import pdfkit
from datetime import datetime
from src.ReadFromDb import read_from_db


#
# Prevelo il path assoluto della macchina
#

output = subprocess.check_output(['pwd'])
str_abs = output.decode('utf8', errors='strict').strip() # Path da concatenare alla cartella delle immagini
output = subprocess.check_output(['which','wkhtmltopdf'])
str_wkhtmltopdf = output.decode('utf8', errors='strict').strip() # Path della libreria wkhtmltopdf

azienda = "DFG" # Selezionatore azienda

#
# Popolo i campi per la creazione del pdf
#

data_nome_pdf = datetime.today().strftime("%Y-%m-%d")
today_date = datetime.today().strftime("%d %b, %Y")
logo=str_abs+"/images/"+azienda+"_logo_intestato.jpeg"

#
# Prelevo da DB le spedizioni
#

# Ottengo una lista in cui ogni elemento è una lista che rappresenta la spedizione
lista_delle_spedizioni=read_from_db() 

#
# Genero un PDF per ogni spedizione
#
if(azienda == "DFG"):
    doc_id=0
    for i in lista_delle_spedizioni:
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

        context = {'logo':logo,'lettera_di_vettura': lettera_di_vettura, 'mittente_nome': mittente_nome, 
                'mittente_via': mittente_via, 'mittente_luogo': mittente_luogo,
                'destinatario_nome':destinatario_nome,'destinatario_via':destinatario_via,
                'destinatario_luogo':destinatario_luogo, 'contrassegno':contrassegno,
                'numero_colli':numero_colli, 'peso':peso, 'data': today_date, 
                'annotazioni':annotazioni, 'DDT':ddt}

        template_loader = jinja2.FileSystemLoader('/')
        template_env = jinja2.Environment(loader=template_loader)
        html_template = str_abs+'/templates/'+azienda+'Template.html'
        template = template_env.get_template(html_template)
        output_text = template.render(context)
        config = pdfkit.configuration(wkhtmltopdf=str_wkhtmltopdf)
        output_pdf = str_abs+'/output/'+str(data_nome_pdf)+'_'+str(doc_id)+'.pdf'
        options={"enable-local-file-access": ""}
        pdfkit.from_string(output_text, output_pdf, configuration=config, options=options)
        doc_id+=1
elif(azienda == "GENERALSERVICE"):
    pass 
else:
    print("... Nome azienda errato")