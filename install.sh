#!/usr/bin/bash
echo "##################################"
echo "#    Installazione Dipendenze    #"
echo "##################################"

sudo apt-get update

sudo apt install software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt install python3.8

sudo apt-get update

pip install jinja2

pip install pdfkit

sudo apt-get install wkhtmltopdf

echo "### Path di which wkhtmltopdf###"
which wkhtmltopdf

echo "##################################"
echo "#    Installazione Completata    #"
echo "##################################"