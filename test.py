import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('loan_data.csv')
df2 = pd.read_csv('home_ownership_data.csv')
merged = df1.merge(df2,on='member_id')

df = merged.groupby('home_ownership')['loan_amnt'].mean().reset_index()
df.rename(columns={'loan_amnt':'Average loan amount($)'}, inplace=True)

df.set_index("home_ownership",drop=True,inplace=True)

df.plot.bar()
plt.show()
