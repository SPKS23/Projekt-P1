import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
pd.set_option('display.max_rows', 10) # begrænser hvor mange rækker der vises ad gangen hvilket er smart senere
pd.__version__

Data = pd.read_csv("Electrical_Circuit_Data.csv",encoding='unicode_escape',on_bad_lines='skip')
Data["Time (s)"] = Data["Time (s)"] + 0.0025
a = Data[(Data["Time (s)"] <0.0050) & (Data["Time (s)"] >=0.0000001)]

t, U_kredsløb, U_kapacitor = a["Time (s)"].to_numpy(),  a["Channel 1 (V)"].to_numpy(), a["Channel 2 (V)"].to_numpy()


R = 1000
U = 2
C = 220 * 10**-9
def Opladning(t, R, C, U):
    return U*(1-np.exp(-(t-0.0025)/(C*R)))

def Afladning(t, R, C, U):
    return U*np.exp(-t/(C*R))

Teo_Op = Opladning(t,R,C,U)
Teo_af = Afladning(t,R,C,U)


Teo = np.where(t>0.0025, Opladning(t, R, C, U), Afladning(t, R, C, U))


af =(U_kapacitor-Teo)
plt.rcParams["font.family"] = "Times New Roman"
plt.figure(dpi=700)
linje = 11/50000 * 5 
linje2 = 11/50000 * 5 + 0.0025
#plt.plot(t,U_kapacitor, "b-",label = "Measured Voltage")
#plt.plot(t,Teo,"r-", label = "Theoretical expectation",linestyle="dashed")
plt.plot(t, af,label = "Relative devation")
plt.plot([linje,linje,linje2,linje2],[-4,100000,100000,-4],"o-", linestyle="dashed", label = "5\u03C4 (Discharged/Charged)")
plt.plot([0.0025,0.0025],[-0,100000],linestyle = "dashed", label = "Change from charge to discharge")
plt.xlabel("Time (s)")
plt.ylabel("Relative deviation (%)")
plt.grid(which = "both")
plt.legend()

#plt.xlim(0.0025,0.005)
plt.ylim(-0.05,0.05)

print(max(af),min(af))
