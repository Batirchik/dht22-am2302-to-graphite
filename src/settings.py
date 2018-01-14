import os

graphite_server = "localhost"
graphite_port = 2003
pin_number = 4
retry_times = 10


if 'GRAPHITE_SERVER' in os.environ:
	graphite_server = os.environ['GRAPHITE_SERVER']
if 'GRAPHITE_PORT' in os.environ:
	graphite_port = os.environ['GRAPHITE_PORT']