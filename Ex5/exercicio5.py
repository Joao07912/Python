import pandas as pd

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

crescimento = seriesAno2 - seriesAno1

ano3 = seriesAno2 + crescimento
ano4 = ano3 + crescimento

linguagem_mais_popular = ano4.nlargest(1)
print("Linguagem mais popular no Ano 4:")
print(linguagem_mais_popular)