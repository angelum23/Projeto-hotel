from rep.reservas import Reservas
from rep.banco import Banco

class entradaCliente:
    def checkin():
        cpf = input('Digite seu cpf: ')
        registros = Banco().recuperar_por_cpf(cpf)
        reservas = Reservas.retorna_lista_reservas(registros)
        print(reservas)
        print('kk')