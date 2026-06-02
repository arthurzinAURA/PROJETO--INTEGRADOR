# A palavra "class" é usada para criar uma classe.
# Uma classe funciona como um molde para criar objetos

class Carro:

    # Método Construtor
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    # Método acelerar
    def acelerar(self, aumento):
        self.velocidade += aumento
        print(f"O carro acelerou para {self.velocidade} km/h")

    # Método frear
    def frear(self, reducao):
        self.velocidade -= reducao
        print(f"O carro freou para {self.velocidade} km/h")

    # Método para exibir informações
    def exibir_info(self):
        print("=== INFORMAÇÕES DO CARRO ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade Atual: {self.velocidade} km/h")


# Criando um objeto da Classe Carro
carro1 = Carro("Chevrolet", "S10", 2013)

# Chamando os métodos
carro1.acelerar(50)
carro1.frear(20)

# Exibindo as informações do carro
carro1.exibir_info()