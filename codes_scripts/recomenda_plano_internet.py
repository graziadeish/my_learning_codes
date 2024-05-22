import textwrap

def recomendar_plano(consumo):
    print(f"Consumo mensal de {consumo:.2f} GB")
    
    #verifica se consumo eh menor ou igual a 10GB
    if consumo <= 10:
        print(f"# - Plano Essencial Fibra - 50 Mbps:\n\t >> Recomendado para um consumo médio de até 10 GB.")
    
    #verifica se consumo eh maior que 10GB e menor ou igual a 20GB
    elif consumo > 10 and consumo <= 20:
        print(f"# - Plano Prata Fibra - 100 Mbps:\n\t >> Recomendado para um consumo médio acima de 10 GB até 20 GB.")
    
    #verifica se consumo eh maior que 20GB
    elif consumo > 20:
        print(f"# - Plano Premium Fibra - 300Mbps:\n\t >> Recomendado para um consumo médio acima de 20 GB.")
    

def main():
    # pergunta o consumo
    consumo = float(input(">> Por favor, informe a estimativa de seu consumos mensal, em GB: "))
    
    # Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
    print(recomendar_plano(consumo))

main()