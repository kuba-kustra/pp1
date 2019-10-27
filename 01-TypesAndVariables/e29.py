from random import randint

a = int(input("Podaj swoją liczbę: "))
d = randint(1, 6)
print(f'Komputer wyrzucił: {d}')
print(f'Zgadłeś: {a == d}')