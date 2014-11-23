'libblockchain - A Blockchain.info"s API wrapper.'
'GNU GPL v3.0 or above - <http://gnu.org/license/gpl.txt>'

import urllib

def get_balance(address):
    reader = urllib.request.urlopen("http://blockchain.info/q/addressbalance/" + address)
    balance = reader.read()
    reader.close()
    return balance

def get_amount_received(address):
    reader = urllib.request.urlopen("http://blockchain.info/q/getreceivedbyaddress/" + address)
    amnt_received = reader.read()
    reader.close()
    return balance

def get_amount_sent(address):
    reader = urllib.request.urlopen("http://blockchain.info/q/getsentbyaddress/" + address)
    amnt_sent = reader.read()
    reader.close()
    return balance

def check_address(address):
    reader = urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/checkaddress/" + address)
    output = reader.read()
    reader.close()
    if output == "X5" or output == "SZ" or output == "CK": return False
    else: return True

def decode_address(address):
    reader = urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/decode_address/" + address)
    output = reader.read()
    reader.close()
    return output
    

def get_address_firstseen(address):
    reader = urllib.request.urlopen("http://blockchain.info/q/addressfirstseen/" + address)
    output = reader.read()
    reader.close()
    return output

def address_to_hash(address):
    reader = urllib.request.urlopen("http://blockchain.info/q/addresstohash/" + address)
    output = reader.read()
    reader.close()
    return output

def hash_to_address(address):
    reader = urllib.request.urlopen("http://blockchain.info/q/hashtoaddress/" + address)
    output = reader.read()
    reader.close()
    return output
    
def get_difficulty():
    reader = urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/getdifficulty")
    output = reader.read()
    reader.close()
    return output
    
def get_block_count():
    reader = urllib.request.urlopen("http://blockchain.info/q/getblockcount")
    output = reader.read()
    reader.close()
    return output
    
def get_total_bc():
    reader = urllib.request.urlopen("http://blockchain.info/q/totalbc")
    output = reader.read()
    reader.close()
    return output

def get_hashrate():
    'Get the hashrate in gigahashes.'
    reader = urllib.request.urlopen("http://blockchain.info/q/hashrate")
    output = reader.read()
    reader.close()
    return output
    
def get_latest_hash():
    'Get the hashrate in gigahashes.'
    reader = urllib.request.urlopen("http://blockchain.info/q/latesthash")
    output = reader.read()
    reader.close()
    return output

def get_market_cap():
    'Get the hashrate in gigahashes.'
    reader = urllib.request.urlopen("http://blockchain.info/q/marketcap")
    output = reader.read()
    reader.close()
    return output

def get_transactions_count_24hr():
    'Get the hashrate in gigahashes.'
    reader = urllib.request.urlopen("http://blockchain.info/q/24hrtransactioncount")
    output = reader.read()
    reader.close()
    return output

def get_btc_sent_count_24hr_satoshi():
    'Get the hashrate in gigahashes.'
    reader = urllib.request.urlopen("http://blockchain.info/q/24hrbtcsent")
    output = reader.read()
    reader.close()
    return output

def get_unconfirmed_count():
    'Get the hashrate in gigahashes.'
    reader = urllib.request.urlopen("http://blockchain.info/q/unconfirmedcount")
    output = reader.read()
    reader.close()
    return output

def generate_key():
    'Generate a new bitcoin address and a private key. Returns public key and then private key.'
    reader = urllib.request.urlopen("http://blockchain.info/q/newkey")
    output = reader.read()
    reader.close()
    splitter = output.split(" ")
    count = 0
    for string in splitter:
        count = count + 1
        if count == 1: return string
        elif count == 2: return string

def get_unconfirmed_count():
    'Get the hashrate in gigahashes.'
    reader = urllib.request.urlopen("http://blockchain.info/q/unconfirmedcount")
    output = reader.read()
    reader.close()
    return output

