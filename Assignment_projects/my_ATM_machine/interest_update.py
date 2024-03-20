from pprint import pprint

emptyDict = {}
with open('account_balances.txt', 'r') as file:
    balance = file.read()


newbalances = balance.splitlines()
for x in newbalances:
    newme = x.split('|')
    emptyDict[newme[0]] = newme[1]

for account, balance in emptyDict.items():
    balance = float(balance)
    interest = 0
    rate = 0
    if balance < 0:
        rate = 10 / 100
        interest = balance + (balance * rate / 12)
    elif balance < 1000:
        rate = balance * (1 / 100)
        interest = balance + (balance * rate / 12)
    elif balance < 5000:
        rate = ce * (2.5 / 100)
        interest = balance + (balance * rate / 12)
    elif balance >= 5000:
        rate = 5 / 100
        interest = balance + (balance * rate / 12)

    print(f'Opening Balance: {balance} Closing Balance: {interest} ({rate}% interest earned')
# Opening Balance: 5000.00   Closing Balance: 5020.833333   (5% interest earned)


# balance + ((balance * rate) / 12)




























"""from pprint import pprint
import math
from datetime import datetime
import csv

storage = {}
date = datetime.now()
formatted_date = date.strftime("%Y-%m-%d")

with open('account_balances.txt', 'r') as file:
    account_balances = file.read()

for balances in account_balances.splitlines():
    balance_list = balances.split('|')
    storage[balance_list[0]] = float(balance_list[1])

pprint(storage)
for account, balance in storage.items():
    if balance < 0:
        rate = + (10.0 / 100)
        interest = balance + ((balance * rate) / 12)
    elif balance < 1000:
        rate = (1.0 / 100)
        interest = balance + ((balance * rate) / 12)
    elif balance < 5000:
        rate = (2.5 / 100)
        interest = balance + ((balance * rate) / 12)
    else:
        rate = (5.0 / 100)
        interest = balance + ((balance * rate) / 12)
    storage[account] = f'{math.floor(interest * 1e6) / 1e6:.6f}'
    print(f'Opening Balance: {balance} Closing Balance: '
          f'{math.floor(interest * 1e6) / 1e6:.6f} ({rate * 100}% interest earned)')
pprint(storage)

file_name = f'{formatted_date}-HD.csv'
with open(file_name, 'w') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(['Account', 'Balance'])
    for account, balance in storage.items():
        csv_writer.writerow([account, balance])

with open(file_name, 'r') as file:
    csv_reader = csv.DictReader(file)
    Account_data = (list(csv_reader))

pprint(Account_data)
"""