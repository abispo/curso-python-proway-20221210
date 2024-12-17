"""
Programação Orientada a Objetos

Composição

Composição ocorre quando um objeto compõe ou é composto por outro(s) objetos
"""

class Carta:
    def __init__(self, valor: str, naipe: str) -> None:
        self._valor = valor
        self._naipe = naipe

    def __str__(self):
        return f"{self._valor}{self._naipe}"

class Baralho:
    def __init__(self):
        self._cartas = []           # Lista que armazena as cartas do baralho
        self._naipes = [
            "\u2660", "\u2665", "\u2663", "\u2666"
        ]
        self._valores = [
            'A', '2', '3', '4', '5',
            '6', '7', '8', '9', '10',
            'J', 'Q', 'K'
        ]

        for naipe in self._naipes:
            for valor in self._valores:
                self._cartas.append(Carta(valor, naipe))

    def __str__(self):
        return ", ".join(str(carta) for carta in self._cartas)

if __name__ == "__main__":
    baralho = Baralho()
    print(baralho)
    # print(baralho._cartas)