from rep.banco import Banco
from rep.reservas import Reservas
from controller import base

class Relatorios:
    def rel_status_r():
        registros = Banco().recuperar_por_status('R')
        listaReservas = Reservas.retorna_lista_reservas(registros)
        for reserva in listaReservas:
            print(reserva.mensagem_format())

    
    def rel_status_a():
        registros = Banco().recuperar_por_status('A')
        listaReservas = Reservas.retorna_lista_reservas(registros)
        for reserva in listaReservas:
            print(reserva.mensagem_format())

    
    def rel_status_c():
        registros = Banco().recuperar_por_status('C')
        listaReservas = Reservas.retorna_lista_reservas(registros)
        for reserva in listaReservas:
            print(reserva.mensagem_format())

    
    def rel_status_f():
        registros = Banco().recuperar_por_status('F')
        listaReservas = Reservas.retorna_lista_reservas(registros)
        for reserva in listaReservas:
            print(reserva.mensagem_format())


    def rel_caixa():
        Banco().rel_caixa()

    def rel_reservas_cpf():
        cpf = input('Digite seu cpf: ')
        registros = Banco().recuperar_por_cpf(cpf)
        reservas = Reservas.retorna_lista_reservas(registros)

        for res in reservas:
            print(res.mensagem_format())    