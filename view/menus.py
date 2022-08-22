from controller.cadastroReserva import CadastroReserva

class Menus:
    def menu_inicial(main):
        print("""
            1 - Cadastrar uma reserva. 
            2 - Entrada do cliente (Check in).
            3 - Saída do cliente (Check out).
            4 - Alterar reserva.
            5 - Relatórios. 
            6 - Sair 
            """)
        opc = input('Qual opção você deseja selecionar? \n')

        if opc == '1': CadastroReserva.cadastro_reserva()
        elif opc == '2': pass
        elif opc == '3': pass
        elif opc == '4': pass
        elif opc == '5': pass
        elif opc == '6': main.fim_execucao()