"""
Example demonstrating how to do the key rotation on the ledger.

Steward already exists on the ledger and its DID/Verkey are obtained using seed.
Trust Anchor's DID/Verkey pair is generated and stored into wallet.
Stewards builds NYM request in order to add Trust Anchor to the ledger.
Once NYM transaction is done, Trust Anchor wants to change its Verkey.
First, temporary key is created in the wallet.
Second, Trust Anchor builds NYM request to replace the Verkey on the ledger.
Third, when NYM transaction succeeds, Trust Anchor makes new Verkey permanent in wallet
(it was only temporary before).

To assert the changes, Trust Anchor reads both the Verkey from the wallet and the Verkey from the ledger
using GET_NYM request, to make sure they are equal to the new Verkey, not the original one
added by Steward
"""


import asyncio
import json
import pprint

from indy import pool, ledger, wallet, did
from indy.error import IndyError


pool_name = 'pool'
wallet_name = 'wallet'
genesis_file_path = '/home/vagrant/code/evernym/indy-sdk/cli/docker_pool_transactions_genesis'
wallet_credentials = json.dumps({"key": "wallet_key"})


def print_log(value_color="", value_noncolor=""):
    """set the colors for text."""
    HEADER = '\033[92m'
    ENDC = '\033[0m'
    print(HEADER + value_color + ENDC + str(value_noncolor))


async def rotate_key_on_the_ledger():
    try:
        # Step 2 code goes here.

        # Step 3 code goes here.

        # Step 4 code goes here.

    except IndyError as e:
        print('Error occurred: %s' % e)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(rotate_key_on_the_ledger())
    loop.close()


if __name__ == '__main__':
    main()

