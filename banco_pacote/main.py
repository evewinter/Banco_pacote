from banco_pacote.banco_lista import BancoLista
from banco_pacote.conta import Conta
from banco_pacote.contapoupanca import ContaPoupanca

def main():
    banco1 = BancoLista("Banco 1", taxa_juros=0.05) 
    banco2 = BancoLista("Banco 2", taxa_juros=0.03)
    banco3 = BancoLista("Bnaco 3", taxa_juros=0.02) 

    conta_alice = ContaPoupanca("Alice") 
    conta_joão = Conta("João") 
    conta_carlos = ContaPoupanca("Carlos")  
    conta_diana = Conta("Diana") 
    conta_ana = ContaPoupanca("Ana")
    conta_julia = Conta("Julia")

    banco1.cadastrar_conta(conta_alice)
    banco1.cadastrar_conta(conta_joão)
    banco2.cadastrar_conta(conta_carlos)
    banco2.cadastrar_conta(conta_diana)
    banco3.cadastrar_conta(conta_ana)
    banco3.cadastrar_conta(conta_julia)

    banco3.remover_conta("Ana")

    print("\n--- Operações no Banco 1 ---")
    banco1.creditar("Alice", 700)
    banco1.debitar("Alice", 500)
    banco1.transferir("Alice", "João", 40) 

    banco1.render_juros("Alice")

    print("\n--- Operações no Banco 2 ---")
    banco2.creditar("Carlos", 500) 
    banco2.debitar("Carlos", 150) 
    banco2.transferir("Carlos", "Diana", 100) 

    banco2.render_juros("Carlos")

    print("\n--- Operações no Banco 3 ---")
    banco3.creditar("Ana", 1000)
    banco3.debitar("Ana", 147.3)
    banco3.transferir("Ana", "Julia", 458)

    banco3.render_juros("Ana")

    print("\n--- Saldos no Banco 1 ---")
    print(f"Saldo de Alice: {banco1.saldo('Alice')}")
    print(f"Saldo de João: {banco1.saldo('João')}")

    print("\n--- Saldos no Banco 2 ---")
    print(f"Saldo de Carlos: {banco2.saldo('Carlos')}")
    print(f"Saldo de Diana: {banco2.saldo('Diana')}")

    print("\n--- Saldos no Banco  ---")
    print(f"Saldo de Ana: {banco3.saldo('Ana')}")
    print(f"Saldo de Julia: {banco3.saldo('Julia')}")

    print("\n--- Contas removidas ---")
    print(f"Conta: {banco3.remover_conta('Ana')}")


if __name__ == "__main__":
    main()

