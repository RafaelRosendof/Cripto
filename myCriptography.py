import argparse
from typing import List



'''

Palavra -> "figas"

get the assic value of each word

permute with 4 or 5 operations or 10 even whatever

each password get his value exemple -> rafael get value 50 so we can operate in this scenario by each word permute one operation



'''

def addF(senha ,  arr):
    '''
    Get the key pass for a number and add for each item in the array skip the * and &
    '''
    acc = 0
    for i in senha:
        acc += ord(i)

    print(f"O valor retornado da senha: {senha} resultou: {acc}")

    for i in range(len(arr)):
        if arr[i] == "*" or arr[i] == "&":
            continue

        arr[i] += acc

def ReverseF(senha , arr):
    ''' Revert the add function'''

    acc = 0
    for i in senha:
        acc += ord(i)

    print(f"O valor retornado da senha: {senha} resultou em : {acc}")

    for i in range(len(arr)):
        if arr[i] == "*" or arr[i] == "&":
            continue
        arr[i] -= acc

def subMethod(senha , arr):
    acc = 0

    for i in senha:
        acc += ord(i)

    print(f"\n\n Senha gerada pela operação de subtração {senha} resultou em: {acc}")

    for i in range(len(arr)):
        if arr[i] == "&" or arr[i] == "*":
            continue
        arr[i] -= acc

def inverseSub(senha , arr):
    acc = 0

    for i in senha:
        acc += ord(i)

    for i in range(len(arr)):
        if arr[i] == "&" or arr[i] == "*":
            continue
        arr[i] += acc


def multiplyMethod(senha , arr):
    acc = 0

    for i in senha:
        acc += ord(i)

    print(f"\n\nSenha gerada pela operação de multiplicação {senha} resultou em : {acc}")

    for i in range(len(arr)):
        if arr[i] == "&" or arr[i] == "*":
            continue
        arr[i] *= acc


def inverseMultiply(senha , arr):

    acc = 0

    for i in senha:
        acc += ord(i)

    print(f"\n\nSenha gerada pela operação de multiplicação {senha} resultou em : {acc}")

    for i in range(len(arr)):
        if arr[i] == "&" or arr[i] == "*":
            continue
        #arr[i] /= acc
        arr[i] = int(arr[i] / acc)


def getAssic(word , array):
    array.append("&")
    for i in word:
        array.append(ord(i))

    array.append("*")

def getString(array):
    word = ""

    for i in array:
        if i == "&":
            word += " "
        elif i == "*":
            word += " "
        else:
            word += chr(i)

    return word


def printaArr(array):
    for i in array:
        print(i , end=" ")
    print()

def main():
    arr = []
    palavras = ['seed' , 'ola' , 'rafael' , 'caro']

    x = lambda word : getAssic(word, arr)

    for i in palavras:
        x(i)

    print("     Original     ")
    printaArr(arr)

    print("\n\n:::     Somador   :::")

    addF("rafinha" , arr)

    printaArr(arr)

    print("\n\n :::     Reverso     :::")
    ReverseF("rafinha", arr)

    printaArr(arr)


    print("\n\n :::     Multiplicador       :::")

    multiplyMethod("rafinha" , arr)

    printaArr(arr)

    print("\n\n         Desvendando Multiplicador       :::")

    inverseMultiply("rafinha", arr)

    printaArr(arr)

    print(":::      Voltando ao normal      :::")


    arr2 = getString(arr)
    printaArr(arr2)

    palau = [
        "apple",
        "banana",
        "crystal",
        "dolphin",
        "elephant",
        "forest",
        "guitar",
        "honey",
        "island",
        "jungle",
        "kangaroo",
        "lighthouse"
    ]
    infoCripto = []

    '''
    Lets gonna do some exemple to encrypt this bitcoin seed the order is gonna be

    times / add / add / sub / add / add / times
    '''

    x1 = lambda word : getAssic(word , infoCripto)

    for i in palau:
        x1(i)

    print("\n\n:::  Original INFO CRIPTOCURRENCY    ::: ")
    printaArr(infoCripto)

    multiplyMethod("rafinha19", infoCripto)
    addF("figas",infoCripto)
    addF("fitz",infoCripto)
    subMethod("Rofinaldo", infoCripto)
    addF("cachorrão", infoCripto)
    addF("çhow",infoCripto)
    multiplyMethod("letícia",infoCripto)

    print("     Array criptografado      :::")

    printaArr(infoCripto)

    print("\n\n Descriptografando as palavras \n\n")

    inverseMultiply("letícia", infoCripto)
    ReverseF("çhow",infoCripto)
    ReverseF("cachorrão",infoCripto)
    inverseSub("Rofinaldo",infoCripto)
    ReverseF("fitz",infoCripto)
    ReverseF("figas",infoCripto)
    inverseMultiply("rafinha19", infoCripto)


    arr3 = getString(infoCripto)
    printaArr(arr3)



if __name__ == "__main__":
    main()


'''
12 ( a , b , c , d, e)

11 ( c , d , g , h)

'''
