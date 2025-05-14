from bs4 import BeautifulSoup

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

#mengambil isi kolom
tag_isi_kolom = soup.find_all('td')
isi_kolom = []
for item in tag_isi_kolom:
    isi_kolom.append(item.getText())

print(judul_kolom)
print(isi_kolom)