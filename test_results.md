# Results 

 | |Baseline|Karp Rabin|Naive|Z Box|
|:---|:---|:---|:---|:---|
|[NM-1](#no-matches-test-1)|0.195811 - (ERROR)|4.080252 - (OK)|29.500526 - (OK)|3.304590 - (OK)|
|[NM-2](#no-matches-test-2)|0.182704 - (ERROR)|3.725812 - (OK)|1.048712 - (OK)|2.562906 - (OK)|
|[NM-3](#no-matches-test-3)|0.146924 - (ERROR)|2.035925 - (OK)|1.108910 - (OK)|1.783287 - (OK)|
|[NM-4](#no-matches-test-4)|0.155195 - (ERROR)|2.070202 - (OK)|1.126415 - (OK)|1.846639 - (OK)|
|[NM-5](#no-matches-test-5)|0.192988 - (ERROR)|3.796156 - (OK)|2.830462 - (OK)|2.083017 - (OK)|
|[NM-6](#no-matches-test-6)|0.151598 - (ERROR)|2.652500 - (OK)|1.233678 - (OK)|1.929517 - (OK)|
|[OM-1](#one-match-test-1)|0.181474 - (ERROR)|3.757486 - (OK)|1.092495 - (OK)|2.224791 - (OK)|
|[OM-2](#one-match-test-2)|0.186437 - (ERROR)|4.196075 - (OK)|15.530255 - (OK)|2.515311 - (OK)|
|[OM-3](#one-match-test-3)|0.243156 - (ERROR)|3.852976 - (OK)|1.117123 - (OK)|2.229032 - (OK)|
|[OM-4](#one-match-test-4)|0.184331 - (ERROR)|3.880824 - (OK)|15.324606 - (OK)|2.580379 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.305499 - (ERROR)|1.192457 - (OK)|0.320200 - (ERROR)|3.094045 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.309514 - (ERROR)|1.188688 - (OK)|0.305151 - (ERROR)|4.811255 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.295664 - (ERROR)|1.194318 - (OK)|0.300240 - (ERROR)|4.422860 - (OK)|
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

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n=5 (Patron corto).
                
## No Matches Test 5 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

La cadena esta conformada por 4 patrones concatenados sin el ultimo caracter. El patron es periodico asi que hay varios matches parciales.
El patron es de largo n, con n=500.
                
## No Matches Test 6 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

No hay 500 posibles candidatos, porque aparecen los n-1 primeros caracters del patron repetidos 500 veces cada n caracteres,
en el string, con n=100 el largo del patron.
                
## One Match Test 1 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

No hay mas de un solo posible candidato, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500.
                
## One Match Test 2 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

Hay varios posibles candidatos ya que, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500 de forma repetida..
                
## One Match Test 3 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

No hay mas de un solo posible candidato, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500.
                
## One Match Test 4 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

Hay varios posibles candidatos ya que, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500 de forma repetida..
                
## Pattern to Pattern 1 

 
Corre 4000 veces el string matcher sobre una cadena de largo 500 en la cual hay solo un match. La cadena es el patron mismo.

No hay mas de un solo posible candidato, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500..
                
## Pattern to Pattern 2 

 
Corre 4000 veces el string matcher sobre una cadena de largo 500 en la cual hay solo un match. La cadena es el patron mismo.

Hay varios posibles candidatos, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500 repetido n-1 veces.
                
## Pattern to Pattern 3 

 
Corre 2000 veces el string matcher sobre una cadena de largo 1000 en la cual hay solo un match. La cadena es el patron mismo.

Hay varios posibles candidatos, solo hay 2 caracteres en la cadena, y se presentan de forma intercalada
en el patron de largo n=1000.
                
