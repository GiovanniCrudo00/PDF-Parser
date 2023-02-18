#!/usr/bin/perl

system("docker build -t pdf-parser .");

system("docker container run --name parser --rm pdf-parser");

system("docker rmi pdf-parser")