import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

incomes = np.random.normal(27000,15000,10000)
print(np.mean(incomes))
print(np.median(incomes))

plt.hist(incomes,50)
print(plt.show())

#Mode
ages = np.random.randint(18,90,500)
print(ages)
print(stats.mode(ages))