





def test_string_matching():
        #0         1         2         3
        #012345678901234567890123456789012345678
    T = "HOLA ESTO ES UN STRING DE PRUEBA. HOLA."
    P1 = "ES"
    P2 = "HOLA"

    print(string_matching_naive(T, P1))
    print(string_matching_naive(T, P2))



def computar_zcajas(texto):
    """Devuelve una lista con las posiciones en texto
    donde aparece patron completo."""

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
                    Zs.append[match_len]
                    break
            Zs.append[match_len]

        else:
            # Estoy dentro de una Zcaja
            Zprima = Zs[k - l]
            
            if (k + Zprima - 1) < r:
                Zs.append[Zprima]
            else:
                for act in range(



    return Zs



test_string_matching()
