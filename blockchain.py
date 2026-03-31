# This class defines the blockchain implementation.
# Imports the Block class used to create blocks in the blockchain
from block import Block
# Imports the Transaction class used to create transactions
from transaction import Transaction
# Imports the datetime module and renames it as 'date' for timestamps
import datetime as date

class Blockchain:

    # Constructor that initializes the blockchain
    def __init__(self):
        self.blocks = [] # Creates an empty list that will store all blocks in the chain
        self.create_genesis_block() # Calls the method to create the first block (Genesis block)

    # Creates the first block of the blockchain
    def create_genesis_block(self):
        # Creates a Genesis block with default transaction values and a previous hash of "0"
        genesis = Block(0, date.datetime.now(), Transaction(0, 0, 0), previous_hash="0")
        self.blocks.append(genesis) # Adds the Genesis block to the blockchain

    # Returns the last block in the blockchain
    def last_block(self):
        return self.blocks[-1]  # Retrieves the most recently added block in the chain

    # Creates a new block using a given transaction
    def create_block(self, transaction):
        # Creates a block with the next index, current timestamp, the transaction, and the previous block's hash
        block = Block(self.last_block().index + 1, date.datetime.now(), transaction, self.last_block().hash())
        return block # Returns the newly created block

    # Adds a block to the blockchain
    def add_block(self, block_to_add):
        self.blocks.append(block_to_add) # Appends the block to the list of blocks

    # Returns a string representation of the entire blockchain
    def __str__(self):
        description = '' # Creates an empty string to store the blockchain description
        for b in self.blocks: # Iterates through each block in the blockchain
            description += str(b) + '\n' # Adds the string representation of each block to the description
        return description # Returns the complete blockchain description

    # Validates the integrity of the blockchain
    def validate(self):
        for i in range(len(self.blocks)): # Iterates through each block in the blockchain

            current_block = self.blocks[i] # Stores the current block being checked

            # Check if the stored hash matches the recalculated hash
            if current_block.hash_value != current_block.hash():
                print("Validation error!!") # Prints an error message if the hash values do not match
                return 1 # Stops execution and returns an error code

            # Skip previous hash verification for the Genesis block
            if i > 0:
                previous_block = self.blocks[i - 1] # Retrieves the previous block in the chain

                # Check if the previous_hash value matches the actual hash of the previous block
                if current_block.previous_hash != previous_block.hash():
                    print("Validation error!!") # Prints an error message if the chain integrity is broken
                    return 1 # Stops execution and returns an error code

        print("The ledger is authentic") # Prints confirmation if all blocks pass validation