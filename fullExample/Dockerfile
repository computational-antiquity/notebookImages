FROM jupyter/base-notebook

MAINTAINER Malte Vogl <mvogl@mpiwg-berlin.mpg.de>

USER root

RUN mkdir -p /srv

COPY packages /srv/

# Add extra Linux packages required by the notebook
# RUN dpkg --set-selections < /srv/packages.txt && apt-get -u dselect-upgrade

# Install required python packages
RUN pip install -r /srv/packages/requierements.txt

# Setup configuration of Jupyter notebooks
COPY config/jupyter_notebook_config.py /home/jovyan/.jupyter

# Add data
COPY data /home/jovyan/data

RUN chown -R jovyan /home/jovyan

# Setup custom design
RUN mkdir /home/jovyan/.jupyter/custom

COPY config/custom /home/jovyan/.jupyter/custom

COPY config/startup /home/jovyan/.ipython/profile_default/startup

RUN chown -R jovyan:users /home/jovyan/.jupyter

USER jovyan

# Add hash for notebook file, to allow automatic evaluation
RUN jupyter trust /home/jovyan/data/index.ipynb
