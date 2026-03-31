# Defines a block in the blockchain.
# Imports the hashlib library and renames it as 'hashing' for creating hash values
import hashlib as hashing

class Block:

    # Constructor that initializes the block with its basic properties
    def __init__(self, index, timestamp, transaction, previous_hash):
        self.index = index # Stores the position of the block in the blockchain
        self.timestamp = timestamp # Stores the time when the block was created
        self.transaction = transaction # Stores the transaction contained in the block
        self.previous_hash = previous_hash # Stores the hash value of the previous block for chain integrity
        self.hash_value = self.hash() # Calculates and stores the hash value of this block

    # Method that calculates the hash value for the block
    def hash(self):
        hash_fct = hashing.sha256() # Creates SHA-256 hashing object
        hash_fct.update((str(self.index) + # Adds the block index to the data being hashed
                         str(self.timestamp) + # Adds the timestamp to the data being hashed
                         str(self.transaction) + # Adds the transaction information to the data being hashed
                         str(self.previous_hash)).encode('utf-8')) # Adds the previous hash and encodes the data to bytes
        return hash_fct.hexdigest() # Returns the final hexadecimal hash value

    # Method that returns a readable string representation of the block
    def __str__(self):
        return 'Index: ' + str(self.index) + ', Timestamp: ' + str(self.timestamp) + \
               ', Transaction: ' + str(self.transaction) + ', \nPrevious hash: ' + \
               str(self.previous_hash) + ', \nBlock hash value: ' + str(self.hash_value)