





def test_string_matching():
        #0         1         2         3
        #012345678901234567890123456789012345678
    T = "HOLA ESTO ES UN STRING DE PRUEBA. HOLA."
    P1 = "ES"
    P2 = "HOLA"

    print(string_matching_zcajas(T, P1))
    print(string_matching_zcajas(T, P2))



def string_matching_zcajas(texto, patron, caracter_reservado='$'):
    """Devuelve una lista con las posiciones en texto
	donde aparece patron completo utilizando el algoritmo z."""

    texto_patron = patron+caracter_reservado+texto
    zcajas = computar_zcajas(texto_patron)

    matches = []

    for x in range(len(zcajas)):
        if zcajas[x] == len(patron):
            matches.append(x-len(patron))

    return matches


def computar_zcajas(texto):
    """Devuelve una lista donde lista[i] contiene el tamanio de la caja zi"""

    Zs = [0]
    r = 0
    l = 0

    for k in range(1, len(texto)):
        if k > r:
            # Estoy fuera de la caja => computo caja nueva
            match_len = 0

            for act in range(len(texto) - k):
                if texto[k + act] == texto[act]:
                    l = k
                    r = k + act
                    match_len += 1
                else:
                    Zs.append(match_len)
                    break
            Zs.append(match_len)

        else:
            # Estoy dentro de una Zcaja
            Zprima = Zs[k - l]

            if (k + Zprima - 1) < r:
                # La caja nueva queda contenida en la vieja.
                Zs.append(Zprima)
            else:
                match_len = Zprima
                for act in range(k-l, len(texto)-k):
                    if texto[k + act] == texto[act]:
                        l = k
                        r = k + act
                        match_len += 1
                    else:
                        Zs.append(match_len)
                        break
                Zs.append(match_len)

    return Zs



test_string_matching()
