# coding=utf-8
"""
Example script that shows how to use PyOTA to send a transfer to an address.
"""
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


def main():
    api = Iota("http://localhost:14265")

    # For more information, see :py:meth:`Iota.send_transfer`.
    ti = time.time()
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
    k = 0
    for k in a["bundle"]:
    	print(k)

if __name__ == '__main__':
    i = 0
    for i in range(1):
    	main()
