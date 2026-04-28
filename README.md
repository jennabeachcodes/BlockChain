# BlockChain

A simple blockchain implementation built in Python, demonstrating the core concepts behind distributed ledger technology, block creation, SHA-256 hashing, chain linking, and tamper detection.

---

## How It Works

Each **block** in the chain contains:
- An index (its position in the chain)
- A timestamp (when it was created)
- A transaction (sender, receiver, and amount)
- The hash of the previous block (linking the chain)
- Its own SHA-256 hash (generated from all of the above)

Because each block's hash depends on the previous block's hash, any modification to a block invalidates every block that follows it. The `validate()` method detects this by recalculating and comparing hashes across the entire chain.

---

## Project Structure

```
BlockChain/
├── block.py          # Defines the Block class and SHA-256 hashing logic
├── blockchain.py     # Defines the Blockchain class — manages blocks and validation
├── transaction.py    # Defines the Transaction class (sender, receiver, amount)
└── main.py           # Demo script — builds a chain, adds transactions, simulates tampering
```

---

## Getting Started

**Requirements:** Python 3.x (no external dependencies)

**Run the demo:**

```bash
python main.py
```

This will:
1. Create a new blockchain with a genesis block
2. Add two transactions as new blocks
3. Print the full chain
4. Validate the chain (passes)
5. Simulate tampering by modifying a transaction
6. Validate again (fails, detecting the change)

---

## Example Output

```
Index: 0, Timestamp: ..., Transaction: 0,0,0,
Previous hash: 0,
Block hash value: ...

Transaction: 12345,23456,100
...

The ledger is authentic
Transaction 1 is being modified...
Validation error at block 1
```

---

## Concepts Demonstrated

- **SHA-256 hashing** via Python's `hashlib`
- **Genesis block** creation
- **Chain integrity** through linked hashes
- **Tamper detection** via hash recomputation and validation

---

## What's Next

Planned improvements:
- Proof-of-work (mining) to simulate real blockchain difficulty
- Multiple transactions per block
- Peer-to-peer network simulation
- Improved CLI output and error reporting

---

## License

This project is provided for educational purposes only as part of the course 26W-CST8400 - Analysis and Design Using Emerging Technologies at Algonquin College, Ottawa, ON, Canada.

