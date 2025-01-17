from bitcoinlib.wallets import Wallet

'''
Melhorias a serem implementadas:
    - testes automatizados pyTestes
    - Argparser nas chamadas do arquivo
    - Interface gráfica com alguma lib do python
'''


# INSIRA AS 24  PALAVRAS AQUI EM BAIXO
seed = ""

'''
Caso queira um nome diferente alterar o campo
Caso queira a seed ou até a chave privada colocar no campo
Importante, escolher também qual o tipo da rede que voce vai operar segwit, etc...
'''

wallet = Wallet.create('nome', keys=seed, network='bitcoin', witness_type='segwit')

# Derive o primeiro endereço de recebimento
receiving_address = wallet.get_key().address

print("Primeiro endereço de recebimento (SegWit):", receiving_address)

# Opcional: Derivar múltiplos endereços
for i in range(5):  # Por exemplo, 5 endereços
    addr = wallet.get_key(i).address
    print(f"Endereço {i}: {addr}")
