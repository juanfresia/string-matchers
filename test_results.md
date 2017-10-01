# Results 

 | |Karp Rabin|Naive|Nothing _Test Only_|Z Box|
|:---|:---|:---|:---|:---|
|[NM-1](#No-Matches-Test-1)|14.086246 - (OK)|32.826846 - (OK)|0.000184 - (ERROR)|89.550775 - (ERROR)|
|[NM-2](#No-Matches-Test-2)|13.801737 - (OK)|0.934633 - (OK)|0.000181 - (ERROR)|30.848899 - (OK)|
|[NM-3](#No-Matches-Test-3)|1.971440 - (OK)|1.111735 - (OK)|0.000185 - (ERROR)|2.208672 - (ERROR)|
|[NM-4](#No-Matches-Test-4)|13.785489 - (OK)|0.924609 - (OK)|0.000187 - (ERROR)|31.019382 - (OK)|
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
                
