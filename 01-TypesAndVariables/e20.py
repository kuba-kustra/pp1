"""
Obliczanie pola powierzchni i obwodu koła o zadanym promieniu
"""

import math

# ustal promień koła i PI
r = 5
pi = math.pi

# oblicz pole i obwód
g = pi * math.pow(r, 2)
c = 2 * pi * r

# wyświetl rezultaty
print(f'Pole koła o promieniu {r} wynosi {g}')
print(f'Obwód koła o promieniu {r} wynosi {c}')
