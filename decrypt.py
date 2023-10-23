import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)

    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        previous_chunk = b''
        while True:
            chunk = infile.read(16)
            if len(chunk) == 0:
                break
            decrypted_chunk = cipher.decrypt(chunk)
            outfile.write(unpad(decrypted_chunk, 16))
            previous_chunk = chunk

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python decrypt_file.py arquivo_criptografado arquivo_descriptografado chave")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    key = sys.argv[3].encode('utf-8')

    if len(key) != 16:
        print("A chave deve ter 16 caracteres.")
        sys.exit(1)

    decrypt_file(input_file, output_file, key)
    print("Arquivo descriptografado com sucesso!")
