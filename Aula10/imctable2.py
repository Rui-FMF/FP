
# Devolve o IMC para uma pessoa com peso w e altura h.
def imc(w, h):
    return w/h**2


def main():
    # Lista de pessoas com nome, peso em kg, altura em metro.
    people = [("John", 64.5, 1.757),
        ("Berta", 64.0, 1.612),
        ("Maria", 45.1, 1.715),
        ("Andy", 98.3, 1.81),
        ("Lisa", 46.8, 1.622),
        ("Kelly", 83.2, 1.78)]

    print("People:", people)

    # Usando list comprehensions, obtenha: 
    # a) Uma lista com os valores de imc de todas as pessoas.
    imcs = [round(imc(x[1], x[2]), 2) for x in people]
    print("IMCs:", imcs)

    # b) Uma lista de (registos de) pessoas com altura superior a 1.7m.
    tallpeople = [x for x in people if x[2]>1.7]
    print("Tall people:", tallpeople)    

    # c) Uma lista de nomes das pessoas com IMC entre 18 e 25.
    midimc = [n for n, w, h in people if (imc(w, h)>18 and imc(w, h)<25) ]
    print("Mid-IMC:", midimc)


# O programa começa aqui
main()

