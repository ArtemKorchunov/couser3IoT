import requests
import json
import sys
import Adafruit_DHT
<<<<<<< HEAD
from random import randint
=======

>>>>>>> c9e6596dea921447559cb801a52196bb44c40c44
print(__name__)


def main():
    content_current = {'identifier': ''}
    f = open("creds.txt", "r")
    content_current['identifier'] = f.read()
    f.close()
<<<<<<< HEAD
    res = requests.post('http://192.168.43.228:4000/iot/auth',
=======
    res = requests.post('http://192.168.0.108:4000/iot/auth',
>>>>>>> c9e6596dea921447559cb801a52196bb44c40c44
                        data={'name': 'raspberry', 'identifier': content_current['identifier']})
    print(res.text)
    if res.status_code == 201:
        res_payload_dict = res.json()
        content_current = res_payload_dict['data']
        f = open("creds.txt", "w+")
        f.write(res_payload_dict['data']['identifier'])
        f.close()

    if content_current:
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(11, 4)
            print("Temp: {} C  Humidity: {}".format(temperatureRand, humidity))
            requests.get('http://192.168.43.228:4000/iot/logger',
                         params={'heat': temperatureRand, 'identifier': content_current['identifier'], 'id': content_current['id']})


if __name__ == "__main__":
    main()
