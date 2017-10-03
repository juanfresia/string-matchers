def test_string_matching():
    # 0         1         2         3
    # 012345678901234567890123456789012345678
    T = "HOLA ESTO ES UN STRING DE PRUEBA. HOLA."
    P1 = "ES"
    P2 = "HOLA"

    T2 = "AAZAAAA"
    P3 = "AA"


    T3 = "c" * 499 + "b" * 50 + "c" * 499 + "b" * 453 + "c" * 499
    P4 = "a" * 500
    print(string_matching_zcajas(T, P1))
    print(string_matching_zcajas(T, P2))
    print(string_matching_zcajas(T2, P3))
    print(string_matching_zcajas(T3, P4))


def string_matching_zcajas(texto, patron, caracter_reservado='$'):
    """Devuelve una lista con las posiciones en texto
    donde aparece patron completo utilizando el algoritmo z."""

    texto_patron = patron + caracter_reservado + texto
    zcajas = computar_zcajas(texto_patron)
    #print(texto)
    #print(patron)
    #print(texto_patron)
    #print("zcajas: ", zcajas)
    matches = []
    # print("largo zcajas: ", len(zcajas))
    # print("largo texto_patron: ", len(texto_patron))
    for x in range(len(patron) + 1, len(zcajas)):
        if zcajas[x] == len(patron):
            matches.append(x - len(patron) - 1)

    #print(matches)
    return matches


def computar_zcajas(texto):
    """Devuelve una lista donde lista[i] contiene el tamanio de la caja zi"""

    Zs = [0]
    r = 0
    l = 0

    for k in range(1, len(texto)):
        if k > r:
            # Estoy fuera de la caja => computo caja nueva
            # print("k: ", k)
            match_len = 0

            for act in range(len(texto) - k):
                # print("act: ", act, "k:", k, texto[act], texto[act + k])
                if texto[k + act] == texto[act]:
                    l = k
                    r = k + act
                    match_len += 1
                else:
                    break
            # print("act: ", act)
            # print("len(texto) - k: ", len(texto) - k)
            Zs.append(match_len)

        else:
            # Estoy dentro de una Zcaja
            Zprima = Zs[k - l]
            # print("k' =", k-l, " Z' = ", Zprima)

            if Zprima + k >= len(texto):
                #print("Caso 1: ", k)
                Zprimareal = len(texto) - k
                Zs.append(Zprimareal)

            elif (k + Zprima - 1) < r:
                #print("Caso 2: ", k)
                # La caja nueva queda contenida en la vieja.
                #print("Zs: ", Zprima)
                Zs.append(Zprima)
            else:
                match_len = r - k + 1
                # print("Caso 3: ", k)
                for act in range(match_len, len(texto) - k - match_len + 1):
                    # print("Inspecting: ", k, act, k+act)
                    # print("act: ", act, "k:", k, texto[act], texto[act + k])
                    if texto[k + act] == texto[act]:
                        l = k
                        r = k + act
                        match_len += 1
                    else:
                        # Zs.append(match_len)
                        break
                #if match_len == len(texto) - k:
                Zs.append(match_len)
                    # print("Zs: ", match_len)
                    # print("Zs: ", Zs)
    # print(texto)
    # print(Zs)
    # print(len(Zs))
    return Zs


if __name__ == '__main__':
    test_string_matching()
