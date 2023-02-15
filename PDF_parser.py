import jinja2
import pdfkit
from datetime import datetime


#
# Prendo i dati da una query o un file di testo
#

my_name = "Frank Andrade"
item1 = "TV"
item2 = "Couch"
item3 = "Washing Machine"
today_date = datetime.today().strftime("%d %b, %Y")

#
# Assegno ai placeholder un valore dai dati recuperati
#

context = {'my_name': my_name, 'item1': item1, 'item2': item2, 'item3': item3,
           'today_date': today_date}

#
# Genero il PDF dando il template, il path della libreria wkhtmltopdf e il nome
#

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'template.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
output_pdf = 'PDF_FICO.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')