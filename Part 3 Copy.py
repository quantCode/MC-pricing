# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:01:28 2019

@author: Maciek
"""

import math
import datetime, time
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import norm
from BS import PriceBlackScholes
from simulation import SimulateAssetPrices

# =============================================================================
# CONSTANTS
# =============================================================================
ERROR = 0.005
SIZE = ERROR # step size
K = 100  # strike
S = 100  # spot
TtM = 1  # time to maturity
V = 0.2  # volatility
INT_RATE = 0.05

# =============================================================================
# Simulating the stock price
# =============================================================================

steps = int(TtM /SIZE)

simulationsRequired = [5] + list(range(100,100100,100))  # number of sumulations

binaryResultsDf = pd.DataFrame(columns = ['Simulations','MCValue','BSValue'], index = simulationsRequired)

simStart = time.time()
tempPrices = SimulateAssetPrices(seed = 123, sims = max(simulationsRequired), stepCnt = steps, stepSize = SIZE,
                                 spot = S, vol = V, r = INT_RATE)
simEnd = time.time()

optionValueBsBin = PriceBlackScholes(S, K, TtM, INT_RATE, V, isCallFlag=True, isBinaryFlag=True)

for sim in list(simulationsRequired):
    payoffBin = np.zeros(sim)
    for p in range(sim):
        if tempPrices[steps - 1, p] >= K:
            payoffBin[p] = 1
        else:
            payoffBin[p] = 0
    optionValueMcBin = math.exp(-INT_RATE * TtM) * payoffBin.mean()
    binaryResultsDf.loc[sim, 'MCValue'] = optionValueMcBin
    binaryResultsDf.loc[sim, 'BSValue'] = optionValueBsBin
    binaryResultsDf.loc[sim, 'Difference'] = optionValueMcBin - optionValueBsBin
    
    plt.plot(binaryResultsDf.index,binaryResultsDf['Difference'])

loopEnd = time.time()

binaryResultsDf.head()

print("The simulation took: ", simEnd - simStart, " The loop for calculation of values took: ", loopEnd - simEnd)
binaryResultsDf.to_csv("BinaryOptionPrices_" + str(int(time.time())), sep='\t', encoding='utf-8')





