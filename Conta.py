class Conta:

    def criaConta(numero, titular, saldo, limite, tipo_conta):
        conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite, "tipo_conta": tipo_conta}
        return conta
    
    def deposita(valor, conta):
        conta["saldo"] += valor

    def saca(tipo_conta, valor, conta):
        if tipo_conta == "corrente" and valor <= conta["saldo"]:
            conta["saldo"] -= valor
        elif tipo_conta == "poupanca" and valor <= conta["saldo"] + conta["limite"]:
            conta["saldo"] -= valor
        else:
            print("Saldo insuficiente")

    def extrato(conta):
        print(f"Número: {conta['numero']}, saldo: {conta['saldo']}")