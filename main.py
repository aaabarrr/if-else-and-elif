print(30*"-")
# deklarasi dan instalasi variable
pelangggan = "budi santoso"
totalbelnja = 1500000

# struktur kendali if dan else
if(totalbelnja > 1000000):
    keterangan = "selamat berbelanja"
else:
    keterangan = "terimaksih telah berbelanja"
print("pelanggan =", pelangggan, "\ntotalbelanja =",
      totalbelnja, "\n", keterangan)

print(30*"-")
# Siswa dinyatakan lulus minimal 60 nilainya
nama = "Budi Santoso"
matpel = "Matematika"
nilai = 59.99
# ternary
keterangan = "Lulus" if nilai >= 60 else "Gagal"
# cetak data
print("Nama Siswa \t:", nama,
      "\nMata Pelajaran \t:", matpel,
      "\nNilai \t\t:", nilai,
      "\nKeterangan \t:", keterangan)
print(30*"=")

# struktur elif

nama = "BUdi Santoso"
matpel = "matematika"
nilai = 55.99

# uji grade dengan if multi kondisi
if(nilai >= 85 and nilai <= 100):
    grade = "A"
elif(nilai >= 75 and nilai < 85):
    grade = "B"
elif(nilai >= 60 and nilai < 75):
    grade = "C"
elif(nilai >= 30 and nilai < 60):
    grade = "D"
else:
    grade = "E"

print("nama \t:", nama, "\nmatpel \t:", matpel,
      "\nnilai \t:", nilai, "\ngrade \t:", grade)
