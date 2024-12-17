# Módulo de contas financeiras

class ContaFinanceira:

    def __init__(self, nome: str, saldo: float = 0) -> None:
        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        self._nome = novo_nome
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    def sacar(self, valor: float) -> float:
        if valor > self._saldo:
            raise Exception(f"O valor R$ {valor} é maior que o saldo na conta (R$ {self._saldo}).")
        else:
            # self._saldo = self._saldo - valor
            self._saldo -= valor
            return valor
        
    def depositar(self, valor: float) -> float:
        if valor <= 0:
            raise Exception("O valor a ser depositado deve ser igual ou maior que 0")
        
        else:
            self._saldo += valor
