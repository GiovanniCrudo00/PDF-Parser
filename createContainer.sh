#!/usr/bin/bash


docker build -t pdf-parser .

docker container run --name parser --rm pdf-parser

docker rmi pdf-parser
