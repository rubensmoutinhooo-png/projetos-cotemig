# Analise de dados - notas dos alunos
# Trabalho da materia de dados / python

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("notas_alunos.csv")

print("primeiras linhas do arquivo:")
print(dados.head())

print("\nmedia geral das notas: " + str(dados["nota"].mean()))
print("nota maxima: " + str(dados["nota"].max()))
print("nota minima: " + str(dados["nota"].min()))

print("\nmedia por materia:")
media_materia = dados.groupby("materia")["nota"].mean()
print(media_materia)

print("\nmedia por aluno:")
media_aluno = dados.groupby("aluno")["nota"].mean()
print(media_aluno)

# grafico com a media de cada materia
media_materia.plot(kind="bar", color="steelblue")
plt.title("Media de notas por materia")
plt.xlabel("Materia")
plt.ylabel("Media")
plt.tight_layout()
plt.savefig("media_por_materia.png")
print("\ngrafico salvo em media_por_materia.png")
