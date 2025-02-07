# código de geração do gráfico 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', markers="o")
plt.title('Preço médio da gasolina na cidade de São Paulo')
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.savefig('gasolina.png')
plt.show()