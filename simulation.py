import numpy as np
import math

def SimulateAssetPrices(seed, sims, stepCnt, stepSize, spot, vol, r):

    np.random.seed(seed)
    normRN = np.random.normal(0, 1, (stepCnt, sims))
    assetPrices: ndarray = np.zeros((stepCnt, sims))
    assetPrices[0, :] = spot

    for i in range(1, stepCnt):
        for j in range(sims):
            assetPrices[i, j] = assetPrices[i - 1, j] * (1 + r * stepSize + vol * math.sqrt(stepSize) * normRN[i, j])

    return assetPrices

# this simulation is simply amazing
