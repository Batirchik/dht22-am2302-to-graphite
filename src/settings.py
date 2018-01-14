import os
import logging

# Debug mode allows you to get much more information about process, but it could be too much information for production.
# Thus, logging level should be 'DEBUG' for debug and development purpose, but 'INFO' for production running.
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s")


graphite_server = "localhost"
graphite_port = 2003
pin_number = 4
retry_times = 10


if 'GRAPHITE_SERVER' in os.environ:
	graphite_server = os.environ['GRAPHITE_SERVER']
if 'GRAPHITE_PORT' in os.environ:
	graphite_port = os.environ['GRAPHITE_PORT']
