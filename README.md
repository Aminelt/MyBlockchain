# Blockchain Application

## Overview
This project implements a simple **blockchain** with a RESTful API for interaction. The blockchain supports creating blocks, mining, and recording transactions. It is built using Python and Flask.

---

## Features
- **Blockchain Management**:
  - Append new blocks to the chain.
  - Retrieve the full blockchain.
- **Mining**:
  - Implements proof-of-work (PoW) for block validation.
  - Rewards miners with a default token.
- **Transactions**:
  - Records sender, recipient, and amount for each transaction.
  - Adds pending transactions to a new block upon mining.

---

## Requirements
- Python 3.8+
- Flask
- Requests

Install dependencies:
```bash
  pip install Flask requests
```

## API Endpoints

1. **Get Blockchain**  
   - **URL**: `/blockchain`  
   - **Method**: `GET`  
   - **Description**: Retrieve the entire blockchain.  
   - **Response**:  
     ```json
     {
       "chain": [...],
       "length": <number_of_blocks>
     }
     ```
2. **Mine a Block**  
   - **URL**: `/mine`  
   - **Method**: `GET`  
   - **Description**: Perform proof-of-work to mine a new block.  
   - **Response**:  
     ```json
     {
       "message": "New Block Mined",
       "index": <block_index>,
       "hash_of_previous_block": <previous_block_hash>
     }
     ```

3. **Add Transaction**  
   - **URL**: `/transactions/new`  
   - **Method**: `POST`  
   - **Payload**:  
     ```json
     {
       "sender": "<sender_address>",
       "recipient": "<recipient_address>",
       "amount": <amount>
     }
     ```  
   - **Description**: Record a new transaction to be added to the next block.  
   - **Response**:  
     ```json
     {
       "message": "Transaction will be added to Block <block_index>"
     }
     ```

 ##  Disclaimer
  This is a simple blockchain prototype designed for educational purposes. It is not secure for production use.
  
