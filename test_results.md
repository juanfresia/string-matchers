# Results 

 | |Baseline|DC3|Karp Rabin|Naive|Z Box|
|:---|---:|---:|---:|---:|---:|
|[NM-1](#no-matches-test-1)|0.186758 - (ERROR)|21.335707 - (OK)|4.192286 - (OK)|32.165430 - (OK)|3.487413 - (OK)|
|[NM-2](#no-matches-test-2)|0.180476 - (ERROR)|19.449736 - (OK)|4.019456 - (OK)|1.144743 - (OK)|2.772528 - (OK)|
|[NM-3](#no-matches-test-3)|0.148340 - (ERROR)|19.352339 - (OK)|2.179705 - (OK)|1.219693 - (OK)|1.884732 - (OK)|
|[NM-4](#no-matches-test-4)|0.147566 - (ERROR)|21.794151 - (OK)|2.204312 - (OK)|1.241128 - (OK)|1.963224 - (OK)|
|[NM-5](#no-matches-test-5)|0.191466 - (ERROR)|21.279387 - (OK)|4.079462 - (OK)|3.111675 - (OK)|2.162703 - (OK)|
|[NM-6](#no-matches-test-6)|0.152863 - (ERROR)|20.182384 - (OK)|2.823645 - (OK)|1.355848 - (OK)|2.061800 - (OK)|
|[OM-1](#one-match-test-1)|0.186683 - (ERROR)|19.590036 - (ERROR)|4.118247 - (OK)|1.170717 - (OK)|2.295819 - (OK)|
|[OM-2](#one-match-test-2)|0.189534 - (ERROR)|21.009670 - (ERROR)|4.262489 - (OK)|16.259317 - (OK)|2.650312 - (OK)|
|[OM-3](#one-match-test-3)|0.187086 - (ERROR)|20.475556 - (ERROR)|4.101038 - (OK)|1.179379 - (OK)|2.298370 - (OK)|
|[OM-4](#one-match-test-4)|0.190192 - (ERROR)|20.847707 - (ERROR)|4.212768 - (OK)|16.635023 - (OK)|2.647501 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.310714 - (ERROR)|19.288125 - (ERROR)|1.305704 - (OK)|0.319772 - (ERROR)|3.426662 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.314328 - (ERROR)|24.395285 - (ERROR)|1.325728 - (OK)|0.350959 - (ERROR)|4.935707 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.306575 - (ERROR)|23.330256 - (ERROR)|1.320236 - (OK)|0.314899 - (ERROR)|4.615034 - (OK)|
|[MM-1](#multiple-matches-test-1)|0.189382 - (ERROR)|23.197783 - (ERROR)|4.296269 - (OK)|1.281807 - (ERROR)|2.135392 - (OK)|
|[OC-1](#one-character-test-1)|0.191620 - (ERROR)|23.684088 - (ERROR)|92.217431 - (OK)|98.165796 - (ERROR)|4.016784 - (ERROR)|
|[OC-2](#one-character-test-2)|0.154102 - (ERROR)|21.505645 - (ERROR)|3.079695 - (OK)|1.300821 - (ERROR)|2.650254 - (OK)|
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
                
## Multiple Matches Test 1 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual hay 4 matches un match.

No hay mas de solo 4 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500, siendo la cadena una concatenacion de 4 veces el patron.
                
## One Character Test 1 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=500 el largo del patron.
                
## One Character Test 2 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=1 el largo del patron (patron corto).
                
