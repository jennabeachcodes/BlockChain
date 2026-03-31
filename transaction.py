# Defines a transaction object that will be stored inside a block
class Transaction:

    # Constructor that initializes a transaction with sender, receiver, and amount
    def __init__(self, sender_id, receiver_id, amount):
        self.sender_id = sender_id # Stores the ID of the sender
        self.receiver_id = receiver_id # Stores the ID of the receiver
        self.amount = amount # Stores the amount being transferred

    # Returns a string representation of the transaction
    def __str__(self):
        # Converts the transaction data into a comma-separated string
        return str(self.sender_id) + "," + str(self.receiver_id) + "," + str(self.amount)