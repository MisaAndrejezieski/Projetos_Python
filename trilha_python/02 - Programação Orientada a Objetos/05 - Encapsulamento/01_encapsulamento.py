class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ... saldo público
        self._saldo += valor

    def sacar(self, valor):
        # ... saque público
        self._saldo -= valor

    def mostrar_saldo(self):
        # ... saldo privado
        print("Seu saldo é: R$ ",self._saldo)
        return self.mostrar_saldo
        


conta = Conta("Agencia = 0001", 000)
conta.depositar(100)
conta.sacar(50)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
