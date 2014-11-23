'libblockchain - A Blockchain.info"s API wrapper.'
'GNU GPL v3.0 or above - <http://gnu.org/license/gpl.txt>'

import urllib

def get_balance(address):
    return urllib.request.urlopen("http://blockchain.info/q/addressbalance/" + address).read()

def get_amount_received(address):
    return urllib.request.urlopen("http://blockchain.info/q/getreceivedbyaddress/" + address).read()

def get_amount_sent(address):
    return urllib.request.urlopen("http://blockchain.info/q/getsentbyaddress/" + address).read()

'def check_address(address):'
    'return urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/checkaddress/" + address)'
    ''
    ''
    'if output == "X5" or output == "SZ" or output == "CK": return False'
    'else: return True'

def decode_address(address):
    return urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/decode_address/" + address).read()

def get_address_firstseen(address):
    return return urllib.request.urlopen("http://blockchain.info/q/addressfirstseen/" + address).read()

def address_to_hash(address):
    return urllib.request.urlopen("http://blockchain.info/q/addresstohash/" + address).read()

def hash_to_address(address):
    return urllib.request.urlopen("http://blockchain.info/q/hashtoaddress/" + address).read()

def get_difficulty():
    return urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/getdifficulty").read()

def get_eta_nextblock():
    return urllib.request.urlopen("http://blockchain.info/q/eta").read()

def get_avgtx_number():
    return urllib.request.urlopen("http://blockchain.info/q/avgtxnumber").read()

def get_block_count():
    return urllib.request.urlopen("http://blockchain.info/q/getblockcount").read()

def get_total_bc():
    return urllib.request.urlopen("http://blockchain.info/q/totalbc").read()

def get_hashrate():
    'Get the hashrate in gigahashes.'
    return urllib.request.urlopen("http://blockchain.info/q/hashrate").read()

def get_latest_hash():
    'Get the hashrate in gigahashes.'
    return urllib.request.urlopen("http://blockchain.info/q/latesthash").read()

def get_market_cap():
    'Get the hashrate in gigahashes.'
    return urllib.request.urlopen("http://blockchain.info/q/marketcap").read()

def get_transactions_count_24hr():
    'Get the hashrate in gigahashes.'
    return urllib.request.urlopen("http://blockchain.info/q/24hrtransactioncount").read()

def get_btc_sent_count_24hr_satoshi():
    'Get the hashrate in gigahashes.'
    return urllib.request.urlopen("http://blockchain.info/q/24hrbtcsent").read()

def get_unconfirmed_count():
    'Get the hashrate in gigahashes.'
     return urllib.request.urlopen("http://blockchain.info/q/unconfirmedcount").read()

def generate_key():
    'Generate a new bitcoin address and a private key. Returns public key and then private key.'
    return urllib.request.urlopen("http://blockchain.info/q/newkey").read()

def get_unconfirmed_count():
    'Get the hashrate in gigahashes.'
    return urllib.request.urlopen("http://blockchain.info/q/unconfirmedcount").read()

def get_version():
    'Get the version of the library.'
    return "1.2.0.0"
