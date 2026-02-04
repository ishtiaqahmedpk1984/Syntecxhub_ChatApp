import subprocess		            # for sub process like clear screen 
import sys				            # for exceptions handling
import time                         # for time using in script
import socket                       # for socket connectivity
from Crypto.Cipher import AES   # for advance encryption system
import base64
KEY = b'abcdefghijklmnopqrstuvwxyz123456'    # 32 bytes for AES
IV = b'1234567890abcedf'                     # 16 bytes for IV

#clear all text from screen
subprocess.call('clear', shell=True)
print("="*60)							# print = 60 times on console
print(" "*20,"SYNTECXHUB CHATAPP")		# print ARCH TECHNOLOGIES on console
print("="*60)

def encrypt_message(msg):                               # function to encrypt the message  
    cipher = AES.new(KEY, AES.MODE_CBC, IV)             # AES.new(...): This initializes the AES algorithm, KEY: The secret 32-byte key used for AES-256.IV (Initialization Vector) A "starting point" for the first block
    encrypted = cipher.encrypt(msg.encode('utf-8'))     # .encode('utf-8'): AES cannot encrypt "text"; it only understands "bytes." This converts your string into binary.
    return base64.b64encode(encrypted).decode('utf-8')  # Encrypted data is "raw binary" and contains characters that might break a network connection or be unprintable. Base64 turns that binary into safe, readable characters (A-Z, 0-9, etc.)

try:
    serverAddress = input("Enter Server Address : ")                        # Enter server address
    # CREATE TCP SOCKET
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # create socket connection
    client_socket.connect((serverAddress, 5000))
	
    message = "Hello"
	
    while message != "quit":
        message = input("Enter Message (max 16 characters) / quit to exit: ")
        encrypted_msg = encrypt_message(message.ljust(16))
        print(f"Encrypted message send by cleint is : {encrypted_msg}")
        client_socket.sendall(encrypted_msg.encode())
    else:
        encrypted_msg = encrypt_message(message.ljust(16))
        print(f"Encrypted message send by cleint is : {encrypted_msg}")
        client_socket.sendall(encrypted_msg.encode())
        print("Exiting ... ")
        time.sleep(3)
        sys.exit()
   
except KeyboardInterrupt:
	print ("You pressed Ctrl + C")
	sys.exit()
	
except socket.gaierror:
	print ("Hostname could not be resolved. Exiting ... ")
	sys.exit()
	
except socket.error:
	print ("Could not connect to server.")
	sys.exit()

client_socket.close()
