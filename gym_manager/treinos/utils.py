import requests
import logging

logger = logging.getLogger(__name__)

BASE_URL = "https://wger.de/api/v2"

def obter_exercicios_objetivo(objetivo=None):
    url = f"{BASE_URL}/exercise/?limit=5"

    if objetivo:
        url += f"&goal={objetivo}"

    response = requests.get(url)

    if response.status_code == 200:
        exercicios = response.json().get('results', [])
        treino_plano = []

        for exercicio in exercicios:
            exercicio_id = exercicio.get('id')
            detalhes = obter_detalhes_exercicio(exercicio_id)

            treino_plano.append({
                'nome': detalhes.get('nome', 'Nome não disponível'),
                'descricao': detalhes.get('descricao', 'Descrição não disponível')
            })

        return treino_plano
    else:
        logger.error(f"Erro ao obter exercícios: {response.status_code} - {response.text}")
        return []
    

def obter_detalhes_exercicio(exercicio_id):
    url = f"{BASE_URL}/exerciseinfo/{exercicio_id}/"
    response = requests.get(url)

    if response.status_code == 200:
        detalhes = response.json()

        # Pegar tradução em português (language=7) ou inglês (language=2)
        traducao = None
        for t in detalhes.get("translations", []):
            if t["language"] == 7:  # Português
                traducao = t
                break
        if not traducao:
            for t in detalhes.get("translations", []):
                if t["language"] == 2:  # Inglês
                    traducao = t
                    break
        
        if traducao:
            nome = traducao.get("name", "Nome não disponível")
            descricao = traducao.get("description", "Descrição não disponível")
        else:
            nome = "Nome não disponível"
            descricao = "Descrição não disponível"

        return {"nome": nome, "descricao": descricao}
    
    logger.error(f"Erro ao obter detalhes do exercício {exercicio_id}: {response.status_code} - {response.text}")
    return {"nome": "Nome não disponível", "descricao": "Descrição não disponível"}
