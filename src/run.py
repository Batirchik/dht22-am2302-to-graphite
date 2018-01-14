# import am2302_ths as am
import graphitesend
from random import *
import settings
import time

PIN = settings.pin_number
RETRY_TIMES = settings.retry_times
graphitesend.init(
	graphite_server=settings.graphite_server,
	graphite_port=settings.graphite_port,
	asynchronous=False,
	autoreconnect=True,
	prefix="",
	group="",
	system_name="")


def get_stats():
	temperature = randint(1, 100)
	humidity = randint(1, 100)
	# temperature = am.get_temperature(PIN)
	# humidity = am.get_humidity(PIN)
	return temperature, humidity


while True:
	tried_times = 1
	temp, hum = get_stats()
	while tried_times <= RETRY_TIMES:
		if temp is not None and hum is not None:
			break

		temp, hum = get_stats()

	# sometimes sensor doesn't read value, so we take '0'
	if temp is None:
		temp = 0
	if hum is None:
		hum = 0

	graphitesend.send_dict({'temperature': temp, 'humidity': hum})
	# graphitesend.send('temperature', temp)
	# graphitesend.send('humidity', hum)

	print 'temperature: {}, humidity: {}'.format(temp, hum)

	time.sleep(5)
