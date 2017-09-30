BASE = 101

def test_string_matching():
        #0         1         2         3
        #012345678901234567890123456789012345678
    T = "HOLA ESTO ES UN STRING DE PRUEBA. HOLA."
    P1 = "ES"
    P2 = "HOLA"
         #012345
    T2 = "AAZAAA"
    P3 = "AA"
    T3 = "ABABZABABAB"
    P4 = "AB"

    print(karpRabin(T, P1))
    print(karpRabin(T, P2))
    print(karpRabin(T2, P3))
    print(karpRabin(T3, P4))

def hash(texto, ini, fin, hash_ant):
    if (ini == 0):
        h = 0
        for x in range(fin):
            h += ord(texto[x]) * BASE**(fin-1-x)
        return h
    return (BASE * (hash_ant - (ord(texto[ini-1]) * BASE**(fin-ini-1))) + ord(texto[fin-1]))


def karpRabin(texto, patron):
    matches = []
    hash_patron = hash(patron, 0, len(patron), 0)
    hash_tent = 0

    for x in range(len(texto)-(len(patron)-1)):
        hash_tent = hash(texto, x, x+len(patron), hash_tent)
        if ((hash_tent == hash_patron) and (patron == texto[x:x+len(patron)])):
            matches.append(x)

    return matches


test_string_matching()
