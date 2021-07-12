import json
from decimal import Decimal
from currency import choices

from bs4 import BeautifulSoup
import requests
from currency.utils import to_decimal, valid_number

# # from currency.models import Rate
#
# # url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
# # response = requests.get(url)
# # print(response.json())
#
# url = 'https://api.monobank.ua/bank/currency'
# response = requests.get(url)
# response.json()
# response.raise_for_status()
# available_currency_type = {840: 'USD', 978: 'EUR'}
# available_currency_type_second = 980
# currencies = response.json()
#
# source = 'vkurse'
#
# for curr in currencies:
#     validity_label_one = curr['currencyCodeA']
#     validity_label_two = curr['currencyCodeB']
#
#     if validity_label_one in available_currency_type and validity_label_two == available_currency_type_second:
#         currencies_type = available_currency_type[validity_label_one]
#         buy = to_decimal(curr['rateBuy'])
#         sale = to_decimal(curr['rateSell'])
#
#         previous_rate = Rate.objects.filter(source=source, type=currencies_type).order_by('created').last()
#
#         if (
#                 previous_rate is None or
#                 previous_rate.sale != sale or
#                 previous_rate.buy != buy
#         ):
#             Rate.objects.create(
#                 type=currencies_type,
#                 buy=buy,
#                 sale=sale,
#                 source=source,
#             )
#

# url = '	http://vkurse.dp.ua/course.json'
# response = requests.get(url)
# response.raise_for_status()
# available_currency_type = {'Dollar': 'USD', 'Euro': 'EUR'}
# currencies = response.json()
#
# source = 'vkurse'
#
# for curr in currencies:
#     currencies_type = curr
#     if curr in available_currency_type:
#         currencies_type = available_currency_type[curr]
#         buy = to_decimal(currencies[curr]['buy'])
#         sale = to_decimal(currencies[curr]['sale'])
from fake_useragent import UserAgent

# currencies = []
# for curr in data:
#     currencies.append(curr.text)
#     print(data.index(curr))
#
# data_currencies = {}
# for curr_currencies in currencies:
#     if curr_currencies in available_currency_type and currencies.index(curr_currencies) < 3:
#         data_currencies[curr_currencies] = currencies[1], currencies[2]
#     else:
#         if curr_currencies in available_currency_type:
#             data_currencies[curr_currencies] = currencies[3], currencies[4]
# print(data_currencies)


# url = 'https://about.pumb.ua/ru/info/currency_converter'
# header = {'User-Agent': UserAgent().firefox}
# response = requests.get(url, headers=header)
# soup = BeautifulSoup(response.content, 'html.parser')
# data = soup.find('div', {'class': 'exchange-rate'}).find_all('td', limit=6)
# available_currency_type = frozenset(('USD', 'EUR'))
#
# source = 'pumb'
# currencies = {}
#
# for curr_from_data in data:
#     if data.index(curr_from_data) < 3:
#         if curr_from_data.text in available_currency_type:
#             currencies[curr_from_data.text] = []
#         else:
#             currencies['USD'].append(curr_from_data.text)
#     else:
#         if curr_from_data.text in available_currency_type:
#             currencies[curr_from_data.text] = []
#         else:
#             currencies['EUR'].append(curr_from_data.text)
#
# for curr in currencies:
#     from currency.models import Rate
#
#     if curr in available_currency_type:
#         currencies_type = curr
#         buy = currencies[curr][0]
#         sale = currencies[curr][1]
#
#         previous_rate = Rate.objects.filter(source=source, type=currencies_type).order_by('created').last()
#
#         if (
#                 previous_rate is None or
#                 previous_rate.sale != sale or
#                 previous_rate.buy != buy
#         ):
#             Rate.objects.create(
#                 type=currencies_type,
#                 buy=buy,
#                 sale=sale,
#                 source=source,
#             )

# print(currencies)
# curr = soup.find_all('tbody')
# # print(curr)
# x = curr.find_all('tr')
# for data in x:
#     print(data.find('td'))

#
#
# a =  []
# for i in curr:
#     i = i.find('tbody')
#     if i != None:
#         a.append(i.text)
# x = ''.join(a).split()
# print(x)
# for row in range(1, len(x), 2):
#     print(x[row])

# y = []
# for x in a:
#     x = x.find('tr')
#     if x != None:
#         y.append(x.text)
# print(y)
#
# url = 'https://my.ukrsibbank.com/ru/personal/operations/currency_exchange/'
# request = requests.get(url)
# for row in request:
#     print(row)

# url = 'https://raiffeisen.ua/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# currencies = soup.find_all('div', class_='bank-info__table-body')
# print(currencies)
# print(soup.title)

# curr = soup.findAll('div', class_='bank-info__table-body')
# print(curr)
# for i in curr:
#     print(i.text)
# print(curr[0].text)
# response.raise_for_status()
# currencies = response.json()
# available_currency_type = frozenset(('USD', 'EUR'))
# print(currencies)

# for curr in currencies:
#     print(curr)
# data = currencies['rates']['cash']['data']
#
# source = 'eximb'
#
# for curr in data:
#     if curr['code'] in available_currency_type:
#         currencies_type = curr['code']
#         buy = to_decimal(valid_number(curr['buy']))
#         sale = to_decimal(valid_number(curr['sell']))
#         print(buy)
#         print(sale)

x = choices.RATE_TYPE_CHOICES
print(x[0][''])
