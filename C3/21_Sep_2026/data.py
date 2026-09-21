import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# g=np.random.default_rng(42)
# d=g.integers(25,51,size=(5,6))
# dg=["User 1","User 2","User 3","User 4","User 5"]
# health_rec = ["Suger ","BP","BMI","SPO 2","Risk Score"]


np.random.seed(42)
df=pd.DataFrame({
    "Sleeping_Hour":np.random.randint(1,15,24),
    "Walk_Hour":np.random.randint(20,40,24),
    "Workout_Hour":np.random.randint(5,30,24),
    "Assesment":np.random.randint(2,15,24)
})
print(df.head())

df["Performance"]=np.where(df["Walk_Hour"]>=30,"High","Low")
print(df)



sns.scatterplot(
    data=df,x="Sleeping_Hour",y="Workout_Hour",hue="Performance"
    )
plt.title("Performance of a person workout based on sleeping hour")
plt.show()
