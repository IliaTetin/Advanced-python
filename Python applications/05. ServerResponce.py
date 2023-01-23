# The file contains the result of the ping command, you need to calculate the average, minimum and maximum server response time. 
# All numbers must be rounded up to an integer and written with a space in the following order: minimum, average, maximum.

import pandas as pd
import numpy as np
    
class Solution():
    def report_stat(self, filepath):
        df = pd.read_csv(filepath, sep=' ')
        arr = []
        for i in range(df.shape[0]):
            arr.append(int(df['с.1'][i].split('=')[1][:-2]))
        arr = np.array(arr)
        return(arr.min(), int(np.round(arr.mean(), 0)), arr.max())

sol = Solution()
print(sol.report_stat('./data/ping.txt'))
