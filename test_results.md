# Results 

 | |Karp Rabin|Naive|Nothing _Test Only_|Z Box|
|:---|:---|:---|:---|:---|
|[NM-1](#No-Matches-Test-1)| 10.0898 - (OK)| 29.1376 - (OK)| 0.000165224 - (ERROR)| 86.9478 - (ERROR)|
|[NM-2](#No-Matches-Test-2)| 10.3575 - (OK)| 0.624578 - (OK)| 0.00016284 - (ERROR)| 29.3248 - (OK)|
# Descriptions 

## No Matches Test 1 

 
Corre 1000 veces el string matcher sobre una cadena de largo 1548 en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n=500 el largo del patron.
                
## No Matches Test 2 

 
Corre 1000 veces el string matcher sobre una cadena de largo 1548 en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n=500.
                
