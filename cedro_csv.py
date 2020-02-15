from funcoes_comuns import daterange, download_csv
from datetime import date


def down_cedro_bmef():
    start_date = date(2020, 1, 1)
    end_date = date.today()

    for single_date in daterange(start_date, end_date):
        data_dia = single_date.strftime("%Y%m%d")
        url = f'http://files.cedrotech.com/tickbytick/Bmf/{data_dia}.log'
        download_csv(url, 'bmef', data_dia)

def down_cedro_bovespa():
    start_date = date(2020, 1, 1)
    end_date = date.today()

    for single_date in daterange(start_date, end_date):
        data_dia = single_date.strftime("%Y%m%d")
        url = f'http://files.cedrotech.com/tickbytick/Bovespa/{data_dia}.log'
        download_csv(url, 'bovespa', data_dia)