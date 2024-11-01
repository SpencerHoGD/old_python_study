"""
SnakeCoin
"""

import hashlib
from datetime import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        # self.previous_hash = previous_hash.encode('utf-8')
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index) + 
                   str(self.timestamp) +
                   str(self.data) + 
                #    str(self.previous_hash))
                   str(self.previous_hash).encode('ascii'))
        return sha.hexdigest()

    # def hash_block(self):
    #     sha = hashlib.sha256()
    #     sha.update(str(self.index))
    #     sha.update(str(self.timestamp))
    #     sha.update(str(self.data))
    #     sha.update(self.previous_hash)
    #     return sha.hexdigest()


def creat_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, datetime.now(), "Genesis Block", "0")


def next_block(previous_block):
    this_index = previous_block.index + 1
    this_timestamp = datetime.now()
    this_data = "Hey! I'm block" + str(this_index)
    this_hash = previous_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


def main():
    # Creat the blockchain and add the genesis block
    blockchain = [creat_genesis_block()]
    previous_block = [blockchain(0)]

    # How many blocks should we add to the chain
    # after the genesis block
    num_of_block_to_add = 20

    # Add blocks to the chain
    for i in range(0, num_of_block_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Tell everyone about it!
        print(f"Block #{block_to_add.index} has been added to the blockchain!")
    print(f"Hash: {block_to_add.hash}")


if __name__ == '__main__':
    main()
