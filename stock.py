import time
import datetime
import json
import random


STREAM_NAME = "ExampleInputStream"


def get_data():
    return {
        'EVENT_TIME': datetime.datetime.now().isoformat(),
        'TICKER': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'PRICE': round(random.random() * 100, 2)}


def generate():
    f = open('app/logs/hello.log','w')
    while True:
        data=get_data()
        datas = json.dumps(data)
        f.write(datas)
        time.sleep(2)
        print(datas)

if __name__ == '__main__':
    generate()
