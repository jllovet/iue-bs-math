FROM python:3.7.2

WORKDIR /opt

RUN apt-get update \
  && apt-get install -y --no-install-recommends graphviz \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir pyparsing pydot diagrams

ENTRYPOINT [ "python3" ]

CMD [ "$1" ]