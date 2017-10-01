# Results 

 | |DC3|Karp Rabin|Naive|Nothing _Test Only_|Z Box|
|:---|:---|:---|:---|:---|:---|
|[NM-1](#No-Matches-Test-1)| 21.2446 - (ERROR)| 10.1559 - (OK)| 29.8035 - (OK)| 0.000154734 - (ERROR)| 88.8623 - (ERROR)|
|[NM-2](#No-Matches-Test-2)| 18.6412 - (ERROR)| 10.3398 - (OK)| 0.589119 - (OK)| 0.000184059 - (ERROR)| 30.2588 - (OK)|
# Descriptions 

## No Matches Test 1 

 
Corre 1000 veces el string matcher sobre una cadena de largo 1548 en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n=500 el largo del patron.
                
## No Matches Test 2 

 
Corre 1000 veces el string matcher sobre una cadena de largo 1548 en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n=500.
                
