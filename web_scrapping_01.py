from bs4 import BeautifulSoup

file_web = open('contoh_web.html', mode='r')
hal_web = file_web.read()
file_web.close()

# membuat soup
soup = BeautifulSoup(hal_web, 'lxml')
# print(soup.prettify())

tag_judul = soup.find('h1', id='main_title')
judul_web = tag_judul.getText()
# print(judul_web)

tag_paragraf = soup.find_all('p', class_='opening')

paragraf1 = tag_paragraf[0].getText()
paragraf2 = tag_paragraf[1].getText()
# print(paragraf1)
# print(paragraf2)
file = open('hasil_scrapping_01.txt', mode='w')
file.write('JUDUL = \n')
file.write(judul_web+'\n')
file.write('ISI PARAGRAF = \n')
file.write(paragraf1+'\n')
file.write(paragraf2+'\n')
