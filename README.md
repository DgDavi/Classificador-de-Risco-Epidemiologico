# 🩺 Classificador de Risco Epidemiológico

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

O **Classificador de Risco Epidemiológico** é uma ferramenta de triagem inicial desenvolvida para auxiliar a população na identificação de possíveis níveis de risco relacionados a doenças infectocontagiosas. Através de um sistema de pontuação baseado em fatores clínicos e sociais, o software oferece orientações preventivas e uma visualização gráfica da análise.

---

## 🎯 Objetivos
- Fornecer uma triagem rápida e educativa.
- Visualizar graficamente o impacto de cada fator de risco no resultado final.
- Orientar o usuário sobre as próximas etapas (prevenção ou busca médica).

## ✨ Funcionalidades
- [x] **Interface via Terminal:** Coleta de dados simples e direta.
- [x] **Tratamento de Erros:** Validação de entradas para idade e respostas (s/n).
- [x] **Geração de Gráfico:** Visualização dinâmica utilizando a biblioteca `Matplotlib`.
- [x] **Feedback Educativo:** Mensagens personalizadas baseadas no nível de risco.

## 📊 Lógica de Classificação
O sistema utiliza uma métrica de pontos acumulativos para definir o nível de risco:

| Fator de Avaliação | Impacto | Pontuação |
| :--- | :---: | :---: |
| Idade (>= 60 anos) | Risco | +2 |
| Presença de Sintomas | Risco | +3 |
| Doenças Pré-existentes | Risco | +2 |
| Contato com Infectados | Risco | +2 |
| **Status de Vacinação** | **Proteção** | **-2** |

### Resultados:
*   **Baixo Risco:** < 2 pontos
*   **Médio Risco:** 2 a 4 pontos
*   **Alto Risco:** >= 5 pontos

---

## 🛠️ Tecnologias e Dependências
Para rodar este projeto, você precisará de:
*   **Python 3.10+**
*   **Matplotlib** (para visualização gráfica)

---

## 🚀 Como Executar

### 1. Preparando o Ambiente (Venv)
Recomenda-se o uso de um ambiente virtual para isolar as dependências.

**No Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
