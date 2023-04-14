import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(7671)

data = pd.read_csv('diabetes.csv')
smp = data.sample(n=25)

smp_pctl = np.percentile(smp['BMI'], 98)
population_pctl = np.percentile(data['BMI'], 98)



plt.hist([smp['BMI'], data['BMI']], bins=10, label=['sample', 'population'])#histogram
plt.axvline(smp_pctl, color='red', linestyle='dashed', linewidth=2, label='98th Percentile of sample')
plt.axvline(population_pctl, color='black', linestyle='dashed', linewidth=2, label='98th Percentile of population ')
plt.legend()
plt.title('BMI Values Sample vs Popultion')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()

print('98th Percentile BMI of sample :', sample_percentile)
print('98th Percentile BMI of population :', pop_percentile)