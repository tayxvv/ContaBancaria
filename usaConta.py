from Conta import Conta

conta = Conta.criaConta(123, "João", 100, 1000, "corrente")
Conta.deposita(100, conta)
Conta.saca("corrente", 50, conta)
Conta.extrato(conta)