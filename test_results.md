# Results 

 | |Baseline|Karp Rabin|Naive|Z Box|
|:---|:---|:---|:---|:---|
|[NM-1](#no-matches-test-1)|0.000303 - (ERROR)|3.996503 - (OK)|30.225734 - (OK)|3.270897 - (OK)|
|[NM-2](#no-matches-test-2)|0.000192 - (ERROR)|3.803708 - (OK)|0.890976 - (OK)|2.580684 - (OK)|
|[NM-3](#no-matches-test-3)|0.000173 - (ERROR)|2.076096 - (OK)|1.030035 - (OK)|1.774460 - (OK)|
|[NM-4](#no-matches-test-4)|0.000171 - (ERROR)|2.096450 - (OK)|1.055992 - (OK)|1.800100 - (OK)|
|[NM-5](#no-matches-test-5)|0.000193 - (ERROR)|3.770415 - (OK)|2.726038 - (OK)|2.017990 - (OK)|
|[NM-6](#no-matches-test-6)|0.000183 - (ERROR)|2.742361 - (OK)|1.160470 - (OK)|1.917397 - (OK)|
|[OM-1](#one-match-test-1)|0.000170 - (ERROR)|3.834253 - (OK)|0.958225 - (OK)|2.169194 - (OK)|
|[OM-2](#one-match-test-2)|0.000174 - (ERROR)|3.965164 - (OK)|15.499788 - (OK)|2.548659 - (OK)|
|[OM-3](#one-match-test-3)|0.000197 - (ERROR)|3.890470 - (OK)|0.942412 - (OK)|2.152935 - (OK)|
|[OM-4](#one-match-test-4)|0.000173 - (ERROR)|3.935453 - (OK)|15.498734 - (OK)|2.506811 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.000757 - (ERROR)|1.157773 - (OK)|0.002416 - (ERROR)|3.109731 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.000701 - (ERROR)|1.159713 - (OK)|0.003363 - (ERROR)|4.631591 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.000388 - (ERROR)|1.173210 - (OK)|0.001334 - (ERROR)|4.363117 - (OK)|
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
                
