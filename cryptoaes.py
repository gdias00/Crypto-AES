import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while True:
            chunk = infile.read(16)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk = pad(chunk, 16)  # Preenchimento PKCS7
            encrypted_chunk = cipher.encrypt(chunk)
            outfile.write(encrypted_chunk)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python encrypt_file.py arquivo_original arquivo_criptografado chave")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    key = sys.argv[3].encode('utf-8')

    if len(key) != 16:
        print("A chave deve ter 16 caracteres.")
        sys.exit(1)

    encrypt_file(input_file, output_file, key)
    print("Arquivo criptografado com sucesso!")
