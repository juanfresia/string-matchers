# Results 

 | |Baseline|Karp Rabin|Naive|Z Box|
|:---|:---|:---|:---|:---|
|[NM-1](#no-matches-test-1)|0.000284 - (ERROR)|4.065619 - (OK)|28.121059 - (OK)|3.287112 - (OK)|
|[NM-2](#no-matches-test-2)|0.000195 - (ERROR)|3.832353 - (OK)|1.043260 - (OK)|2.567424 - (OK)|
|[NM-3](#no-matches-test-3)|0.000206 - (ERROR)|2.177399 - (OK)|1.290075 - (OK)|1.783878 - (OK)|
|[NM-4](#no-matches-test-4)|0.000184 - (ERROR)|2.163374 - (OK)|1.141080 - (OK)|1.746892 - (OK)|
|[NM-5](#no-matches-test-5)|0.000185 - (ERROR)|3.801541 - (OK)|2.774083 - (OK)|2.054825 - (OK)|
|[NM-6](#no-matches-test-6)|0.000211 - (ERROR)|2.751896 - (OK)|1.233610 - (OK)|1.920269 - (OK)|
|[OM-1](#one-match-test-1)|0.000201 - (ERROR)|3.843536 - (OK)|1.071899 - (OK)|2.151427 - (OK)|
|[OM-2](#one-match-test-2)|0.000185 - (ERROR)|3.971433 - (OK)|14.385470 - (OK)|2.470239 - (OK)|
|[OM-3](#one-match-test-3)|0.000180 - (ERROR)|3.834003 - (OK)|1.078352 - (OK)|2.150358 - (OK)|
|[OM-4](#one-match-test-4)|0.000175 - (ERROR)|3.936775 - (OK)|14.386969 - (OK)|2.447863 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.000751 - (ERROR)|1.192665 - (OK)|0.295625 - (ERROR)|3.100002 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.000726 - (ERROR)|1.196710 - (OK)|0.303112 - (ERROR)|4.548844 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.000403 - (ERROR)|1.203310 - (OK)|0.289854 - (ERROR)|4.293066 - (OK)|
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
                
