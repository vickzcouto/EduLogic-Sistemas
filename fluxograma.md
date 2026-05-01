# Fluxograma — Assistente de Aprovação (EduLogic Sistemas)

```mermaid
flowchart TD
    A([Início]) --> B[main]

    B --> C[coletar_dados_interativo\nLer: Nome · N1 · N2 · Frequência]

    C --> D{KeyboardInterrupt\nCtrl+C?}
    D -- Sim --> E([Operação cancelada\npelo usuário])
    D -- Não --> F[processar_estudante\nnome · n1 · n2 · frequencia]

    F --> G{0 ≤ N1 ≤ 10?}
    G -- Não --> H([Erro de validação:\nN1 fora do intervalo])
    G -- Sim --> I{0 ≤ N2 ≤ 10?}

    I -- Não --> J([Erro de validação:\nN2 fora do intervalo])
    I -- Sim --> K{0 ≤ Frequência ≤ 100?}

    K -- Não --> L([Erro de validação:\nFrequência fora do intervalo])
    K -- Sim --> M[calcular_media\nM = N1 + N2 / 2]

    M --> N{M ≥ 7,0\nE Freq ≥ 75%?}
    N -- Sim --> O[Situação: APROVADO]
    N -- Não --> P{5,0 ≤ M < 7,0\nE Freq ≥ 75%?}

    P -- Sim --> Q[Situação: RECUPERAÇÃO]
    P -- Não --> R[Situação: REPROVADO]

    O --> S[exibir_resultado\nNome · N1 · N2 · Média · Freq · Situação]
    Q --> S
    R --> S

    S --> T([Fim])
```

## Legenda das funções

| Função                    | Responsabilidade                                              |
|---------------------------|---------------------------------------------------------------|
| `main`                    | Coordena o fluxo e trata exceções (`ValueError`, `KeyboardInterrupt`) |
| `coletar_dados_interativo` | Lê nome, N1, N2 e frequência via teclado                    |
| `validar_nota`            | Verifica se a nota está entre 0,0 e 10,0                     |
| `validar_frequencia`      | Verifica se a frequência está entre 0% e 100%                |
| `calcular_media`          | Calcula M = (N1 + N2) / 2                                    |
| `determinar_situacao`     | Aplica as regras de aprovação, recuperação e reprovação       |
| `exibir_resultado`        | Formata e imprime os dados finais do estudante                |

## Regras de negócio

| Condição                                  | Situação      |
|-------------------------------------------|---------------|
| Média ≥ 7,0 **e** Frequência ≥ 75%        | Aprovado      |
| 5,0 ≤ Média < 7,0 **e** Frequência ≥ 75% | Recuperação   |
| Qualquer outro caso                        | Reprovado     |
