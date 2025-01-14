from mnemonic import Mnemonic
from eth_account import Account
import os

mnemo = Mnemonic("english")
seed_frase = mnemo.generate(strength=256)

print("AS 24 PALAVRAS: ", seed_frase, "\n\n\n")

Account.enable_unaudited_hdwallet_features()
conta = Account.create(seed_frase)

print("ENDEREÇO ETHERIUM: ", conta.address, "\n\n")

print("CHAVE PRIVADA: ", conta.key.hex(), "\n\n")
