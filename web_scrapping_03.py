from bs4 import BeautifulSoup
import pandas

file_web = open('contoh_web.html', mode='r')
hal_web = file_web.read()
file_web.close()

soup = BeautifulSoup(hal_web, 'lxml')

box_table = soup.find('table')
# print(box_table.prettify())

tag_judul_kolom = box_table.find_all('th')
judul_kolom = []
for item in tag_judul_kolom:
    judul_kolom.append(item.getText())
print(judul_kolom)

#mengambil isi kolom
tag_isi_kolom = soup.find_all('td')
isi_kolom = []
for item in tag_isi_kolom:
    isi_kolom.append(item.getText())

bahasa_pemrograman = (isi_kolom[0::3])
waktu_kursus = (isi_kolom[1::3])
biaya_kursus = (isi_kolom[2::3])

informasi_kursus = {
    judul_kolom[0]: bahasa_pemrograman,
    judul_kolom[1]: waktu_kursus,
    judul_kolom[2]: biaya_kursus
}

df_informasi_kursus = pandas.DataFrame(informasi_kursus)
df_informasi_kursus.to_csv ('hasil_scrapping_03.csv')
