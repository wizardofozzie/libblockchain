'libdogechain - A Dogechain.info"s API wrapper.'
'GNU GPL v3.0 or above - <http://gnu.org/license/gpl.txt>'

import urllib

def get_balance(address):
    reader = urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/addressbalance/" + address)
    balance = reader.read()
    reader.close()
    return balance

def get_amount_received(address):
    reader = urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/getreceivedbyaddress/" + address)
    amnt_received = reader.read()
    reader.close()
    return balance

def get_amount_sent(address):
    reader = urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/getsentbyaddress/" + address)
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
    
def address_to_hash(address):
    reader = urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/addresstohash/" + address)
    output = reader.read()
    reader.close()
    return output

def hash_to_address(address):
    reader = urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/hashtoaddress/" + address)
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
    reader = urllib.request.urlopen("http://dogechain.info/chain/Dogecoin/q/gettotalbc")
    output = reader.read()
    reader.close()
    return output
