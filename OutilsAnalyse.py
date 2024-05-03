import numpy as np
import pandas as pd
import sklearn as sk

class OutilsAnalyse:
    
    def __init__(self):
        print("")
        
        
    def coefCorrel(self, grp1, grp2):
        return np.corrcoef(grp1, grp2)[0, 1]
    
    
    
    
    
    
    
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 1, 6, 4, 5])
o = OutilsAnalyse()
print(o.coefCorrel(x, y))