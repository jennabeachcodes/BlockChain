# Imports the Blockchain class used to create and manage the ledger
from blockchain import Blockchain
# Imports the Transaction class used to create transactions
from transaction import Transaction

def main():
    ledger = Blockchain() # Creates a new blockchain object (the ledger)
    print(ledger) # Prints the current blockchain (initially only the Genesis block)

    # Create the first transaction where user 12345 sends 100 to user 23456
    transaction = Transaction(12345, 23456, 100)
    print(transaction) # Prints the transaction details

    block = ledger.create_block(transaction) # Creates a new block containing the transaction
    ledger.add_block(block) # Adds the new block to the blockchain
    print(ledger) # Prints the updated blockchain with the new block

    # Create the second transaction where user 34567 sends 150 to user 45678
    transaction2 = Transaction(34567, 45678, 150)
    print(transaction2) # Prints the transaction details

    block2 = ledger.create_block(transaction2) # Creates a block for the second transaction
    ledger.add_block(block2) # Adds the second block to the blockchain
    print(ledger) # Prints the blockchain showing all three blocks

    ledger.validate() # Calls the validate method to check if the blockchain is still authentic

    # Messing with the ledger to simulate tampering
    print('Transaction 1 is being modified...') # Displays a message indicating the blockchain is being altered

    # Changes the transaction in block 1 to simulate fraudulent modification
    ledger.blocks[1].transaction = Transaction(12345, 23456, 200)

    ledger.validate() # Runs validation again, which should now detect the tampering

# Ensures the main function runs only when this script is executed directly
if __name__ == '__main__':
    main()