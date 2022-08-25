import numpy as np
import h5py
from PyEMD import EEMD
import matplotlib.pyplot as plt
from scipy import signal
import multiprocessing
def eemd_p(case,data,index=0):
    t=np.linspace(0,5,625)
    EEG_size=data["EEG"].size
    bis_size=data["bis"].size
    EEG_index=index*625
    for n in range(index,bis_size):
        eemd = EEMD()

        # Say we want detect extrema using parabolic method
        emd = eemd.EMD
        emd.extrema_detection="parabol"
        try: 
            if EEG_index+625>EEG_size:
                break
            tEEG_data=data["EEG"][0,EEG_index:EEG_index+625]
            EEG_index+=625


            # Execute EEMD on S
            eIMFs = eemd.eemd(tEEG_data, t)
            if(eIMFs.size<4):
                continue
            f1, tt1, Sxx1 = signal.stft(eIMFs[0],fs=125,nperseg=16,scaling="spectrum",nfft=256)
            f2, tt2, Sxx2 = signal.stft(eIMFs[1],fs=125,nperseg=16,scaling="spectrum",nfft=256)
            f3, tt3, Sxx3 = signal.stft(eIMFs[2],fs=125,nperseg=16,scaling="spectrum",nfft=256)
            f4, tt4, Sxx4 = signal.stft(eIMFs[3],fs=125,nperseg=16,scaling="spectrum",nfft=256)
            tA=np.hstack((Sxx1,Sxx2))
            tB=np.hstack((Sxx3,Sxx4))
            tC=np.vstack((tB,tA))
            plt.pcolormesh(np.abs(tC))
            plt.axis('off')
            if data["bis"][0,n]<=40:
                plt.savefig("img/AD/%s-%d.png"%(case,n), bbox_inches="tight",pad_inches = 0)
            elif data["bis"][0,n]<=60:
                plt.savefig("img/AO/%s-%d.png"%(case,n), bbox_inches="tight",pad_inches = 0)
            else:
                plt.savefig("img/AL/%s-%d.png"%(case,n), bbox_inches="tight",pad_inches = 0)
            plt.close()
        except:
            print("%s %d error"%(case,n))
    print("%s finish"%(case))
names=["case3","case11","case15"]
indexs=[2617,2307,2226]
datas=[]
for name in names:
    data=h5py.File("data/%s.mat"%(name),"r")
    datas.append(data)
procs=[]
for i in range(np.size(names)):
    # print(name)
    proc = multiprocessing.Process(target=eemd_p, args=(names[i],datas[i],indexs[i]))
    procs.append(proc)
    proc.start()