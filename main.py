import pandas as pd
import matplotlib.pyplot as pl

df = pd.read_csv('divanparse/divanparse/spiders/divan.csv')

prices = df['price'].str.replace(' ', '').astype(float)
average_price = prices.mean()
print('average_price', average_price)

pl.hist(prices, bins=4)
pl.xlabel('Цена')
pl.ylabel('Кол-во')
pl.xticks(rotation=45, ha='right')
pl.title('Сравнение цен на диваны')
pl.show()