# Projeto2-VamoAI

### Comandos git
* git status
* git pull origin main
* git checkout origin nome_branch
* git checkout main (para voltar para a branch main)




import requests

api_URL = 'https://api.nasa.gov/planetary/apod?api_key=F8pxcg3lpaCoKgUISPrEQZwVKGY5G2IOdukbywfu'

request = requests.get(api_URL)
print(request.text)

print("O estado da requisição foi: ", request.status_code)
