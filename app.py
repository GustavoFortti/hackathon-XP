# -*- coding: utf-8 -*-

from xmlrpc.client import boolean
from flask import  Flask, jsonify, request
from uuid import uuid4
from xp_blockchain import Blockchain
import os
from request_api.get_token import GetToken
from request_api.make_requests import MakeRequests
import json

credentials = {
  'client_id': os.getenv('CLIENT_ID'),
  'client_secret': os.getenv('CLIENT_SECRET')
}

node_address = str(uuid4()).replace('-', '')

app = Flask(__name__)
blockchain = Blockchain()

token = GetToken(
  credentials["client_id"],
  credentials["client_secret"]
).access_token
requests = MakeRequests(token, credentials)


@app.route("/user_auth", methods = ['POST'])
def user_auth():
  req_data = request.get_json()
  authorized = req_data["authorized"]

  if authorized and type(authorized) == bool:
    response = requests.try_request(requests.users, 1)
    return jsonify(json.loads(response.text))
  else:
    pass
    return jsonify("User did not authorize data sharing")

@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Parabéns, você minerou um bloco!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

app.run(host='0.0.0.0', port=5000)