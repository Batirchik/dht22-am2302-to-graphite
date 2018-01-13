FROM resin/raspberry-pi-python

# install necessary C library 'bcm2835'
RUN wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.50.tar.gz \
    && tar xvfz bcm2835-1.50.tar.gz \
    && cd bcm2835-1.50  \
    && ./configure \
    && make \
    && sudo make install

RUN sudo pip install am2302_rpi
COPY src/ /opt/from-dht22-am2302-to-grafana

CMD python /opt/from-dht22-am2302-to-grafana/run.py