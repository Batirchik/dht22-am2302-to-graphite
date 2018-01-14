import am2302_ths as am

PIN = 4
temp = am.get_temperature(PIN)
hum = am.get_humidity(PIN)

print 'temperature: {}, humidity: {}' % temp, hum
