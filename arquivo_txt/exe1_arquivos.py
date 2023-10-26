import random

prod = [
    ["celular", "Samsung", 4000.00],
    ["celular", "Xiaomi", 2450.00],
    ["SmartTv", "Samsung", 3859.99],
    ["SmartTv", "LG", 3199.99],
    ["Geladeira", "Brastemp", 2800],
    ["Geladeira", "Panasonic", 3890],
    ["Notebook", "Acer", 2700],
    ["Notebook", "Lenovo", 2350],
    ["Microondas", "Brastemp", 750],
    ["Microondas", "LG", 680 ]
]

lojas = ["Center Norte", "Paulista", "Cidade de São Paulo"]

with open('faturamento.txt', 'w') as arq:

    for i in range(8000):
        x = random.randint(0, 7)
        y = random.randint(0, 2)
        qtd = random.randint(5, 20)
        dia = random.randint(1, 31)
        mes = random.randint(1, 12)

        if dia == 31 and mes in [4, 6, 9, 11]:
            dia = 1
        elif mes == 2 and dia > 28:
            dia = 1

        r = f"{prod[x][0]};{prod[x][1]};{lojas[y]};2022-{mes}-{dia};{qtd};{prod[x][2]}"
        arq.write(r + '\n')
