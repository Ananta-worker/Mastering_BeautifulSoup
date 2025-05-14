from bs4 import BeautifulSoup

file_web = open('contoh_web.html', mode='r')
hal_web = file_web.read()
file_web.close()

soup = BeautifulSoup(hal_web, 'lxml')

tag_judul = soup.find('h1', id='main_title')
judul_web = tag_judul.getText()
# print(judul_web)

tag_paragraf = soup.find_all('p')
paragraf1 = tag_paragraf[0].getText()
paragraf2 = tag_paragraf[1].getText()
paragraf3 = tag_paragraf[2].getText()

file = open('hasil_scrapping_01_challenge.txt', mode='w')
file.write('JUDUL = \n')
file.write(judul_web+'\n')
file.write('ISI PARAGRAF = \n')
file.write(paragraf1+'\n')
file.write(paragraf2+'\n')
file.write(paragraf3+'\n')
