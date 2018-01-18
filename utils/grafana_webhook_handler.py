from flask import Flask
from flask import request
import os
import logging


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s")


app = Flask(__name__)


@app.route('/webhook', methods=['POST', 'PUT'])
def webhook():
	json = request.json

	logging.debug(json)

	if json['state'] == "alerting":
		# just because I can.
		os.system("sudo reboot")

	if json['state'] == "no_data":
		# sometimes am2302 library stop working after a while.
		# Don't care why and too lazy to figure this out. So, I have to restart the process.
		os.system("sudo service sensors-to-grafana restart")
	return 200

if __name__ == '__main__':
    app.run(debug=True)

