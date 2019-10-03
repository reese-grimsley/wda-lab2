"""
Embedded Python Blocks:

Each this file is saved, GRC will instantiate the first class it finds to get
ports and parameters of your block. The arguments to __init__  will be the
parameters. All of them are required to have default values!
"""

import pmt
import time
import numpy as np
from gnuradio import gr

class lora_message(gr.basic_block):
    def __init__(self):  # only default arguments here
        gr.basic_block.__init__(
            self,
            name='Print LoRa Message',
            in_sig=[],
            out_sig=[]
        )
        self.message_port_register_in(pmt.intern("in"))
        self.set_msg_handler(pmt.intern("in"), self.msg_handler)

    def msg_handler(self, msg):
        msg = pmt.to_python(msg)
        print str(time.time()) + ": " + msg.tobytes()[3:] #skip printing header
