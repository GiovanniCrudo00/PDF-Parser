#!/usr/bin/bash
echo "##################################"
echo "#    Installazione Dipendenze    #"
echo "##################################"

apt-get update

apt install software-properties-common

add-apt-repository ppa:deadsnakes/ppa

apt install python3.8

apt-get update

pip install --upgrade pip

pip install jinja2

pip install pdfkit

apt-get install wkhtmltopdf

echo "### Path di which wkhtmltopdf###"
which wkhtmltopdf

echo "##################################"
echo "#    Installazione Completata    #"
echo "##################################"