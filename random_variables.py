import pandas as pd
import matplotlib.pyplot as plt

die = pd.DataFrame([1, 2, 3, 4, 5, 6])
dice_sum = die.sample(2, replace=True).sum().loc[0]

print(dice_sum)

trial = 5000
results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]
print(results)

freq = pd.DataFrame(results).value_counts()
sorted_freq = freq.sort_index()
relative_frequency = sorted_freq/sorted_freq.sum()
print(sorted_freq)
print(relative_frequency)

sorted_freq.plot(kind='bar')
plt.savefig('images/random_variables.png')

relative_frequency.plot(kind='bar')
plt.savefig('images/random_variables_relative_freq.png')
