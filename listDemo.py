import numpy as ny
x = [1, 2, 3, 4, 5, 6]
print x[:3]
x.append(7)
print x
captains = {}
captains['voyager'] = 'king'
captains['mars1'] = 'Great'
captains['explorer'] = 'Awesome'


print captains['explorer']

for drivers in captains:
    print drivers + ':' + captains[drivers]

"""to print the list of integers and show only the even numbers"""
integersList= {}
integersList=range(100)
print integersList
for integ in integersList:
    if integ%2==0:
        print integ





