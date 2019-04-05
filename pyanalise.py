# ! / usr / bin / python3
# - * - codificação: utf-8 - * -

__author__       =  ' Gabriel Gregório da Silva '
__email__        =  ' gabriel.gregorio.1@outlook.com '
__description__  =  ' Comparador de letras em uma frase '
__status__       =  ' Desenvolvimento '
__date__         =  ' 05/04/2019 '
__version__      =  ' 1.0 '

def compare(a,b):
    # o 'b' tem que ser maior que o 'a' ou no minimo igual!
    if len(a)>len(b):
        c = b
        b = a
        a = c

    # Remoção de espaços | Todos para minisculos | Adição de espaços | Para lista
    a = a.replace(' ','').lower().replace('',' ').split(" ")
    b = b.replace(' ','').lower().replace('',' ').split(" ")

    # Corte dos espaços no começo e no fim
    a = a[1:len(a)-1]
    b = b[1:len(b)-1]

    # Quantidade de caracteres do maior valor
    total_b = len(b)

    for x in a:
        for y in b:
            if x == y:
                b.remove(y)
                break

    return ((100/total_b)*(total_b-len(b)))
