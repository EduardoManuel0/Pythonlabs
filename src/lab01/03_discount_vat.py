price=float(input("what is the price: "))
descount=float(input("what is the descount: "))
vat=float(input("what is the VAT: "))

base = price * (1 - descount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} ₽")
print(f"НДС: {vat_amount:>20.2f} ₽")
print(f"Итого к оплате: {total:>10.2f} ₽")