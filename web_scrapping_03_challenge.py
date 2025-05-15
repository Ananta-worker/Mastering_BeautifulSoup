from bs4 import BeautifulSoup
import pandas

file_web = open('contoh_tabel.html', mode='r')
hal_web = file_web.read()
file_web.close()

soup = BeautifulSoup(hal_web, 'lxml')

box_table = soup.find("thead")
# print(box_table.prettify())

tag_judul_kolom = soup.find_all('th')
# print(tag_judul_kolom)

judul_kolom = []
for item in tag_judul_kolom:
    judul_kolom.append(item.getText())
# print(judul_kolom)

isi_tabel_all = soup.find("tbody")

tag_isi_tabel = soup.find_all('td')

isi_tabel = []
for item in tag_isi_tabel:
    isi_tabel.append(item.getText())
# print(isi_tabel)

nama = (isi_tabel[0::3])
umur = (isi_tabel[1::3])
kota = (isi_tabel[2::3])

daftar_isi_tabel = {
    judul_kolom[0]: nama,
    judul_kolom[1]: umur,
    judul_kolom[2]: kota
}

df_daftar_isi_tabel = pandas.DataFrame(daftar_isi_tabel)
df_daftar_isi_tabel.to_csv('hasil_scrapping_tabel.csv')