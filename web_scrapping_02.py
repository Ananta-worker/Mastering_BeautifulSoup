from bs4 import BeautifulSoup

file_web = open('contoh_web.html', mode='r')
hal_web = file_web.read()
file_web.close()

soup = BeautifulSoup(hal_web, 'lxml')

"""
print("pengulangan umum/standar")
daftar_buah = ['apple', 'mangga', 'rambutan', 'nangka']
for item in daftar_buah:
    print(item)

print("\npenambahan dalam list")
daftar_buah = ['apple', 'mangga', 'rambutan', 'nangka']
daftar_belanja = ['garam', 'gula']

for item in daftar_buah:
    daftar_belanja.append(item)
print(daftar_belanja)


# memerlukan list
print("\npengulangan dengan enumerate")
daftar_buah = ['apple', 'mangga', 'rambutan', 'nangka']
for indeks, buah in enumerate(daftar_buah, start=1):
    print(f" indeks {indeks}: {buah}")

# tdk memerlukan list, jumlah pengulangan sudah tertentu
print("\nPengulangan dengan for-range")
for i in range(5):
    print(f"Pengulangan ke-{i+1}")
"""

# box_ul = soup.find('ul', class_ ='daftar_kursus')
# kursus = box_ul.find_all('li')
#
# daftar_kursus = []
# for item in kursus:
#     x = item.getText()
#     daftar_kursus.append(x)
# print(daftar_kursus)

langkah_belajar = soup.find('ol', class_ = 'langkah_belajar')
lbelajar = langkah_belajar.find_all('li')


daftar_langkah = []
for item in lbelajar:
    x = item.getText()
    daftar_langkah.append(x)
daftar_langkah_belajar = daftar_langkah

for index, daftar in enumerate(daftar_langkah_belajar, start=1):
    print(f"{index} :{daftar}")
