import subprocess
import jinja2
import pdfkit
from datetime import datetime
from src.ReadFromDb import read_from_db, numero_spedizioni


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
bordero_template = str_abs+'/templates/bordero.html'

#
# Prelevo da DB le spedizioni
#
# In questa sezione mi aspetto che i dati mi vengano forniti nel seguente modo:
#   Una lista di spedizioni, una lista per ogni corriere
#   Un intero che indica il numero di spedizioni di ogni corriere
#       cioè il numero di spedizioni che hanno il destinatario diverso.
#
# Ottengo una lista in cui ogni elemento è una lista che rappresenta la spedizione
lista_delle_spedizioni=read_from_db() 
numero_sped = numero_spedizioni()


# Inizializzo il file html del borderò
newHtmlFile = open('templates/bordero.html', 'w')
newHtmlFile.write("""<!doctype html>\n""")
newHtmlFile.write("""<html lang="en">\n""")
newHtmlFile.write("""\t<head>\n""")
newHtmlFile.write("""\t\t<meta charset="utf-8">\n""")
newHtmlFile.write("""\t\t<meta name="viewport" content="width=device-width, initial-scale=1">\n""")
newHtmlFile.write("""\t\t<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">\n""")
newHtmlFile.write("""\t</head>\n""")
newHtmlFile.write("""\t<body>\n""")
newHtmlFile.write("""\t\t<div class="container-fluid">\n""")
newHtmlFile.write("""\t\t\t<div class="row">\n""")
newHtmlFile.write("""\t\t\t\t<div class="col-sm" style="text-align: left;"> <img style="height: 120px;" src={{logo}}></div>\n""")
newHtmlFile.write("""\t\t\t</div>\n""")
newHtmlFile.write("""\t\t\t<div class="row">\n""")
newHtmlFile.write("""\t\t\t\t<table class="table table-borderless">\n""")
newHtmlFile.write("""\t\t\t\t\t<thead>\n""")
newHtmlFile.write("""\t\t\t\t\t\t<tr>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope="col" style="border: 1px solid black;">Data: <a style="font-weight: lighter;">{{data}}</a></th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope="col"></th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope="col" style="border: 1px solid black;">Autista: <a style="font-weight: lighter;">{{autista}}</a></th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t</tr>\n""")
newHtmlFile.write("""\t\t\t\t\t</thead>\n""")
newHtmlFile.write("""\t\t\t\t</table>\n""")
newHtmlFile.write("""\t\t\t</div>\n""")
newHtmlFile.write("""\t\t\t<div class="row">\n""")
newHtmlFile.write("""\t\t\t\t<table class="table table-borderless">\n""")
newHtmlFile.write("""\t\t\t\t\t<thead>\n""")
newHtmlFile.write("""\t\t\t\t\t\t<tr>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Mittente</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Destinatario</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Via Destinatario</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Luogo</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Colli</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Peso</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Contrassegno</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t</tr>\n""")
newHtmlFile.write("""\t\t\t\t\t</thead>\n""")
newHtmlFile.write("""\t\t\t\t\t<tbody>\n""")
newHtmlFile.close()

# Inizializzo il dictionary di contesto del borderò
context_bord = {}
nome_corriere = ""
doc_id, somma_contrassegni, somma_peso, somma_colli, somma_spedizioni = 0, 0, 0, 0, 0


#
# Genero un PDF per ogni spedizione
#
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
    corriere = i[13]

    # Aggiungo al dictionary i valori di data e autista e logo che vanno agigunti una sola volta
    if(doc_id == 0):
        context_bord['data'] = today_date
        context_bord['autista'] = corriere
        nome_corriere = corriere
        context_bord['logo'] = logo

    # Aggiungo al dictionary del context del borderò i campi necessari
    context_bord['mitt_'+str(doc_id)] = mittente_nome
    context_bord['dest_'+str(doc_id)] = destinatario_nome
    context_bord['viadest_'+str(doc_id)] = destinatario_via
    context_bord['luogo_'+str(doc_id)] = destinatario_luogo
    context_bord['colli_'+str(doc_id)] = numero_colli
    context_bord['peso_'+str(doc_id)] = peso
    context_bord['contrassegno_'+str(doc_id)] = contrassegno

    somma_contrassegni+=int(contrassegno)
    somma_spedizioni+=1
    somma_peso +=int(peso)
    somma_colli +=int(numero_colli)

    # Appendo all' HTML il placeholder
    newHtmlFile = open('templates/bordero.html', 'a')
    newHtmlFile.write("""\t\t\t\t\t\t<tr>\n""")
    newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{mitt_"""+str(doc_id)+"""}}</a></td>\n""")
    newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{dest_"""+str(doc_id)+"""}}</a></td>\n""")
    newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{viadest_"""+str(doc_id)+"""}}</a></td>\n""")
    newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{luogo_"""+str(doc_id)+"""}}</a></td>\n""")
    newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{colli_"""+str(doc_id)+"""}}</a></td>\n""")
    newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{peso_"""+str(doc_id)+"""}}</a></td>\n""")
    newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{contrassegno_"""+str(doc_id)+"""}}</a></td>\n""")
    newHtmlFile.write("""\t\t\t\t\t\t<tr>\n""")
    newHtmlFile.close()

    # Genero il contesto passando il dictionary delle variabili dell'HTML
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

# Ultimi tag di chiusura dell'html
newHtmlFile = open('templates/bordero.html', 'a')
newHtmlFile.write("""\t\t\t\t\t</tbody>\n""")
newHtmlFile.write("""\t\t\t\t</table>\n""")
newHtmlFile.write("""\t\t\t</div>\n""")
newHtmlFile.write("""\t\t\t<div class="row">\n""")
newHtmlFile.write("""\t\t\t\t<table class="table table-borderless">\n""")
newHtmlFile.write("""\t\t\t\t\t<thead>\n""")
newHtmlFile.write("""\t\t\t\t\t\t<tr>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Totale Spedizioni</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Totale Colli</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Totale Peso</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Totale Contrassegni</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<th scope='col' style='border: 1px solid black;'>Totale Consegne</th>\n""")
newHtmlFile.write("""\t\t\t\t\t\t</tr>\n""")
newHtmlFile.write("""\t\t\t\t\t</thead>\n""")
newHtmlFile.write("""\t\t\t\t\t<tbody>\n""")
newHtmlFile.write("""\t\t\t\t\t\t<tr>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{somma_spedizioni}}</a></td>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{somma_colli}}</a></td>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{somma_peso}}</a></td>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{somma_contrassegni}}</a></td>\n""")
newHtmlFile.write("""\t\t\t\t\t\t\t<td scope='col' style='border: 1px solid black;'><a style='font-weight: lighter;'>{{numero_sped}}</a></td>\n""")
newHtmlFile.write("""\t\t\t\t\t\t<tr>\n""")
newHtmlFile.write("""\t\t\t\t\t</tbody>\n""")
newHtmlFile.write("""\t\t\t\t</table>\n""")
newHtmlFile.write("""\t\t\t</div>\n""")
newHtmlFile.write("""\t\t</div>\n""")
newHtmlFile.write("""\t</body>\n""")
newHtmlFile.write("""</html>""")
newHtmlFile.close()

# Aggiungo i campi di riepilogo al context del bordero
context_bord['somma_contrassegni'] = somma_contrassegni
context_bord['somma_colli'] = somma_colli
context_bord['somma_peso'] = somma_peso
context_bord['somma_spedizioni'] = somma_spedizioni
context_bord['numero_sped'] = numero_sped


# Genero il borderò
template_loader = jinja2.FileSystemLoader('/')
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template(bordero_template)
output_text = template.render(context_bord)
config = pdfkit.configuration(wkhtmltopdf=str_wkhtmltopdf)
output_pdf = str_abs+'/output/'+'borderò_'+str(nome_corriere)+'_'+str(data_nome_pdf)+'.pdf'
options={"enable-local-file-access": ""}
pdfkit.from_string(output_text, output_pdf, configuration=config, options=options)
