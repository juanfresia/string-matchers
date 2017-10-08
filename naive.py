from string_encoder import encode_string


def test_string_matching():
    # 0         1         2         3
    # 012345678901234567890123456789012345678
    T = "HOLA ESTO ES UN STRING DE PRUEBA. HOLA."
    P1 = "ES"
    P2 = "HOLA"

    print(string_matching_naive(T, P1))
    print(string_matching_naive(T, P2))


def multi_string_matching_naive(texto, patrones):
    texto = encode_string(texto)
    resultado = []
    for patron in patrones:
        patron = encode_string(patron)
        resultado.append(naive_matching(patron, texto))
    return resultado


def string_matching_naive(texto, patron):
    """Devuelve una lista con las posiciones en texto
    donde aparece patron completo utilizando el algoritmo naive."""

    texto = encode_string(texto)
    patron = encode_string(patron)

    return naive_matching(patron, texto)


def naive_matching(patron, texto):
    matches = []
    for inicio in range(len(texto) - len(patron) + 1):
        match = True
        for act in range(len(patron)):
            if texto[inicio + act] != patron[act]:
                match = False
                break
        if match:
            matches.append(inicio)
    return matches


if __name__ == '__main__':
    test_string_matching()
