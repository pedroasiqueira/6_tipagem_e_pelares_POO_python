class TV:
    def __init__(self, tamanho) -> None:
        self.volume = 50
        self.canal = 1
        self.tamanho = tamanho
        self.ligada = False

    def aumentar_volume(self):
        if self.volume == 99:
            return 'Volume já está no máximo'

        self.volume += 1

    def diminuir_volume(self):
        if self.volume == 0:
            return 'Volume já está no mínimo'

        self.volume -= 1

    def modificar_canal(self, num):
        if 1 < num < 99:
            self.canal = num
        else:
            raise ValueError('Valor está fora do limite')

    def ligar_desligar(self):
        if self.ligada is False:
            self.ligada = True
        else:
            self.ligada = False


# lg = TV(50)

# print(lg.volume)
# print(lg.canal)
# print(lg.ligada)
# print(lg.tamanho)

# lg.aumentar_volume()
# lg.aumentar_volume()
# lg.aumentar_volume()
# lg.diminuir_volume()
# lg.modificar_canal(23)
# lg.ligar_desligar()

# print(lg.volume)
# print(lg.canal)
# print(lg.ligada)
# print(lg.tamanho)
