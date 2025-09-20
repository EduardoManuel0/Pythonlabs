name=input("ФИО:")
name=' '.join(name.split())
init=""

for part in name.split():
    init=init+part[0].upper()
size=len(name)

print (f"Инициалы: {init}")
print (f"Длина (символов): {size}")