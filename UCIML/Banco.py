import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Carregar dados do mesmo diretório do script
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "UCI_Credit_Card.csv")

df = pd.read_csv(file_path)
df.rename(columns={"default.payment.next.month": "default"}, inplace=True)

# Distribuição de clientes por inadimplência
fig = px.histogram(df, x="default", color="default", barmode="group",
                   title="Distribuição de Clientes por Inadimplência")
fig.show()

# Inadimplência por sexo
fig = px.histogram(df, x="SEX", color="default", barmode="group",
                   category_orders={"SEX": [1, 2]},
                   labels={"SEX": "Sexo (1=Homem, 2=Mulher)", "default": "Inadimplente"},
                   title="Inadimplência por Sexo")
fig.show()

# Inadimplência por escolaridade
fig = px.histogram(df, x="EDUCATION", color="default", barmode="group",
                   title="Inadimplência por Escolaridade")
fig.show()

# Inadimplência por estado civil
fig = px.histogram(df, x="MARRIAGE", color="default", barmode="group",
                   title="Inadimplência por Estado Civil")
fig.show()

# Boxplot: limite de crédito vs inadimplência
fig = px.box(df, x="default", y="LIMIT_BAL", color="default",
             title="Limite de Crédito vs Inadimplência")
fig.show()

# Matriz de correlação
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm', annot=False)
plt.title("Matriz de Correlação")
plt.show()
