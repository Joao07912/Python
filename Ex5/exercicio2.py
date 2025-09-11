import pandas as pd

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

total_ano1 = seriesAno1.sum()
total_ano2 = seriesAno2.sum()

print("Porcentagem total Ano 1:", total_ano1,"%")
print("Porcentagem total Ano 2:", total_ano2,"%")