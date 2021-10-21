import boto3
import json

s3 = boto3.client('s3')

# Região da AWS
REGION = 'us-east-1'
comprehend = boto3.client('comprehend', region_name=REGION)
output_bucket = 'dio-live-comprehend-output-data'

# Function para detectar a linguagem dominante do texto informado
def detect_dominant_language(text):
    
    response = comprehend.detect_dominant_language(Text=text)
    return response


# Função para detectar nomes no texto
def detect_entities(text, language_code):
    response = comprehend.detect_entities(Text=text, LanguageCode=language_code)
    return response


# Função para detectar frases chaves no texto
def detect_key_phrases(text, language_code):
    response = comprehend.detect_key_phrases(Text=text, LanguageCode=language_code)
    return response


# Função para detectar o sentimento no texto
def detect_sentiment(text, language_code):
    response = comprehend.detect_sentiment(Text=text, LanguageCode=language_code)
    return response


def lambda_handler(event, context):
   
    text = event['text']

    # language code
    language_code = event['code']


    # detecting the dominant language
    print("->INICIANDO DETECÇÃO DE IDIOMA DOMINANTE: ")
    
    result = detect_dominant_language(text)
    response_path = 'dominant_language.json'
    s3.put_object(Body=json.dumps(result), Bucket=output_bucket, Key=response_path)
    
    print(json.dumps(result, sort_keys=True, indent=4))
    print("->FIM DA DETECÇÃO DE IDIOMA DOMINANTE\n")


    # detecting named entities
    print("->INICIANDO DETECÇÃO DE ENTIDADES NOMEADAS: ")

    result = detect_entities(text, language_code)
    response_path = 'named_entities.json'
    s3.put_object(Body=json.dumps(result), Bucket=output_bucket, Key=response_path)
    
    print(json.dumps(result, sort_keys=True, indent=4))
    print("FIM DA DETECÇÃO DE ENTIDADES NOMEADAS\n")


    # detecting key phrases
    print("INICIANDO DETEÇÃO DE FRASES CHAVES")
    
    result = detect_key_phrases(text, language_code)
    response_path = 'key_phrases.json'
    s3.put_object(Body=json.dumps(result), Bucket=output_bucket, Key=response_path)
    
    print(json.dumps(result, sort_keys=True, indent=4))
    print("FIM DA  DETEÇÃO DE FRASES CHAVES\n")


    # detecting sentiment
    print("INICIANDO DETECÇÃO DE SENTIMENTOS")
    
    result = detect_sentiment(text, language_code)
    response_path = 'sentiment.json'
    s3.put_object(Body=json.dumps(result), Bucket=output_bucket, Key=response_path)
    
    print(json.dumps(result, sort_keys=True, indent=4))
    print("FIM DA DETECÇÃO DE SENTIMENTOS\n")
