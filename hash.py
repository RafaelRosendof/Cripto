import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def chave(senha: str) -> bytes:
    figas = hashlib.sha256(senha.encode()).digest()

    print("Chave: ", figas)

    return figas

def criptografar(dados: str, senha: str) -> str:
    key = chave(senha)
    iv = get_random_bytes(16) #vetor de inicialização
    cipher = AES.new(key, AES.MODE_CBC, iv)

    dados_p = pad(dados.encode() , AES.block_size)
    cripto = cipher.encrypt(dados_p)

    return base64.b64encode(iv + cripto).decode('utf-8')


def descriptografar(dados_criptografados: str, senha: str) -> str:
    key = chave(senha)

    dados = base64.b64decode(dados_criptografados)

    iv = dados[:16]

    cripto = dados[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    dados_descr = unpad(cipher.decrypt(cripto), AES.block_size)

    return dados_descr.decode('utf-8')


#TODO -> Implementar a lógica da main
def main():

    senha = ''
    palavras = ""

    chave(senha)


if __name__ == "__main__":
    main()
