from rep.banco import Banco
from rep.reservas import Reservas
from controller import base

class AlteraReserva:
    def alterar(registro):
        registro.set_qtd_pessoas(int(input('Quantas pessoas vão: ')))
        registro.set_tipo_quarto(input('\nS – Standard\nD – Deluxe\nP – Premium\Digite o tipo do quarto você deseja: '))
        registro.set_qtd_dias(input('Quantidade de dias: '))
        registro.set_status(input('R - Reservado\nC – Cancelado\nA – Ativo\nF - Finalizado\Digite o novo status: '))
        registro.calcula_valor()

        Banco().altera_registro(registro)


    def escolher_reserva():
        cpf = input('Digite seu cpf: ')
        registros = Banco().recuperar_por_cpf(cpf)
        reservas = Reservas.retorna_lista_reservas(registros)

        if len(reservas) < 1: return print('Nenhum registro encontrado')

        if len(reservas)  > 1:
            reserva = Reservas.escolhe_registro(reservas)
            AlteraReserva.alterar(reserva)

        if len(reservas) == 1:
            AlteraReserva.alterar(reservas[0])

        print('\nRegistro alterado com sucesso!\n')
        base.pause_enter()