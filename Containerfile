FROM registry.access.redhat.com/ubi8/ubi-minimal

ENV PORT 8080
EXPOSE 8080
WORKDIR /usr/src/app

USER 0 
RUN microdnf install python38 \
    && microdnf clean all
    
COPY imagelookup /usr/src/app/imagelookup
RUN chown -R 1001:0 /usr/src/app/imagelookup

WORKDIR /usr/src/app/imagelookup
RUN pip3 install -U pip3 wheel && \
    pip3 install --no-cache-dir -r requirements.txt

USER 1001
CMD [ "python", "app.py"]
