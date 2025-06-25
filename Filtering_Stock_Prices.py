import numpy as np

prices = np.array([50, 120, 80, 200])
filtered = prices[prices > 100]
print(filtered)
