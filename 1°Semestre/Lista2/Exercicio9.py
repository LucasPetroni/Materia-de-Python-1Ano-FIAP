preco = int(input("Digite o preco do preco do produto: "))
porcentagem = int(input("Digite a porcetagem que vai ser descontado ou acrescentado ao produto: "))

valorD = preco * (porcentagem/100)
desconto = preco - valorD
aumento = preco + valorD

print()