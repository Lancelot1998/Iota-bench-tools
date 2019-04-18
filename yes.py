from iota import Iota, Address, ProposedTransaction, Tag, Transaction, TryteString
import requests
import json
from iota import (
  __version__,
  Address,
  Iota,
  ProposedTransaction,
  Tag,
  TryteString,
)
from six import text_type

api = Iota('http://localhost:14265')
txn_2 =\
  ProposedTransaction(
    address =
      Address(
        b'FJHSSHBZTAKQNDTIKJYCZBOZDGSZANCZSWCNWUOCZXFADNOQSYAHEJPXRLOVPNOQFQXXGEGVDGICLMOXX'
      ),

    message = TryteString.from_unicode('thx fur cheezburgers'),
    tag     = Tag(b'KITTEHS'),
    value   = 0,
  )

c = api.prepare_transfer([txn_2])["trytes"]

K = api.send_trytes(depth=3, trytes=c, min_weight_magnitude=9)
print('Transfer complete.')
print(c)
print('\n')
print(K["trytes"])
