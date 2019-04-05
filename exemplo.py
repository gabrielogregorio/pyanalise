from pyanalise import compare

while True:
    a = input('Digite a primeira frase: ')
    b = input('Digite a segunda frase : ')
    print("A semelhança entre '{}' e '{}' é de {}% \n".format(a,b,compare(a,b)))


