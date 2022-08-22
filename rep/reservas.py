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

    def set_reservado(self):
        self.__status = 'R'
        
    def set_cancelado(self):
        self.__status = 'C'
        
    def set_ativo(self):
        self.__status = 'A'
        
    def set_finalizado(self):
        self.__status = 'F'

    class Status(Enum):
        Reservado = 'R'
        Cancelado = 'C'
        Ativo = 'A'
        Finalizado = 'F'