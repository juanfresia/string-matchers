# Results 

 | |Karp Rabin|Naive|Nothing _Test Only_|Z Box|
|:---|:---|:---|:---|:---|
|[NM-1](#no-matches-test-1)|13.341476 - (OK)|30.857795 - (OK)|0.000170 - (ERROR)|88.694739 - (ERROR)|
|[NM-2](#no-matches-test-2)|13.220517 - (OK)|0.930800 - (OK)|0.000158 - (ERROR)|30.338631 - (OK)|
|[NM-3](#no-matches-test-3)|2.077976 - (OK)|1.057990 - (OK)|0.000187 - (ERROR)|2.158815 - (ERROR)|
|[NM-4](#no-matches-test-4)|13.193669 - (OK)|0.926853 - (OK)|0.000160 - (ERROR)|30.373515 - (OK)|
|[NM-5](#no-matches-test-5)|13.265501 - (OK)|2.777061 - (OK)|0.000156 - (ERROR)|5.565936 - (OK)|
|[OM-1](#one-match-test-1)|13.216904 - (OK)|0.977546 - (OK)|0.000178 - (ERROR)|2.473283 - (OK)|
|[OM-2](#one-match-test-2)|13.149849 - (OK)|16.195215 - (OK)|0.000175 - (ERROR)|59.138818 - (ERROR)|
|[OM-3](#one-match-test-3)|13.232920 - (OK)|0.989832 - (OK)|0.000177 - (ERROR)|2.525178 - (OK)|
|[OM-2](#one-match-test-2)|13.570741 - (OK)|16.776300 - (OK)|0.000179 - (ERROR)|59.000027 - (ERROR)|
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

No hay ningun posible candidato porque no hay caracteres en comun entre el patron y el string. Patron de largo n=500 (Patron corto).
                
## No Matches Test 5 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual no hay matches.

La cadena esta conformada por 4 patrones concatenados sin el ultimo caracter. El patron es periodico asi que hay varios matches parciales. 
El patron es de largo n, con n=500.
                
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
                
## One Match Test 2 

 
Corre 1000 veces el string matcher sobre una cadena de largo 2000 en la cual hay solo un match.

Hay varios posibles candidatos ya que, solo hay 3 caracteres en la cadena, y uno solo se presenta al inicio del
patron de largo n=500 de forma repetida..
                
