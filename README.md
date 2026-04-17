# Projeto: Analytics e Monitoramento para Estufas IoT

### 1. Identificação do Grupo
* **Instituição:** Centro Educacional da Fundação Salvador Arena
* **Curso:** Engenharia de Controle e Automação
* **Grupo:** B
* **Integrantes:**
  * Jhuan Henrique Luz Dias - RA: 062210023
  * Lucas Veiga Bezerra - RA: 062210006
  * Yasmin Souza Correia - RA: 062210008
  * Tifany Mariane Ferreira - RA: 062210019
  * Vinicius Koiti Vila Nova Tsuchiya - RA: 062210022

---

### 2. Área Problema Selecionada
* [X] Gêmeos Digitais (Digital Twins) e Analytics em Tempo Real
---

### 3. Diagnóstico e Definição do Problema
* **Contexto:** Aplicação da Indústria 4.0 na agricultura de precisão, utilizando telemetria contínua para mapear processos biológicos em ambientes protegidos.
* **Problema:** A alta densidade de dados provenientes da instrumentação IoT costuma carregar ruídos de leitura, dificultando a extração de variáveis confiáveis para o controle preditivo.
* **Impacto:** Uma infraestrutura de dados tratada viabiliza a implementação de malhas orientadas a dados, maximizando a produtividade agrícola apenas com informações empíricas.

---

### 4. Arquitetura de Dados (Fonte e Dataset)
* **Origem dos Dados:** Advanced IoT Dataset (Tikrit University). Dados reais de laboratório, garantindo rigor e ausência de informações sintéticas.
* **Características:** Conjunto com 30.000 amostras instrumentais (ACHP, ALAP, AWWGV, etc.).
* **Volume:** Banco de dados de alta dimensionalidade para fundamentação estatística sólida.

---

### 5. Plano de Tratamento de Dados (ETL)

1. **Extração:** Carga das amostras brutas da malha de telemetria.  
2. **Transformação:**
   - Exclusão de perdas de pacote e falhas de rede (valores nulos).
   - Aplicação do filtro IQR no sinal da célula de carga (AWWGV) para supressão de *outliers* elétricos ou mecânicos.  
3. **Carga:** Consolidação dos *dataframes* otimizados no diretório `/data/processed`.

---

### 6. Estrutura do Repositório

* `/docs` → documentação técnica do sistema  
* `/data/raw` → base de dados original (`Advanced_IoT_Dataset.csv`)  
* `/data/processed` → dados tratados após o pipeline de ETL  
* `/scripts` → notebook Python contendo os algoritmos de análise  
* `requirements.txt` → relação de dependências do ambiente  

---

### 7. Instruções para Execução

1. Clone o repositório.  
2. Instale as dependências executando:

```bash
pip install -r requirements.txt
```

3. Inicialize o ambiente e execute o notebook presente no diretório `/scripts`.

---

### 8. Etapa 02 (M2) - Análise Exploratória de Dados (EDA)

**Link do Notebook Executável:**  
https://colab.research.google.com/drive/1ColVSLeGc4DaJKByNFKhonDa7GhRRF9K?usp=sharing

---

**Contexto da Aplicação:**  
A análise se limitou ao processamento da telemetria de campo. O objetivo principal foi mapear as relações físicas entre variáveis do processo (como morfologia vs. biomassa) para pavimentar a construção de modelos preditivos, sem o artifício de geração matemática de dados.

---

**Pipeline de Limpeza:**  
O uso do corte interquartil (IQR) na variável de peso blindou a estatística contra perturbações no sinal do sensor, assegurando a confiabilidade das conclusões operacionais.

---

**Hipóteses Validadas:**

- A Área Foliar (ALAP) mantém proporcionalidade física com a Biomassa Úmida (AWWGV).  
- As estufas com instrumentação de ponta (Smart IoT) apresentam estabilidade superior às plantas tradicionais.  

---

**Conclusão Técnica:**  
Os resultados obtidos permitem futura aplicação em estratégias de controle e predição baseadas em modelos orientados a dados (*data-driven control*).

---

### 9. Apêndice de Uso Ético de Ferramentas

A assistência da ferramenta (Google Gemini) limitou-se à estruturação técnica do código e formatação de plots estatísticos.

---

**A. Exemplos de Uso:**

- Refatoração de scripts em Python (Pandas).  
- Sugestões semânticas para exibição de matrizes térmicas densas.  

---

**B. Rigor e Decisão do Grupo:**

O grupo descartou orientações iniciais da ferramenta para gerar dados de atuação controlada (sinal PWM simulado). A decisão unânime foi restringir a análise estritamente aos sinais instrumentais disponíveis no *datacard* oficial.

---

**C. Validação da Engenharia:**

- Verificação lógica da exclusão de dados pelo método IQR.
