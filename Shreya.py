# your code goes here
import math
#Inputs
floors = list(map(int, input().split()))
yoda_capacity = int(input())
jedi_capacity = int(input())

total_floors = len(floors)
jedi = [0]*total_floors

for index,i in enumerate(floors):
    jedi[index] = math.ceil(i/jedi_capacity)
total_jedi = sum(jedi)

min_jedi = float('inf')
for index, children in enumerate(floors):
    children = max(0,children-yoda_capacity)
    k = total_jedi - jedi[index] + math.ceil(children / jedi_capacity)
    min_jedi = min(min_jedi,k)
    
print(min_jedi)
