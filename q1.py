import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(7671)

data = pd.read_csv('diabetes.csv')

smp = data.sample(n=25)

smp_mean = smp['Glucose'].mean()
smp_max = smp['Glucose'].max()


glc_mean = data['Glucose'].mean() #calculations
glc_max = data['Glucose'].max()

plt.boxplot([smp['Glucose'], data['Glucose']], labels=['sample', 'Population'])#boxplot
plt.title('Glucose levels sample vs population')
plt.ylabel('Glucose')
plt.show()


plt.hist([smp['Glucose'], data['Glucose']], bins=10, label=['sample', 'Population'])#histogram
plt.axvline(smp_mean, color='red', linestyle='dashed', linewidth=2, label='mean of sample')
plt.axvline(glc_mean, color='black', linestyle='dashed', linewidth=2, label='mean of Population')
plt.legend()
plt.title('Glucose maean values plot')
plt.xlabel('Glucose')
plt.ylabel('Frequency')
plt.show()



print('Mean Glucose_sample:', smp_mean)
print('Maximum Glucose_sample:', smp_max)
print('Mean Glucose_Population :', glc_mean)
print('Maximum Glucose_Population :', glc_max)
