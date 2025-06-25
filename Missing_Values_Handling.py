import numpy as np
data = np.array([5.0, 7.0, np.nan, 10.0])
mean = np.nanmean(data)
data[np.isnan(data)] = mean
print(data)
