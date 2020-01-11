student = {
'imie' : 'Andrzej',
'nazwisko' : 'Nowak',
'wiek' : '30',
'płeć' : 'm',
'kierunek' : 'informatyka',
'hobby' : ['rower', 'siłka', 'koleżanki'],
'adres' : {
    'miasto' : 'Zgorzelec',
    'ulica' : 'Królewska',
    'nr domu' : '69',
    }
}
for k, v in student.items():
    print(k , v)
