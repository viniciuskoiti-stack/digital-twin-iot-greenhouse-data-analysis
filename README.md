# 🔧 Projeto: Gêmeo Digital (Digital Twin) e Analytics para Agricultura de Precisão

> Projeto desenvolvido para a disciplina de Ciência de Dados, focado na aplicação da Indústria 4.0 na agricultura. O objetivo é utilizar telemetria IoT contínua para mapear processos biológicos em ambientes controlados e, por meio de Machine Learning, realizar a predição da biomassa vegetal para controle preditivo em malha fechada.

![Status do Projeto](https://img.shields.io/badge/Status-Conclu%C3%ADdo%20/%20M4-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Modelagem-orange?logo=scikit-learn)
![Google AI Studio](https://img.shields.io/badge/Google%20AI%20Studio-Dashboard-purple)

---

# 👥 1. Identificação do Grupo

- Instituição: Centro Educacional da Fundação Salvador Arena
- Curso: Engenharia de Controle e Automação
- Disciplina: Ciência de Dados
- Grupo: B

## Integrantes

- Jhuan Henrique Luz Dias — RA: 062210023
- Lucas Veiga Bezerra — RA: 062210006
- Yasmin Souza Correia — RA: 062210008
- Tifany Mariane Ferreira — RA: 062210019
- Vinicius Koiti Vila Nova Tsuchiya — RA: 062210022

---

# 🎯 2. Área-Problema Selecionada

O grupo selecionou a área de Gêmeos Digitais (Digital Twins) e Analytics em Tempo Real.

## ✅ Recorte do Projeto

Predição em tempo real da biomassa úmida (peso) de plantas em estufas inteligentes, utilizando variáveis morfológicas monitoradas por telemetria IoT para fundamentar sistemas de controle orientados a dados (data-driven control).

## 📌 Justificativa e Hipótese

Sensores físicos para medição direta de biomassa são invasivos, caros e de difícil calibração em larga escala. A hipótese central do projeto é que variáveis indiretas, como Área Foliar e Nível de Clorofila, possuem forte correlação com a biomassa vegetal, permitindo que algoritmos de Machine Learning atuem como sensores virtuais de alta precisão.

---

# 🧩 3. Diagnóstico e Definição do Problema

- Problema: A elevada quantidade de dados provenientes da instrumentação IoT agrícola carrega ruídos de leitura, perdas de pacote e outliers, dificultando a extração de variáveis fisiológicas confiáveis para controle preditivo.

- Impacto: A utilização de um pipeline robusto de tratamento de dados aliado a modelos preditivos permite maior eficiência no acionamento de atuadores, redução de desperdícios hídricos e energéticos e aumento da produtividade agrícola.

---

# 🗂️ 4. Arquitetura de Dados (Fonte e Dataset)

- Origem: Advanced IoT Dataset — Tikrit University
- Características: Dataset real de laboratório contendo aproximadamente 30.000 amostras telemétricas.
- Variáveis Principais:
  - Average leaf area of the plant (ALAP)
  - Average of chlorophyll in the plant (ACHP)
  - Plant height rate (PHR)

- Variável Alvo:
  - Average wet weight of the growth vegetative (AWWGV)

---

# 🔄 5. Plano de Tratamento de Dados (ETL)

O pipeline de dados segue as seguintes etapas:

## 1. Extração

Leitura da base de dados bruta localizada na pasta /data/raw.

## 2. Transformação

- Remoção de valores nulos
- Tratamento de falhas de leitura
- Aplicação do método estatístico IQR (Interquartile Range)
- Supressão de outliers elétricos e mecânicos

## 3. Carga

Armazenamento dos dados tratados em /data/processed para utilização pelo modelo preditivo.

---

# 📈 6. Desenvolvimento e Otimização (M2, M3 e M4)

## 🔍 M2 — Análise Exploratória (EDA)

A análise exploratória permitiu identificar:

- Correlação direta entre Área Foliar (ALAP) e Biomassa Vegetal (AWWGV)
- Relação entre Clorofila e Taxa de Crescimento
- Estabilidade superior em sistemas Smart IoT
- Viabilidade do modelo preditivo baseado em sensores indiretos

---

## 🤖 M3 — Modelagem de IA

Foi implementada uma arquitetura híbrida composta por:

### Camada de Predição Matemática

Modelo RandomForestRegressor treinado com os dados pós-ETL.

### Camada de Decisão Inteligente

Interface desenvolvida no Google AI Studio responsável por:

- Receber as variáveis telemétricas
- Interpretar o estado fisiológico da planta
- Gerar diagnósticos e comandos atuados em formato JSON

---

## ⚙️ M4 — Refinamento e Otimização Profissional

### Ajuste de Hiperparâmetros

Utilização do GridSearchCV para busca das melhores configurações matemáticas do modelo:

- max_depth = 10
- min_samples_split = 10
- n_estimators = 150

### Cross-Validation

Aplicação de validação cruzada (cv=5) para garantir robustez estatística e evitar overfitting.

### Engenharia de Atributos (Feature Importance)

As variáveis mais relevantes identificadas foram:

| Variável | Importância |
|---|---|
| ACHP | 56.2% |
| PHR | 35.4% |
| ALAP | 5.4% |
| ANPL | 2.8% |

---

## 📊 Métricas Finais do Modelo Otimizado

| Métrica | Resultado |
|---|---|
| MAE | 0.0080 |
| RMSE | 0.0099 |
| R² | 99.84% |

Os resultados demonstram elevada capacidade preditiva e aderência industrial do modelo.

---

# 🖥️ 7. Dashboard de Monitoramento

Interface visual implementada utilizando Google AI Studio.

## Funcionalidades

- Entrada manual de variáveis telemétricas
- Predição da biomassa vegetal
- Diagnóstico fisiológico
- Sugestão automática de atuação
- Exibição de métricas do modelo
- Respostas estruturadas em JSON

## Link do Protótipo

[COLE_AQUI_O_LINK_DO_AI_STUDIO]

---

# 🧱 8. Estrutura do Repositório

Organização das pastas conforme o padrão profissional exigido:

```bash
/
├── data/               # Conjuntos de dados
│   ├── raw/            # Arquivos originais (imutáveis)
│   └── processed/      # Arquivos tratados após ETL
│
├── docs/               # Documentação técnica e Apêndice de IA
│
├── images/             # Identidade visual, screenshots do dashboard e diagramas
│
├── notebooks/          # Notebooks Jupyter (EDA e Modelagem)
│   ├── M2_EDA.ipynb    # Análise Exploratória
│   ├── M3_ML.ipynb     # Modelagem inicial
│   ├── M4_Otimizacao.ipynb # Refinamento e Cross-Validation
│   └── n1_individual/  # Testes estatísticos de cada integrante
│
├── scripts/            # Código-fonte principal
│   ├── etl.py          # Script de tratamento
│   └── train_model.py  # Script de treino final
│
├── requirements.txt    # Lista de bibliotecas (pandas, sklearn, etc.)
└── README.md           # Documentação principal
```

---

# 🚀 9. Instruções para Execução

## 1. Clonar o Repositório

git clone [COLE_AQUI_O_LINK_DO_REPOSITORIO]

## 2. Instalar Dependências

pip install -r requirements.txt

## 3. Executar o Notebook Principal

Abrir e executar:

/notebooks/EDA_DIGITALTWINS_V2.ipynb

O notebook executa automaticamente:

- ETL
- Limpeza estatística
- EDA
- Treinamento do modelo
- GridSearchCV
- Cross-Validation
- Métricas finais
- Feature Importance

---

# 🧪 10. N1 Individual — Aprofundamento Estatístico

| Integrante | Variável | Teste Estatístico | Link |
|---|---|---|---|
| Jhuan Henrique | [PREENCHER] | [PREENCHER] | notebooks/n1_individual/arq1.ipynb |
| Lucas Veiga | [PREENCHER] | [PREENCHER] | notebooks/n1_individual/arq2.ipynb |
| Yasmin Souza | [PREENCHER] | [PREENCHER] | notebooks/n1_individual/arq3.ipynb |
| Tifany Mariane | [PREENCHER] | [PREENCHER] | notebooks/n1_individual/arq4.ipynb |
| Vinicius Koiti | [PREENCHER] | [PREENCHER] | notebooks/n1_individual/arq5.ipynb |

---

# 🎥 11. Demonstração do Projeto

## Pitch e Demonstração (2–3 min)

[COLE_AQUI_O_LINK_DO_VIDEO]

O vídeo apresenta:

- Estrutura do projeto
- Pipeline ETL
- Modelo Random Forest
- Métricas finais
- Otimização M4
- Interface no AI Studio
- Funcionamento do Gêmeo Digital

---

# 🤖 12. Apêndice de IA

## Ferramentas Utilizadas

- Google Gemini
- Google AI Studio

## Aplicações da IA

As ferramentas de IA auxiliaram:

- Estruturação do código Python
- Organização do pipeline ETL
- Revisão da sintaxe Scikit-Learn
- Criação de prompts JSON
- Organização do GitHub
- Estruturação do Dashboard

## Processo de Validação

Todas as decisões técnicas foram verificadas manualmente pelo grupo.

Foram auditados:

- Método IQR
- Cross-Validation
- GridSearchCV
- Métricas industriais
- Importância das variáveis
- Resultados do modelo

Nenhuma decisão técnica foi aplicada automaticamente sem validação humana.

---

© 2026 — Projeto de Ciência de Dados — Faculdade Engenheiro Salvador Arena
