"""
Embedded Python Blocks:

Each this file is saved, GRC will instantiate the first class it finds to get
ports and parameters of your block. The arguments to __init__  will be the
parameters. All of them are required to have default values!
"""

from gnuradio import gr
import json
import socket

class blk(gr.basic_block):
    def __init__(self, msg="WelcomeToWDA!", tx_power=20, sf=7):  # only default arguments here
        gr.basic_block.__init__(
            self,
            name='LoPy Config',
            in_sig=[],
            out_sig=[]
        )
        self.msg = msg
        self.tx_power = tx_power
        self.sf = sf
        self.host = "10.230.8.5"
        self.port = 18747
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.update()

    def get_sf(self):
        return self.sf

    def set_sf(self, sf):
        self.sf = sf
        self.update()

    def get_tx_power(self):
        return self.tx_power

    def set_tx_power(self, tx_power):
        self.tx_power = tx_power
        self.update()

    def get_msg(self):
        return self.msg

    def set_msg(self, msg):
        self.msg = msg
        self.update()

    def update(self):
        params = {'msg': self.msg, 'tx_power': self.tx_power, 'sf': self.sf}
        #print params
        #up = json.dumps(params)
	sentData = self.msg + " " + str(self.tx_power) + " " + str(self.sf)
        self.client.sendto(sentData, (self.host, self.port))

