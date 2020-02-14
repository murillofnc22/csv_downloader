from datetime import timedelta, date
import requests
import os.path

start_date = date(2020, 1, 1)
end_date = date(2020, 2, 13)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

for single_date in daterange(start_date, end_date):
    data_dia = single_date.strftime("%Y%m%d")
    url = f'http://files.cedrotech.com/tickbytick/Bmf/{data_dia}.log'
    if os.path.isfile(f'{data_dia}.csv'):
        print(f'O arquivos {data_dia}.csv já existe!')
    else:
        print(f'Baixando arquivo csv {data_dia}...')
        r = requests.get(url)
        
    if r.status_code == 200:
        open(f'{data_dia}.csv', 'wb').write(r.content)
        print(f'{data_dia} salvo.')            
    else:
        print(f'Dia {single_date.strftime("%Y-%m-%d")} inexistente.')