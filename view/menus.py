from controller.cadastroReserva import CadastroReserva
from controller.entradaCliente import EntradaCliente
from controller.saidaCliente import SaidaCliente
from rep.banco import Banco
from controller import base
class Menus:
    def menu_inicial(main):
        base.cls()
        print("""
===================
    Hotel plus
===================

1 - Cadastrar uma reserva. 
2 - Entrada do cliente (Check in).
3 - Saída do cliente (Check out).
4 - Alterar reserva.
5 - Relatórios.
6 - Menu banco. 
7 - Sair.
            """)
        opc = input('Qual opção você deseja selecionar? \n')
        if opc == '1': CadastroReserva.cadastro_reserva()
        elif opc == '2': EntradaCliente.checkin()
        elif opc == '3': SaidaCliente.checkout()
        elif opc == '4': pass
        elif opc == '5': pass
        elif opc == '6': Menus.menu_banco()
        elif opc == '7': main.fim_execucao()

    def menu_banco():
        base.cls()
        print(""" 
1 - Criar tabela reservas
2 - Selecionar todos os registros
3 - Limpar tabela reservas
4 - Dropar tabela reservas
         """)
        opc = input('Qual opção você deseja selecionar? \n')

        if opc == '1': Banco().cria_tabela_reservas()
        elif opc == '2': Banco().seleciona_todos_registros()
        elif opc == '3': pass
        elif opc == '4': pass
        base.pause_enter()
        
