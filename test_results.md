# Results 

 | |Karp Rabin|Naive|Nothing _Test Only_|Z Box|
|:---|:---|:---|:---|:---|
|[NM-1](#No-Matches-Test-1)|13.840912 - (OK)|33.674607 - (OK)|0.000213 - (ERROR)|94.704509 - (ERROR)|
|[NM-2](#No-Matches-Test-2)|14.102590 - (OK)|0.983606 - (OK)|0.000190 - (ERROR)|31.850172 - (OK)|
|[NM-3](#No-Matches-Test-3)|2.096661 - (OK)|1.118155 - (OK)|0.000198 - (ERROR)|2.167529 - (ERROR)|
|[NM-4](#No-Matches-Test-4)|13.849442 - (OK)|0.959968 - (OK)|0.000197 - (ERROR)|31.848936 - (OK)|
|[NM-5](#No-Matches-Test-5)|14.106570 - (OK)|2.984683 - (OK)|0.000194 - (ERROR)|6.208126 - (OK)|
# Descriptions 

## No Matches Test 1 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n=500 el largo del patron.
                
## No Matches Test 2 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n=500.
                
## No Matches Test 3 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2004 en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n=5 el largo del patron (patron corto).
                
## No Matches Test 4 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2004 en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n=500 (Patron corto).
                
## No Matches Test 5 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

La cadena esta conformada por 4 patrones concatenados sin el ultimo caracter. El patron es periodico asi que hay varios matches parciales. 
El patron es de largo n, con n=500.
                
