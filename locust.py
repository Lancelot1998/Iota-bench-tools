# -*- coding: utf-8 -*-
"""
    Locust Shell (API)
    ~~~~~~~~

    :author: Jason Liu
"""

from flask import Flask, request
import os
from argparse import ArgumentParser
from sys import argv

import time
from iota import (
  __version__,
  Address,
  Iota,
  ProposedTransaction,
  Tag,
  TryteString,
)
from six import text_type

app = Flask(__name__)
api = Iota("http://localhost:14265")

@app.route("/node", methods=['GET', 'POST'])
def hello():
    a = api.send_transfer(
        depth=3,        
        transfers=[
            ProposedTransaction(
                # Recipient of the transfer.
                address=Address("RECEIVINGWALLETADDRESSGOESHERE9WITHCHECKSUMANDSECURITYLEVELB999999999999999999999999999999"),
                value=0,

                # Optional tag to attach to the transfer.
                tag=Tag(b'KITTEHS'),

                # Optional message to include with the transfer.
                message=TryteString.from_unicode('thx fur cheezburgers'),
            ),
        ],
        min_weight_magnitude=1
    )
    return 'hello'


@app.route("/transaction", methods=['GET', 'POST'])
def transaction():
    a = api.send_transfer(
        depth=3,        
        transfers=[
            ProposedTransaction(
                # Recipient of the transfer.
                address=Address("RECEIVINGWALLETADDRESSGOESHERE9WITHCHECKSUMANDSECURITYLEVELB999999999999999999999999999999"),
                value=0,

                # Optional tag to attach to the transfer.
                tag=Tag(b'KITTEHS'),

                # Optional message to include with the transfer.
                message=TryteString.from_unicode('thx fur cheezburgers'),
            ),
        ],
        min_weight_magnitude=1
    )
    return 'right'


if __name__ == "__main__":
    app.run()
