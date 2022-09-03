from controller.alteraReserva import AlteraReserva
from controller.cadastroReserva import CadastroReserva
from controller.entradaCliente import EntradaCliente
from controller.saidaCliente import SaidaCliente
from controller.relatorios import Relatorios
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
        elif opc == '4': AlteraReserva.escolher_reserva()
        elif opc == '5': Menus.menu_relatorios()
        elif opc == '6': Menus.menu_banco()
        elif opc == '7': main.fim_execucao()



    def menu_banco():
        base.cls()
        print(""" 
1 - Criar tabela reservas
2 - Selecionar todos os registros
3 - Limpar tabela reservas
4 - Dropar tabela reservas
5 - Retornar
         """)
        opc = input('Qual opção você deseja selecionar? \n')

        if opc == '1': Banco().cria_tabela_reservas()
        elif opc == '2': Banco().seleciona_todos_registros()
        elif opc == '3': Banco().deleta_todos_registros()
        elif opc == '4': Banco().drop_reservas()
        base.pause_enter()



    def menu_relatorios():
        base.cls()
        print(""" 
1 - Relatório de todas as reservas com status R. 
2 - Relatório de todas as reservas com status C. 
3 - Relatório de todas as reservas com status A. 
4 - Relatório de todas as reservas com status F. 
5 - Relatório total recebido (somar valor de todas as reservas finalizadas) 
6 – Relatório de Reserva por pessoa (Pesquisa por CPF)
7 - Retornar
        """)
        opc = input('Qual opção você deseja selecionar? \n')
        if opc == '1': Relatorios.rel_status_r()
        elif opc == '2': Relatorios.rel_status_c()
        elif opc == '3': Relatorios.rel_status_a()
        elif opc == '4': Relatorios.rel_status_f()
        elif opc == '5': Relatorios.rel_caixa()
        elif opc == '6': Relatorios.rel_reservas_cpf()

        base.pause_enter()