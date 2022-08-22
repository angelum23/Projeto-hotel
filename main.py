from view.menus import Menus


class Main:
    def __init__(self):
        self.__executando = True

    @property
    def executando(self):
        return self.__executando

    def fim_execucao(self):
        self.__executando = False


    def main(self):
        while self.executando:
            Menus.menu_inicial(self)



if __name__ == "__main__":
    Main().main()