# streamlit_app.py

import streamlit as st
import hashlib
import datetime

# Initialize blockchain
blockchain = []

def calculate_hash(data, timestamp, previous_hash):
    return hashlib.sha256(f"{data}{timestamp}{previous_hash}".encode()).hexdigest()

def create_block(data, previous_hash="None"):
    timestamp = str(datetime.datetime.now())
    block_hash = calculate_hash(data, timestamp, previous_hash)
    block = {
        "data": data,
        "timestamp": timestamp,
        "previous_hash": previous_hash,
        "hash": block_hash
    }
    return block

# Streamlit app
st.title("Simple Blockchain Demo")

# Initialize blockchain with a button
if st.button("Initialize Blockchain"):
    blockchain.clear()
    first_block = create_block("Ticket-1")
    blockchain.append(first_block)
    second_block = create_block("Ticket-2", previous_hash=first_block['hash'])
    blockchain.append(second_block)
    third_block = create_block("Ticket-3", previous_hash=second_block['hash'])
    blockchain.append(third_block)

# Display blockchain
if blockchain:
    st.subheader("Blockchain Content:")
    for idx, block in enumerate(blockchain):
        st.markdown(f"### Block {idx + 1}")
        st.json(block)
else:
    st.info("Click the 'Initialize Blockchain' button to create blocks.")
