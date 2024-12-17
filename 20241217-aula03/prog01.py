"""
Programação Orientada a Objetos

Classes, objetos, atributos e métodos
"""

"""
Convenções de código no Python
PascalCase  -> Nomes de classes (ex. Pokemon, FolhaDePagamento)
snake_case  -> Nomes de funções ou métodos (ex. imprimir(), gerar_recibo())
UPPER_CASE  -> Utilizado para constantes (ex. PINOUT, MAX_NUMBER)
"""

class Pokemon:
    
    # O método __init__ é o método inicializados da classe, ou seja, nesse método criamos os atributos da classe e também podemos chamar os métodos. No caso abaixo, criamos 3 atributos: _name, _type e _health. Quando criamos um método, obrigatoriamente o primeiro parâmetro deve ser o self, que é uma referência ao objeto atual.
    def __init__(self, name: str, type: str, health: int) -> None:

        # Abaixo estamos criando os atributos da classe Pokemon. O Python, diferentemente de linguagens como Java ou C#, não possui palavras reservadas que definem o escopo de acesso de um objeto (no Java por exemplo, temos private, protected e public), portanto tudo é considerado público.
        self._name: str = name
        self._type: str = type
        self._health: int = health

    def attack(self) -> None:
        print(f"{self._name} attacks!")

    def dodge(self) -> None:
        print(f"{self._name} dodges!")

    def evolve(self) -> None:
        print(f"{self._name} evolves!")

if __name__ == "__main__":
    # Na linha abaixo instanciamos a classe Pokemon, salvando esse objeto instanciado na variável pikachu. Passamos valores para o método inicializador da classe, que serão atribuídos as propriedades.
    pikachu = Pokemon(name="Pikachu", type="Electric", health=70)
    pikachu._name = "Raichu"
    pikachu.attack()

    bulbasauro = Pokemon(name="bulbasauro", type="Planta", health=100)


