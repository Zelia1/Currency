from bs4 import BeautifulSoup
import requests
from currency.utils import to_decimal
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

url = 'https://minfin.com.ua/company/pumb/currency/'
request = requests.get(url)

soup = BeautifulSoup(request.text, 'html.parser')
curr = soup.find_all('table', class_='currency-data')


a =  []
for i in curr:
    i = i.find('tbody')
    if i != None:
        a.append(i.text)
x = ''.join(a).split()
print(x)
for row in range(1, len(x), 2):
    print(x[row])

# y = []
# for x in a:
#     x = x.find('tr')
#     if x != None:
#         y.append(x.text)
# print(y)
