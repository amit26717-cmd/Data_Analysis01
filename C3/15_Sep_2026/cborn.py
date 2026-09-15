import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
penguins = sns.load_dataset("penguins")
# sns.pairplot(penguins,hue= "species")
plt.show()

sns.scatterplot(data=penguins, x='bill_length_mm', y='body_mass_g', hue='sex', style='island')
plt.show()

sns.relplot(data = penguins,x='bill_length_mm',y='body_mass_g',kind='scatter',hue='sex',style='island')
plt.show()

gap=px.data.gapminder()
print(gap)
temp_df=gap[gap['country']=='India']
print(temp_df)

# axes level function 
sns.barplot(data=temp_df,x='year',y='lifeExp',color='g')
plt.show()