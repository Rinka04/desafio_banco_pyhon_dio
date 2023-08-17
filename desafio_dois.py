menu = """

===========Bem VIndo===========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

===============================

"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True :

    opcao = input(menu)

    if opcao == "1":
        print ("Deposito")
        valor = float(input ("Quanto Gostaria de Depositar? \n"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito R$ {valor: .2f} \n"
            print (" Depositando ...")
            print ("Deposto Feito com sucesso!")
        
                   

    elif opcao == "2":
        valor = float(input("Quanto Gostaria de Sacar? \n"))
        
        excedeu_saldo = valor>saldo
        
        excedeu_limite = valor>limite
        
        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES
         
        if excedeu_saldo:
           print (" Você não tem saldo o suficiente! Vá Para o Depósito.")
           continue
        elif excedeu_limite:
            print (" Você não tem limite para fazer esse saque!")
        elif excedeu_limite_saques:
            print ("Você já usou todos os seus saques!")
        

        elif valor > 0:
         saldo -= valor
         extrato += f"Saque R$ {valor: .2f} \n"
         numero_saques +=1
         
         
        
        else:
            print ("Erro")

    elif opcao == "3":
         saques_restantes = LIMITE_SAQUES - numero_saques
         
         print(" ======== Opção Extrato ======== ")
         print (" Não foram realizadas movimentações." if not extrato else extrato)
         print (f"\nSaldo: R$ {saldo:.2f}")
         print (f"\nSaques Restantes : {saques_restantes} ")

         saldo = saldo
         saques= LIMITE_SAQUES

         

         
    
    elif opcao == "4":
        print("Saindo...")

        break