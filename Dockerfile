FROM ubuntu:22.04
FROM python:latest 
COPY . /tmp 
ENTRYPOINT sleep infinity