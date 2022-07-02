import numpy as np

def variance(numbers): 
    return np.sum(np.square(np.array(numbers) - np.mean(numbers))) / len(numbers)
    
    

print(variance([-10, 0, 10, 20, 30]))