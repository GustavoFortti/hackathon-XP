import datetime, hashlib, json, time


class Blockchain:
    def __init__(self):
        self.chain = []
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

    def operate_data(self, user, permission):
        f = open('./users.json')
        data = json.load(f)
        f.close()
        result = list(filter(lambda x: x["name"] == user, data))[0]
        result["permission"] = permission
        self.mem_pool.append(result)
        return list(filter(lambda x: x["name"] == user, data))


    def get_user_data_from_chain(self):
        # função que percorre o blockchain
        pass

 
if __name__ == '__main__':

    blockchain = Blockchain()


    print(blockchain.chain)

    blockchain.mine_block()
    time.sleep(5)
    print(blockchain.chain)
    
    blockchain.operate_data("MARCO", True)
    blockchain.operate_data("HENRIQUE", True)
    # dados caem no mem_pool a cima e abaixo são minerados
    blockchain.mine_block()
    time.sleep(3)
    print(blockchain.chain)

    blockchain.operate_data("GUSTAVO", True)
    blockchain.operate_data("LEO", True)
    # dados caem no mem_pool a cima e abaixo são minerados
    blockchain.mine_block()
    time.sleep(3)
    print(blockchain.chain)

    blockchain.operate_data("MARCO", False)
    blockchain.operate_data("HENRIQUE", False)
    # dados caem no mem_pool a cima e abaixo são minerados
    blockchain.mine_block()
    time.sleep(3)
    print(blockchain.chain)