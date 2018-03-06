FROM jupyter/scipy-notebook:latest

MAINTAINER Malte Vogl <mvogl@mpiwg-berlin.mpg.de>

RUN pip install beautifulsoup requests

COPY config/jupyter_notebook_config.py /home/jovyan/.jupyter

COPY data /home/jovyan/data
