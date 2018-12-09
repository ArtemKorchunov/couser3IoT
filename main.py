import requests
import json
import sys
import Adafruit_DHT

print(__name__)


def main():
    content_current = ''
    f = open("creds.txt", "r")
    fread = f.read()
    if fread != '':
        content_current = json.loads(fread)
    f.close()
    res = requests.post('http://http://192.168.0.108:4000/iot/auth',
                        data={'name': 'raspberry', 'identifier': content_current != '' if ['identifier'] else ''})
    print(res.text)
    if res.status_code == 201:
        res_payload_dict = res.json()
        content_current = json.loads(res_payload_dict)
        f = open("creds.txt", "w+")
        f.write(res_payload_dict)
        f.close()

    if content_current:
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(11, 4)

            print("Temp: {} C  Humidity: {}".format(temperature, humidity))
            requests.get('http://192.168.0.108:4000/iot/logger',
                         params={'heat': temperature, 'identifier': content_current['identifier'], 'id': content_current['id']})


if __name__ == "__main__":
    main()
