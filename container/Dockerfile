FROM python:3.10-bookworm

RUN apt update
RUN apt upgrade -y
RUN apt install  iputils-ping -y

RUN mkdir /opt/yangsuite && \
    groupadd --gid 999 --system yangsuite && \
    useradd --uid 999 --gid 999 --system --shell /bin/bash --create-home --home-dir /opt/yanguite yangsuite && \
    chown -R yangsuite:yangsuite /opt/yangsuite

USER yangsuite

RUN cd /opt/yangsuite && python3 -m venv .venv
ENV PATH /opt/yangsuite/.venv/bin:/opt/yanguite/.local/bin:$PATH
RUN . /opt/yangsuite/.venv/bin/activate

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /opt/yanguite/.config/yangsuite
RUN mkdir -p /opt/yangsuite/cache
RUN mkdir -p /opt/yangsuite/uwsgi/
COPY yangsuite.ini /opt/yanguite/.config/yangsuite/
COPY production.py /opt/yangsuite/.venv/lib/python3.10/site-packages/yangsuite/settings/production.py
COPY uwsgi.ini /opt/yangsuite/
CMD ["sleep", "infinity"]
