from cryptography.fernet import Fernet
import base64
import qrcode
from bitcoinlib.wallets import Wallet
import argparse
from typing import List
from mnemonic import Mnemonic
from eth_account import Account


###Parde do etherium 

''' 
mnemo = Mnemonic("english")
seed_frase = mnemo.generate(strength=256)

print("AS 24 PALAVRAS: ", seed_frase, "\n\n\n")

Account.enable_unaudited_hdwallet_features()
conta = Account.create(seed_frase)

print("ENDEREÇO ETHERIUM: ", conta.address, "\n\n")

print("CHAVE PRIVADA: ", conta.key.hex(), "\n\n")
'''



### Código QR

def gerador(stringAlvo, output_name):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )

    qr.add_data(stringAlvo)

    qr.make(fit=True)

    img = qr.make_image(fill="black" , back_colors="white")

    img.save(f"{output_name}.png")

    print("Deu bom ")

 
### Gerador de chaves públicas

def gerador(
    seed_frase: str,
    carteiraName: str,
    network: str= "bitcoin",
    wtness_type: str = "segwit",
    num_add: int = 5
)-> List[str]:

    try:
        wallet = Wallet.create(
            carteiraName,
            keys=seed_frase,
            network=network,
            witness_type=wtness_type
        )

        lista = []

        for i in range(num_add):
            key = wallet.get_key(i)
            lista.append(key.address)

        return lista

    except Exception as e:
        raise Exception(f"Error generating wallet: {str(e)}")





### Parte de criptografia 

def gerar_chave(senha: str) -> bytes:
    return base64.urlsafe_b64encode(senha.encode('utf-8').ljust(32)[:32])

def criptografar(dados: str, senha: str) -> str:
    chave = gerar_chave(senha)
    fernet = Fernet(chave)
    return fernet.encrypt(dados.encode()).decode()

def descriptografar(dados_criptografados: str, senha: str) -> str:
    chave = gerar_chave(senha)
    fernet = Fernet(chave)
    return fernet.decrypt(dados_criptografados.encode()).decode()

def geradorPalavras(seed_frase,senha) -> str:
    #senha = getpass.getpass("Digite uma senha: ")
    antes = seed_frase
    chavePa = criptografar(seed_frase , senha)

    print("Chave anterior: ", antes, "\n")
    print("Senha utilizada: ", senha , "\n")
    print("Chave depois: ", chavePa, "\n")
    return chavePa

def geradorPrivate(private_key,senha) -> str:
    #senha = getpass.getpass("Digite uma senha: ")
    antes = private_key
    chavePr = criptografar(private_key, senha)

    print("Chave anterior: ", antes , "\n\n")
    print("Senha utilizada: ", senha , "\n\n")
    print("Chave depois: ", chavePr , " \n\n")
    return chavePr

def descriptografarPalavras(seed_frase, senha) -> str:
    antes = seed_frase
    chavePa = descriptografar(seed_frase, senha)

    print("Chave anterior: ", antes , "\n\n")
    print("Senha utilizada: ", senha , "\n\n")
    print("Chave depois: ", chavePa , " \n\n")

    return chavePa

def descriptografarPrivate(private_key, senha) -> str:
    antes = private_key
    chavePr = descriptografar(private_key, senha)

    print("Chave anterior: ", antes , "\n\n")
    print("Senha utilizada: ", senha , "\n\n")
    print("Chave depois: ", chavePr , " \n\n")

    return chavePr

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-S', '--palavras', type=str  , help=" 12 Palavras ")
    parser.add_argument('-P', '--senha-privada',  type=str, help="Senha privada ")
    parser.add_argument('-SC', '--palavras_codi',  type=str, help="Palarvas codificadas  ")
    parser.add_argument('-PC', '--senha_codi',  type=str, help="Senha privada codificada ")
    parser.add_argument('-K', '--senhaNormal', required=True , type=str , help="Senha para criptografar e reverso ")

    parser.add_argument('-T', '--tipo' , required=True , choices=[
        "criptoPalavras",
        "criptoChavePrivada",
        "descriptoPalavras",
        "descriptoPrivada"

    ] , help = "Tipo de operação para fazer ")

    args = parser.parse_args()



    choice = args.tipo

    if choice == "criptoPalavras":
        geradorPalavras(args.palavras ,args.senhaNormal)


    elif choice == "criptoChavePrivada":
        geradorPrivate(args.senha_privada , args.senhaNormal)

    elif choice == "descriptoPalavras":
        descriptografarPalavras(args.palavras_codi , args.senhaNormal)

    else:
        descriptografarPrivate(args.senha_codi , args.senhaNormal)

    print("Deu certo, precisar de mais algo é só falar: ")



if __name__ == "__main__":
    main()
