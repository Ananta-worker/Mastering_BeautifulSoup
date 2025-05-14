# Mastering_BeautifulSoup
Web scrapping using BeautifulSoup

pip install beautifulsoup4
pip install lxml
pip instal html.parser

soup.find(#tag)
contoh soup.find('h1')
soup.find(#attribute)
soup.find(class='title')
soup.find(#tag, #attribute)
soup.find('h1', class='tittle')
soup.find(#tag, #attribute)
output:<tag html>
contoh: <h1>...</h1>
soup.find_all(#tag)
soup.find_all('h1')
soup.find_all(#attribute)
soup.find_all(class='title)
soup.find_all(#tag, #attribute)
soup.fine_all('h1', class='title')
soup.find_all(#tag, #attribute)
Output: list dari <tag html>
contoh : [<h1>...</h1>,<h1>.../h1]
contoh tag:<h1 id="main_title">Selamat Datang</h1>
Mendapatkan value/informasi dari tag dapat menggunakan cara berikut:
1.tag.getText()   --> 'Selamat Datang'
2.tag['id'] --> 'main_title'
