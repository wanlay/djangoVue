FROM wanlay/dev:alpine

COPY . /code

WORKDIR /code

RUN pip3 install -r requirements.txt

COPY supervisord.conf /etc/supervisord.conf

EXPOSE 9000 9528 22

CMD    ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]