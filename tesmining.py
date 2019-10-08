import time
import hashlib
from uuid import uuid4
from blockchain import *
from argparse import ArgumentParser
from flask import Flask, jsonify, request

blockchain = BlockChain()
app = Flask(__name__)

node_address = uuid4().hex
print("Node Address = ", node_address)

@app.route('/')
def mainpage():
    return "Tutorial web mining 101"

@app.route('/chain', methods=['GET'])
def get_full_chain():
    response = {'chain': blockchain.get_serialized_chain}
    return jsonify(response)

@app.route('/create-transaction', methods = ['POST'])
def create_transaction():
    transaction_data = request.get_json()
    index = blockchain.create_new_transaction(**transaction_data)
    response = {
        'message': 'Transaksi jalan!',
        'block_index': index,
        'node address': node_address
    }
    return jsonify(response)

@app.route('/mine', methods=['GET'])
def mine():
    block = blockchain.mine_block(node_address)
    response = {
        'message': 'Berhasil mining! (tapi gak jadi miliarder)',
        'block_data': block
    }
    return jsonify(response)

@app.route('/about')
def about():
    return "Buatan Eriz Ghozi, 18/07/2018"


parser = ArgumentParser()
parser.add_argument('-H', '--host', default='127.0.0.1')    #Ubah jadi 0.0.0.0 biar bisa dibaca semua orang
                                                            #Atau 192.168.20.205 untuk jadi IP LAN BDV ane
parser.add_argument('-p', '--port', default=5000, type=int)
args = parser.parse_args()

app.run(host = args.host, port = args.port, debug = True)
