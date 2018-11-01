from random import randint


naipes = {
    0: "Paus",
    1: "Ouros",
    2: "Copas",
    3: "Espadas",
    4: "Paus do baralho 1",
    5: "Ouros do baralho 1",
    6: "Copas do baralho 1",
    7: "Espadas do baralho 1",
    8: "Paus do baralho 2",
    9: "Ouros do baralho 2",
    10: "Copas do baralho 2",
    11: "Espadas do baralho 2",
    12: "Paus do  baralho 3",
    13: "Ouros do baralho 3",
    14: "Copas do baralho 3",
    15: "Espadas do baralho 3"









}
cartas = {
    0: "As",
    1: "2",
    2: "3",
    3: "4",
    4: "5",
    5: "6",
    6: "7",
    7: "8",
    8: "9",
    9: "10",
    10: "Valete",
    11: "Rainha",
    12: "Rei",


}
def construir_cartas(num_cartas, list_default=[]):
    for z in range(num_cartas):
        x = randint(0, 15)
        y = randint(0, 12)
        minhas_cartas = "{0} de {1}".format(cartas[y], naipes[x])
        if minhas_cartas not in list_default:
            list_default.append(minhas_cartas)
        else:
            num_cartas = num_cartas-z
            return construir_cartas(num_cartas, list_default)
    return list_default
meu_desenho = construir_cartas(20)


i = 0
for x in meu_desenho:
    i += 1
    if i == len(meu_desenho):
        print("... E a sua ultima carta é o : {0}".format(str(x)))
    else:
        print(" {0}  ".format(str(x)))
