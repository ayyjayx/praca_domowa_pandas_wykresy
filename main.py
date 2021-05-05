import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_excel('imiona.xlsx')
print(df)
#zad 1
# grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# wykres = grupa.plot(subplots=True, fontsize=15)
# plt.xlabel('Rok', fontsize=30)
# plt.ylabel('Ilosc urodzonych dzieci', fontsize=30)
# plt.show()
#zad 2
# grupa2 = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# wykres2 = grupa2.plot.bar(subplots=True, fontsize=15)
# plt.legend(loc='lower right')
# plt.xlabel('Plec')
# plt.ylabel('Liczba dzieci (w milionach)')
# plt.show()

#zad 3
df2 = (df[df['Rok']>=2013])
grupa3 = df.groupby(['Plec']).agg({'Liczba': ['sum']})
wykres3 = grupa3.plot.pie(labels = {'kobiety', 'mezczyzni'}, subplots=True, autopct='%.2f %%',
                          fontsize=20, figsize=(6,6), legend=(0,0))
plt.legend(loc='lower right')
plt.show()

#zad 4

