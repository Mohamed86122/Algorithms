#Algorithme Factorielle

nbr=int(input('Donner un nombre'))
result = 1
for i in range(1, nbr+1):
  result = result * i
print (nbr,'! = ',result)