import requests
import sys
import Adafruit_DHT

print(__name__)


def main():
    f = open("creds.txt", "r")
    content_current = f.read()
    f.close()
    if content_current == "":
        res = requests.post('http://192.168.0.108:4000/iot/auth',
                            data={'name': 'raspberry'})
        print(res)
        if res.status_code == 201:
            res_payload_dict = res.json()
            content_current = res_payload_dict
            f = open("creds.txt", "w+")
            f.write(res_payload_dict['data']['identifier'])
            f.close()
    if content_current:
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(11, 4)

		print("Temp: {} C  Humidity: {}".format(temperature, humidity))
		requests.get('http://192.168.0.108:4000/iot/logger',
			params={'heat': temperature, 'identifier': content_current})


if __name__ == "__main__":
    main()
