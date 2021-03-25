import datetime
import sys
import random
import math
from strassen import *

dim = int(sys.arv[2])
    
m1 = populate_matrix(generate_matrix(dim))
m2 = populate_matrix(generate_matrix(dim))
    
def ceil(n):
  return int(-1 * n // 1 * -1)    

t = [ceil(dim/2**n) for n in range(1, ceil(math.log2(dim)))]  
for x in t:
   t_start = datetime.datetime.now()
   product = strassen(m1, m2, x)
   end = datetime.datetime.now()
   time = end - begin
   print("Threshold:")
   print(x)
   print("Time taken", str(time))
   #printmatrix(product)         
    
   
    
        
