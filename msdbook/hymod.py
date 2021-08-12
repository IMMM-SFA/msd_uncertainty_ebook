import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

sns.set()


def Pdm01(Hpar, Bpar, Hbeg, PP, PET):
    """Fill in description.

    """

    b = math.log(1-Bpar/2)/math.log(0.5)
    Cpar = Hpar/(1+b)
    Cbeg = Cpar*(1-(1-Hbeg/Hpar)**(1+b))

    OV2 = max(PP+Hbeg-Hpar, 0)
    PPinf = PP-OV2

    Hint = min((PPinf+Hbeg), Hpar)
    Cint = Cpar*(1-(1-Hint/Hpar)**(1+b))
    OV1 = max(PPinf+Cbeg-Cint, 0)

    OV = OV1+OV2
    ET = min(PET, Cint)
    Cend = Cint-ET
    Hend = Hpar*(1-(1-Cend/Cpar)**(1/(1+b)))

    return OV, ET, Hend, Cend


def Nash(K, N, Xbeg, Inp):
    """Fill in description.

    """

    OO = np.zeros(N)
    Xend = np.zeros(N)

    for Res in range(0,N):
        OO[Res] = K*Xbeg[Res]
        Xend[Res] = Xbeg[Res]-OO[Res]

        if Res == 0:
            Xend[Res] = Xend[Res] + Inp
        else:
            Xend[Res] = Xend[Res] + OO[Res-1]

    out = OO[N-1]

    return out, Xend


def Hymod01(Data, Pars, InState):
    """Need to grow XHuz and others

    """

    # initialize arrays
    XHuz = np.zeros(len(Data))
    XHuz[0] = InState['XHuz']

    Xs = np.zeros(len(Data))
    Xs[0] = InState['Xs']

    Xq = np.zeros([len(Data), Pars['Nq']])
    Xq[0, :] = InState['Xq']

    OV = np.zeros(len(Data))
    ET = np.zeros(len(Data))
    XCuz = np.zeros(len(Data))
    Qq = np.zeros(len(Data))
    Qs = np.zeros(len(Data))
    Q = np.zeros(len(Data))

    for i in range(0, len(Data)):

        # run soil moisture accounting including evapotranspiration
        OV[i], ET[i], XHuz[i], XCuz[i] = Pdm01(Pars['Huz'], Pars['B'], XHuz[i], Data['Precip'].iloc[i],
                                               Data['Pot_ET'].iloc[i])

        # run Nash Cascade routing of quickflow component
        Qq[i], Xq[i, :] = Nash(Pars['Kq'], Pars['Nq'], Xq[i, :], Pars['Alp'] * OV[i])

        # run slow flow component, one infinite linear tank
        Qs[i], Xs[i] = Nash(Pars['Ks'], 1, [Xs[i]], (1 - Pars['Alp']) * OV[i])

        if i < len(Data) - 1:
            XHuz[i + 1] = XHuz[i]
            Xq[i + 1] = Xq[i]
            Xs[i + 1] = Xs[i]

        Q[i] = Qs[i] + Qq[i]

    # write to a dict
    Model = {'XHuz': XHuz,
             'XCuz': XCuz,
             'Xq': Xq,
             'Xs': Xs,
             'ET': ET,
             'OV': OV,
             'Qq': Qq,
             'Qs': Qs,
             'Q': Q}

    return Model


def main(Nq, Kq, Ks, Alp, Huz, B, Data_name, ndays):
    """Hymod main function.

    :param Nq: number of quickflow routing tanks
    :param Kq: quickflow routing tanks parameters 				- Range [0.1, 1]
    :param Ks: slowflow routing tanks rate parameter 			- Range [0, 0.1]
    :param Alp: Quick-slow split parameters 						- Range [0, 1]
    :param Huz: Max height of soil moisture accounting tanks 	- Range [0, 500]
    :param B: Distribution function shape parameter 				- Range [0, 2]

    """
    # read in observed rainfall-runoff data for one year
    Data = pd.read_csv(Data_name)
    Data = Data.iloc[0:ndays]

    # assign parameters
    Pars = {'Nq': Nq,
            'Kq': Kq,
            'Ks': Ks,
            'Alp': Alp,
            'Huz': Huz,
            'B': B}

    # Initialize states
    InState = {'Xq': np.zeros(Pars['Nq']),
               'Xs': 0,
               'XHuz': 0}

    Model = Hymod01(Data, Pars, InState)

    return Model
