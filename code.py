import pandas as pd
import matplotlib.pyplot as plt

exc = 'C:/Users/youne/Downloads/python/Projet/ival-2023-154664.xlsx'

# Lire le fichier Excel dans un DataFrame pandas

df_sc = pd.read_excel(exc, sheet_name='LGT',  header=[0, 1])
df_idf = df_sc[df_sc[('Informations établissement','Académie')].isin(['PARIS', 'VERSAILLES', 'CRETEIL'])]

# Trier les établissements par taux de réussite décroissant et prendre les 50 premiers
df_top50 = df_idf.sort_values(by=('Taux de mentions bruts', 'GNLE'), ascending=False).head(100)

# Sélectionner les colonnes d'intérêt pour le graphique
y = df_top50[('Taux de mentions bruts', 'GNLE')]
x = df_top50[('Informations établissement', 'Etablissement')]

"""
y = df_idf[("Taux de mentions bruts", 'TOTAL')]
x = df_idf[('Informations établissement', 'Etablissement')]
"""
print(df_top50[[('Informations établissement', 'Etablissement'),('Taux de mentions bruts', 'GNLE')]].to_string(index=False)) 


# Now create a scatter plot
plt.scatter(x, y)

# Adding labels and title
plt.xlabel('Etablissement') 
plt.ylabel('Nombre d\'élèves présents au Bac ')
plt.title('Taux de mention au bac bruts')
# Espacer les ticks sur l'axe X
plt.xticks(rotation=75, ha='right', fontsize=6)  # Rotation des labels à 45 degrés et alignement à droite
# Show the plot
plt.show()



exc2 = 'C:/Users/youne/Downloads/python/Projet/dv3f_prix_volumes_communes_2020_2022.xlsx'


df2_sc = pd.read_excel(exc2, sheet_name='Ensemble des appartements')
df2_idf = df2_sc[df2_sc['codgeo'].astype(str).str.match('^(75[1-9][0-9]{3}|77[0-9]{3}|78[0-9]{3}|91[0-9]{3}|92[0-9]{3}|93[0-9]{3}|94[0-9]{3}|95[0-9]{3})$')]
df2_top50 = df2_idf.sort_values(by=('pxm2_median_cod121'), ascending=False).head(100)

# Sélectionner les colonnes d'intérêt pour le graphique
y = df2_top50[('pxm2_median_cod121')]
x = df2_top50[('libgeo')]


# Now create a scatter plot
plt.scatter(x, y)

# Adding labels and title
plt.xlabel('Commune') 
plt.ylabel('Prix médian par m² (€)')
plt.title('Prix médian au m² (€) par commune')
plt.xticks(rotation=75, ha='right', fontsize=6)  # Rotation des labels à 45 degrés et alignement à droite
# Show the plot
plt.show()