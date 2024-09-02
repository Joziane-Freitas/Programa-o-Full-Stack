class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def sacar(self, valor):
        if valor > 0:
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")
    
    def exibir_saldo(self):
        print(f"Saldo atual: R${self._saldo:.2f}")
    
    def get_titular(self):
        return self._titular

# Exemplo de uso da classe
conta = ContaBancaria(titular="João da Silva", saldo_inicial=1000)

conta.exibir_saldo()  # Deve mostrar o saldo inicial
conta.depositar(500)  # Deve realizar o depósito e atualizar o saldo
conta.exibir_saldo()  # Deve mostrar o saldo atualizado
conta.sacar(200)      # Deve realizar o saque e atualizar o saldo
conta.exibir_saldo()  # Deve mostrar o saldo atualizado
conta.sacar(1500)    # Deve mostrar saldo insuficiente
