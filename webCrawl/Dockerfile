FROM jupyter/scipy-notebook:latest

MAINTAINER Malte Vogl <mvogl@mpiwg-berlin.mpg.de>

USER root

RUN mkdir -p /srv/packages

COPY packages/requierements.txt /srv/packages/requierements.txt 

RUN pip install -r /srv/packages/requierements.txt

COPY config/jupyter_notebook_config.py /home/jovyan/.jupyter

COPY data /home/jovyan/data

RUN chown -R jovyan /home/jovyan

USER jovyan

RUN jupyter trust /home/jovyan/data/index.ipynb
