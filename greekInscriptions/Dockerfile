FROM jupyter/base-notebook

MAINTAINER Malte Vogl <mvogl@mpiwg-berlin.mpg.de>

# Enable table of contents and widgets
RUN pip install jupyter_contrib_nbextensions ipywidgets

RUN jupyter contrib nbextension install --user && jupyter nbextension enable toc2/main

RUN jupyter nbextension enable --py widgetsnbextension

USER root

RUN mkdir -p /srv

COPY packages /srv/packages

# Uncomment to add extra Linux packages as required.

# RUN dpkg --set-selections < /srv/packages.txt

# RUN apt-get -u dselect-upgrade

RUN pip install -r /srv/packages/requirements.txt

COPY config/jupyter_notebook_config.py /home/jovyan/.jupyter

COPY data /home/jovyan/work

RUN chown -R jovyan /home/jovyan

USER jovyan

RUN jupyter trust /home/jovyan/work/index.ipynb
