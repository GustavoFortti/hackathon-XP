import datetime, hashlib, json, time
from random import randint
from fake_openfinance import gen_distinct, gen_stock

class Blockchain:
    def __init__(self):
        self.chain = []
        self.users = []
        self.mem_pool = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'data_transaction': self.mem_pool,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.mem_pool = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof, check_proof= (1, False)
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if ['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            previous_block += 1
        return True

    def mine_block(self):
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        block = self.create_block(proof, previous_hash)

    def search_data(self, user):
        dados_usuario = [block["data_transaction"] for block in self.chain]
        return dados_usuario

    def operate_data(self, data, user, permission):
        print("DATA ", type(data))
        print("USERNAME", user)
        data["permission"] = permission
        self.mem_pool.append(data)
        return data

    def start_share_data(self, user, permission, data):
        result = dict(
        name = hashlib.sha256(user.encode()).hexdigest(),
        permission = permission,
        stock_operations = data
        )
        self.users.append(result["name"])
        self.mem_pool.append(result)
        return result


    def track_user_data(self, permission):
        if len(self.users) > 0:
            user_list = [hashlib.sha256(name.encode()).hexdigest() for name in self.users]
            for i in range(5):
                result = dict(
                permission = permission,
                stock_operation = gen_stock(initial_offer=False, names=user_list)
                )
                result["name"] = gen_distinct(user_list)
            self.mem_pool.append(result)

        return self.mem_pool

    def get_user_data_from_chain(self, user):
        # função que percorre o blockchain
        pass
