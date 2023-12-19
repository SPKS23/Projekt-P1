# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:41:29 2023

@author: h4sor
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




D_HP = pd.read_csv('Highpass_filter.csv', sep = ',', encoding='unicode_escape',on_bad_lines='skip',skiprows=20)
D_LP = pd.read_csv('Lowpass_filter.csv', sep = ',' ,encoding='unicode_escape',on_bad_lines='skip',skiprows=20)

L_Freq, L_magni, L_magni_o, L_phase = D_LP["Frequency (Hz)"].to_numpy(),D_LP["Channel 1 Magnitude (dB)"].to_numpy(), D_LP["Channel 2 Magnitude (dB)"].to_numpy(), D_LP["Channel 2 Phase (deg)"].to_numpy()
H_Freq, H_magni, H_magni_o, H_phase = D_HP["Frequency (Hz)"].to_numpy(),D_HP["Channel 1 Magnitude (dB)"].to_numpy(), D_HP["Channel 2 Magnitude (dB)"].to_numpy(), D_HP["Channel 2 Phase (deg)"].to_numpy()

L_phase = L_phase *(np.pi/180)
H_phase =H_phase *(np.pi/180)

R = 1000
C = 220 * 10**-9

Cutoff = 1/(2*np.pi*R*C)

tick_locations_HP = np.arange(0, np.pi/2 + np.pi/8, np.pi/8)
tick_labels_HP = ['0'] + ['$\pi$/8','$\pi$/4','3$\pi$/8','$\pi$/2']

tick_locations = np.arange(-0, -np.pi/2 + -np.pi/8, -np.pi/8)
tick_labels = ['0'] + ['-$\pi$/8','-$\pi$/4','-3$\pi$/8','-$\pi$/2']

def mag_low(frequency):
    return 20 * np.log10(1 / (np.sqrt(1 + (R * C * frequency * 2 * np.pi) ** 2)))


def mag_High(frequency):
    return 20 * np.log10(R * C * frequency*2*np.pi / (np.sqrt(1 + (R * C * frequency *2* np.pi) ** 2)))

def phasor_low(f):
    return -np.degrees(np.arctan(R*C*f*2*np.pi)) * (np.pi/180)
    
def phasor_high(f):
    return np.degrees(np.arctan(1/(R*C*f*2*np.pi)))* (np.pi/180)



def plot_M_LP_BD():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Lowpass")
    plt.plot(L_Freq, L_magni_o,label = "Data")
    plt.plot(L_Freq,mag_low(L_Freq), label = "Theoretical",linestyle = "dashed")
    plt.plot([Cutoff,Cutoff],[-120,120],"g-", linestyle="dashed", label = "Cutoff frequency")
    #plt.plot([0,1000000],[-3,-3],"r-", linestyle="dashed", label = "-3 dB")
    plt.ylim(-45,0.5)
    #plt.xlim(40,100000)
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(which = "both")
    plt.legend()

def plot_M_HP_BD():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Highpass")
    plt.plot(H_Freq, H_magni_o,label = "Data")
    plt.plot(H_Freq,mag_High(H_Freq), linestyle = "dashed", label = "Theoretical")
    plt.plot([Cutoff,Cutoff],[-30,4],"o-", linestyle="dashed", label = "Cutoff frequency")
    plt.ylim(-25,0.2)
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(which = "both")
    plt.legend()


def plot_P_LP_BD():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Lowpass")    
    plt.plot(L_Freq, L_phase,label = "Data")
    plt.plot(L_Freq,phasor_low(L_Freq), label = "Theoretical",linestyle = "dashed")
    #plt.plot([0,1000000],[-45,-45],"r-",linestyle = "dashed", label = "-45 degrees")
    plt.plot([Cutoff,Cutoff],[-120,120],"g-", linestyle="dashed", label = "Cutoff frequency")
    plt.ylim(-(np.pi/2),0)
    #plt.xlim(40,100000)
    plt.yticks(tick_locations, tick_labels)
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (rad)")
    plt.grid(which = "both")
    plt.legend()

def plot_P_HP_BD():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Highpass")
    plt.plot(H_Freq, H_phase, label = "Data")
    plt.plot(H_Freq,phasor_high(H_Freq), linestyle = "dashed", label = "Theoretical")
    plt.plot([Cutoff,Cutoff],[-30,120],"g-", linestyle="dashed", label = "Cutoff frequency")
    #plt.plot([0,1000000],[np.pi/4,np.pi/4],"r-", linestyle="dashed", label = "$\pi / 4$")
    plt.ylim(-0.05,np.pi/2)
    plt.xlim(40,110000)
    plt.yticks(tick_locations_HP, tick_labels_HP)
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (rad)")
    plt.grid(which = "both")
    plt.legend()

def plot_PD_HP():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Highpass")
    plt.plot(H_Freq, -(phasor_high(H_Freq)-H_phase),"r-" , label = "Deviation")
    plt.plot([Cutoff,Cutoff],[-30,120],"g-", linestyle="dashed", label = "Cutoff frequency")
    plt.ylim(-0.0,0.03)
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (rad)")
    plt.grid(which = "both")
    plt.legend()
    

def plot_MD_HP():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Highpass")
    plt.plot(H_Freq, -(mag_High(H_Freq)-H_magni_o),"r-" , label = "Deviation")
    plt.plot([Cutoff,Cutoff],[-30,120],"g-", linestyle="dashed", label = "Cutoff frequency")
    plt.ylim(-0.5,0.1)
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(which = "both")
    plt.legend()

def plot_PD_LP():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Low pass")
    plt.plot(L_Freq, -(phasor_low(L_Freq)-L_phase),"r-" , label = "Deviation")
    plt.plot([Cutoff,Cutoff],[-30,120],"g-", linestyle="dashed", label = "Cutoff frequency")
    plt.ylim(-0,0.04)
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (rad)")
    plt.grid(which = "both")
    plt.legend()
    

def plot_MD_LP():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Low pass")
    plt.plot(L_Freq, -(mag_low(L_Freq)-L_magni_o),"r-" , label = "Deviation")
    plt.plot([Cutoff,Cutoff],[-30,120],"g-", linestyle="dashed", label = "Cutoff frequency")
    plt.ylim(-0.1,1)
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(which = "both")
    plt.legend()

def plot_RPD_HP():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Highpass")
    plt.plot(H_Freq, abs(100*(phasor_high(H_Freq)-H_phase))/phasor_high(H_Freq),"r-" , label = "Deviation")
    plt.plot([Cutoff,Cutoff],[-30,120],"g-", linestyle="dashed", label = "Cutoff frequency")
    plt.ylim(-0,10)
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative Deviation (%)")
    plt.grid(which = "both")
    plt.legend()
    

def plot_RMD_HP():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Highpass")
    plt.plot(H_Freq, abs(100*(mag_High(H_Freq)-H_magni_o)/mag_High(H_Freq)),"r-" , label = "Deviation")
    plt.plot([Cutoff,Cutoff],[-30,20000],"g-", linestyle="dashed", label = "Cutoff frequency")
    plt.xscale("log")
    plt.yscale("log")
    plt.ylim(-0,10000)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative Deviation (%)")
    plt.grid(which = "both")
    plt.legend()

def plot_RPD_LP():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Low pass")
    plt.plot(L_Freq, abs(100*-(phasor_low(L_Freq)-L_phase)/phasor_low(L_Freq)),"r-" , label = "Deviation")
    plt.plot([Cutoff,Cutoff],[-30,120],"g-", linestyle="dashed", label = "Cutoff frequency")
    plt.ylim(-0,6)
    plt.xscale("log")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative Deviation (%)")
    plt.grid(which = "both")
    plt.legend()
    

def plot_RMD_LP():
    plt.figure(dpi=1200)
    plt.title("Bode Plot - Low pass")
    plt.plot(L_Freq, abs(100*-(mag_low(L_Freq)-L_magni_o)/mag_low(L_Freq)),"r-" , label = "Deviation")
    plt.plot([Cutoff,Cutoff],[-30,1000],"g-", linestyle="dashed", label = "Cutoff frequency")
    plt.xscale("log")
    plt.ylim(-0,20)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative Deviation (%)")
    plt.grid(which = "both")
    plt.legend()

#for i in range(len(L_magni_o)):
 #   if L_magni_o[i] >-4 and L_magni_o[i]<-2:
  #      print(L_magni_o[i],L_Freq[i])

#for i in range(len(L_phase)):
 #   if L_phase[i]<-np.pi/8  and L_phase[i]>-3*np.pi/8:
  #      print(L_phase[i], L_Freq[i])
        
#for i in range(len(H_magni_o)):
  #  if H_magni_o[i] >-4 and H_magni_o[i]<-2:
        #print(H_magni_o[i],H_Freq[i])

#print("ny")
#for i in range(len(H_phase)):
    #if H_phase[i]>np.pi/8  and H_phase[i]<3*np.pi/8:
       #print(H_phase[i], H_Freq[i])
