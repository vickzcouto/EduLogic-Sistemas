"""
EduLogic Sistemas — Assistente de Aprovação
Módulo responsável por calcular a situação final de estudantes.
"""


# --- Cálculo da média ---
# Recebe as duas notas e devolve o resultado da fórmula M = (N1 + N2) / 2
def calcular_media(n1: float, n2: float) -> float:
    return (n1 + n2) / 2


# --- Regras de aprovação ---
# Compara média e frequência com os critérios definidos pela escola
def determinar_situacao(media: float, frequencia: float) -> str:
    # Aprovado: média ≥ 7,0 E frequência ≥ 75% (as duas condições precisam ser verdadeiras)
    if media >= 7.0 and frequencia >= 75.0:
        return "Aprovado"

    # Recuperação: média entre 5,0 e 6,9 E frequência ≥ 75%
    if 5.0 <= media < 7.0 and frequencia >= 75.0:
        return "Recuperação"

    # Reprovado: qualquer caso que não se encaixou acima
    # (média < 5,0 OU frequência abaixo de 75%)
    return "Reprovado"

# Melhorias pensadas além da atividade para garantir o bom funcionamento do EduLogic


# --- Validação da nota ---
# Garante que a nota esteja dentro do intervalo permitido (0 a 10)
# Se não estiver, interrompe o programa com uma mensagem de erro clara
def validar_nota(valor: float, nome: str) -> None:
    if not (0.0 <= valor <= 10.0):
        raise ValueError(f"{nome} deve estar entre 0,0 e 10,0. Recebido: {valor}")


# --- Validação da frequência ---
# Garante que a frequência seja um percentual válido (0% a 100%)
def validar_frequencia(valor: float) -> None:
    if not (0.0 <= valor <= 100.0):
        raise ValueError(f"Frequência deve estar entre 0% e 100%. Recebido: {valor}")


# --- Processamento completo de um estudante ---
# Junta todas as etapas: valida, calcula e retorna um dicionário com tudo
def processar_estudante(nome: str, n1: float, n2: float, frequencia: float) -> dict:
    # Passo 1: verificar se os valores recebidos são válidos
    validar_nota(n1, "N1")
    validar_nota(n2, "N2")
    validar_frequencia(frequencia)

    # Passo 2: calcular a média final
    media = calcular_media(n1, n2)

    # Passo 3: aplicar as regras e descobrir a situação
    situacao = determinar_situacao(media, frequencia)

    # Passo 4: montar e devolver um dicionário com todos os dados do estudante
    return {
        "nome": nome,
        "n1": n1,
        "n2": n2,
        "media": media,
        "frequencia": frequencia,
        "situacao": situacao,
    }


# --- Exibição dos resultados na tela ---
# Formata e imprime todas as informações do estudante de forma legível
def exibir_resultado(resultado: dict) -> None:
    print("-" * 40)
    print(f"Estudante : {resultado['nome']}")
    print(f"N1        : {resultado['n1']:.1f}")        # 1 casa decimal
    print(f"N2        : {resultado['n2']:.1f}")
    print(f"Média     : {resultado['media']:.2f}")     # 2 casas decimais
    print(f"Frequência: {resultado['frequencia']:.1f}%")
    print(f"Situação  : {resultado['situacao']}")
    print("-" * 40)


# --- Coleta de dados pelo teclado ---
# Exibe o menu e lê o que o professor digitar; .strip() remove espaços acidentais no nome
def coletar_dados_interativo() -> dict:
    print("\n=== Assistente de Aprovação — EduLogic Sistemas ===\n")
    nome = input("Nome do estudante: ").strip()
    n1 = float(input("Nota N1 (0 a 10): "))
    n2 = float(input("Nota N2 (0 a 10): "))
    frequencia = float(input("Frequência % (0 a 100): "))
    return {"nome": nome, "n1": n1, "n2": n2, "frequencia": frequencia}


# --- Ponto de entrada do programa ---
# Coordena todas as etapas e trata erros para não deixar o programa travar
def main() -> None:
    try:
        # Coleta os dados digitados pelo professor
        dados = coletar_dados_interativo()

        # Processa e calcula a situação do estudante
        # O ** "desempacota" o dicionário como se fossem argumentos separados
        resultado = processar_estudante(**dados)

        # Mostra o resultado final na tela
        exibir_resultado(resultado)

    except ValueError as erro:
        # Captura erros de validação (nota inválida, frequência inválida etc.)
        print(f"\n[Erro de validação] {erro}")

    except KeyboardInterrupt:
        # Captura Ctrl+C — o professor cancelou a operação
        print("\nOperação cancelada pelo usuário.")


# Só executa o programa se este arquivo for rodado diretamente
# (não executa se for importado por outro módulo)
if __name__ == "__main__":
    main()
