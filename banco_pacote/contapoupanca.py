from banco_pacote.conta import Conta 

class ContaPoupanca(Conta):

    def __init__(self, numero):
        super().__init__(numero)
    def render_juros(self, taxa):
        if taxa > 0: 
            juros = self.get_saldo() * taxa
            self.creditar(juros)
            print(f"Juros de R${juros:.2f} aplicados à conta {self.get_numero()}.")
        else:
            print("A taxa de juros deve ser positiva!")