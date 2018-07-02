FROM wanlay/dev:alpine

COPY . /code

COPY supervisord.conf /etc/supervisord.conf

WORKDIR /code

RUN pip3 install -r requirements.txt

RUN cd frontend && npm install

EXPOSE 9000 9528 22

CMD    ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]