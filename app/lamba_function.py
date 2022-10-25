import json
import requests
from bs4 import BeautifulSoup


curso_urls = {
    'IA':'https://www.impacta.edu.br/mba/artificial-intelligence',
    'Big Data':'https://www.impacta.edu.br/mba/business-intelligence-e-analytics',
    'DE': 'https://www.impacta.edu.br/mba/data-engineering',
    'Marketing': 'https://www.impacta.edu.br/mba/executivo-em-marketing-digital',
    'Full Stack': 'https://www.impacta.edu.br/mba/full-stack-developer',
    'UX': 'https://www.impacta.edu.br/mba/ux-design-digital-experience',
    'Cloud': 'https://www.impacta.edu.br/mba/cloud-computing-devops'
}


def lambda_handler(event, context):
    
    result = {}

    if event.get('httpMethod') == "POST":
        result = json.loads(event.get('body'))
    elif event.get('httpMethod') == "GET":
        result = event.get('queryStringParameters')

    task = result.get("task")
    if task == 'info':
        
        curso = result.get("curso")

        #crawler para pegar informações
        nome_curso = curso_urls.get(curso)
        if nome_curso:
            r = requests.get(nome_curso).text
            info = BeautifulSoup(r, 'html.parser')(class_='background-base-site')[0].text
    
            #retornar informações no campo info, no formato JSON
            return { 'statusCode': 200, 'body': info} 
        # curso não encontrado
        else:
            return { 'statusCode': 400, 'body': 'Não encontramos informações sobre este curso'}
        
    
    return {
        'statusCode': 200,
        'body': result
    }