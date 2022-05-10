import numpy as np
import pandas as pd
import sys
from numpy import random

#=== Get arguments
hop=int(sys.argv[1])
delay_data=sys.argv[2]
outputfile=sys.argv[3]

#=== Get data
# ,ESP1_to_GWYB,UL_Delay,GWYB_to_GWYA,GWYA_to_ESP2,DL_Delay,RTT_Delay,LOS_NLOS,Distance
delay_df=pd.read_csv(delay_data, header=0, sep=",")

# Get LoRa hop delay
lora_delay = delay_df['GWYB_to_GWYA'].to_numpy()
lora_delay_400 = delay_df[delay_df['Distance'] == 400]

# Get ESP1_to_GWYB (first hop delay)
lora_delay_400_hop1 = lora_delay_400['ESP1_to_GWYB'].to_numpy()

# Get GWYA_to_ESP2 (last hop [return] delay) 
lora_delay_400_hopN = lora_delay_400['GWYA_to_ESP2'].to_numpy()

# These Packet Loss Rates are based on our measurements at 400m LOS at SF7 and Liando et al's measurements at 1km NLOS with SF7 and 5km LOS with SF7
rtx_400=0.2877
rtx_liando_1km=0.1
rtx_liando_5km=0.3

# =================================================
# Run simulation based on our measurements for 400m
# =================================================
for i in range(1000):
    TX=0
    RTX=0
    # See if the first hop is successful; if it is not, add a mean LoRa RTT to the delay
    hop1_delay=random.choice(lora_delay_400_hop1, replace=True)
    TX+=1
    while random.random() < rtx_400:
        hop1_delay+=(2*np.mean(lora_delay))
        TX+=1
        RTX+=1

    # See if last hop is successful; if it is not, add a mean LoRa RTT to the delay    
    hopN_delay=random.choice(lora_delay_400_hopN, replace=True)
    TX+=1
    while random.random() < rtx_400:
        hopN_delay+=(2*np.mean(lora_delay))
        TX+=1
        RTX+=1

    # See if next (hops-1)*2 are successful
    cum_hop_delay=0
    TX+=1
    for h in range(((hop-1)*2)):
        hop_delay=random.choice(lora_delay, replace=True)
        TX+=1
        while random.random() < rtx_400:
            hop_delay+=(2*np.mean(lora_delay))
            cum_hop_delay+=hop_delay
            TX+=1
            RTX+=1

    total_delay_400=hop1_delay+hopN_delay+cum_hop_delay
    plr=float(RTX)/float(TX)

    with open(outputfile, "a") as fo:
        fo.write("400m,%s,%s,%s\n" % (hop, total_delay_400, plr))

# =================================================
# Run simulation based on Liando 1km
# =================================================
for i in range(1000):
    TX=0
    RTX=0
    # See if the first hop is successful; if it is not, add a mean LoRa RTT to the delay
    hop1_delay=random.choice(lora_delay_400_hop1, replace=True)
    TX+=1
    while random.random() < rtx_liando_1km:
        hop1_delay+=(2*np.mean(lora_delay))
        TX+=1
        RTX+=1

    # See if last hop is successful; if it is not, add a mean LoRa RTT to the delay
    hopN_delay=random.choice(lora_delay_400_hopN, replace=True)
    TX+=1
    while random.random() < rtx_liando_1km:
        hopN_delay+=(2*np.mean(lora_delay))
        TX+=1
        RTX+=1

    # See if next (hops-1)*2 are successful
    cum_hop_delay=0
    TX+=1
    for h in range(((hop-1)*2)):
        hop_delay=random.choice(lora_delay, replace=True)
        TX+=1
        while random.random() < rtx_liando_1km:
            hop_delay+=(2*np.mean(lora_delay))
            cum_hop_delay+=hop_delay
            TX+=1
            RTX+=1

    total_delay_1km=hop1_delay+hopN_delay+cum_hop_delay 
    plr=float(RTX)/float(TX)

    with open(outputfile, "a") as fo:
        fo.write("1km,%s,%s,%s\n" % (hop, total_delay_1km, plr))


# =================================================
# Run simulation based on Liando 1km
# =================================================
for i in range(1000):
    TX=0
    RTX=0
    # See if the first hop is successful; if it is not, add a mean LoRa RTT to the delay
    hop1_delay=random.choice(lora_delay_400_hop1, replace=True)
    TX+=1
    while random.random() < rtx_liando_5km:
        hop1_delay+=(2*np.mean(lora_delay))
        TX+=1
        RTX+=1

    # See if last hop is successful; if it is not, add a mean LoRa RTT to the delay
    hopN_delay=random.choice(lora_delay_400_hopN, replace=True)
    TX+=1
    while random.random() < rtx_liando_5km:
        hopN_delay+=(2*np.mean(lora_delay))
        TX+=1
        RTX+=1

    # See if next (hops-1)*2 are successful
    cum_hop_delay=0
    TX+=1
    for h in range(((hop-1)*2)):
        hop_delay=random.choice(lora_delay, replace=True)
        TX+=1
        while random.random() < rtx_liando_5km:
            hop_delay+=(2*np.mean(lora_delay))
            cum_hop_delay+=hop_delay
            TX+=1
            RTX+=1

    total_delay_5km=hop1_delay+hopN_delay+cum_hop_delay 
    plr=float(RTX)/float(TX)

    with open(outputfile, "a") as fo:
        fo.write("5km,%s,%s,%s\n" % (hop, total_delay_5km, plr))
