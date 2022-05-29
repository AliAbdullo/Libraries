import math
from pprint import pprint
import json
import re

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

# Andoza bilan ishlash
matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn)
print(f"\n{email}")

# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '

while True:
    password = input(msg)
    if re.match(andoza,password):
        print("\nMaxfiy so'z qabul qilindi")
        break
    else:
        print("\nMaxfiy so'z talabga javob bermadi\n")