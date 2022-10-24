#Algorithme nombre max

#Methode 1
A=int(input('Donner un nombre '))
B=int(input('Donner un 2eme nombre '))
C=int(input('Donner un 3eme nombre '))

if(A>B):
    if(A>C):
        print(A,' est le plus grand nombre ')
    else:
        print(C,' est le plus grand nombre ')
else:
    if(B>C):
        print(B,' est le plus grand nombre ')
    else:
        print(C,' est le plus grand nombre ')

#Methode 2

result=max(A,B,C)

print(result,' est le plus grand nombre ')
