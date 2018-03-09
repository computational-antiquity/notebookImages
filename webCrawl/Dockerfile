FROM jupyter/base-notebook

MAINTAINER Malte Vogl <mvogl@mpiwg-berlin.mpg.de>

USER root

RUN mkdir -p /srv

COPY packages /srv/

# Uncomment to add extra Linux packages as required.

# RUN dpkg --set-selections < /srv/packages.txt

# RUN apt-get -u dselect-upgrade

RUN pip install -r /srv/packages/requierements.txt

COPY config/jupyter_notebook_config.py /home/jovyan/.jupyter

COPY data /home/jovyan/data

RUN chown -R jovyan /home/jovyan

USER jovyan

RUN jupyter trust /home/jovyan/data/index.ipynb
