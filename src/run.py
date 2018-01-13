import am2302_ths as am

PIN = 4
temp = am.get_temperature(PIN)
hum = am.get_humidity(PIN)

print 'temperature: %(temp), humidity: %(hum)' % {"temp": "Python", "hum": 2}
