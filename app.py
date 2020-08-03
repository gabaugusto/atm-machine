print('Caixa Eletrônico em Python')
restart = ('y')
attempts = 3
balance = 999.12

while attempts < 3:
    pin = int(input('Por favor, informe sua senha: '))
    if pin == 1234: 
        print("""
        1. Saldo
        2. Saque
        3. Depósito
        4. Sair
        """)
        try: 
            option = int(input("Escolha uma opção "))

        except Exception as e: 
            print("Error:", e)
            print("Escolha uma opção entre 1, 2, 3 e 4", e)
            continue

        if option == 1:
            print("Saldo R$", balance)

        if option == 2:

            print("Balance R$", balance)
            withdraw= float (input("Insira o valor para saque: "))
            if withdraw > 0:
                balance = balance - withdraw
                print("O saldo na sua conta é de: ", balance)
            elif withdraw > balance:
                print("Não há saldo suficiente na conta")
            else:          
                print("Sua conta não foi movimentada")

        if option == 3:
            deposit = float(input("informe o valor do depósito")) 
            if deposit > 0:
                balance = balance + deposit
                print("Depósito realizado com sucesso. O saldo na sua conta é de ", balance)

        if  option == 4:
            exit() 

    elif pin != 1234:
        print('Senha incorreta. Por favor, tente novamente')
        attempts = attempts - 1
        if attempts == 0:
            print("Sua conta foi bloqueada. Por favor, contate o gerente do seu banco")
            break
    