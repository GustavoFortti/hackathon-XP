from random import randint
from datetime import datetime as dt
import time

tickers = ["CAB91", "GAA77", "PETR4"]
banks = ["xp", "itau", "santander", "bradesco"]

def gen_distinct(distinct=[]):
    return distinct[randint(0,len(distinct) - 1)] if len(distinct) > 0 else None

def gen_str_num(length):
    return str(randint(0, 10**length - 1)).zfill(length)

def gen_date(start, end, formato):
    start, end = (dt.timestamp(dt.strptime(start, formato)), dt.timestamp(dt.strptime(end, formato)))
    return dt.strftime(dt.fromtimestamp(randint(start, end)), formato)

def gen_stock(initial_offer=True, **kwargs):
    if initial_offer:
        name = kwargs.get("name")
    else:
        if len(kwargs.get("names")) == 0:
            name = "MARCO"
        else:
            name = gen_distinct(kwargs.get("names"))

    acquisition_date = gen_date(start="1/1/2010", end="1/1/2022", formato="%d/%m/%Y") if initial_offer else \
        dt.strftime(dt.fromtimestamp(time.time()), "%d/%m/%Y")
        
    bank = gen_distinct(banks)
    return {
        "identity": f"{bank}-stocks-{gen_str_num(10)}",
        "bankId": f"{bank}",
        "ticker": f"{gen_distinct(tickers)}",
        "volume": randint(100, 1000) if randint(1, 10) < 8 else 10* randint(100, 1000),
        "value": randint(10, 70) if randint(1, 10) < 7 else 3 * randint(10, 70),
        "acquisitionDate": acquisition_date,
        "risk": randint(0,100)
    }


if __name__ == '__main__':

    # Operação de criar um dado para representar o historico daquela pessoa
    res = gen_stock(initial_offer=True, name = "Marcelo")
    print(res)

    res = gen_stock(initial_offer=False, names = ["Marco", "Leonardo", "Gustavo", "Henrique", "Rubens"])
    print(res)