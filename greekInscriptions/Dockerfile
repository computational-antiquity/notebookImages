FROM jupyter/base-notebook

MAINTAINER Malte Vogl <mvogl@mpiwg-berlin.mpg.de>

# Enable table of contents
RUN pip install jupyter_contrib_nbextensions

RUN jupyter contrib nbextension install --user && jupyter nbextension enable toc2/main

USER root

RUN mkdir -p /srv

COPY packages /srv/packages

# Uncomment to add extra Linux packages as required.

# RUN dpkg --set-selections < /srv/packages.txt

# RUN apt-get -u dselect-upgrade

RUN pip install -r /srv/packages/requirements.txt

# For python packages without a release on pypi
RUN apt update
RUN apt install -y git
RUN pip install git+https://github.com/paudan/treetagger-python.git

COPY config/jupyter_notebook_config.py /home/jovyan/.jupyter

COPY data /home/jovyan/data

RUN chown -R jovyan /home/jovyan

USER jovyan

# Extra routines to install treetagger
RUN sh /home/jovyan/data/install-tagger.sh

RUN export TREETAGGER_HOME='/home/jovyan/data/cmd/tree-tagger-german'

RUN jupyter trust /home/jovyan/data/index.ipynb
