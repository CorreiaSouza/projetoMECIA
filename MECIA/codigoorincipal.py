import os
import random
from datetime import datetime, timedelta

# ---------- FUNÇÕES DE APOIO ----------

def gerar_codigo_paciente() -> str:
    """Gera um código de 8 dígitos para o paciente."""
    return f"{random.randint(0, 99999999):08}"

def proxima_consulta() -> datetime:
    """Agenda para o próximo dia útil às 09 h."""
    hoje = datetime.now()
    dia = hoje + timedelta(days=1)
    # Se cair em sábado(5) ou domingo(6), pula para segunda‑feira
    while dia.weekday() >= 5:
        dia += timedelta(days=1)
    return dia.replace(hour=9, minute=0, second=0, microsecond=0)

# ---------- ANÁLISE DE SINTOMAS ----------

def processar_resposta(pergunta, nome, sintomas_dengue, sintomas_covid):
    """Atualiza listas de sintomas e imprime orientações imediatas."""
    # --- Dengue ---
    if "dor de cabeça" in pergunta:
        sintomas_dengue.append("Dor de cabeça")
        print(f'\n{nome}, continuaremos os exames. Pode ser que precise apenas de um analgésico.')
    elif "vomito" in pergunta:
        sintomas_dengue.extend("vômito", "náusea","enjoos","vomitando")
        print(f'\n{nome}, isso é preocupante. Beba bastante água.')
    elif "sangramentos" in pergunta:
        sintomas_dengue.extend("Sangramentos")
        print(f'\n{nome}, mantenha a cabeça erguida e pressione o local do sangramento.')
    elif "cansaço" in pergunta:
        sintomas_dengue.extend("Cansaço extremo")
        print(f'\n{nome}, reforce a ingestão de vitamina C e faça repouso.')
    elif "dor nas articulações" in pergunta:
        sintomas_dengue.extend("Dor nas articulações")
        print(f'\n{nome}, recomendamos repouso e alongamentos suaves.')

    # --- COVID‑19 ---
    if "dificuldade para respirar" in pergunta:
        sintomas_covid.extend("Dificuldade para respirar")
        print(f'\n{nome}, isso é sério. Procure atendimento médico se piorar.')
    elif "paladar e do olfato" in pergunta:
        sintomas_covid.extend("Perda de paladar", "Perda de olfato", "Perda de paladar e olfato")
        print(f'\n{nome}, mantenha boa hidratação e alimentação.')
    elif "dor de garganta" in pergunta:
        sintomas_covid.extend("Dor de garganta", "Dor de garganta leve", "Dor de garganta intensa", "Tossindo")
        print(f'\n{nome}, faça gargarejos mornos e descanse a voz.')
    elif "febre ou calafrios" in pergunta:
        sintomas_covid.extend("Febre", "Calafrios")
        print(f'\n{nome}, descanse bastante e controle a febre com antitérmico se necessário.')
    elif "congestão ou corrimento nasal" in pergunta:
        sintomas_covid.extend("Congestão nasal", "Corrimento nasal", "Gripe", "Espiros frequentes")
        print(f'\n{nome}, use solução salina para aliviar a congestão.')

def diagnosticar_imediato(sintomas_dengue, sintomas_covid):
    """Diagnóstico crítico quando >=5 sintomas."""
    if len(sintomas_dengue) >= 5:
        return "Você apresenta vários sintomas de dengue. Procure um médico imediatamente."
    if len(sintomas_covid) >= 5:
        return "Você apresenta vários sintomas de COVID‑19. Procure um médico imediatamente."
    return None

def verificar_suspeita(sintomas_dengue, sintomas_covid, nome) -> bool:
    """Gera mensagem de suspeita a partir de 2 sintomas."""
    if len(sintomas_dengue) == 3:
        codigo = gerar_codigo_paciente()
        consulta = proxima_consulta()
        print(f"\n{name_msg(nome)} Suspeita de **dengue** detectada.")
        print(f"Código do paciente: {codigo}")
        print(f"Sua consulta com um infectologista foi agendada para {consulta:%d/%m/%Y às %H:%M}.")
        return True
    if len(sintomas_covid) == 3:
        codigo = gerar_codigo_paciente()
        consulta = proxima_consulta()
        print(f"\n{name_msg(nome)} Suspeita de **COVID‑19** detectada.")
        print(f"Código do paciente: {codigo}")
        print(f"Sua consulta com um pneumologista foi agendada para {consulta:%d/%m/%Y às %H:%M}.")
        return True
    return False

def name_msg(nome: str) -> str:
    """Formata saudação personalizada."""
    return f"{nome},"

# ---------- FLUXO PRINCIPAL ----------

def start():
    print("Olá, eu sou MECIA, sua assistente médica.")
    nome = input("Digite seu nome: ")

    sintomas_dengue, sintomas_covid = [], []
    suspeita_enviada = False
    diagnostico = None

    while True:
        pergunta = input("\nComo está se sentindo? ").lower().strip()
        if not pergunta:
            continue  # evita strings vazias

        processar_resposta(pergunta, nome, sintomas_dengue, sintomas_covid)

        # Checa suspeita após adicionar o sintoma
        if not suspeita_enviada:
            suspeita_enviada = verificar_suspeita(sintomas_dengue, sintomas_covid, nome)

        # Diagnóstico crítico
        diagnostico = diagnosticar_imediato(sintomas_dengue, sintomas_covid)
        if diagnostico:
            print(f"\n{diagnostico}")
            break

        # Se já foi gerada suspeita ou diagnóstico, não continuar perguntando
        if suspeita_enviada or diagnostico:
            break

        continuar = input("\nDeseja continuar descrevendo sintomas (sim/não)? ").strip().lower()
        if continuar != "sim":
            break
# Pergunta se o usuário quer continuar

    if not diagnostico and not suspeita_enviada:
        print("\nVocê relatou poucos sintomas. Continue monitorando sua saúde e, se piorar, procure um médico.")

        # Recomendação de remédio leve, se não houver suspeita, diagnóstico e poucos sintomas
    if not suspeita_enviada and not diagnostico:
        if len(sintomas_dengue) < 3 and len(sintomas_covid) < 3:
            remedios = ["Benegrip", "Cimegripe", "Tylenol Sinus", "Vick Pyrena"]
            recomendado = random.choice(remedios)
            print(f"\n{nome}, seus sintomas parecem leves. Recomendamos que tome {recomendado} e continue monitorando sua saúde.")


    print(f"\nObrigado por usar o MECIA, {nome}. Cuide‑se!")

if __name__ == "__main__":
    start()
