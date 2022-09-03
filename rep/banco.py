from os import stat
import sqlite3
from controller import base

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
                    valor real not null,
                    status text default 'R')""")
        self.conexao.commit()

    def deleta_todos_registros(self):
        if(input("Digite 'S' para confirmar: ").upper() != 'S'): return
        self.cursor.execute("DELETE FROM RESERVAS WHERE 1 = 1")
        self.conexao.commit()


    def drop_reservas(self):
        if(input("Digite 'S' para confirmar: ").upper() != 'S'): return
        self.cursor.execute("DROP TABLE RESERVAS")
        self.conexao.commit()


    def seleciona_todos_registros(self):
        self.cursor.execute("SELECT * FROM RESERVAS")
        registros = self.cursor.fetchall()
        for registro in registros:
            print(registro)


    def insere_registro(self, reserva):
        insert = "INSERT INTO reservas values(null, {0}, '{1}', {2}, '{3}', {4}, '{5}', '{6}')"
        self.cursor.execute(insert.format(reserva.cpf, reserva.nome, reserva.qtd_pessoas, reserva.tipo_quarto, reserva.qtd_dias, reserva.valor, reserva.status))
        self.conexao.commit()


    def altera_registro(self, reserva):
        update = "UPDATE reservas set numeropessoas = {0}, tipoquarto = '{1}', numerodias = {2}, status = '{3}', valor = {4} where idreserva = {5}"
        self.cursor.execute(update.format(reserva.qtd_pessoas, reserva.tipo_quarto, reserva.qtd_dias, reserva.status, reserva.valor, reserva.idreserva))
        self.conexao.commit()


    def recuperar_por_cpf(self, cpf):
        self.cursor.execute(f"SELECT * FROM RESERVAS WHERE cpf = {cpf}")
        return self.cursor.fetchall()


    def recuperar_por_cpf_status(self, cpf, status):
        self.cursor.execute(f"SELECT * FROM RESERVAS WHERE cpf = {cpf} and status = '{status}'")
        return self.cursor.fetchall()


    def checkin(self, id):
        self.cursor.execute(f"UPDATE RESERVAS SET STATUS = 'A' WHERE idreserva = {id}")
        self.conexao.commit()


    def checkout(self, id):
        self.cursor.execute(f"UPDATE RESERVAS SET STATUS = 'F' WHERE idreserva = {id}")
        self.conexao.commit()


    def recuperar_por_status(self, status):
        self.cursor.execute(f"SELECT * FROM RESERVAS WHERE STATUS = '{status}'")
        return self.cursor.fetchall()


    def rel_caixa(self):
        self.cursor.execute("SELECT SUM(VALOR) FROM RESERVAS")
        print(f"O saldo em caixa é de {self.cursor.fetchone()[0]}")
