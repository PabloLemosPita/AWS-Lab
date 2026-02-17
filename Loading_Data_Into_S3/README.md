Upload de Arquivos para S3 (LocalStack)

Este projeto demonstra como criar um bucket S3 e fazer upload de arquivos locais utilizando Python + Boto3, com foco em ambiente local via LocalStack. Ele é ideal para testes de pipelines ETL, automações ou aprendizado de serviços AWS sem custos.

O script realiza as seguintes etapas:

-Conecta-se a um endpoint S3 local (http://localhost:4566) usando credenciais fictícias. 

-Cria um bucket S3. -Percorre um diretório local (../data). 

-Faz upload de todos os arquivos encontrados para o bucket. 

-Lista e imprime os objetos armazenados no bucket.

Pré-requisitos:

-Python 3.8+ 

-Docker (para rodar o LocalStack, use o docker-compose.yaml disponibilizado.) 

-LocalStack em execução -boto3
