FROM python:3.8.1

WORKDIR /gwg

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-dev \
        build-essential \
        libgdal-dev \
        nano

RUN python -m pip install --upgrade pip

RUN pip3 install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"

RUN rm -rf /var/lib/apt/lists/* && \
    useradd -ms /bin/bash gwg && \
    chown -R gwg:gwg ./

USER gwg

COPY --chown=gwg:gwg . ./

RUN PATH=$PATH:/home/gwg/.local/bin

RUN pip install --no-cache-dir --user -r requirements.txt

RUN rm requirements.txt

WORKDIR /gwg/backend
