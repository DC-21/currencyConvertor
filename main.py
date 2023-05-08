from forex_python.converter import CurrencyRates

c = CurrencyRates()

currencies = c.get_rates('USD')  # replace 'USD' with your base currency

# print the available currencies
print('Available currencies:')
for currency in currencies:
    print(currency)

amount = float(input("Enter amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()

result = c.convert(from_currency, to_currency, amount)

print(f"{amount} {from_currency} is equal to {result} {to_currency}")
