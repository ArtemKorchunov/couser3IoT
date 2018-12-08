import requests

print(__name__)


def main():
    f = open("creds.txt", "r")
    content_current = f.read()
    f.close()
    if content_current == "":
        res = requests.post('http://localhost:4000/iot/auth',
                            data={'name': 'raspberry'})
        print(res)
        if res.status_code == 201:
            res_payload_dict = res.json()
            content_current = res_payload_dict
            f = open("creds.txt", "w+")
            f.write(res_payload_dict['data']['identifier'])
            f.close()
    if content_current:
        requests.get('http://localhost:4000/iot/logger',
                     params={'heat': 25, 'identifier': content_current})


if __name__ == "__main__":
    main()
