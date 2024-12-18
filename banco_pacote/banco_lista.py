from banco_pacote.contapoupanca import ContaPoupanca


class BancoLista:
    def __init__(self, nome, taxa_juros=0.01): 
        self.nome = nome
        self.contas = []
        self.taxa_juros = taxa_juros

    def cadastrar_conta(self, conta):
         if not any(c.get_numero() == conta.get_numero() for c in self.contas):
            self.contas.append(conta)
            print(f"Conta {conta.get_numero()} cadastrada no banco {self.nome}!")
         else:
            print(f"Conta {conta.get_numero()} já cadastrada no banco {self.nome}.")

    def procurar_conta(self, numero):
        for conta in self.contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print(f"Conta {numero} não encontrada no banco {self.nome}.")

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print(f"Conta {numero} não encontrada no banco {self.nome}.")

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print(f"Conta {numero} não encontrada no banco {self.nome}.")
            return None
        
    def listar_contas(self):
         if not self.contas:
            print(f"Nenhuma conta registrada no banco {self.nome}.")
         else:
            print(f"Contas do banco {self.nome}:")
            for conta in self.contas:
                    print(f"Conta {conta.get_numero()} - Saldo: {conta.get_saldo()}")


    def transferir(self, origem, destino, valor):
        conta_origem = self.procurar_conta(origem)
        conta_destino = self.procurar_conta(destino)


        if conta_origem and conta_destino:
            if conta_origem.get_saldo() >= valor:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
                print(f"Transferência de R${valor} realizada de {origem} para {destino}.")
            else:
                print("Saldo insuficiente na conta de origem!")
        else:
            print("Conta de origem ou destino inexistente!")

    def render_juros(self, numero):
        conta = self.procurar_conta(numero)
        if isinstance(conta, ContaPoupanca):  
            conta.render_juros(self.taxa_juros)
        else:
            print(f"Conta {numero} não é uma conta poupança ou não existe no banco {self.nome}.")

    def remover_conta(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            self.contas = [c for c in self.contas if c.get_numero() != numero] 
            print(f"Conta {numero} removida do banco {self.nome}.")
        else:
            print(f"Conta {numero} não encontrada no banco {self.nome}.")
