#!/Users/ashmitbathla/opt/anaconda3/bin/python3
import sys 
import numpy as np 

# generates the netlist code for the SHH-circuit with userspecified 't' and unit cell count
node_count = int( sys.argv[1] ) 
# 'node_count' variable must be a even number 
# node_count == 2 --> signifies a unit cell  of the transitional lattice 
# total number of unitcells --> node_count/2 
if node_count < 2 or node_count % 2 != 0 : 
    sys.exit( 1 )
t = float( sys.argv[2] )

ini_stdout = sys.stdout
c1 = 1e-7
c2 = str( t*c1 )  
c1 = str( c1 )
l = '1e-5' 

filename = 'file' + str( int(10*t) ) + '.cir'

# creates and save the code into a cir file which is later runn to simulate the circuit
with open( filename , 'w') as f :
    sys.stdout = f  
    print( '*SSH circuit netlist with N =' , str( node_count ) , '\n')
    print('*sources')
    print('vin 1 0 SINE() AC 1 \n')
    print('*capacitors')
    for i in range( 1 , node_count + 1 ):
        if i % 2 == 0 :
            print( 'c' + str(i), str(i-1) , str(i) , c2 )
        else :
            print( 'c' + str(i) , str(i-1), str(i) , c1 )
    print('\n *inductors')
    for i in range( 1 , node_count +1): 
        print( 'l'+ str(i), str(i) , '0' , l ) 
    print('\n * directive ')
    print('.ac lin 10000 100e3 200e3')
    print('.end')
    sys.stdout = ini_stdout 