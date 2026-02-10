#task1
import numpy as np
std_score=([[60,70,59],[70,75,80],[80,55,90],[60,78,90],[69,85,90]])
mean_avg=np.mean(std_score,axis=0)
print(mean_avg)
result = mean_avg-std_score
print(result)

#task2
sensor_R=np.arange(24)
print(sensor_R)
print(sensor_R.reshape(4,3,2))
print(sensor_R.reshape(4,2,3))


        