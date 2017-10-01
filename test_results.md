# Results 

 | |Karp Rabin|Naive|Nothing _Test Only_|Z Box|
|:---|:---|:---|:---|:---|
|[NM-1](#No-Matches-Test-1)| 13.6288 - (OK)| 32.8937 - (OK)| 0.000173092 - (ERROR)| 88.0794 - (ERROR)|
|[NM-2](#No-Matches-Test-2)| 13.4054 - (OK)| 0.926558 - (OK)| 0.000178337 - (ERROR)| 30.9628 - (OK)|
|[NM-3](#No-Matches-Test-3)| 1.9871 - (OK)| 1.09069 - (OK)| 0.000179291 - (ERROR)| 2.20032 - (ERROR)|
|[NM-4](#No-Matches-Test-4)| 13.5212 - (OK)| 0.925315 - (OK)| 0.00019455 - (ERROR)| 30.7301 - (OK)|
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
                
