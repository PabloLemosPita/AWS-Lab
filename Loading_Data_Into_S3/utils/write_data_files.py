import requests
import pandas as pd
import extract_info

def write_data_file(response, format, path_to_write):
    data = response.json()["results"]
    parsed_users = [extract_info.parse_user(user) for user in data]
    df = pd.DataFrame(parsed_users)

    format = format.lower()
    path_to_write = f"{path_to_write}/users_{format}.{format}"

    if format == 'xlsx':
        df.to_excel(path_to_write, index=False)
        print(f"Escrito em -> {path_to_write}")
    elif format == 'csv':
        df.to_csv(path_to_write, index=False)
        print(f"Escrito em -> {path_to_write}")
    elif format == 'parquet':
        df.to_parquet(path_to_write, index=False)
        print(f"Escrito em -> {path_to_write}")
    else:
        print(f"Formato Inválido: {format}")

formats = ['xlsx', 'csv', 'parquet']
url = "https://randomuser.me/api/?results=1000&nat=br"
path_to_write = "/home/pablolemospita/WorkSpace/Projetos/LocalStack/ETL_S3_DynamoDB/data"

for format in formats:
    response = requests.get(url)
    write_data_file(response, format, path_to_write)


