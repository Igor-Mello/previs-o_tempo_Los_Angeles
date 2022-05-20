import requests


#adquirindo as informacoes da cidade

API_key = "be55b259aeb4e603d00f4ad3cc994768"
cidade = "los angeles"
part = "daily"
lang = "pt_br"
lat = "-22.9028"
lon = "-43.2075"

#link para conectar com o API

link = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_key}&lang={lang}"

#comandos para coletar os dados requeridos
requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['current']['weather'][0]['description']
temperatura = int(requisicao_dic['current']['temp']- 273.15)
sensacao = int(requisicao_dic['current']['feels_like']- 273.15)

print(f"Em los angeles está {descricao},com uma temperatura de ,aproximadamente, {temperatura}°C e sensação térmica de {sensacao}°C.")
