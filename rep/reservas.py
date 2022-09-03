from enum import Enum

class Reservas:
    def __init__(self, idreserva, nome, cpf, qtd_pessoas, tipo_quarto, qtd_dias):
        self.__idreserva = idreserva
        self.__nome = nome
        self.__cpf = cpf
        self.__qtd_pessoas = qtd_pessoas
        self.__tipo_quarto = tipo_quarto
        self.__qtd_dias = qtd_dias
        self.__valor = self.valor_tipo_quarto() * qtd_dias * qtd_pessoas
        self.__status = 'R'


    def calcula_valor(self):
        self.__valor = self.valor_tipo_quarto() * self.qtd_dias * self.qtd_pessoas


    def retorna_lista_reservas(lista):
        listaReservas = list()
        for item in lista:
            reserva = Reservas(item[0], item[2], item[1], item[3], item[4], item[5])
            listaReservas.append(reserva)
        return listaReservas

    def retorna_reserva(item):
        return Reservas(item[0], item[2], item[1], item[3], item[4], item[5])


    def retorna_item_por_id(lista, codigo):
        for item in lista:
            if item.id == codigo:
                return item
        
        print('Registro não encontrado')

        
    def escolhe_registro(registros):
        for item in registros:
            print(f'{item.idreserva} - cpf: {item.cpf} / nome: {item.nome} / valor: {item.valor}\n')
        
        codigo = input('Digite o código da reserva escolhida: ')
        return Reservas.retorna_item_por_id(registros, codigo)

    
    def mensagem_format(self):
        return """ 
► Reserva {0} ◄
Nome: {1}
Cpf: {2}
Numero de pessoas: {3}
Tipo do quarto: {4}
Dias reservados: {5}
Valor: {6}
Status: {7}
        """.format(self.idreserva, self.nome, self.cpf, self.qtd_pessoas, self.tipo_quarto_ext, self.qtd_dias, self.valor, self.status_ext)


    @property
    def idreserva(self):
        return self.__idreserva


    @property
    def nome(self):
        return self.__nome


    @property
    def cpf(self):
        return self.__cpf


    @property
    def qtd_pessoas(self):
        return self.__qtd_pessoas

    def set_qtd_pessoas(self, qtd_pessoas):
        self.__qtd_pessoas = qtd_pessoas
        
    def set_tipo_quarto(self, tipo_quarto):
        self.__tipo_quarto = tipo_quarto
        
    def set_qtd_dias(self, qtd_dias):
        self.__qtd_dias = qtd_dias
        
    def set_status(self, status):
        self.__status = status
        

    @property
    def tipo_quarto(self):
        return self.__tipo_quarto


    @property
    def qtd_dias(self):
        return self.__qtd_dias


    @property
    def valor(self):
        return self.__valor


    @property
    def status(self):
        return self.__status


    def valor_tipo_quarto(self):
        if self.__tipo_quarto.upper() == 'S': return 100
        elif self.__tipo_quarto.upper() == 'D': return 200
        elif self.__tipo_quarto.upper() == 'P': return 300

    @property        
    def tipo_quarto_ext(self):
        if self.__tipo_quarto.upper() == 'S': return 'Standard'
        elif self.__tipo_quarto.upper() == 'D': return 'Deluxe'
        elif self.__tipo_quarto.upper() == 'P': return 'Premium'

    @property
    def status_ext(self):
        if self.__status.upper() == 'R': return 'Reservado'
        elif self.__status.upper() == 'C': return 'Cancelado'
        elif self.__status.upper() == 'A': return 'Ativo'
        elif self.__status.upper() == 'F': return 'Finalizado'


    def set_reservado(self):
        self.__status = 'R'


    def set_cancelado(self):
        self.__status = 'C'


    def set_ativo(self):
        self.__status = 'A'


    def set_finalizado(self):
        self.__status = 'F'