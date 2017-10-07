# Results 

 | |Baseline|DC3|Karp Rabin|Naive|Z Box|
|:---|---:|---:|---:|---:|---:|
|[NM-1](#no-matches-test-1)|0.017186 - (ERROR)|2.135775 - (OK)|0.415706 - (OK)|2.886849 - (OK)|0.344236 - (OK)|
|[NM-2](#no-matches-test-2)|0.016811 - (ERROR)|1.918817 - (OK)|0.396505 - (OK)|0.111752 - (OK)|0.267526 - (OK)|
|[NM-3](#no-matches-test-3)|0.013687 - (ERROR)|1.918957 - (OK)|0.210301 - (OK)|0.127184 - (OK)|0.180395 - (OK)|
|[NM-4](#no-matches-test-4)|0.013580 - (ERROR)|2.132799 - (OK)|0.210409 - (OK)|0.126176 - (OK)|0.183933 - (OK)|
|[NM-5](#no-matches-test-5)|0.017340 - (ERROR)|2.111235 - (OK)|0.399254 - (OK)|0.284318 - (OK)|0.214527 - (OK)|
|[NM-6](#no-matches-test-6)|0.014175 - (ERROR)|1.997571 - (OK)|0.278740 - (OK)|0.137198 - (OK)|0.207236 - (OK)|
|[OM-1](#one-match-test-1)|0.017079 - (ERROR)|1.929349 - (OK)|0.404964 - (OK)|0.120484 - (OK)|0.223060 - (OK)|
|[OM-2](#one-match-test-2)|0.020413 - (ERROR)|2.101337 - (OK)|0.415317 - (OK)|1.536240 - (OK)|0.258156 - (OK)|
|[OM-3](#one-match-test-3)|0.016960 - (ERROR)|2.004611 - (OK)|0.397295 - (OK)|0.125813 - (OK)|0.226778 - (OK)|
|[OM-4](#one-match-test-4)|0.017502 - (ERROR)|2.104273 - (OK)|0.412363 - (OK)|1.549076 - (OK)|0.257271 - (OK)|
|[PP-1](#pattern-to-pattern-1)|0.028399 - (ERROR)|1.920810 - (OK)|0.120553 - (OK)|0.050667 - (OK)|0.326068 - (OK)|
|[PP-2](#pattern-to-pattern-2)|0.029853 - (ERROR)|2.461420 - (OK)|0.119746 - (OK)|0.051231 - (OK)|0.486984 - (OK)|
|[PP-3](#pattern-to-pattern-3)|0.032240 - (ERROR)|2.338171 - (OK)|0.125935 - (OK)|0.056065 - (OK)|0.451795 - (OK)|
|[MM-1](#multiple-matches-test-1)|0.017858 - (ERROR)|2.297375 - (OK)|0.424408 - (OK)|0.140403 - (OK)|0.229957 - (OK)|
|[OC-1](#one-character-test-1)|0.018020 - (ERROR)|2.461347 - (ERROR)|9.025571 - (OK)|8.749499 - (OK)|0.384011 - (ERROR)|
|[OC-2](#one-character-test-2)|0.014013 - (ERROR)|2.126503 - (OK)|0.304606 - (OK)|0.137791 - (OK)|0.291629 - (OK)|
|[OC-3](#one-character-test-3)|0.013981 - (ERROR)|2.211520 - (OK)|0.398479 - (OK)|0.164537 - (OK)|0.359853 - (OK)|
|[OC-4](#one-character-test-4)|0.014484 - (ERROR)|2.243217 - (OK)|0.438049 - (OK)|0.183010 - (OK)|0.361047 - (ERROR)|
|[OC-5](#one-character-test-5)|0.013885 - (ERROR)|2.281308 - (OK)|0.440162 - (OK)|0.183095 - (OK)|0.362828 - (ERROR)|
|[OC-6](#one-character-test-6)|0.013797 - (ERROR)|2.312930 - (OK)|0.458482 - (OK)|0.212102 - (OK)|0.363694 - (ERROR)|
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
                
