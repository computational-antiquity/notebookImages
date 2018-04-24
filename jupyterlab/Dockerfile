FROM jupyter/base-notebook

MAINTAINER Malte Vogl <mvogl@mpiwg-berlin.mpg.de>

# Install jupyterlab
#RUN conda install -c conda-forge jupyterlab
#RUN jupyter serverextension enable --py jupyterlab --sys-prefix

USER jovyan

CMD ['start.sh','jupyter','lab']
