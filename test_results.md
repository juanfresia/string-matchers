# Results 

 | |Baseline|DC3|Karp Rabin|Naive|Z Box|
|:---|---:|---:|---:|---:|---:|
|[NM-1](#no-matches-test-1)|0.020010 - (ERROR)|2.138648 - (OK)|0.430606 - (OK)|2.857470 - (OK)|0.357549 - (OK)|
|[NM-2](#no-matches-test-2)|0.020532 - (ERROR)|1.961005 - (OK)|0.425238 - (OK)|0.120893 - (OK)|0.290270 - (OK)|
|[NM-3](#no-matches-test-3)|0.017258 - (ERROR)|2.004683 - (OK)|0.227165 - (OK)|0.127362 - (OK)|0.189746 - (OK)|
|[NM-4](#no-matches-test-4)|0.015552 - (ERROR)|2.156485 - (OK)|0.225138 - (OK)|0.131414 - (OK)|0.195797 - (OK)|
|[NM-5](#no-matches-test-5)|0.020038 - (ERROR)|2.154016 - (OK)|0.413804 - (OK)|0.293855 - (OK)|0.220554 - (OK)|
|[NM-6](#no-matches-test-6)|0.016536 - (ERROR)|2.000564 - (OK)|0.287415 - (OK)|0.142367 - (OK)|0.210569 - (OK)|
|[OM-1](#one-match-test-1)|0.019849 - (ERROR)|1.952039 - (OK)|0.417889 - (OK)|0.125091 - (OK)|0.233109 - (OK)|
|[OM-2](#one-match-test-2)|0.020042 - (ERROR)|2.117404 - (OK)|0.425167 - (OK)|1.530876 - (OK)|0.275647 - (OK)|
|[OM-3](#one-match-test-3)|0.020285 - (ERROR)|2.037482 - (OK)|0.419996 - (OK)|0.123487 - (OK)|0.237840 - (OK)|
|[OM-4](#one-match-test-4)|0.020568 - (ERROR)|2.132070 - (OK)|0.431753 - (OK)|1.600938 - (OK)|0.268111 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.032569 - (ERROR)|1.953012 - (OK)|0.125146 - (OK)|0.053978 - (OK)|0.336104 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.033305 - (ERROR)|2.471364 - (OK)|0.129729 - (OK)|0.057738 - (OK)|0.492201 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.034879 - (ERROR)|2.358911 - (OK)|0.132908 - (OK)|0.058514 - (OK)|0.463973 - (OK)|
|[MM-1](#multiple-matches-test-1)|0.020206 - (ERROR)|2.296535 - (OK)|0.432462 - (OK)|0.134051 - (OK)|0.222378 - (OK)|
|[MM-2](#multiple-matches-test-1)|0.019608 - (ERROR)|2.048163 - (OK)|0.438325 - (OK)|0.138398 - (OK)|0.215965 - (OK)|
|[MM-3](#multiple-matches-test-3)|0.018220 - (ERROR)|2.285376 - (ERROR)|0.351407 - (OK)|0.139450 - (OK)|0.186974 - (OK)|
|[MM-4](#multiple-matches-test-4)|0.018060 - (ERROR)|2.226560 - (ERROR)|0.338356 - (OK)|0.138575 - (OK)|0.186306 - (OK)|
|[OC-1](#one-character-test-1)|0.020153 - (ERROR)|2.501601 - (ERROR)|9.435830 - (OK)|8.904728 - (OK)|0.405780 - (ERROR)|
|[OC-2](#one-character-test-2)|0.016165 - (ERROR)|2.145621 - (OK)|0.305543 - (OK)|0.135063 - (OK)|0.270649 - (OK)|
|[OC-3](#one-character-test-3)|0.016181 - (ERROR)|2.202274 - (OK)|0.397910 - (OK)|0.165541 - (OK)|0.365495 - (OK)|
|[OC-4](#one-character-test-4)|0.016258 - (ERROR)|2.277241 - (OK)|0.444322 - (OK)|0.186591 - (OK)|0.367978 - (ERROR)|
|[OC-5](#one-character-test-5)|0.015922 - (ERROR)|2.259384 - (OK)|0.447060 - (OK)|0.183813 - (OK)|0.365252 - (ERROR)|
|[OC-6](#one-character-test-6)|0.015933 - (ERROR)|2.306003 - (OK)|0.460413 - (OK)|0.206890 - (OK)|0.371021 - (ERROR)|
|[CT-1](#classic-test-1)|0.034899 - (ERROR)|1.065556 - (OK)|0.187372 - (OK)|0.098036 - (OK)|0.186555 - (OK)|
|[CT-2](#classic-test-2)|0.038633 - (ERROR)|0.896876 - (OK)|0.138176 - (OK)|0.077756 - (OK)|0.164971 - (OK)|
|[CT-3](#classic-test-3)|0.025628 - (ERROR)|1.166041 - (OK)|0.131936 - (OK)|0.073032 - (OK)|0.137353 - (OK)|
|[CT-4](#classic-test-4)|0.024542 - (ERROR)|1.170143 - (OK)|0.165872 - (OK)|0.082057 - (OK)|0.129606 - (OK)|
|[CT-5](#classic-test-5)|0.026980 - (ERROR)|1.156468 - (OK)|0.130872 - (OK)|0.071770 - (OK)|0.136758 - (OK)|
|[CT-6](#classic-test-6)|0.024355 - (ERROR)|1.132212 - (OK)|0.125436 - (OK)|0.076418 - (OK)|0.129711 - (OK)|
# Descriptions 

## No Matches Test 1 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n=500 el largo del patron.
                
## No Matches Test 2 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n=500.
                
## No Matches Test 3 

 
Corre 100 veces el string matcher sobre una cadena de largo 2004 en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n=5 el largo del patron (patron corto).
                
## No Matches Test 4 

 
Corre 100 veces el string matcher sobre una cadena de largo 2004 en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n=5 (Patron corto).
                
## No Matches Test 5 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

La cadena esta conformada por 4 patrones concatenados sin el ultimo caracter. El patron es periodico asi que hay varios matches parciales.
El patron es de largo n, con n=500.
                
## No Matches Test 6 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

No hay 500 posibles candidatos, porque aparecen los n-1 primeros caracters del patron repetidos 500 veces cada n caracteres,
en el string, con n=100 el largo del patron.
                
## One Match Test 1 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

No hay mas de un solo posible candidato, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500.
                
## One Match Test 2 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

Hay varios posibles candidatos ya que, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500 de forma repetida..
                
## One Match Test 3 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

No hay mas de un solo posible candidato, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500.
                
## One Match Test 4 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

Hay varios posibles candidatos ya que, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500 de forma repetida..
                
## Pattern to Pattern 1 

 
Corre 400 veces el string matcher sobre una cadena de largo 500 en la cual hay solo un match. La cadena es el patron mismo.

No hay mas de un solo posible candidato, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500..
                
## Pattern to Pattern 2 

 
Corre 400 veces el string matcher sobre una cadena de largo 500 en la cual hay solo un match. La cadena es el patron mismo.

Hay varios posibles candidatos, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500 repetido n-1 veces.
                
## Pattern to Pattern 3 

 
Corre 200 veces el string matcher sobre una cadena de largo 1000 en la cual hay solo un match. La cadena es el patron mismo.

Hay varios posibles candidatos, solo hay 2 caracteres en la cadena, y se presentan de forma intercalada
en el patron de largo n=1000.
                
## Multiple Matches Test 1 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay 4 matches un match.

No hay mas de solo 4 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500, siendo la cadena una concatenacion de 4 veces el patron.
                
## Multiple Matches Test 1 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay 4 matches un match.

No hay mas de solo 8 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio y al final del
patron de largo n=500, siendo la cadena una concatenacion de 4 veces el patron.
                
## Multiple Matches Test 3 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay 4 matches un match.

No hay mas de solo 8 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=250, siendo la cadena una concatenacion de 4 veces el patron mas 4 veces un match parcial.
                    
## Multiple Matches Test 4 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay 4 matches un match.

No hay mas de solo 8 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=250, siendo la cadena una concatenacion de 4 veces un match parcial mas 4 veces el patron.
                    
## One Character Test 1 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=500 el largo del patron.
                
## One Character Test 2 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=1 el largo del patron (patron corto).
                
## One Character Test 3 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=2 el largo del patron (patron corto de largo par).
                
## One Character Test 4 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=3 el largo del patron (patron corto de largo impar).
                
## One Character Test 5 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=3 el largo del patron (patron corto limite ventana DC3).
                
## One Character Test 6 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=4 el largo del patron (patron limite+1 ventana DC3).
                
## Classic Test 1 

 
Corre 16666 veces el string matcher sobre "banana" buscando el patron "ana". Ejemplo de DC3
                
## Classic Test 2 

 
Corre 16666 veces el string matcher sobre "banana" buscando el patron "yaba". Ejemplo de DC3
                
## Classic Test 3 

 
Corre 8333 veces el string matcher sobre "yabbadabbado" buscando el patron "yabba". Ejemplo de DC3
                
## Classic Test 4 

 
Corre 8333 veces el string matcher sobre "yabbadabbado" buscando el patron "bba". Ejemplo de DC3
                
## Classic Test 5 

 
Corre 8333 veces el string matcher sobre "yabbadabbado" buscando el patron "dabba". Ejemplo de DC3
                
## Classic Test 6 

 
Corre 8333 veces el string matcher sobre "yabbadabbado" buscando el patron "ana". Ejemplo de DC3
                
