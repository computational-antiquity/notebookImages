FROM jupyter/base-notebook

MAINTAINER Malte Vogl <mvogl@mpiwg-berlin.mpg.de>

RUN python3 -m pip install --no-cache jupyterhub==0.8.1

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

# Setup custom design
RUN mkdir /home/jovyan/.jupyter/custom

COPY config/custom /home/jovyan/.jupyter/custom

RUN chown -R jovyan:users /home/jovyan/.jupyter

# Setup startup file
COPY config/startup /home/jovyan/.ipython/profile_default/startup

RUN chown -R jovyan:users /home/jovyan/.ipython

USER jovyan

RUN jupyter trust /home/jovyan/work/index.ipynb
