import datetime as dt
import re

# 10 ta sana konsolga chiqarish 
iyun18 = dt.datetime(2022,6,18)
print(iyun18)

iyul20 = dt.date(2022,7,20)
print(iyul20)

avgust25 = dt.datetime(2022,8,25)
print(avgust25)

bizda = avgust25.strftime("%d-%m-%Y")
print(bizda)

iyul3 = dt.date(2022,7,3)  
print(iyul3)

uz_iyul3 = iyul3.strftime("%d/%m/%Y")
print(uz_iyul3)

iyun17 = dt.date(2022,6,17).strftime("%d-%m-%Y")
print(iyun17)

noyabr16 = dt.date(2022,11,16).strftime("%d-%m/%Y")
print(noyabr16)

iyul9 = dt.datetime(2022,8,9,23,43,54)
print(iyul9)

bugun = dt.datetime.today()
print(bugun.strftime("%d-%m-%Y"))

# 2.Qurbor hayitigacha qolgan mudat
qurbonHayiti = dt.datetime(2022,7,13)
qoldi = qurbonHayiti - bugun
print(f"\nQurbon hayitga {qoldi} vaqt qoldi!\n")

# 3.Tug'ulgan kunimdan bugungacha o'tgan vaqt
tugulganKunim = dt.datetime(2022,1,30)
otdi = bugun - tugulganKunim
print(f"Bu yilgi tug'ulgan kunim o'tganiga {otdi} vaqt bo'libdi!\n")

# 4.Foydalanuvchidan kiritilgan telefon raqamini tekshiruvchi andoza
andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9 ]{4,6}$'
msg = "Telefon raqamingizni kiriting"
msg += "('+' ishorasi bilan boshlang, "
msg += "0-dan 9 gacha son ishlating):"

while True:
  nomer = input(msg)
  if re.match(andoza,nomer):
    print(f"\n{nomer} raqami muvafaqiyyatli qabul qilindi!\n")
    break
  else:
    print(f"\nKiritgan {nomer} raqamingiz xato !/n")

# 5.Veb sahifani ajratib ollish
domen = []
matnlar = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI
Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

andoza1 = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{ 1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'
veb = re.findall(andoza1,matnlar)
print(veb)
# Hammasi muvafaqiyatli bajarildai faqat 5 dan tashqari
#5-topshiriqda muamoni topa olmadim!!!