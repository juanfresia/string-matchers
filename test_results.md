# Results 

 | |Baseline|DC3|Karp Rabin|Naive|Z Box|
|:---|---:|---:|---:|---:|---:|
|[NM-1](#no-matches-test-1)|0.018657 - (ERROR)|2.261688 - (OK)|0.412709 - (OK)|2.855299 - (OK)|0.344815 - (OK)|
|[NM-2](#no-matches-test-2)|0.016932 - (ERROR)|2.130356 - (OK)|0.398677 - (OK)|0.108229 - (OK)|0.272524 - (OK)|
|[NM-3](#no-matches-test-3)|0.013546 - (ERROR)|2.245360 - (OK)|0.215829 - (OK)|0.121158 - (OK)|0.183878 - (OK)|
|[NM-4](#no-matches-test-4)|0.013892 - (ERROR)|2.176253 - (OK)|0.214759 - (OK)|0.122414 - (OK)|0.189167 - (OK)|
|[NM-5](#no-matches-test-5)|0.017894 - (ERROR)|2.314574 - (OK)|0.403532 - (OK)|0.290805 - (OK)|0.201016 - (OK)|
|[NM-6](#no-matches-test-6)|0.015026 - (ERROR)|2.275028 - (OK)|0.272254 - (OK)|0.136602 - (OK)|0.208750 - (OK)|
|[OM-1](#one-match-test-1)|0.017516 - (ERROR)|2.235028 - (OK)|0.406709 - (OK)|0.110731 - (OK)|0.221442 - (OK)|
|[OM-2](#one-match-test-2)|0.017949 - (ERROR)|2.336982 - (OK)|0.410823 - (OK)|1.424070 - (OK)|0.262573 - (OK)|
|[OM-3](#one-match-test-3)|0.017392 - (ERROR)|2.215662 - (OK)|0.400449 - (OK)|0.109061 - (OK)|0.214861 - (OK)|
|[OM-4](#one-match-test-4)|0.018152 - (ERROR)|2.322869 - (OK)|0.405465 - (OK)|1.423368 - (OK)|0.261492 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.028561 - (ERROR)|2.156216 - (OK)|0.116590 - (OK)|0.050933 - (OK)|0.316944 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.033302 - (ERROR)|2.515708 - (OK)|0.119321 - (OK)|0.052438 - (OK)|0.480446 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.030052 - (ERROR)|2.428448 - (OK)|0.121683 - (OK)|0.053509 - (OK)|0.450569 - (OK)|
|[MM-1](#multiple-matches-test-1)|0.017470 - (ERROR)|2.309843 - (OK)|0.431149 - (OK)|0.129625 - (OK)|0.206317 - (OK)|
|[MM-2](#multiple-matches-test-1)|0.017630 - (ERROR)|2.299047 - (OK)|0.423297 - (OK)|0.133858 - (OK)|0.200335 - (OK)|
|[MM-3](#multiple-matches-test-3)|0.015716 - (ERROR)|2.280431 - (OK)|0.332313 - (OK)|0.133507 - (OK)|0.186491 - (OK)|
|[MM-4](#multiple-matches-test-4)|0.015659 - (ERROR)|2.270664 - (OK)|0.328698 - (OK)|0.134849 - (OK)|0.187113 - (OK)|
|[OC-1](#one-character-test-1)|0.018991 - (ERROR)|21.627113 - (OK)|8.961150 - (OK)|8.750289 - (OK)|0.393716 - (ERROR)|
|[OC-2](#one-character-test-2)|0.015316 - (ERROR)|2.431578 - (OK)|0.310463 - (OK)|0.137822 - (OK)|0.271061 - (OK)|
|[OC-3](#one-character-test-3)|0.015222 - (ERROR)|2.485957 - (OK)|0.397262 - (OK)|0.172338 - (OK)|0.364788 - (OK)|
|[OC-4](#one-character-test-4)|0.015906 - (ERROR)|2.549362 - (OK)|0.448859 - (OK)|0.188325 - (OK)|0.374075 - (ERROR)|
|[OC-5](#one-character-test-5)|0.015293 - (ERROR)|2.537808 - (OK)|0.431581 - (OK)|0.184377 - (OK)|0.369026 - (ERROR)|
|[OC-6](#one-character-test-6)|0.015060 - (ERROR)|2.601587 - (OK)|0.469188 - (OK)|0.205410 - (OK)|0.370842 - (ERROR)|
|[CT-1](#classic-test-1)|0.032312 - (ERROR)|1.004419 - (OK)|0.179509 - (OK)|0.096968 - (OK)|0.185352 - (OK)|
|[CT-2](#classic-test-2)|0.034427 - (ERROR)|0.857260 - (OK)|0.132774 - (OK)|0.072353 - (OK)|0.166082 - (OK)|
|[CT-3](#classic-test-3)|0.023598 - (ERROR)|1.133422 - (OK)|0.129516 - (OK)|0.070347 - (OK)|0.132927 - (OK)|
|[CT-4](#classic-test-4)|0.021408 - (ERROR)|1.136983 - (OK)|0.158385 - (OK)|0.077121 - (OK)|0.127728 - (OK)|
|[CT-5](#classic-test-5)|0.023126 - (ERROR)|1.117691 - (OK)|0.127841 - (OK)|0.069468 - (OK)|0.135830 - (OK)|
|[CT-6](#classic-test-6)|0.021238 - (ERROR)|1.089060 - (OK)|0.122279 - (OK)|0.074021 - (OK)|0.128023 - (OK)|
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
                
## Multiple Matches Test 1 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay 4 matches un match.

No hay mas de solo 8 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio y al final del
patron de largo n=500, siendo la cadena una concatenacion de 4 veces el patron.
                
## Multiple Matches Test 3 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay 4 matches un match.

No hay mas de solo 8 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=250, siendo la cadena una concatenacion de 4 veces el patron mas 4 veces un match parcial.
                    
## Multiple Matches Test 4 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay 4 matches un match.

No hay mas de solo 8 posible candidatos, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=250, siendo la cadena una concatenacion de 4 veces un match parcial mas 4 veces el patron.
                    
## One Character Test 1 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=500 el largo del patron.
                
## One Character Test 2 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=1 el largo del patron (patron corto).
                
## One Character Test 3 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=2 el largo del patron (patron corto de largo par).
                
## One Character Test 4 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=3 el largo del patron (patron corto de largo impar).
                
## One Character Test 5 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=3 el largo del patron (patron corto limite ventana DC3).
                
## One Character Test 6 

 
Corre 100 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un caracter.

Hay largo de la cadena menos n matches, siendo n=4 el largo del patron (patron limite+1 ventana DC3).
                
## Classic Test 1 

 
Corre 16666 veces el string matcher sobre "banana" buscando el patron "ana". Ejemplo de DC3
                
## Classic Test 2 

 
Corre 16666 veces el string matcher sobre "banana" buscando el patron "yaba". Ejemplo de DC3
                
## Classic Test 3 

 
Corre 8333 veces el string matcher sobre "yabbadabbado" buscando el patron "yabba". Ejemplo de DC3
                
## Classic Test 4 

 
Corre 8333 veces el string matcher sobre "yabbadabbado" buscando el patron "bba". Ejemplo de DC3
                
## Classic Test 5 

 
Corre 8333 veces el string matcher sobre "yabbadabbado" buscando el patron "dabba". Ejemplo de DC3
                
## Classic Test 6 

 
Corre 8333 veces el string matcher sobre "yabbadabbado" buscando el patron "ana". Ejemplo de DC3
                
