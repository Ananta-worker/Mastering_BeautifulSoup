"""
Tipe data dictionary
"""
import pandas

data_murid={
    'nama' : 'Andi',
    'umur' : 20,
    'asal' : 'Bandung'
}

# print(data_murid)

nama = ['Andi', 'Siska', 'Yuda', 'Bimbim']
umur = [20, 21, 20, 19]
asal = ['Bandung', 'Jogja', 'Bali', 'Semarang']

data_murid={
    'nama': nama,
    'umur': umur,
    'asal': asal
}

# print(data_murid)

print(pandas.DataFrame(data_murid))