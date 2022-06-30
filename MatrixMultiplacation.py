import numpy as np
Climate_Data=[[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,11,12],
              [13,14,15]]
weights=[0.2,0.3,0.4]
Weights=np.array(weights)
climate=np.array(Climate_Data)
print(np.matmul(Climate_Data , Weights))
print(Climate_Data @ Weights)