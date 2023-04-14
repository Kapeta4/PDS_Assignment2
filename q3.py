import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(7671)
population = pd.DataFrame({'BloodPressure': np.random.normal(loc=120, scale=15, size=10000)})

# Computing population statistics
pop_mean = population['BloodPressure'].mean()
pop_std = population['BloodPressure'].std()
pop_25th_percentile = np.percentile(population['BloodPressure'], 25)
pop_75th_percentile = np.percentile(population['BloodPressure'], 75)

# Creating empty lists to store sample statistics
sample_means = []
sample_stds = []
sample_25th_percentiles = []
sample_75th_percentiles = []


n_samples = 500
sample_size = 150
for i in range(n_samples):
    sample = population.sample(n=sample_size, replace=True)
    sample_means.append(sample['BloodPressure'].mean())
    sample_stds.append(sample['BloodPressure'].std())
    sample_25th_percentiles.append(np.percentile(sample['BloodPressure'], 25))
    sample_75th_percentiles.append(np.percentile(sample['BloodPressure'], 75))


fig, axs = plt.subplots(2, 2, figsize=(12, 8))

axs[0, 0].hist(sample_means, bins=20)
axs[0, 0].axvline(pop_mean, color='red', linestyle='dashed', linewidth=2)
axs[0, 0].set_title('Sample Means vs Population Mean')

axs[0, 1].hist(sample_stds, bins=20)
axs[0, 1].axvline(pop_std, color='red', linestyle='dashed', linewidth=2)
axs[0, 1].set_title('Sample Standard Deviations vs Population Standard Deviation')

axs[1, 0].hist(sample_25th_percentiles, bins=20)
axs[1, 0].axvline(pop_25th_percentile, color='red', linestyle='dashed', linewidth=2)
axs[1, 0].set_title('Sample 25th Percentiles vs Population 25th Percentile')

axs[1, 1].hist(sample_75th_percentiles, bins=20)
axs[1, 1].axvline(pop_75th_percentile, color='red', linestyle='dashed', linewidth=2)
axs[1, 1].set_title('Sample 75th Percentiles vs Population 75th Percentile')

plt.show()
findings="""Based on the plots generated from the code above, here are three findings:

The distribution of sample means is centered around the population mean, and the mean of the sample means is very close to the population mean. This indicates that the sample means are good estimates of the population mean.

The distribution of sample standard deviations is centered around the population standard deviation, and the mean of the sample standard deviations is very close to the population standard deviation. This indicates that the sample standard deviations are good estimates of the population standard deviation.

The distribution of sample percentiles (specifically the 25th and 75th percentiles) is centered around the corresponding population percentiles, and the means of the sample percentiles are very close to the population percentiles. This indicates that the sample percentiles are good estimates of the population percentiles."""
print(findings)