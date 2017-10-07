# Results 

 | |Baseline|DC3|Karp Rabin|Naive|Z Box|
|:---|---:|---:|---:|---:|---:|
|[NM-1](#no-matches-test-1)|0.016456 - (ERROR)|2.129789 - (OK)|0.434065 - (OK)|2.876832 - (OK)|0.347248 - (OK)|
|[NM-2](#no-matches-test-2)|0.016541 - (ERROR)|1.929683 - (OK)|0.418871 - (OK)|0.108562 - (OK)|0.269542 - (OK)|
|[NM-3](#no-matches-test-3)|0.013430 - (ERROR)|1.914481 - (OK)|0.232381 - (OK)|0.122749 - (OK)|0.188201 - (OK)|
|[NM-4](#no-matches-test-4)|0.013343 - (ERROR)|2.154105 - (OK)|0.232962 - (OK)|0.119063 - (OK)|0.188928 - (OK)|
|[NM-5](#no-matches-test-5)|0.017118 - (ERROR)|2.140459 - (OK)|0.420220 - (OK)|0.279786 - (OK)|0.214850 - (OK)|
|[NM-6](#no-matches-test-6)|0.014161 - (ERROR)|2.001456 - (OK)|0.298859 - (OK)|0.138058 - (OK)|0.207552 - (OK)|
|[OM-1](#one-match-test-1)|0.017016 - (ERROR)|1.936703 - (OK)|0.424397 - (OK)|0.117867 - (OK)|0.232321 - (OK)|
|[OM-2](#one-match-test-2)|0.017259 - (ERROR)|2.106913 - (OK)|0.436343 - (OK)|1.491656 - (OK)|0.259428 - (OK)|
|[OM-3](#one-match-test-3)|0.016730 - (ERROR)|2.017195 - (OK)|0.419436 - (OK)|0.116758 - (OK)|0.228740 - (OK)|
|[OM-4](#one-match-test-4)|0.016991 - (ERROR)|2.122989 - (OK)|0.428649 - (OK)|1.485783 - (OK)|0.257669 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.028356 - (ERROR)|1.927103 - (OK)|0.123628 - (OK)|0.049309 - (OK)|0.328978 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.028327 - (ERROR)|2.492405 - (OK)|0.125662 - (OK)|0.049818 - (OK)|0.490412 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.027652 - (ERROR)|2.344944 - (OK)|0.132168 - (OK)|0.051090 - (OK)|0.463182 - (OK)|
|[MM-1](#multiple-matches-test-1)|0.017139 - (ERROR)|2.280765 - (OK)|0.448121 - (OK)|0.131713 - (OK)|0.220735 - (OK)|
|[MM-2](#multiple-matches-test-1)|0.017476 - (ERROR)|2.040534 - (OK)|0.444634 - (OK)|0.133241 - (OK)|0.215398 - (OK)|
|[MM-3](#multiple-matches-test-3)|0.015532 - (ERROR)|2.233530 - (ERROR)|0.346415 - (OK)|0.131043 - (OK)|0.184008 - (OK)|
|[MM-4](#multiple-matches-test-4)|0.015543 - (ERROR)|2.222516 - (ERROR)|0.345968 - (OK)|0.132099 - (OK)|0.180376 - (OK)|
|[OC-1](#one-character-test-1)|0.017298 - (ERROR)|2.498204 - (ERROR)|9.744886 - (OK)|8.970904 - (OK)|0.403840 - (ERROR)|
|[OC-2](#one-character-test-2)|0.013664 - (ERROR)|2.134173 - (OK)|0.298437 - (OK)|0.127826 - (OK)|0.264582 - (OK)|
|[OC-3](#one-character-test-3)|0.013373 - (ERROR)|2.203474 - (OK)|0.414106 - (OK)|0.156026 - (OK)|0.368488 - (OK)|
|[OC-4](#one-character-test-4)|0.013473 - (ERROR)|2.267330 - (OK)|0.451810 - (OK)|0.176918 - (OK)|0.370282 - (ERROR)|
|[OC-5](#one-character-test-5)|0.013427 - (ERROR)|2.273291 - (OK)|0.456627 - (OK)|0.180976 - (OK)|0.373647 - (ERROR)|
|[OC-6](#one-character-test-6)|0.014055 - (ERROR)|2.346628 - (OK)|0.477325 - (OK)|0.198744 - (OK)|0.368680 - (ERROR)|
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
                
