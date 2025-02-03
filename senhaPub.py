from bitcoinlib.wallets import Wallet
import argparse
from typing import List

'''
Melhorias a serem implementadas:
    - testes automatizados pyTestes
    - Argparser nas chamadas do arquivo
    - Interface gráfica com alguma lib do python
'''

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


def main():
    parser = argparse.ArgumentParser(description='Generate Bitcoin wallet addresses')
    parser.add_argument('--seed', type=str, help='Seed phrase for wallet generation')
    parser.add_argument('--name', type=str, default='default_wallet', help='Wallet name')
    parser.add_argument('--network', type=str, default='bitcoin', help='Network type')
    parser.add_argument('--witness-type', type=str, default='segwit',
                       help='Address type (segwit, legacy)')
    parser.add_argument('--num-addresses', type=int, default=5,
                       help='Number of addresses to generate')

    args = parser.parse_args()

    if not args.seed:
        print("Error: Seed phrase is required")
        return

    try:
        addresses = gerador(
            args.seed,
            args.name,
            args.network,
            args.witness_type,
            args.num_addresses
        )

        print(f"\nWallet Name: {args.name}")
        print(f"Network: {args.network}")
        print(f"Address Type: {args.witness_type}")
        print("\nGenerated Addresses:")
        for i, addr in enumerate(addresses):
            print(f"Address {i}: {addr}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
