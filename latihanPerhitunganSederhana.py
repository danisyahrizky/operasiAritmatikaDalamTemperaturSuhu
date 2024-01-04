#program konversi suhu satuan temperature

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam celcius :"))
print("Suhu dalam celcius adalah", celcius)

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur :", reamur)

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit :", fahrenheit)

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin:", kelvin)