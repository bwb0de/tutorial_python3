#
# Crie um tipo/classe para trabalhar com datas no formato brasileiro DD/MM/AAAA
#
# Esta classe deve permitir a compração entre diferentes instancias da classe
# de forma a possibilitar ordenamento de registros conforme a data.
#
# Deve também implementar um método de visualização para que possa ser vista 
# mediante print
#


class DataBR:
    def __init__(self, data_br: str):
        dia, mes, ano = data_br.strip().split('/')
        dia, mes, ano = int(dia), int(mes), int(ano)

        ano_bisexto = False #self.ano_bisexto(ano)

        if any([dia < 0, mes < 0, ano < 0, mes > 12]):
            raise ValueError("Data fornecida parece inadequada...")

        elif mes in {1, 3, 5, 7, 8, 10, 12} and dia > 31:
            raise ValueError("Data fornecida parece inadequada...")

        elif mes in {4, 6, 9, 11} and dia > 30:
            raise ValueError("Data fornecida parece inadequada...")

        elif mes == 2 and ano_bisexto and dia > 29:
            raise ValueError("Data fornecida parece inadequada...")

        elif mes == 2 and not ano_bisexto and dia > 28:
            raise ValueError("Data fornecida parece inadequada...")

        self.__ano = ano
        self.__mes = mes
        self.__dia = dia

    def __eq__(self, other):
        return all([
            self.dia == other.dia,
            self.mes == other.mes,
            self.ano == other.ano
        ])

    def __lt__(self, other):
        return any([
            self.ano < other.ano,
            self.ano == other.ano and self.mes < other.mes,
            self.ano == other.ano and self.mes == other.mes and self.dia < other.dia
        ])

    def __gt__(self, other):
        return any([
            self.ano > other.ano,
            self.ano == other.ano and self.mes > other.mes,
            self.ano == other.ano and self.mes == other.mes and self.dia > other.dia
        ])

    def __str__(self):
        return f'br[{str(self.dia).zfill(2)}/{str(self.mes).zfill(2)}/{str(self.ano).zfill(4)}]'

    @property
    def dia(self):
        return self.__dia

    @property
    def mes(self):
        return self.__mes
   
    @property
    def ano(self):
        return self.__ano



# Testando
if __name__ == '__main__':
    d1 = DataBR('12/01/1982')
    d2 = DataBR('14/02/1984')
    d3 = DataBR('25/11/1989')
    lista = [d2, d3, d1]
    print(*lista)
    lista.sort()
    print(*lista)

