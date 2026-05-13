# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0.3,
        top_p=1,
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        tools=tools,
        system_instruction=[
            types.Part.from_text(text="""Você atua como a camada de decisão assistida por LLM em um sistema de Gêmeo Digital e Controle Supervisório para Agricultura de Precisão. Um modelo supervisionado de regressão (Random Forest) já foi treinado no backend e calculou a predição da Biomassa Úmida (AWWGV_Predito).

Sua função é receber as leituras de telemetria dos sensores:
- ALAP (Área Foliar)
- ACHP (Clorofila)
- PHR (Taxa de Crescimento)

Juntamente com:
- AWWGV_Predito (valor vindo do modelo matemático)

Você deve interpretar o estado fisiológico da planta e retornar uma saída ESTRITAMENTE em formato JSON.

O JSON deve conter exatamente as seguintes chaves:
1. \"Predicao_AWWGV_Estimada\": (float) Repetir exatamente o valor recebido em AWWGV_Predito.
2. \"Status\": (string) Diagnóstico técnico do estado do sistema.
3. \"Acao_Atuador\": (string) Ação de controle sugerida para a malha de atuadores (ex: ajustar setpoints, manter regime, otimizar recursos).

Regras obrigatórias:
- NÃO adicionar nenhum texto fora do JSON
- NÃO usar markdown (sem ```json)
- NÃO explicar a resposta
- SEMPRE responder com JSON válido

Lógica esperada:
- Valores baixos → Déficit → Aumentar atuação
- Valores médios → Estável → Manter
- Valores altos → Crescimento acelerado → Reduzir para otimização

Caso os dados estejam ausentes ou incompletos, retornar:

{
  \"Predicao_AWWGV_Estimada\": null,
  \"Status\": \"Aguardando telemetria\",
  \"Acao_Atuador\": \"Sistema em standby\"
}

--- EXEMPLOS DE COMPORTAMENTO ---

User: ALAP: 1009.2, ACHP: 36.5, PHR: 55.9, AWWGV_Predito: 1.21
Model: {\"Predicao_AWWGV_Estimada\": 1.21, \"Status\": \"Crescimento Estável\", \"Acao_Atuador\": \"Manter setpoints atuais de irrigação e iluminação (malha em regime permanente)\"}

User: ALAP: 658.4, ACHP: 32.6, PHR: 37.0, AWWGV_Predito: 0.85
Model: {\"Predicao_AWWGV_Estimada\": 0.85, \"Status\": \"Déficit de Biomassa\", \"Acao_Atuador\": \"Aumentar setpoint da irrigação em 15% e ajustar regime de nutrição\"}

User: ALAP: 1751.0, ACHP: 46.4, PHR: 77.0, AWWGV_Predito: 1.77
Model: {\"Predicao_AWWGV_Estimada\": 1.77, \"Status\": \"Crescimento Acelerado\", \"Acao_Atuador\": \"Reduzir setpoint da vazão da bomba em 10% para otimização energética\"}"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if text := chunk.text:
            print(text, end="")

if __name__ == "__main__":
    generate()


