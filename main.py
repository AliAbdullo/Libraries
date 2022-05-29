import datetime as dt

hozir= dt.datetime.now()
print(hozir)

# sanani ajratib olish 
print(hozir.date())

# vaqtni ajratib olish 
print(hozir.time())

# soatni ajratib olish 
print(hozir.hour)

# minutni ajratib olish 
print(hozir.minute)

# sekundni ajratib olish 
print(hozir.second)


# Agar bugungi kunning sanasi talab qilinsa datetime moduli ichidagi date.today() moduliga murojat qilamiz.
bugun = dt.date.today()
print(bugun)

ertaga= dt.date(2022, 5, 30)
print(f"Ertangi sana: {ertaga}")

hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")

# istalgan vaqt kiritish 
vaqtKeyin = dt.time(21,00,10)



# Oradagi farqlarni xisoblash
bugun = dt.date.today()
iyul = dt.date(2022,7,1)
farq = iyul-bugun
print(farq)
print(f"Iyul oyiga {farq.days} kun qoldi\n")

bugun = dt.date.today()
ramazon = dt.date(2021, 4, 13)
farq = ramazon-bugun
print(farq)
print(f"Ramazonga {farq.days} kun qoldi")

# kun, soat, minut, sekundlardagi  farq

hozir = dt.datetime.now()
working = dt.datetime(2022,11,16,12,00,00)
farq = working - hozir
kunlar = farq.days
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Working boshlanishiga {kunlar} kun, {sekundlar} sekund qoldi\n ")
print(f"Working boshlanishiga {kunlar} kun, {minutlar} minut qoldi\n")
print(f"Working boshlanishiga {kunlar} kun, {soatlar} soat qoldi\n")


# vaqtni millisekundsiz chiqaramiz 
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat: {vaqt}")

# sanani kun- oy-yil ko'rinishida chaqiramiz
sana = hozir.strftime("%d-%m-%Y")
print(f"Bugun sana: {sana}")

#sanani kun/oy/yil ko'rinishida chiqaramiz
sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
print(sana_vaqt)
