import textwrap

def recomendar_plano(consumo):
    
    #verifica se consumo eh menor ou igual a 10GB
    if consumo <= 10:
        print(f"Plano Essencial Fibra - 50Mbps")
    
    #verifica se consumo eh maior que 10GB e menor ou igual a 20GB
    elif consumo > 10 and consumo <= 20:
        print(f"Plano Prata Fibra - 100Mbps")
    
    #verifica se consumo eh maior que 20GB
    elif consumo > 20:
        print(f"Plano Premium Fibra - 300Mbps")
    
    return

#consumo = float(input())
consumo = float(input(">> Por favor, informe a estimativa de seu consumos mensal, em GB: "))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
recomendar_plano(consumo)