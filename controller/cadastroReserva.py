from rep.reservas import Reservas
from rep.banco import Banco
from controller import base

class CadastroReserva:
    def retorna_erros(nome,cpf,qtd_pessoas,tipo_quarto,qtd_dias):
        erros = list()

        if(nome == ''): erros.append('Nome em branco')
        if(len(cpf) != 11): erros.append('Cpf invalido')
        if(qtd_pessoas < 1): erros.append('Quantidade de pessoas inválida')
        if(tipo_quarto not in ['S','D','P']): erros.append('Tipo do quarto inválido')
        if(qtd_dias < 1): erros.append('Quantidade de dias inválida')
        return erros


    def cadastro_reserva():
        try:
            nome = input('Digite seu nome: ')
            cpf = input('Digite seu cpf: ').replace('.','').replace('-','').strip()
            qtd_pessoas = int(input('Quantas pessoas irão: '))
            tipo_quarto = input('S - Standard\nD - Deluxe\nP - Premium\nQual quarto você deseja?').upper()
            qtd_dias = int(input('Quantos dias vocë vai ficar? '))

            erros = CadastroReserva.retorna_erros(nome,cpf,qtd_pessoas,tipo_quarto,qtd_dias)
            if len(erros) > 1:
                print('\n')
                print(erros)
                print('\n')

                base.pause_enter()
                return

            reserva = Reservas(None, nome, cpf, qtd_pessoas, tipo_quarto, qtd_dias)

            Banco().insere_registro(reserva)
            print('Cadastro realizado com sucesso!')
            base.pause_enter()

        except:
            print('Houve um erro ao realizar o cadastro, tente novamente!')
            base.pause_enter()