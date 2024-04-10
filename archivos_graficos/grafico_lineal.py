import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_graficos\\ensayos.csv")
#creando el grafico
sns.lineplot(x="fecha",y="ensayos",data=df)

#creando el punto en el momento mas alto de ensayos
plt.plot("09-29",11,"o")

#mostrando el grafico
plt.show()