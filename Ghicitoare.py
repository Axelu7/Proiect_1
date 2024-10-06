import random

print("Giceste numarul! \n Ai 7 incercari...")

numarul = random.randrange(100)

sanse = 7

incercari = 0

while incercari < sanse:

    incercari += 1
    nr_ales = int(input('Te rog scrie numarul: '))

    if nr_ales == numarul:
        print(f'Numarul corect este {numarul} si l-ai nimerit din a {incercari} -a incercare!!!')
        break

    elif incercari >= sanse and nr_ales != numarul:
        print(f'Imi pare rau, dar numarul era {numarul}...')

    elif nr_ales > numarul:
        print('Numarul tau este mai mare decat cel corect.')

    elif nr_ales < numarul:
        print('Numarul tau este mai mic decat cel corect.')