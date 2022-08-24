import zmq
import math
import time
import random
from pytz import timezone
from datetime import datetime
import json
import sys

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://0.0.0.0:5555')

class InstrumentPrice(object):
    def __init__(self):
        self.symbol = 'A005930'
        self.t = time.time()
        self.value = 60000.
        self.sigma = 0.4
        self.r = 0.01

    def simulate_value(self):
        ''' Generates a new, random stock price.
        '''
        t = time.time()
        dt = (t - self.t) / (252 * 8 * 60 * 60)
        dt *= 500
        self.t = t
        self.value *= math.exp((self.r - 0.5 * self.sigma ** 2) * dt +
                               self.sigma * math.sqrt(dt) * random.gauss(0, 1))
        return self.value

    def simulate_time(self):
        ''' Generates a currunt time.
        '''
        self.time = datetime.now(timezone('Asia/Seoul')).strftime("%H:%M:%S").replace(':','')
        return self.time


ip = InstrumentPrice()

write, flush = sys.stdout.write, sys.stdout.flush
while True:
    msg = dict()
    msg['code'] = ip.symbol
    msg['name'] = "Samsung"
    msg['price'] = float(f'{ip.simulate_value():.2f}')
    msg['time'] = int(ip.simulate_time())
    sendmsg = json.dumps(msg)
    # print(str(sendmsg))
    write(str(sendmsg))
    flush()
    write('\x08' * len(str(sendmsg)))
    socket.send_string(sendmsg)
    time.sleep(random.random() * 1)



