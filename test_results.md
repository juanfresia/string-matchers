# Results 

 | |Karp Rabin|Naive|Nothing _Test Only_|Z Box|
|:---|:---|:---|:---|:---|
|[NM-1](#no-matches-test-1)|5.028254 - (OK)|21.052159 - (OK)|0.000257 - (ERROR)|19.076937 - (OK)|
|[NM-2](#no-matches-test-2)|4.677829 - (OK)|4.763910 - (OK)|0.000306 - (ERROR)|23.157431 - (OK)|
|[NM-3](#no-matches-test-3)|1.670249 - (OK)|1.254417 - (OK)|0.000258 - (ERROR)|15.575812 - (OK)|
|[NM-4](#no-matches-test-4)|1.569478 - (OK)|1.217247 - (OK)|0.000301 - (ERROR)|16.199581 - (OK)|
|[NM-5](#no-matches-test-5)|4.529851 - (OK)|5.775233 - (OK)|0.000277 - (ERROR)|2.904460 - (OK)|
|[NM-6](#no-matches-test-6)|4.534778 - (OK)|2.099046 - (OK)|0.000272 - (ERROR)|9.161657 - (OK)|
|[OM-1](#one-match-test-1)|4.546615 - (OK)|4.843360 - (OK)|0.000258 - (ERROR)|19.977975 - (OK)|
|[OM-2](#one-match-test-2)|4.609749 - (OK)|13.222513 - (OK)|0.000254 - (ERROR)|18.323535 - (OK)|
|[OM-3](#one-match-test-3)|4.644990 - (OK)|4.840212 - (OK)|0.000268 - (ERROR)|19.978075 - (OK)|
|[OM-4](#one-match-test-4)|4.585012 - (OK)|13.143845 - (OK)|0.000277 - (ERROR)|18.525110 - (OK)|
|[PP-1](#pattern-to-pattern-1)|1.071860 - (OK)|0.003327 - (ERROR)|0.001004 - (ERROR)|12.415299 - (OK)|
|[PP-2](#pattern-to-pattern-2)|1.071881 - (OK)|0.003339 - (ERROR)|0.001013 - (ERROR)|7.053412 - (OK)|
|[PP-3](#pattern-to-pattern-3)|1.058699 - (OK)|0.001646 - (ERROR)|0.000503 - (ERROR)|21.051285 - (OK)|
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
                
