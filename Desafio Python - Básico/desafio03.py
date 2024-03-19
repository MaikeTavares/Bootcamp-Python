# Descrição
# Com as máquinas pesadas agrupadas estrategicamente, 
# graças ao seu algoritmo de cálculo energético,
# agora a mineração está muito mais eficiente! Com isso, 
# os CodeMiners logo terão que aumentar a capacidade de armazenamento de dados em seus discos de Mithril. 
# Atualmente, cada máquina tem uma capacidade em teraflops e todas terão um upgrade! Escreva um programa que calcule a nova capacidade total de todas as máquinas após um aumento percentual específico.

# Entrada
# Dois valores inteiros positivos, representando a capacidade atual total em teraflops e o aumento percentual, separados por espaço.

# Saída
# A nova capacidade total em teraflops.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada:
# 100 20
# 50 10
# 200 50

# Saida:
# 120
# 55
# 300

capacidade_atual, aumento_percentual = map(int, input().split())

# Calcula a nova capacidade total
nova_capacidade = capacidade_atual * (1 + aumento_percentual / 100)

# Imprime a nova capacidade
print(int(nova_capacidade))