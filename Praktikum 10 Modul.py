class Matematika:
    def tambah(a, b):
        return a + b
    
    def kurang(a, b):
        return a - b
    
    def kali(a, b):
        return a * b
    
    def bagi(a, b):
        return a / b
    
    def pangkat(a, b):
        return a ** b


# ====== Modul ======
M = Matematika


# ====== Import sebagian fungsi  ======
def tambah(a, b): return Matematika.tambah(a, b)
def kurang(a, b): return Matematika.kurang(a, b)


# ====== Import semua fungsi ======
kali = Matematika.kali
bagi = Matematika.bagi
pangkat = Matematika.pangkat


print("--gunakan modul--")
print("hasil tambah dari 5 + 2 =", Matematika.tambah(5, 2))
print("hasil pengurangan dari 10 - 3 =", Matematika.kurang(10, 3))
print("hasil perkalian dari 5 * 6 =", Matematika.kali(5, 6))

print("\n--gunakan modul yg ada dgn alias--")
print("hasil pembagian dari 20 / 2 =", M.bagi(20, 2))
print("hasil pemangkatan dari 2 ^ 3 =", M.pangkat(2, 3))

print("\n--gunakan modul dgn memanggil sebagian fungsinya--")
print("hasil tambah dari 20 + 30 =", tambah(20, 30))
print("hasil pengurangan dari 2 - 3 =", kurang(2, 3))

print("\n--gunakan modul dgn memanggil seluruh fungsinya--")
print("hasil tambah dari 20 + 30 =", tambah(20, 30))
print("hasil pengurangan dari 2 - 3 =", kurang(2, 3))
print("hasil perkalian dari 5 * 6 =", kali(5, 6))
print("hasil pembagian dari 20 / 2 =", bagi(20, 2))
print("hasil pemangkatan dari 2 ^ 3 =", pangkat(2, 3))

print("\n--gunakan modul dgn memanggil sebagian fungsinya dengan alias--")

tmb = Matematika.tambah
krg = Matematika.kurang
print("hasil tambah dari 3 + 7 =", tmb(3, 7))
print("hasil pengurangan dari 10 - 12 =", krg(10, 12))

