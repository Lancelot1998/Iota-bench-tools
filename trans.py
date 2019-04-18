# coding=utf-8
"""
Example script that shows how to use PyOTA to send a transfer to an address.
"""
from argparse import ArgumentParser
from sys import argv

from iota import (
  __version__,
  Address,
  Iota,
  ProposedTransaction,
  Tag,
  TryteString,
)
from six import text_type
#from address_generator import get_seed, output_seed


def main():
    # Ensure seed is not displayed in cleartext.
    #seed = get_seed()
    # Create the API instance.
    while(1):
    	api = Iota("http://localhost:14265")

    	#if not seed:
    	#    print('A random seed has been generated. Press return to see it.')
    	#    output_seed(api.seed)

    	#print('Starting transfer.')
    	# For more information, see :py:meth:`Iota.send_transfer`.
    	api.send_transfer(
            depth=3,
            # One or more :py:class:`ProposedTransaction` objects to add to the
            # bundle.
            transfers=[
                ProposedTransaction(
                    # Recipient of the transfer.
                    address=Address("RECEIVINGWALLETADDRESSGOESHERE9WITHCHECKSUMANDSECURITYLEVELB999999999999999999999999999999"),

                    # Amount of IOTA to transfer.
                    # By default this is a zero value transfer.
                    value=0,

                    # Optional tag to attach to the transfer.
                    tag=Tag(b'KITTEHS'),

                    # Optional message to include with the transfer.
                    message=TryteString.from_unicode('thx fur cheezburgers'),
                ),
            ],
            min_weight_magnitude=1
        )

if __name__ == '__main__':
    main()
