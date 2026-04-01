produto = float(input('DIgite o valor do produto: '))
desconto = float(input('DIgite o desconto do profuto (ex: 15): '))

desconto = desconto / 100
descontoFinal = produto * desconto

valorComDesconto = produto - descontoFinal

print(f'Valor do desconto:{descontoFinal:.2f}')
print(f'valor com desconto: {valorComDesconto:.2f}')