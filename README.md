# Assistente de Aprovação — EduLogic Sistemas

> **Desafio Profissional de Lógica e Técnicas de Programação**
> Centro Universitário Leonardo da Vinci

---

## Sobre o projeto

Módulo desenvolvido para a empresa fictícia **EduLogic Sistemas**, com o objetivo de automatizar o cálculo da situação final de estudantes em uma disciplina, eliminando o processo manual feito por planilhas e calculadoras.

---

## Regras de negócio

| Situação | Média (M) | Frequência |
|---|---|---|
| Aprovado | M ≥ 7,0 | ≥ 75% |
| Recuperação | 5,0 ≤ M < 7,0 | ≥ 75% |
| Reprovado | M < 5,0 | qualquer |
| Reprovado | qualquer | < 75% |

**Fórmula da média:** `M = (N1 + N2) / 2`

---

## Como executar

```bash
python assistente_aprovacao.py
```

Informe quando solicitado: nome do estudante, nota N1, nota N2 e frequência percentual.

---

## Estrutura do código

| Função | Descrição |
|---|---|
| `calcular_media` | Calcula M = (N1 + N2) / 2 |
| `determinar_situacao` | Aplica as regras e retorna a situação |
| `validar_nota` | Garante que a nota esteja entre 0 e 10 |
| `validar_frequencia` | Garante que a frequência esteja entre 0% e 100% |
| `processar_estudante` | Orquestra validação, cálculo e resultado |
| `exibir_resultado` | Exibe os dados formatados no terminal |
| `coletar_dados_interativo` | Lê os dados digitados pelo professor |
| `main` | Ponto de entrada do programa |

---

