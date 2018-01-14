import os

graphite_server = "localhost"
graphite_port = 2003
pin_number = 4
retry_times = 10


if os.environ['GRAPHITE_SERVER']:
	graphite_server = os.environ['GRAPHITE_SERVER']
if os.environ['GRAPHITE_PORT']:
	graphite_port = os.environ['GRAPHITE_PORT']