from datetime import timedelta, date
import requests
import os.path


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def download_csv(url, nome_pasta, nome_arquivo):
    if not verifica_pasta_arquivo(nome_pasta, nome_arquivo):
        print(f'O arquivos {nome_arquivo}.csv já existe!')
    else:
        print(f'Verificando arquivo csv {nome_arquivo}...')
        r = requests.get(url)

        if r.status_code == 200:
            open(f'{nome_pasta}/{nome_arquivo}.csv', 'wb').write(r.content)
            print(f'{nome_arquivo} salvo.')
        else:
            print(f'O arquivo {nome_arquivo} não existe no servidor.')


def verifica_pasta_arquivo(nome_pasta, nome_arquivo):
    if not os.path.exists(f'{nome_pasta}'):
        os.mkdir(nome_pasta)
    elif os.path.exists(f'{nome_pasta}/{nome_arquivo}.csv'):
        return False
    else:
        return True
