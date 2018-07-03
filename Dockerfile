FROM wanlay/dev:alpine

COPY . /code

ADD ./supervisord.conf /etc/supervisord.conf

WORKDIR /code

RUN pip3 install -r requirements.txt

RUN cd frontend && npm install

VOLUME /code

# django: 9000
# vue(frontend): 9528
# ssh
EXPOSE 9000 9528 22

CMD    ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]