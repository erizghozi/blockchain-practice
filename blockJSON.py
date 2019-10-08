import time
import hashlib
import json
from collections import OrderedDict

class Block(object):
    def __init__(self, index, proof, previous_hash, transactions):
        self.index = index
        self.proof = proof
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        
    @property
    def get_block_hash(self):
        block_string = "{}{}{}{}{}".format(self.index, self.proof, self.previous_hash, self.transactions, self.timestamp)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def get_dict_default(self):
        return dict(vars(self), get_block_hash=self.get_block_hash)
    
    def get_dict_custom(self):
        return OrderedDict(
                index = self.index,
                proof = self.proof,
                previous_hash = self.previous_hash,
                transactions = self.transactions,
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S UTC 0:00", time.gmtime(self.timestamp)),
                get_block_hash=self.get_block_hash)
   
    def strAttr(self):
        strAtr = """index: %s\n
        proof: %s\n
        previous_hash: %s\n
        transactions: %s\n
        timestamp: %s\n
        hash: %s\n
        """ % (self.index, self.proof,self.previous_hash, self.transactions, 
        time.strftime("%Y-%m-%d %H:%M:%S UTC 0:00", time.gmtime(self.timestamp)), 
        self.get_block_hash)
        return strAtr

    def printAttr(self):
        print("index: ", self.index)
        print("proof: ", self.proof)
        print("previous_hash: ", self.previous_hash)
        print("transactions : ", self.transactions)
        print("timestamp    : ", self.timestamp)
    
    def __repr__(self):
        #Kembalian string. 
        #Pada contoh pakai dictionary yang dijadikan string, tetapi bisa langsung dibangun pakai string saja.
        #Toggle comment untuk lihat hasil yang berbeda.
        #Cara 1
        #strRepr = json.dumps(self.__dict__)
        #Cara 2
        #strRepr = json.dumps(self.get_dict_default)
        #Cara 3
        #strRepr = json.dumps(self.get_dict_custom(), indent=2)
        #Cara 4
        strRepr = self.strAttr()
        #Cara 5
        #strRepr = self.printAttr()
        
        return strRepr
