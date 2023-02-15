import subprocess
import jinja2
import pdfkit
from datetime import datetime


#
# Prevelo il path assoluto della macchina
#

output = subprocess.check_output(['pwd'])
str_abs = output.decode('utf8', errors='strict').strip() # Path da concatenare alla cartella delle immagini
output = subprocess.check_output(['which','wkhtmltopdf'])
str_wkhtmltopdf = output.decode('utf8', errors='strict').strip() # Path della libreria wkhtmltopdf

#
# Popolo i campi per la creazione del pdf
#

logo=str_abs+"/images/logoDFG.jpeg"
lettera_di_vettura = "445"
today_date = datetime.today().strftime("%d %b, %Y")
mittente_nome = "DFG Servizi s.r.l."
mittente_via = "Via Marcellinara s.n.c."
mittente_luogo = "Marcellinara, Catanzaro, 88100"
destinatario_nome = "LORY EXPRESS S.N.C."
destinatario_via = "Via Montepalma, 1"
destinatario_luogo = "95125 Catania CT"
contrassegno = "Tipica stringa del contrassegno non lo so"
annotazioni= "Non è arrivato niente"
data_inizio_trasporto = "23/09/2023"
numero_colli = "2"
peso = "2kg"
ddt="5"

#
# Assegno ai placeholder un valore dai dati recuperati
#

context = {'logo':logo,'lettera_di_vettura': lettera_di_vettura, 'mittente_nome': mittente_nome, 
            'mittente_via': mittente_via, 'mittente_luogo': mittente_luogo,
            'destinatario_nome':destinatario_nome,'destinatario_via':destinatario_via,
            'destinatario_luogo':destinatario_luogo, 'contrassegno':contrassegno,
            'data_inizio_trasporto':data_inizio_trasporto, 'numero_colli':numero_colli,
            'peso':peso, 'data': today_date, 'annotazioni':annotazioni, 'DDT':ddt}

#
# Genero il PDF dando il template, il path della libreria wkhtmltopdf e il nome
#

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = './templates/bollaTemplate.html'
template = template_env.get_template(html_template)
output_text = template.render(context)
config = pdfkit.configuration(wkhtmltopdf=str_wkhtmltopdf)
output_pdf = './output/PDF_FICO.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config)