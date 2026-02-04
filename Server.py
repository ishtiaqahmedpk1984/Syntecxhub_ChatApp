import subprocess		#for sub process like clear screen 
import sys				#for exceptions handling
import time
import socket
from Cryptodome.Cipher import AES
import base64
KEY = b'abcdefghijklmnopqrstuvwxyz123456'    # 32 bytes for AES
IV = b'1234567890abcedf'                     # 16 bytes for IV

#clear all text from screen
subprocess.call('clear', shell=True)
print("="*60)							# print = 60 times on console
print(" "*20,"SYNTECXHUB CHATAPP")		# print ARCH TECHNOLOGIES on console
print("="*60)

def decrypt_message(enc_msg):                   # Defing a function to decrypt message
    encrypted_data = base64.b64decode(enc_msg)  #This line converts that "readable" Base64 text back into the raw, "unreadable" binary bytes that the AES algorithm requires.
    cipher = AES.new(KEY, AES.MODE_CBC, IV)     # This creates a new AES cipher object. It must use the exact same KEY (32 bytes), the same Mode (Cipher Block Chaining), and the same IV (Initialization Vector) that were used to encrypt the message, otherwise, decryption will fail.
    decrypted = cipher.decrypt(encrypted_data)  # This is the core step where the AES algorithm uses the Key and IV to mathematically reverse the encryption on the binary data. The output (decrypted) is still in byte format.
    return decrypted.decode('utf-8')            # This converts the raw decrypted bytes back into a human-readable string using UTF-8 encoding so you can print it or display it on the console.

try:

    # CREATE TCP SOCKET
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # socket.socket(): This creates the actual communication endpoint, AF_INET: This tells the system to use IPv4 addresses
    server_socket.bind(("0.0.0.0", 5000))       # recive connection from external sources
    server_socket.listen(3)                     # Open doors and allows 3 person to wait in line
    print("Server listening on port 5000 ... ")
    conn, addr = server_socket.accept()         # When the code reaches this line, it pauses (blocks). It will sit there and wait until a client (like your Kali machine) attempts to connect. Once a connection is made, it returns two distinct pieces of information:
                                                # conn to send and receive the actual encrypted data (conn.recv() and conn.send()), not the original server_socket
                                                # addr (The Address Information),Client's IP address and their Random Port number i.e ('192.168.56.102', 45230)
    print(f"Connected by {addr}")
    decoded_data = "3OPKgyqXqwNqBZN89V8dsR=="
    
    while decoded_data != "3OPKgyqXqwNqBZN89V8dsQ==":
        data = conn.recv(1024)                  # Receive 1024 bytes at once
        decoded_data = data.decode()
        print(f"Encrypted Data received by server is: {decoded_data}")
        decrypted_text = decrypt_message(decoded_data)
        print(f"After decryption, message is : {decrypted_text}")
    else:
          print("Exiting ..... ")
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

conn.close()                            # close the connection
server_socket.close()


