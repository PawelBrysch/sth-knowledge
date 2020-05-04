from functools import partial
def suma(a, b):
    return a+b

suma_z_piatka = partial(suma, b=5)

print(suma_z_piatka(3))