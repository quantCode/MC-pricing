# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:42:11 2019

@author: Maciek
"""

from scipy.stats import norm
import math

def PriceBlackScholes(S, K, T, r, sigma, isCallFlag, isBinaryFlag = False):
    
    d1 = (math.log(S/K) + (r + 0.5 * sigma**2)*T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    if isCallFlag == True:
        phi = 1
    else:
        phi = -1
        
    if isBinaryFlag == True:
        # (-0.5*phi + 0.5) is to give 0 for call and 1 for put
        optionPrice = math.exp(-r * T) * ((-0.5*phi + 0.5) + phi * norm.cdf(phi * d2))
    else:
        optionPrice = phi * S * norm.cdf(phi * d1) \
                      - math.exp(-r * T) * phi * K * norm.cdf(phi * d2)
    
    return optionPrice