print("LATIHAN 11")

print("<<<\t\tlatihan\t\t>>>")
print("Berikut akan tampil list dengan kondisi : ")
print("1. range(1.100)")
print("2. value/item : genap (i >= 10 dan i <= 20)")
print("3. value/item : ganjil (i >= 90 dan i <= 100)")

data1 = [ i for i in range(10, 22) if i % 2 == 0]
data2 = [ i for i in range(90, 100) if i % 2 == 1]
print(f"{data1 + data2}")