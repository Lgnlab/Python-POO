class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} \033[32mautorizado\033[m na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"\033[31mSaque NEGADO\033[m de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} \033[32mautorizado\033[m na conta {self.id}")



c1 = ContaBancaria(112, "Gustavo", 3_000)
c1.depositar(500)
c1.sacar(200)
print(c1)