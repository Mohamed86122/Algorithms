#Calcul de nombre premier

A = int(input('Donner un nombre'))
P=0
for i in range(2,A-1):
    if(int(A) % i == 0):
        P=P+1

if(P==2):
    print(A , "est premier")
else:
    print(A, "n'est pas premier")



