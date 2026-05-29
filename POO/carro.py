# A palavra "class" é usada para criar uma classe.
# Uma classe funciona como um molde para criar objetos
class Carro:

<<<<<<< HEAD
=======
    # "def" definir uma função ou método.
    # "__init__" é o método construtor da classe.
    # Ele é executado automaticamente quando um objeto é criado

    # "self" representa o próprio objeto.
    # É através do self que acessamos atributos e métodos do objeto

    # "marca", "modelo", "ano" e "velocidade"
    # São Parâmetros recebidos pela classe.

>>>>>>> 694b47a3b8d54a85b557848c4e1e6370061b1493
    # Método Construtor
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    # Métodos
    # Método acelerar
    def acelerar(self, aumento):
<<<<<<< HEAD
        # self.velocidade = self.velocidade + aumento 
        self.velocidade += aumento

        print(f"O carro acelerou para{self.velocidade} km/h")

=======
        # self.velocidade = self.velocidade + aumento:
        self.velocidade += aumento

        print(f" O carro acelerou para{self.velocidade}km/h")
>>>>>>> 694b47a3b8d54a85b557848c4e1e6370061b1493

# Criando um objeto da Classe Carro

# "carro1" é uma variável que recebe um objeto
carro1 = Carro("Chevrolet", "S10", 2013)

<<<<<<< HEAD
# Exibir informações do carro 1
print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Ano: {carro1.ano}")

carro1.acelerar(50)

# # "carro2" é uma variável que recebe um objeto
carro2 = Carro("BYD", "Dolphin Mini", 2025)

# # Exibir informações do carro 2
print(f"Marca: {carro2.marca}")
print(f"Modelo: {carro2.modelo}")
print(f"Ano: {carro2.ano}")

=======
# Exibir informações do carro
print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"ano: {carro1.ano}") 

carro1.acelerar(180)

# "carro2" é uma variável que recebe um objeto
carro2 = Carro( "BYD", "eletrico", "2027")

# Exibir informações do carro
print(f"Marca: {carro2.marca}")
print(f"Modelo: {carro2.modelo}")
print(f"ano: {carro2.ano}")
>>>>>>> 694b47a3b8d54a85b557848c4e1e6370061b1493
