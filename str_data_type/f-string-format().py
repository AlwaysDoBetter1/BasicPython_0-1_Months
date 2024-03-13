"""
write a string using f-string and format()
"""

year = 2010
amount = '10K'
currency = 'Bitcoin'

print(f'In {year}, someone paid {amount} {currency} for two pizzas.')  #f-string
print('In {0}, someone paid {1} {2} for two pizzas.'.format(year, amount, currency)) #format()