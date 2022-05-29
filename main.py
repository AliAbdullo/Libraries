import math
from pprint import pprint
import json
PI = math.pi
print(f"PI ning qiymati: {PI}")

E = math.e
print(f"e ning qiymati:{E}")

x = 81

# Kvadrat ildiz 
math.sqrt(x)

#Darajaga oshirish 
math.pow(x,3) # x ning kubi
print(math.pow(x,5)) # x ning 5-darajasi
print(math.pow(x,1/3)) # x dan kub ildiz


## CHIROYLI PRINT-pprint
filename = 'bemor.json'
with open(filename) as f:
  bemor = json.load(f)

print(f"\n{bemor}\n")
pprint(bemor)

