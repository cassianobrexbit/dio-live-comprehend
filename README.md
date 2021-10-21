# dio-live-comprehend
Repositório para o Live Coding do dia 21/10/2021

## Serviços utilizados nessa demonstração:

- Amazon S3
- AWS Lambda
- Amazon Comprehend

## Passos para o desenvolvimento

## No AWS Lambda

- Acessar o Console do AWS Lambda
- Create Function -> Author from scracth -> Function name [nome_da_função] -> Execution role [Create a new role with basic Lambda permissions] -> Create function
- Inserir o código que está na pasta ```/src``` deste repositório

### Configurando permissões do AWS Lambda para acessar recursos do Amadon S3 e Amazon Comprehend

- Acessar o Console do AWS Lambda
- Functions -> Selecionar a função criada -> Configuration -> Permissions -> Execution Role -> Selecionar a Role Criada

## No console do IAM

- Roles -> Permissions -> Attach Policies [AmazonS3FullAccess, ComprehendFullAccess]
