import numpy as np
import pandas as pd
from scipy import stats
import sys
from numpy import random

#=== Get arguments
data=sys.argv[1]
distance=sys.argv[2]

# Test,RTX_1,Hop1,RTX_2,Hop2,RTX_3,Hop3,RTX_4,Hop4,Nodal_HopUp,Nodal_HopDown,RTT
df=pd.read_csv(data, header=0, sep=",")

hop1=df['Hop1'].to_numpy()
mean1=np.mean(hop1)
var1=stats.sem(hop1)
cmean1=mean1
cvar1=var1

hop2=df['Hop2'].to_numpy()
mean2=np.mean(hop2)
var2=stats.sem(hop2)
chop2=np.add(hop1,hop2)
cmean2=np.mean(chop2)
cvar2=stats.sem(chop2)

hop3=df['Hop3'].to_numpy()
mean3=np.mean(hop3)
var3=stats.sem(hop3)
chop3=np.add(hop3, np.add(hop1,hop2))
cmean3=np.mean(chop3)
cvar3=stats.sem(chop3)


hop4=df['Hop4'].to_numpy()
mean4=np.mean(hop4)
var4=stats.sem(hop4)
chop4=np.add(hop4, np.add(hop3, np.add(hop1,hop2)))
cmean4=np.mean(chop4)
cvar4=stats.sem(chop4)



print("%s,%s,%s,%s,%s,%s" % (distance, 1, mean1, var1, cmean1, cvar1))
print("%s,%s,%s,%s,%s,%s" % (distance, 2, mean2, var2, cmean2, cvar2))
print("%s,%s,%s,%s,%s,%s" % (distance, 3, mean3, var3, cmean3, cvar3))
print("%s,%s,%s,%s,%s,%s" % (distance, 4, mean4, var4, cmean4, cvar4))


