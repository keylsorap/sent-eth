from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Infura URL and private key from the environment variables
infura_url = os.getenv('INFURA_URL')
private_key = os.getenv('PRIVATE_KEY')

# Debugging prints to verify loading
if infura_url is None:
    print("Infura URL tidak ditemukan. Periksa file .env Anda.")
else:
    print(f"Infura URL: {infura_url}")

if private_key is None:
    print("Private key tidak ditemukan. Periksa file .env Anda.")
else:
    print(f"Private Key: {private_key}")

# Create a Web3 instance with the Infura URL
web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.is_connected():
    print("Berhasil terhubung ke jaringan Ethereum")
    
    # Alamat pengirim (harus sesuai dengan alamat dari private key)
    from_address = "0x. . ."
    
    # Alamat penerima
    to_address = "0x. . ."
    
    # Jumlah ETH yang akan dikirim (dalam Ether)
    value = web3.to_wei(0.01, 'ether')
    
    # Nonce (nomor transaksi) untuk alamat pengirim
    nonce = web3.eth.get_transaction_count(from_address)
    
    # Membangun transaksi
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': value,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei')
    }
    
    # Menandatangani transaksi dengan private key
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    
    # Mengirimkan transaksi
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    # Menampilkan hash transaksi
    print(f"Transaksi berhasil dikirim! Hash transaksi: {tx_hash.hex()}")
    
    # Memeriksa status transaksi
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    if receipt.status == 1:
        print(f"Transaksi berhasil! Receipt: {receipt}")
    else:
        print(f"Transaksi gagal. Receipt: {receipt}")
else:
    print("Gagal terhubung ke jaringan Ethereum")
