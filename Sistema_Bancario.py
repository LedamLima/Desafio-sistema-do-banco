from random import randint
from math import radians
from math import remainder
print('####'*10)
print('==='*10)
print('{:^30}'.format('Banco Inovação'))
print('==='*10)

class ContaBancaria:
    def __init__(self, saldo_inicial, limite_saque_diario):
        self.saldo = saldo_inicial
        self.limite_saque_diario = limite_saque_diario
        self.saldo_total = saldo_inicial
        self.transacoes = []

    def saque(self, valor):
        if valor > self.limite_saque_diario:
            print(f"Valor máximo de saque diário atingido: R$ {self.limite_saque_diario}")
        elif self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            self.saldo_total -= valor
            self.transacoes.append(-valor)
            print(f"Saque de R$ {valor} realizado com sucesso")

    def deposito(self, valor):
        self.saldo += valor
        self.saldo_total += valor
        self.transacoes.append(valor)
        print(f"Depósito de R$ {valor} realizado com sucesso")

    def extrato(self):
        print("Extrato:")
        for t in self.transacoes:
            if t < 0:
                print(f"Saque de R$ {-t}")
            else:
                print(f"Depósito de R$ {t}")
        print(f"Saldo atual: R$ {self.saldo_total}")

conta = ContaBancaria(1000, 300)

conta.saque(200)
conta.saque(400)
conta.deposito(500)
conta.saque(100)

conta.extrato()















valor = int(input('Que valor vc quer sacar? R$  '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        print(f'Total de {totcéd} células de R$ {céd} ')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        if total == 0:
            break
         
print ('####'*10)
