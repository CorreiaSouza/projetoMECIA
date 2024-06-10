import os

def processar_resposta(pergunta, nome, sintomas):
    if "dor de cabeça intença" in pergunta:
        sintomas.append("Dor de cabeça intensa")
        print(f'{os.linesep}{nome}, certo, continuaremos os exames. Pode ser que precise só de um remédio.')
    elif "náuseas e vômito" in pergunta:
        sintomas.append("Náuseas e vômito")
        print(f'{os.linesep}{nome}, é preocupante. Beba muita água.')
    elif "sangramentos leves" in pergunta:
        sintomas.append("Sangramentos leves")
        print(f'{os.linesep}{nome}, mantenha a cabeça levantada e use um papel para o sangramento.')
    elif "cansaço extremo" in pergunta:
        sintomas.append("Cansaço extremo")
        print(f'{os.linesep}{nome}, comece a ingerir mais vitaminas, principalmente vitamina C.')
    elif "dor nas articulações" in pergunta:
        sintomas.append("Dor nas articulações")
        print(f'{os.linesep}{nome}, precisa de repouso. Tente se espreguiçar se conseguir.')

def diagnosticar(sintomas):
    if len(sintomas) == 0:
        return "Você parece estar bem, mas continue monitorando seus sintomas."
    elif len(sintomas) < 3:
        return "Você apresenta alguns sintomas. Recomendamos um remédio e observação."
    else:
        return "Você apresenta vários sintomas de dengue. Procure um médico imediatamente, poça ser que voce tenha e precisse de tratamento."

def start():
    # Apresentar o chatbot
    print('Olá, eu sou MECIA, sua assistente médica. Como está se sentindo?')

    # Pedir o nome
    nome = input('Digite seu nome: ')

    sintomas = []

    while True:
        # Pedir a pergunta
        pergunta = input('Como está se sentindo: ')

        # Processar a pergunta e fornecer a resposta
        processar_resposta(pergunta.lower(), nome, sintomas)

        # Verificar se deseja continuar ou obter um diagnóstico
        continuar = input('Deseja continuar descrevendo sintomas?  ').strip().lower()
        if continuar != 'sim':
            break

    # Diagnóstico final
    print(diagnosticar(sintomas))

if __name__ == '__main__':
    start()
