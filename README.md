# OpenAQ NGSI Adapter

Este projeto tem como objetivo coletar dados de qualidade do ar da [API OpenAQ](https://docs.openaq.org), formatá-los no padrão [NGSI](https://fiware.github.io/specifications/ngsiv2/latest/) e prepará-los para integração com brokers contextuais como o FIWARE Orion.

## Funcionalidades

- Busca de localizações com sensores no Brasil
- Coleta de sensores por localização
- Coleta de medições por sensor
- Formatação dos dados em NGSI (AirQualityObserved)
- Pronto para integração com plataformas FIWARE

## Como iniciar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/openaq-ngsi-adapter.git
cd openaq-ngsi-adapter
````

### 2. Crie e ative o ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate.bat  # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a API Key da OpenAQ

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
OPENAQ_API_KEY=sua_chave_aqui
```

Você pode obter a chave da API gratuitamente em: [https://docs.openaq.org/](https://docs.openaq.org/)

### 5. Execute o script principal

```bash
python main.py
```

## Estrutura do projeto

```
.
├── main.py              # Script principal que orquestra a coleta e formatação
├── openaq_client.py     # Cliente HTTP para consumir a API OpenAQ
├── ngsi_formatter.py    # Classe que transforma os dados para o formato NGSI
├── .env                 # Arquivo com variáveis de ambiente (não commitável)
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
```

## Exemplo de saída NGSI

```json
{
  "id": "AirQuality:Sao_Paulo:Ibirapuera:o3",
  "type": "AirQualityObserved",
  "parameter": { "type": "Text", "value": "o3" },
  "value": { "type": "Number", "value": 12.0 },
  "unit": { "type": "Text", "value": "µg/m³" },
  "city": { "type": "Text", "value": "Sao Paulo" },
  "location": { "type": "Text", "value": "Ibirapuera" },
  "dateObservedFrom": { "type": "DateTime", "value": "2017-06-30T20:00:00-03:00" },
  "dateObservedTo": { "type": "DateTime", "value": "2017-06-30T21:00:00-03:00" }
}
```
