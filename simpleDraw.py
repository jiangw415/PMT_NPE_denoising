import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    energys = list(range(1,10,1))
    xyz = ['X','Y','Z','R']
    #all,<4000,>4000:xyzr
    bias = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
    res = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
    index = -1
    with open("qian_test_result.txt") as f:
        for lines in f.readlines():
            line = lines.strip("\n")
            data = line.split()
            #energys.append(int(data[0]))
            if len(data)==1:
                index += 1
                print(index)
            elif len(data)==9:
                for i in range(4):
                    #print("asd:%d"%index)
                    #print("len:%d"%len(data))
                    bias[index][i].append(float(data[2*i+1]))
                    res[index][i].append(float(data[2*i+2]))

    #for i in range(4):
    for i in [2]:
        plt.plot(energys,res[0][i],'o-',alpha=0.5,label='All')
        plt.plot(energys,res[1][i],'<-',alpha=0.5,label='<4000')
        plt.plot(energys,res[2][i],'>-',alpha=0.5,label='>4000')
        plt.legend()
        plt.xlabel("Kinetic Energy/MeV")
        plt.ylabel("rec "+xyz[i]+" resolution/mm")
        plt.ylim(0,120)
        plt.title('Resnet50\' '+xyz[i]+' resoluton@epoch11')
        plt.grid()
    # plt.ylim(60,120)
        plt.show()
    # plt.plot(energys,res_all[3],'o-',color='red',alpha=0.5,label='All')
    #plt.plot(energys,bias_all[3],'o-',color='red',alpha=0.5,label='All')
    #plt.legend()
    #plt.xlabel("Kinetic Energy/MeV")
    #plt.ylabel("rec resolution/mm")
    #plt.title('Resnet50\' resolution @epoch11')
    #plt.grid()
    # plt.ylim(60,120)
    #plt.show()

    if 0:#new fit resolution
        energys = list(range(1,10,1))
        resall = [118.1566,98.655538,88.434332,82.032668,77.376148,74.116051,71.380121,69.679176,68.683046]
        resin  = [119.011435,98.678001,87.615653,80.722099,75.979145,72.648594,69.797324,67.86798,66.718378]
        resout = [115.660873,98.555194,90.548095,85.581485,81.279641,78.286632,75.919639,74.901007,74.480925]
        plt.plot(energys,resall,'o-',color='red',alpha=0.5,label='All')
        plt.plot(energys,resin,'v-',color='green',alpha=0.5,label='<4000m3')
        plt.plot(energys,resout,'^-',color='blue',alpha=0.5,label='>4000m3')
        plt.legend()
        plt.xlabel("Kinetic Energy/MeV")
        plt.ylabel("rec X resolution/mm")
        plt.title('Resnet18 X resolution @epoch12')
        plt.grid()
        plt.ylim(60,120)
        plt.show()
    if 0:#new fit bias
        energys = list(range(1,10,1))
        resall = [-32.296322,-27.411021,-27.059749,-27.672647,-28.116301,-28.617048,-28.208538,-26.961323,-25.366253]
        resin  = [-34.098953,-27.819641,-27.778986,-28.031274,-27.664169,-27.570265,-26.979242,-25.81561,-24.736407]
        resout = [-27.703855,-26.345546,-25.209624,-26.842826,-29.566084,-31.856454,-32.043921,-30.61214,-27.555184]
        plt.plot(energys,resall,'o-',color='red',alpha=0.5,label='All')
        plt.plot(energys,resin,'v-',color='green',alpha=0.5,label='<4000m3')
        plt.plot(energys,resout,'^-',color='blue',alpha=0.5,label='>4000m3')
        plt.legend()
        plt.xlabel("Kinetic Energy/MeV")
        plt.ylabel("rec X bias/mm")
        plt.title('Resnet18 X bias @epoch12')
        plt.grid()
        plt.ylim(-40,0)
        plt.show()
