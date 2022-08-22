from rep.reservas import Reservas
from rep.banco import Banco

class CadastroReserva:
    def cadastro_reserva():
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu cpf: ')
        qtd_pessoas = int(input('Quantas pessoas irão: '))
        tipo_quarto = input('S - Standard\nD - Deluxe\nP - Premium\nQual quarto você deseja? ')
        qtd_dias = int(input('Quantos dias vocë vai ficar? '))

        reserva = Reservas(None, nome, cpf, qtd_pessoas, tipo_quarto, qtd_dias)

        Banco.insere_registro(reserva)