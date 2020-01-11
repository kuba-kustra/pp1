#całość "osoba" to słownik  
# poszczególne elementy w słowniku to listy

osoba = {                                                          
"imie": "Marek",
"nazwisko": "Banach",
"wiek": 25,
"hobby": ["programowanie","wycieczki"],
"student": True,
"telefon":{"stacjonarny":"2233","komorkowy":"7788"}
}
#a
print(osoba)
#b
print(osoba['nazwisko'])
#c
print(osoba['hobby'])
#d
osoba['nazwisko'] = 'Nowak'
print(osoba['nazwisko'])
#e
osoba['student'] = 'False'
print(osoba['student'])
#f
osoba['Płeć'] = 'Mężczyzna'
print(osoba['Płeć'])
#g
osoba['hobby'].append('rower')
print(osoba['hobby'])
#h
osoba['telefon']['służbowy'] = '3131' #ważne
print(osoba['telefon'])

print(osoba)



    


