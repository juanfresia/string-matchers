# Results 

 | |Baseline|DC3|Karp Rabin|Naive|Z Box|
|:---|---:|---:|---:|---:|---:|
|[NM-1](#no-matches-test-1)|0.171151 - (ER)|21.640188 - (OK)|4.310440 - (OK)|28.771114 - (OK)|3.459670 - (OK)|
|[NM-2](#no-matches-test-2)|0.180706 - (ER)|19.360498 - (OK)|3.927241 - (OK)|1.048827 - (OK)|2.687769 - (OK)|
|[NM-3](#no-matches-test-3)|0.143208 - (ER)|19.194017 - (OK)|2.211963 - (OK)|1.134796 - (OK)|1.839131 - (OK)|
|[NM-4](#no-matches-test-4)|0.139074 - (ER)|21.494204 - (OK)|2.215020 - (OK)|1.126212 - (OK)|1.823552 - (OK)|
|[NM-5](#no-matches-test-5)|0.178341 - (ER)|21.465367 - (OK)|3.938446 - (OK)|2.803443 - (OK)|2.100056 - (OK)|
|[NM-6](#no-matches-test-6)|0.147482 - (ER)|19.973395 - (OK)|2.783521 - (OK)|1.265248 - (OK)|2.020246 - (OK)|
|[OM-1](#one-match-test-1)|0.176192 - (ER)|19.437621 - (OK)|4.041516 - (OK)|1.100546 - (OK)|2.229324 - (OK)|
|[OM-2](#one-match-test-2)|0.174858 - (ER)|21.058702 - (OK)|4.174372 - (OK)|14.612443 - (OK)|2.554902 - (OK)|
|[OM-3](#one-match-test-3)|0.175897 - (ER)|20.190707 - (OK)|4.036645 - (OK)|1.118924 - (OK)|2.246230 - (OK)|
|[OM-4](#one-match-test-4)|0.175056 - (ER)|21.076318 - (OK)|4.145706 - (OK)|14.820179 - (OK)|2.599741 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.287342 - (ER)|19.313957 - (OK)|1.212006 - (OK)|0.308746 - (ER)|3.218728 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.292502 - (ER)|24.585692 - (OK)|1.230538 - (OK)|0.301590 - (ER)|4.790393 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.291560 - (ER)|23.451054 - (OK)|1.223487 - (OK)|0.300987 - (ER)|4.460674 - (OK)|
|[MM-1](#multiple-matches-test-1)|0.180862 - (ER)|22.791822 - (ER)|4.192650 - (OK)|1.188481 - (ER)|1.994562 - (OK)|
|[OC-1](#one-character-test-1)|0.176645 - (ER)|24.723565 - (ER)|90.214034 - (OK)|87.179937 - (ER)|3.892204 - (ER)|
|[OC-2](#one-character-test-2)|0.141661 - (ER)|21.485090 - (ER)|3.129281 - (OK)|1.250883 - (ER)|2.623100 - (OK)|
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
                
