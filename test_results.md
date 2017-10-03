# Results 

 | |Karp Rabin|Naive|Nothing _Test Only_|Z Box|
|:---|:---|:---|:---|:---|
|[NM-1](#no-matches-test-1)|9.063347 - (OK)|27.038854 - (OK)|0.000140 - (ERROR)|80.919145 - (ERROR)|
|[NM-2](#no-matches-test-2)|9.042908 - (OK)|0.806719 - (OK)|0.000139 - (ERROR)|27.136711 - (OK)|
|[NM-3](#no-matches-test-3)|2.480593 - (OK)|0.969731 - (OK)|0.000138 - (ERROR)|1.837047 - (ERROR)|
|[NM-4](#no-matches-test-4)|2.479081 - (OK)|0.964506 - (OK)|0.000147 - (ERROR)|1.883745 - (OK)|
|[NM-5](#no-matches-test-5)|9.128102 - (OK)|2.475219 - (OK)|0.000139 - (ERROR)|5.119014 - (OK)|
|[NM-6](#no-matches-test-6)|3.780147 - (OK)|1.068223 - (OK)|0.000147 - (ERROR)|1.961807 - (OK)|
|[OM-1](#one-match-test-1)|9.397650 - (OK)|0.864595 - (OK)|0.000138 - (ERROR)|2.166929 - (OK)|
|[OM-2](#one-match-test-2)|9.375024 - (OK)|14.129606 - (OK)|0.000142 - (ERROR)|54.569227 - (ERROR)|
|[OM-3](#one-match-test-3)|9.368624 - (OK)|1.015340 - (OK)|0.000143 - (ERROR)|2.389517 - (OK)|
|[OM-4](#one-match-test-4)|9.322602 - (OK)|15.551849 - (OK)|0.000154 - (ERROR)|60.442173 - (ERROR)|
|[PP-1](#pattern-to-pattern-1)|2.035284 - (OK)|0.002673 - (ERROR)|0.001098 - (ERROR)|3.315365 - (OK)|
|[PP-2](#pattern-to-pattern-2)|1.930932 - (OK)|0.002062 - (ERROR)|0.000584 - (ERROR)|114.675791 - (OK)|
|[PP-3](#pattern-to-pattern-3)|1.839271 - (OK)|0.001047 - (ERROR)|0.000297 - (ERROR)|73.162578 - (OK)|
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
                
