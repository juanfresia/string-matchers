BASE = 3

from string_encoder import encode_string

asciiConv = {}


def test_string_matching():
    # 0         1         2         3
    # 012345678901234567890123456789012345678
    T = "HOLA ESTO ES UN STRING DE PRUEBA. HOLA."
    P1 = "ES"
    P2 = "HOLA"
    # 012345
    T2 = "AAZAAA"
    P3 = "AA"
    T3 = "ABABZABABAB"
    P4 = "AB"

    print(karpRabin(T, P1))
    print(karpRabin(T, P2))
    print(karpRabin(T2, P3))
    print(karpRabin(T3, P4))


def ascii(letra):
    conv = asciiConv.get(letra, None)
    if (not conv):
        conv = ord(letra)
        asciiConv[letra] = conv
    return conv


def cadenaAAscii(cadena):
    asciis = []
    for letra in cadena:
        asciis.append(ascii(letra))
    return asciis


def hash(texto, ini, fin, hash_ant, base, mod):
    if (ini == 0):
        h = 0
        for x in range(fin):
            h = (base*h+texto[x]) % mod
        return h % mod
    viejaLetra = ((texto[ini - 1]) * base ** (fin - ini - 1)) % mod
    return (base * (hash_ant - viejaLetra) + (texto[fin - 1])) % mod

def cmpSubLista(patron, lista, inicio):
    for x in range(len(patron)):
        if patron[x] != lista[inicio+x]:
            return False
    return True

def karpRabin(texto, patron):
    matches = []
    patron = encode_string(patron)
    texto = encode_string(texto)
    hash_patron = hash(patron, 0, len(patron), 0, BASE, 1000)
    hash_tent = 0

    colisiones = 0

    for x in range(len(texto) - (len(patron) - 1)):
        hash_tent = hash(texto, x, x + len(patron), hash_tent, BASE, 1000)
        if (hash_tent == hash_patron):
            if (cmpSubLista(patron, texto, x)):
                matches.append(x)
            else:
                colisiones += 1
    if colisiones > 0:
        print("malditas colisiones!!: ", colisiones)
        print("cantidad de subcadenas: ", len(texto)-(len(patron) - 1))
    return matches


if __name__ == '__main__':
    test_string_matching()
