import numpy as np


data = np.array([100, 200, 300, 400])
norm = (data - np.min(data)) / (np.max(data) - np.min(data))
print(norm)
