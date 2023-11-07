import requests
from twilio.rest import Client
from datetime import datetime
from api_key import api_key, phone_number, twilio_number, token

# API do OpenWeatherMap
api_key = api_key
city = "clonlara"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br&units=metric"

api_result = requests.get(url)
api_response = api_result.json()

if api_result.status_code == 200:
    print('Conexao')
else:
    print("Erro")
    exit()

# Dados da temperatura
ta = api_response['main']['temp']
tmin = api_response['main']['temp_min']
tmax = api_response['main']['temp_max']
condicao = api_response['weather'][0]['description']

data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Configurações Twilio
account_sid = "ACa4c62ae4199ebbd7806de0cd72b248aa"
auth_token = token
twilio_phone_number = twilio_number
recipient_phone_number = phone_number

client = Client(account_sid, auth_token)

# Mensagem
message = client.messages.create(
    body=f""" Informações meteorológicas {data}
    Temperatura Atual: {ta}ºC
    Mínima de: {tmin}ºC
    Máxima de: {tmax}ºC
    Sensação Termica: {api_response['main']['feels_like']}
    Condição: {condicao}
    """,
    from_=twilio_phone_number,
    to=recipient_phone_number
)

print("Mensagem enviada com sucesso!")
