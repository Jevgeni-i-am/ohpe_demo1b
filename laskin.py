luku = 0
print("Luku on", luku)
while True:

    syotto = str(input("Anna operaatio(tyhjä lopettaa): "))
    if syotto == "":
        print("Kiitos ja moi!")
        break
    operaatio = syotto[0]
    operaation_luku = int(syotto[1:])
    if operaation_luku == 0 and operaatio == '/':
        print("Et voi jakaa nollaan! Syötä muu operaatio, ole hyvä!")
        print("Luku on", luku)

    elif operaatio != "+" and operaatio != "-" and operaatio != "*" and operaatio != "/":
        print("Et ole syöttänyt operaation merkki!")
        print(f'Syötä luvun eteen " + "," - "," * " tai " / " - merkki, ole hyvä!')
        print("Luku on", luku)

    elif operaatio == '+':
        luku = luku+operaation_luku
        print("Luku on: ", luku)

    elif operaatio == '-':
        luku = luku-operaation_luku
        print("Luku on: ", luku)
    elif operaatio == '*':
        luku = luku*operaation_luku
        print("Luku on: ", luku)
    elif operaatio == '/':
        luku = luku/operaation_luku
        print("Luku on: ", luku)
