from controller import base
from rep.reservas import Reservas
from rep.banco import Banco

class SaidaCliente:
    def escolhe_registro(registros):
        for item in registros:
            print(f'{item.idreserva} - cpf: {item.cpf} / nome: {item.nome} / valor: {item.valor}\n')
        
        codigo = input('Digite o código da reserva escolhida: ')
        return Reservas.retorna_item_por_id(registros, codigo)


    def checkout():
        cpf = input('Digite seu cpf: ')
        registros = Banco().recuperar_por_cpf_status(cpf, 'A')
        reservas = Reservas.retorna_lista_reservas(registros)

        if len(reservas) < 1: return print('Nenhum registro encontrado')

        if len(reservas)  > 1:
            reserva = Reservas.escolhe_registro(reservas)
            Banco().checkin(reserva.idreserva)

        if len(reservas) == 1:
            Banco().checkout(reservas[0].idreserva)
        
        print('\n Checkout realizado com sucesso! \n')
        
        base.pause_enter()