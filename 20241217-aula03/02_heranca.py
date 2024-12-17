"""
Programação Orientada a Objetos

Herança

Herança acontece quando uma classe (classe filha ou subclasse) herda atributos e métodos de uma outra classe (classe mãe ou superclasse)
"""

from contas import ContaCorrente, ContaInvestimento

if __name__ == "__main__":

    conta_viacredi = ContaCorrente(nome="Conta Corrente Viacredi")
    print(f"Saldo da '{conta_viacredi.nome}': R$ {conta_viacredi.saldo}")

    valor_deposito = conta_viacredi.depositar(100)
    print(f"Você depositou R$ {valor_deposito} com sucesso!")
    print(f"Saldo da '{conta_viacredi.nome}': R${conta_viacredi.saldo}")

    conta_poupanca_caixa = ContaInvestimento(
        nome="Conta Poupança Caixa",
        taxa=1,
        saldo=1000
    )

    print(f"Saldo da '{conta_poupanca_caixa.nome}': R$ {conta_poupanca_caixa.saldo}")
    conta_poupanca_caixa.render()
    print(f"Saldo da '{conta_poupanca_caixa.nome}': R$ {conta_poupanca_caixa.saldo}")
