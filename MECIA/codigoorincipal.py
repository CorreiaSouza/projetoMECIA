import os

def processar_resposta(pergunta, nome, sintomas_dengue, sintomas_COVID19):
    # Processar sintomas de dengue
    if "dor de cabeça intença" in pergunta:
        sintomas_dengue.append("Dor de cabeça intensa")
        print(f'{os.linesep}{nome}, certo, continuaremos os exames. Pode ser que precise só de um remédio.')
    elif "náuseas e vômito" in pergunta:
        sintomas_dengue.append("Náuseas e vômito")
        print(f'{os.linesep}{nome}, é preocupante. Beba muita água.')
    elif "sangramentos leves" in pergunta:
        sintomas_dengue.append("Sangramentos leves")
        print(f'{os.linesep}{nome}, mantenha a cabeça levantada e use um papel para o sangramento.')
    elif "cansaço extremo" in pergunta:
        sintomas_dengue.append("Cansaço extremo")
        print(f'{os.linesep}{nome}, comece a ingerir mais vitaminas, principalmente vitamina C.')
    elif "dor nas articulações" in pergunta:
        sintomas_dengue.append("Dor nas articulações")
        print(f'{os.linesep}{nome}, precisa de repouso. Tente se espreguiçar se conseguir.')

    # Processar sintomas de COVID-19
    if "dificuldade para respirar" in pergunta:
        sintomas_COVID19.append("Dificuldade para respirar")
        print(f'{os.linesep}{nome}, isso é preocupante. Talvez você precise de atendimento médico.')
    elif "perda de paladar ou olfato" in pergunta:
        sintomas_COVID19.append("Perda de paladar ou olfato")
        print(f'{os.linesep}{nome}, hidrate-se e alimente-se bem. Mesmo com a perda de paladar, é importante manter uma boa hidratação e alimentação.')
    elif "dor de garganta" in pergunta:
        sintomas_COVID19.append("Dor de garganta")
        print(f'{os.linesep}{nome}, vou recomendar um medicamento para você e beba chá de ervas para relaxar a garganta.')
    elif "febre ou calafrios" in pergunta:
        sintomas_COVID19.append("Febre ou calafrios")
        print(f'{os.linesep}{nome}, descanse bastante para ajudar seu corpo a combater a infecção ou qualquer outra causa subjacente.')
    elif "congestão ou corrimento nasal" in pergunta:
        sintomas_COVID19.append("Congestão ou corrimento nasal")
        print(f'{os.linesep}{nome}, recomendo que use um spray nasal salino para hidratar e limpar as passagens nasais. Isso pode ajudar a aliviar a congestão nasal.')

def diagnosticar_imediato(sintomas_dengue, sintomas_COVID19):
    if len(sintomas_dengue) >= 5:
        return "Você apresenta vários sintomas de dengue. Procure um médico imediatamente, pode ser que você precise de tratamento."
    elif len(sintomas_COVID19) >= 5:
        return "Você apresenta vários sintomas de COVID-19. Procure um médico imediatamente. Você já tomou a vacina contra a COVID-19?"
    return None

def start():
    # Apresentar o chatbot
    print('Olá, eu sou MECIA, sua assistente médica.')

    # Pedir o nome
    nome = input('Digite seu nome: ')

    sintomas_dengue = []
    sintomas_COVID19 = []

    while True:
        # Pedir a pergunta
        pergunta = input('Como está se sentindo: ')

        # Processar a pergunta e fornecer a resposta
        processar_resposta(pergunta.lower(), nome, sintomas_dengue, sintomas_COVID19)

        # Diagnosticar imediatamente se necessário
        diagnostico = diagnosticar_imediato(sintomas_dengue, sintomas_COVID19)
        if diagnostico:
            print(diagnostico)
            break

        # Verificar se deseja continuar ou obter um diagnóstico
        continuar = input('Deseja continuar descrevendo sintomas? (s/n): ').strip().lower()
        if continuar != 's':
            break

    # Diagnóstico final se não tiver diagnosticado antes
    if not diagnostico:
        print("Você parece estar bem, mas continue monitorando seus sintomas,.")

if __name__ == '__main__':
    start()
