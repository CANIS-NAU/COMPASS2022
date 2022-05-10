import numpy as np
import pandas as pd
import sys
from numpy import random

#=== Get arguments
hop=int(sys.argv[1])
delay_data=sys.argv[2]
rtx_data=sys.argv[3]

#--- FUNCTIONS


#--- END FUNCTIONS

#=== Get data
# ,ESP1_to_GWYB,UL_Delay,GWYB_to_GWYA,GWYA_to_ESP2,DL_Delay,RTT_Delay,LOS_NLOS,Distance
delay_df=pd.read_csv(delay_data, header=0, sep=",")

# DISTANCE,TEST,RTT,RTX
rtx_df=pd.read_csv(rtx_data, header=0, sep=",")

# Get an ECDF of the LoRa hop delay
lora_delay = delay_df['GWYB_to_GWYA'].to_numpy()

lora_delay_400 = delay_df[delay_df['Distance'] == 400]
lora_delay_200 = delay_df[delay_df['Distance'] == 200]
lora_delay_100 = delay_df[delay_df['Distance'] == 100]

lora_delay_400_serial = lora_delay_400['GWYA_to_ESP2'].to_numpy()
lora_delay_200_serial = lora_delay_200['GWYA_to_ESP2'].to_numpy()
lora_delay_100_serial = lora_delay_100['GWYA_to_ESP2'].to_numpy()

lora_rtx_400 = rtx_df[rtx_df['DISTANCE'] == 400]['RTX'].to_numpy()
lora_rtx_200 = rtx_df[rtx_df['DISTANCE'] == 200]['RTX'].to_numpy()
lora_rtx_100 = rtx_df[rtx_df['DISTANCE'] == 100]['RTX'].to_numpy()

#--- run simulation for n hops 1000 times ---
sim_200={}
sim_400={}
sim_100={}
for i in range(0, 999):
    sim_200[i]={}
    sim_400[i]={}
    sim_100[i]={}

    # For each hop (there and back again)
    for h in range(1,hop*2):
      # How many times will the message be retransmitted
      rtx_400=random.choice(lora_rtx_400, replace=True)
      rtx_200=random.choice(lora_rtx_200, replace=True)
      rtx_100=random.choice(lora_rtx_100, replace=True)

      # Get delay for first attempt
      delay=random.choice(lora_delay, replace=True)
      sim_400[i]["%s_rtx" % h] = rtx_400
      sim_200[i]["%s_rtx" % h] = rtx_200
      sim_100[i]["%s_rtx" % h] = rtx_100

      # For every time the packet is retransmitted, add to the delay at that hop
      for r in range(1,rtx_400):
          delay+=random.choice(lora_delay, replace=True)
          delay+=(2*np.mean(lora_delay))
      sim_400[i]["%s_delay" % h] = delay

      #200m
      delay=random.choice(lora_delay, replace=True)
      for r in range(1,rtx_200):
          delay+=random.choice(lora_delay, replace=True)
          delay+=(2*np.mean(lora_delay))
      sim_200[i]["%s_delay" % h] = delay


      #100m
      delay=random.choice(lora_delay, replace=True)
      for r in range(1,rtx_100):
          delay+=random.choice(lora_delay, replace=True)
          delay+=(2*np.mean(lora_delay))
      sim_100[i]["%s_delay" % h] = delay


      nodal_delay_up_100=random.choice(lora_delay_100_serial, replace=True)
      nodal_delay_down_100=random.choice(lora_delay_100_serial, replace=True)
      nodal_delay_up_200=random.choice(lora_delay_200_serial, replace=True)
      nodal_delay_down_200=random.choice(lora_delay_200_serial, replace=True)
      nodal_delay_up_400=random.choice(lora_delay_400_serial, replace=True)
      nodal_delay_down_400=random.choice(lora_delay_400_serial, replace=True)

      sim_100[i]["nodal_delay_up"] = nodal_delay_up_100
      sim_100[i]["nodal_delay_down"] = nodal_delay_down_100
      sim_200[i]["nodal_delay_up"] = nodal_delay_up_200
      sim_200[i]["nodal_delay_down"] = nodal_delay_down_200
      sim_400[i]["nodal_delay_up"] = nodal_delay_up_400
      sim_400[i]["nodal_delay_down"] = nodal_delay_down_400



with open("simulation_100_%s.csv" % hop, "a") as fo:
    for i in sim_100:
        sum_delay=sim_100[i]["1_delay"] + sim_100[i]["2_delay"] + sim_100[i]["3_delay"] + sim_100[i]["4_delay"] + sim_100[i]["nodal_delay_down"] + sim_100[i]["nodal_delay_up"]
        fo.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (i, sim_100[i]["1_rtx"], sim_100[i]["1_delay"], sim_100[i]["2_rtx"], sim_100[i]["2_delay"], sim_100[i]["3_rtx"], sim_100[i]["3_delay"], sim_100[i]["4_rtx"], sim_100[i]["4_delay"], sim_100[i]["nodal_delay_up"], sim_100[i]["nodal_delay_down"], sum_delay))

'''
with open("simulation_200_%s.csv" % hop, "a") as fo:
    for i in sim_200:
        sum_delay=sim_200[i]["1_delay"] + sim_200[i]["2_delay"] + sim_200[i]["3_delay"] + sim_200[i]["4_delay"] + sim_200[i]["nodal_delay_down"] + sim_200[i]["nodal_delay_up"]
        fo.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (i, sim_200[i]["1_rtx"], sim_200[i]["1_delay"], sim_200[i]["2_rtx"], sim_200[i]["2_delay"], sim_200[i]["3_rtx"], sim_200[i]["3_delay"], sim_200[i]["4_rtx"], sim_200[i]["4_delay"], sim_200[i]["nodal_delay_up"], sim_200[i]["nodal_delay_down"], sum_delay))
    
with open("simulation_400_%s.csv" % hop, "a") as fo:
    for i in sim_400:
        sum_delay=sim_400[i]["1_delay"] + sim_200[i]["2_delay"] + sim_200[i]["3_delay"] + sim_200[i]["4_delay"] + sim_200[i]["nodal_delay_down"] + sim_200[i]["nodal_delay_up"]
        fo.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (i, sim_400[i]["1_rtx"], sim_400[i]["1_delay"], sim_400[i]["2_rtx"], sim_400[i]["2_delay"], sim_400[i]["3_rtx"], sim_400[i]["3_delay"], sim_400[i]["4_rtx"], sim_400[i]["4_delay"], sim_400[i]["nodal_delay_up"], sim_400[i]["nodal_delay_down"], sum_delay))
'''
