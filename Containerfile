FROM registry.access.redhat.com/ubi8/python-38

ENV PORT 8080
EXPOSE 8080
WORKDIR /usr/src/app

USER 0 
RUN yum remove npm -y
COPY imagelookup /usr/src/app/imagelookup
RUN chown -R 1001:0 /usr/src/app/imagelookup
USER 1001

WORKDIR /usr/src/app/imagelookup
RUN pip install -U pip wheel && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py"]
