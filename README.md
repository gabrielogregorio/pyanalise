# Py Analise
Script para comparar a semelhança entre duas frases, se baseando nas letras de ambas e retornando um valor de 0 a 100. Ele pega todas as letras da frase maior e compara com a frase menor, retornando um valor de 0 a 100 de acordo com a quantidade de letras iguais encontradas na frase menor.

# Comparação
* Todos os espaços são removidos
* Todos os caracteres maiusculos são substituidos por minusculos
* As frases são transformadas em listas

# Resultados
Esse script não leva em consideração o contexto das letras, portanto, __abacaxi__ e __axicaba__ são considerados iguais e retornam um valor de __100%__ já que ambas possuem as mesmas letras nas mesmas quantidades. 

