# Results 

 | |Baseline|DC3|Karp Rabin|Naive|Z Box|
|:---|---:|---:|---:|---:|---:|
|[NM-1](#no-matches-test-1)|0.021890 - (ERROR)|2.113028 - (OK)|0.421571 - (OK)|2.849498 - (OK)|0.331117 - (OK)|
|[NM-2](#no-matches-test-2)|0.020190 - (ERROR)|1.906255 - (OK)|0.399873 - (OK)|0.109802 - (OK)|0.257085 - (OK)|
|[NM-3](#no-matches-test-3)|0.016676 - (ERROR)|1.901079 - (OK)|0.219443 - (OK)|0.121467 - (OK)|0.170303 - (OK)|
|[NM-4](#no-matches-test-4)|0.017129 - (ERROR)|2.158773 - (OK)|0.220825 - (OK)|0.124255 - (OK)|0.175905 - (OK)|
|[NM-5](#no-matches-test-5)|0.021063 - (ERROR)|2.133265 - (OK)|0.405910 - (OK)|0.276156 - (OK)|0.210409 - (OK)|
|[NM-6](#no-matches-test-6)|0.016739 - (ERROR)|1.995160 - (OK)|0.280819 - (OK)|0.134403 - (OK)|0.193145 - (OK)|
|[OM-1](#one-match-test-1)|0.021195 - (ERROR)|1.940585 - (OK)|0.408529 - (OK)|0.117265 - (OK)|0.212083 - (OK)|
|[OM-2](#one-match-test-2)|0.020389 - (ERROR)|2.105624 - (OK)|0.421826 - (OK)|1.527367 - (OK)|0.252469 - (OK)|
|[OM-3](#one-match-test-3)|0.020021 - (ERROR)|2.008154 - (OK)|0.402349 - (OK)|0.121392 - (OK)|0.216382 - (OK)|
|[OM-4](#one-match-test-4)|0.020140 - (ERROR)|2.109426 - (OK)|0.417147 - (OK)|1.505443 - (OK)|0.251801 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.033899 - (ERROR)|1.917501 - (OK)|0.126847 - (OK)|0.056766 - (OK)|0.312796 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.033731 - (ERROR)|2.461529 - (OK)|0.128659 - (OK)|0.056918 - (OK)|0.466855 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.033092 - (ERROR)|2.315895 - (OK)|0.129116 - (OK)|0.059344 - (OK)|0.441238 - (OK)|
|[MM-1](#multiple-matches-test-1)|0.020892 - (ERROR)|2.295643 - (OK)|0.425371 - (OK)|0.133526 - (OK)|0.210887 - (OK)|
|[OC-1](#one-character-test-1)|0.020723 - (ERROR)|2.472130 - (ERROR)|9.136136 - (OK)|8.751623 - (OK)|0.372082 - (ERROR)|
|[OC-2](#one-character-test-2)|0.016634 - (ERROR)|2.136124 - (OK)|0.311376 - (OK)|0.133521 - (OK)|0.253064 - (OK)|
# Descriptions 

## No Matches Test 1 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n=500 el largo del patron.
                
## No Matches Test 2 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n=500.
                
## No Matches Test 3 

 
Corre 100 veces el string matcher sobre una cadena de largo 2004 en la cual no hay matches.

Hay 3 posibles candidatos de n-1 elementos, con n=5 el largo del patron (patron corto).
                
## No Matches Test 4 

 
Corre 100 veces el string matcher sobre una cadena de largo 2004 en la cual no hay matches.

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n=5 (Patron corto).
                
## No Matches Test 5 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

La cadena esta conformada por 4 patrones concatenados sin el ultimo caracter. El patron es periodico asi que hay varios matches parciales.
El patron es de largo n, con n=500.
                
## No Matches Test 6 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

No hay 500 posibles candidatos, porque aparecen los n-1 primeros caracters del patron repetidos 500 veces cada n caracteres,
en el string, con n=100 el largo del patron.
                
## One Match Test 1 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

No hay mas de un solo posible candidato, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500.
                
## One Match Test 2 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

Hay varios posibles candidatos ya que, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500 de forma repetida..
                
## One Match Test 3 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

No hay mas de un solo posible candidato, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500.
                
## One Match Test 4 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

Hay varios posibles candidatos ya que, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500 de forma repetida..
                
## Pattern to Pattern 1 

 
Corre 400 veces el string matcher sobre una cadena de largo 500 en la cual hay solo un match. La cadena es el patron mismo.

No hay mas de un solo posible candidato, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500..
                
## Pattern to Pattern 2 

 
Corre 400 veces el string matcher sobre una cadena de largo 500 en la cual hay solo un match. La cadena es el patron mismo.

Hay varios posibles candidatos, solo hay 2 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500 repetido n-1 veces.
                
## Pattern to Pattern 3 

 
Corre 200 veces el string matcher sobre una cadena de largo 1000 en la cual hay solo un match. La cadena es el patron mismo.

Hay varios posibles candidatos, solo hay 2 caracteres en la cadena, y se presentan de forma intercalada
en el patron de largo n=1000.
                
## Multiple Matches Test 1 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay 4 matches un match.

No hay mas de solo 4 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500, siendo la cadena una concatenacion de 4 veces el patron.
                
## One Character Test 1 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=500 el largo del patron.
                
## One Character Test 2 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=1 el largo del patron (patron corto).
                
