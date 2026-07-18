#API utilizada weatherapi.com
import requests
import pprint
api_key = "5fa5f64fbfb4437c9e6173700253012"
link_api_Clima_em_Tempo_real = "http://api.weatherapi.com/v1/current.json"
link_api_forecast = "http://api.weatherapi.com/v1/forecast.json"
parametros = {
    "key" : api_key,
    "q" : "USA",
    "lang" : "pt"
}


def Inicio():
    cidade_pesquisada = input("Digite um cidade ou estado ou pais:")
    parametros.update({"q": cidade_pesquisada})
    resposta_forecast = requests.get(link_api_forecast,params=parametros)
    dados_requisao_forecast = resposta_forecast.json()
    resposta = requests.get(link_api_Clima_em_Tempo_real, params=parametros)
    if resposta.status_code == 200:
        dados_requisao = resposta.json()
        temperatura = dados_requisao['current']['temp_c']
        velocidade_vento = dados_requisao['current']['wind_kph']
        descricao = dados_requisao['current']['condition']['text']
        sensacao_termica = dados_requisao['current']['feelslike_c']
        hora_local = dados_requisao['location']['localtime']
        umidade = dados_requisao['current']['humidity']
        chance_de_chover = dados_requisao_forecast['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
        temperatura_maxima = dados_requisao_forecast['forecast']['forecastday'][0]['day']['maxtemp_c']
        temperatura_minima = dados_requisao_forecast['forecast']['forecastday'][0]['day']['mintemp_c']
        regiao = dados_requisao_forecast['location']['region']
        cidade = dados_requisao_forecast['location']['name']
        pais = dados_requisao_forecast['location']['country']
        sunrise = dados_requisao_forecast["forecast"]["forecastday"][0]["astro"]["sunrise"]
        sunset = dados_requisao_forecast["forecast"]["forecastday"][0]["astro"]["sunset"]



        print(f"""
🌡️ Temperatura: {temperatura}°C
🥵 Sensação Térmica: {sensacao_termica}°C
⬆️ Máxima: {temperatura_maxima}°C
⬇️ Mínima: {temperatura_minima}°C
💨 Vento: {velocidade_vento} km/h
💧 Umidade: {umidade}%
🌧️ Chance de chuva: {chance_de_chover}%
🕒 Hora Local: {hora_local[11:16]}
🌅 Nascer do Sol: {sunrise}
🌇 Pôr do Sol: {sunset}
🌍 País: {pais}
🏙️ Cidade: {cidade}
📍 Região: {regiao}
☁️  Descrição: {descricao}
""")
    else:
        print("Erro")

def teste():
    resposta = requests.get(link_api_Clima_em_Tempo_real, params=parametros)
    dados_requisao = resposta.json() 

    resposta_forecast = requests.get(link_api_forecast,params=parametros)
    dados_requisao_forecast = resposta_forecast.json()
    pprint.pprint(dados_requisao_forecast)
#teste()
Inicio()