import qrcode


'''
public_key = "Zpub74wNmic8UDaTpqpEuZ39YRBtdhUER7koiAy3W7EgQ8UzuYsnVWi7MJF8D1F4QJh33BeWqSCw5kgVGZ7j18iUE2svCWkKGe5gB8xv5h9mWZx"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(public_key)
qr.make(fit=True)

img = qr.make_image(fill="black" , back_colors="white")

img.save("publica.png")

print("Deu bom ")
'''

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


#def criptografar(stringAlvo, output_name):


def main():
    public_key = "Zpub74wNmic8UDaTpqpEuZ39YRBtdhUER7koiAy3W7EgQ8UzuYsnVWi7MJF8D1F4QJh33BeWqSCw5kgVGZ7j18iUE2svCWkKGe5gB8xv5h9mWZx"

    gerador(public_key, "chave_publica" )

if __name__ == "__main__":
    main()
