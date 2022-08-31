from controller import base
from rep.reservas import Reservas
from rep.banco import Banco

class EntradaCliente:
    def escolhe_registro(registros):
        for item in registros:
            print(f'{item.idreserva} - cpf: {item.cpf} / nome: {item.nome} / valor: {item.valor}\n')
        
        codigo = input('Digite o código da reserva escolhida: ')
        return Reservas.retorna_item_por_id(registros, codigo)


    def checkin():
        cpf = input('Digite seu cpf: ')
        registros = Banco().recuperar_por_cpf_status(cpf, 'R')
        reservas = Reservas.retorna_lista_reservas(registros)

        if len(reservas) < 1: return print('Nenhum registro encontrado')

        if len(reservas)  > 1:
            reserva = EntradaCliente.escolhe_registro(reservas)
            Banco().checkin(reserva.idreserva)

        if len(reservas) == 1:
            Banco().checkin(reservas[0].idreserva)
        
        print('\n Checkin realizado com sucesso! \n')

        base.pause_enter()