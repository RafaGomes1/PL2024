# TPC6

## Autor

**Nome:** Rafael Gomes

**ID:** A96208

## Resumo
Construir uma gramática correspondente aos seguintes exemplos:

### Exemplos:
```
? a
b = a * 2 / ( 27 - 3 )
! a + b
c = ( a * b ) / ( a / b )
```

### Resolução
```
T = {'(', ')', '-', '+', '*', '/', '=', '?', '!', VAR, NUM}

N = {S, Expressão, Expressão2, Expressão3, Sinal, Sinal2}

S = S

P = {
    S -> '?' VAR                         LA = {'?'}
       | '!' Expressão                   LA = {'!'}
       | VAR '=' Expressão               LA = {VAR}

    Expressão -> Expressão2 Sinal

    Sinal -> '+' Expressão               LA = {'+'}
        | '-' Expressão                  LA = {'-'}
        | &                              LA = {$, ')'} 
    
    Expressão2 -> Expressão3 Sinal2      LA = {'(', VAR, NUM}

    Sinal2 -> '*' Expressão              LA = {'*'}
         | '/' Expressão                 LA = {'/'}
         | &                             LA = {'+', '-', $, ')'}

    Expressão3 -> '(' Expressão ')'      LA = {'('}
           | VAR                         LA = {VAR}
           | NUM                         LA = {NUM}
}               
```
