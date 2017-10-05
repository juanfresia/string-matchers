# Results 

 | |Baseline|DC3|Karp Rabin|Naive|Nothing _Test Only_|Z Box|
|:---|:---|:---|:---|:---|:---|:---|
|[NM-1](#no-matches-test-1)|0.191757 - (ERROR)|21.560081 - (OK)|4.260287 - (OK)|29.854980 - (OK)|0.000173 - (ERROR)|3.553794 - (OK)|
|[NM-2](#no-matches-test-2)|0.207159 - (ERROR)|20.366583 - (OK)|4.248946 - (OK)|1.136765 - (OK)|0.000186 - (ERROR)|2.749097 - (OK)|
|[NM-3](#no-matches-test-3)|0.161601 - (ERROR)|20.237051 - (OK)|2.483148 - (OK)|1.332444 - (OK)|0.000253 - (ERROR)|2.026029 - (OK)|
|[NM-4](#no-matches-test-4)|0.165390 - (ERROR)|22.726758 - (OK)|2.421369 - (OK)|1.296926 - (OK)|0.000158 - (ERROR)|1.939456 - (OK)|
|[NM-5](#no-matches-test-5)|0.218638 - (ERROR)|20.973191 - (OK)|3.985295 - (OK)|2.800650 - (OK)|0.000197 - (ERROR)|2.143248 - (OK)|
|[NM-6](#no-matches-test-6)|0.164783 - (ERROR)|19.768741 - (OK)|3.044007 - (OK)|1.357988 - (OK)|0.000187 - (ERROR)|2.032005 - (OK)|
|[OM-1](#one-match-test-1)|0.200484 - (ERROR)|19.239297 - (OK)|4.200824 - (OK)|1.084951 - (OK)|0.000177 - (ERROR)|2.153550 - (OK)|
|[OM-2](#one-match-test-2)|0.193556 - (ERROR)|19.860096 - (ERROR)|4.123873 - (OK)|14.470390 - (OK)|0.000171 - (ERROR)|2.505943 - (OK)|
|[OM-3](#one-match-test-3)|0.195346 - (ERROR)|19.150739 - (OK)|4.014500 - (OK)|1.114235 - (OK)|0.000203 - (ERROR)|2.185950 - (OK)|
|[OM-4](#one-match-test-4)|0.210326 - (ERROR)|19.915132 - (ERROR)|4.037391 - (OK)|14.444129 - (OK)|0.000175 - (ERROR)|2.510152 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.319129 - (ERROR)|18.017651 - (OK)|1.249346 - (OK)|0.323104 - (ERROR)|0.000790 - (ERROR)|3.201581 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.322191 - (ERROR)|22.722943 - (OK)|1.259082 - (OK)|0.325974 - (ERROR)|0.000778 - (ERROR)|4.794131 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.314332 - (ERROR)|21.691277 - (OK)|1.247972 - (OK)|0.327081 - (ERROR)|0.000407 - (ERROR)|4.478853 - (OK)|
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
                
