import boto3
import pandas as pd

acesso = boto3.Session(
    aws_access_key_id= 'ASIAQ3EGQUV4EZZJWE5A',
    aws_secret_access_key= 'ju5oJA360Om8TTAfNS+ALc0ceUCnipTm/mZdKP9f',
    aws_session_token= 'IQoJb3JpZ2luX2VjEKr//////////wEaCXVzLWVhc3QtMSJGMEQCIH0fzRaM293mLBCgcJCQm/YU7Vn1TDW7NKQe5UnUY9XiAiA57sMXB8COlFbvQLYdG/sOi1nBRlycdr9aCmSLzEEE9yqnAwhiEAAaDDA1ODI2NDE2NzgwMCIMZM6dYDxpyAD+eViaKoQDcWxSQgycjA+OcK0gl2Hw0AyY6d9MVtfQhLAzju3ujz+vCQTik9e7FjwIBkKRulTTunnjEagutvzyKNM2HvNtwXJ4SLqipdrAz55kULQuh0qUZSi/mZ6hs0jBhOMJEFHtIhkUAuqq4kF5PgS87e5L++9f095sW8XXJX/B71KVhyMedANy0/h9j4MO8QdeiffCU9m4HYIei3w0opMGbqePECbwSLr5RdeLYcgmNwJrmN0q8ZLq8Fp+7DOi+ssRRynUgNsKDtn2eQlR5T8ve39hJNxRdP5v2tywRY0I5nPpbXOvhaO2P9mMAmTy5CI1MM93zcKWdUFVgQXYrw3JBhRy8TOkynSPu4ORzU8hkNWBtqGZeXHbk9YfRAO+BHjD9JGV3jZKn2gcfKny6RwyYbTeXdXgaxWSbIBKh+IRjIjDc+DhZGueV8AAWFCBp3wpfEznsAascS3Gm4Uo0WZwp7n6D8+90GfYDRIVGTeJ8+QZAA5wRLH1eXTMiAaUrvT2M/ou+5hdMTDOxou0BjqnAXb2VoI8Bs41ePmQ9RFddDRHdk4XodrMXYG5KAQXb3ZfVPzF4LA1YJFu3/mWjiYjB6odNQWzKOclLC9ansSO7UQ4FOsogBmq5wcKx9AV57dS8DgP6kNpcqPhGPP6+j096VSgcyIWrgYlWGPKWpADC2yumQkRe3OSUMuLP6ngxVGDkz63XV9J8CGxu0vRNtRy975ili/hohQ1kUU/dzZoekNxKWIXCP6F',
    region_name= 'us-east-1'
)

s3 = acesso.resource('s3')

bucket_name = 'dadoseconomicas'
bucket = s3.Bucket(bucket_name)

arquivo = 'Setor Econômico.csv'

salvar_arq = r'C:\Users\Matheus\Desktop\Nova pasta\Setor Econômico.csv'

bucket.download_file(arquivo, salvar_arq)

dados = pd.read_csv(salvar_arq, delimiter=';', decimal=',')

dados = dados.drop(columns=['Unnamed: 5'])

# Operadores Lógicos
filtro_logico = dados[(dados['Tipo Contribuinte'] == 'Pessoa Jurídica') & (dados['Setor Econômico_Ocupação Principal'] != 'Indústria ')]

# Agregação
def calcular_soma_ano(df):
    return df.groupby('Ano')['Valor Apurado (R$)'].sum()

#Condicional
def antigo_atual(df):
    df['Status Ano'] = df['Ano'].apply(lambda x: 'Antigo' if x <= 2014 else 'Atual')
    return df

# Conversão
def ano_datetime(df):
    df['Ano'] = pd.to_datetime(df['Ano'], format='%Y')
    return df

# Data
def filtro_apartir_ano(df, ano_limite):
    df = ano_datetime(df)
    return df[df['Ano'].dt.year >= ano_limite]

# String
def maiusculas(df):
    df['Setor Econômico_Ocupação Principal'] = df['Setor Econômico_Ocupação Principal'].str.upper()
    return df

print("Dados de Pessoa Juridícas que não são do ramo Indústrial:")
print(filtro_logico)


soma_por_ano = calcular_soma_ano(dados)
print("\nSoma do valor apurado por ano:")
print(soma_por_ano)


data = antigo_atual(dados)
print("\nDados definidos como Antigo ou Atual 'Status':")
print(data.head())


dados = ano_datetime(dados)
print("\nDados com a coluna 'Ano' convertida para datetime:")
print(dados.head())


dados_filtrada_dadoss = filtro_apartir_ano(dados, 2020)
print("\nDados a partir de 2020:")
print(dados_filtrada_dadoss)


dados = maiusculas(dados)
print("\nDados com a coluna 'Setor Econômico_Ocupação Principal' em maiúsculas:")
print(dados.head())
