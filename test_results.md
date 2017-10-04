# Results 

 | |Karp Rabin|Naive|Nothing _Test Only_|Z Box|
|:---|:---|:---|:---|:---|
|[NM-1](#no-matches-test-1)|12.106328 - (OK)|30.536572 - (OK)|0.000192 - (ERROR)|3.306305 - (OK)|
|[NM-2](#no-matches-test-2)|12.083147 - (OK)|0.852761 - (OK)|0.000178 - (ERROR)|2.642055 - (OK)|
|[NM-3](#no-matches-test-3)|2.174428 - (OK)|1.027539 - (OK)|0.000172 - (ERROR)|1.828261 - (OK)|
|[NM-4](#no-matches-test-4)|2.176117 - (OK)|0.984416 - (OK)|0.000179 - (ERROR)|1.806408 - (OK)|
|[NM-5](#no-matches-test-5)|12.010734 - (OK)|2.782068 - (OK)|0.000183 - (ERROR)|2.116584 - (OK)|
|[NM-6](#no-matches-test-6)|3.888826 - (OK)|1.134596 - (OK)|0.000195 - (ERROR)|1.985886 - (OK)|
|[OM-1](#one-match-test-1)|12.242568 - (OK)|0.910926 - (OK)|0.000186 - (ERROR)|2.200817 - (OK)|
|[OM-2](#one-match-test-2)|12.057074 - (OK)|15.818200 - (OK)|0.000202 - (ERROR)|2.589057 - (OK)|
|[OM-3](#one-match-test-3)|12.210989 - (OK)|0.961912 - (OK)|0.000190 - (ERROR)|2.224503 - (OK)|
|[OM-4](#one-match-test-4)|12.041879 - (OK)|15.814974 - (OK)|0.000179 - (ERROR)|2.611771 - (OK)|
|[PP-1](#pattern-to-pattern-1)|1.064224 - (OK)|0.002496 - (ERROR)|0.000815 - (ERROR)|3.270570 - (OK)|
|[PP-2](#pattern-to-pattern-2)|1.033856 - (OK)|0.002478 - (ERROR)|0.000793 - (ERROR)|4.821477 - (OK)|
|[PP-3](#pattern-to-pattern-3)|1.029794 - (OK)|0.001244 - (ERROR)|0.000414 - (ERROR)|4.494520 - (OK)|
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
                
