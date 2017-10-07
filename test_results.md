# Results 

 | |Baseline|DC3|Karp Rabin|Naive|Z Box|
|:---|:---|:---|:---|:---|:---|
|[NM-1](#no-matches-test-1)|0.180331 - (ERROR)|22.253642 - (OK)|4.266371 - (OK)|30.556130 - (OK)|3.518905 - (OK)|
|[NM-2](#no-matches-test-2)|0.183148 - (ERROR)|20.067799 - (OK)|4.142555 - (OK)|1.115096 - (OK)|2.804140 - (OK)|
|[NM-3](#no-matches-test-3)|0.145559 - (ERROR)|19.893018 - (OK)|2.227760 - (OK)|1.227732 - (OK)|1.980528 - (OK)|
|[NM-4](#no-matches-test-4)|0.144761 - (ERROR)|22.238207 - (OK)|2.238292 - (OK)|1.246535 - (OK)|1.923206 - (OK)|
|[NM-5](#no-matches-test-5)|0.183277 - (ERROR)|22.079206 - (OK)|4.139962 - (OK)|2.919098 - (OK)|2.197335 - (OK)|
|[NM-6](#no-matches-test-6)|0.151528 - (ERROR)|20.695435 - (OK)|2.926377 - (OK)|1.343369 - (OK)|2.115527 - (OK)|
|[OM-1](#one-match-test-1)|0.179296 - (ERROR)|19.859842 - (OK)|4.130027 - (OK)|1.153284 - (OK)|2.329299 - (OK)|
|[OM-2](#one-match-test-2)|0.181611 - (ERROR)|21.558775 - (ERROR)|4.326532 - (OK)|15.999115 - (OK)|2.704179 - (OK)|
|[OM-3](#one-match-test-3)|0.185486 - (ERROR)|20.714089 - (OK)|4.138151 - (OK)|1.184104 - (OK)|2.391059 - (OK)|
|[OM-4](#one-match-test-4)|0.184391 - (ERROR)|21.258537 - (ERROR)|4.410290 - (OK)|15.900023 - (OK)|2.708091 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.302331 - (ERROR)|19.115997 - (OK)|1.255451 - (OK)|0.310300 - (ERROR)|3.431270 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.309127 - (ERROR)|23.864658 - (OK)|1.350150 - (OK)|0.314440 - (ERROR)|5.032148 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.304032 - (ERROR)|23.736630 - (OK)|1.306671 - (OK)|0.313629 - (ERROR)|4.715852 - (OK)|
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
                
