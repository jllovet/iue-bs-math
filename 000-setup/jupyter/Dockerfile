FROM jupyter/scipy-notebook

WORKDIR /opt

USER root
RUN sudo apt-get update \
  && sudo apt-get install -y --no-install-recommends graphviz \
  && rm -rf /var/lib/apt/lists/*

USER jovyan
RUN pip install --no-cache-dir handcalcs

ENTRYPOINT [ "/usr/bin/tini", "--" ]

CMD [ "jupyter", "notebook", "--ip=0.0.0.0", "--port=3000", "--no-browser", "--notebook-dir=/home/jovyan/"]
