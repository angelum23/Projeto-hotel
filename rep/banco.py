import sqlite3

class Banco:
    def __init__(self):
        self.__conexao = sqlite3.connect('projeto_hotel.db')
        self.__cursor = self.__conexao.cursor()


    @property
    def conexao(self):
        return self.__conexao

    @property
    def cursor(self):
        return self.__cursor

    
    def cria_tabela_reservas(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS
                    reservas(
                    idreserva integer primary key autoincrement,
                    cpf text not null,
                    nome text not null,
                    numeropessoas integer not null,
                    tipoquarto text not null,
                    numerodias integer not null,
                    valor numeric not null,
                    status text default 'R')""")

    def insere_registro(self, reserva):
        insert = "INSERT INTO reservas values(null, {0}, '{1}', {2}, '{3}', {4}, '{5}', '{6}')"
        self.cursor.execute(insert.format(reserva.cpf, reserva.nome, reserva.qtd_pessoas, reserva.tipo_quarto, reserva.qtd_dias, reserva.valor, reserva.status))

    def altera_registro(self, reserva):
        update = "UPDATE reservas set numeropessoas = {0}, tipoquarto = '{1}', numerodias = {2}, status = '{3}', valor = {4} where idreserva = {5}"
        self.cursor.execute(update.format(reserva.qtd_pessoas, reserva.tipo_quarto, reserva.qtd_dias, reserva.status, reserva.valor, reserva.idreserva))