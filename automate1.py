import subprocess as sub 
import numpy as np 

t = np.array( [ 0.1 , 0.2 , 0.3 , 0.5 , 1 , 2 , 5  ])
t = t.astype( str )

# This script runs the 'circuit_netlist.py' script multiple times 
# to generate the  circuit code for different values of t 
for i in t: 
    sub.run( ['//Users/ashmitbathla/Desktop/SHH-Circuit/circuit_netlist.py' , 
              '10' , i ] )