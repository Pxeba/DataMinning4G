import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum 
import os



class Plots(Enum):
    THROUGHTPUT_DISTANCE = 1
    THROUGHTPUT_SPEED = 2

class DataMinning4G:
    def start(self): 

        path = '\\'

        files = {}
        # r=root, d=directories, f = files
        currentRoot = '-1'
        for r, d, f in os.walk(".", topdown=False):
            if 'git' in r:
                continue
            r  = r[2:]
            if currentRoot != r:
                currentRoot = r
                files[r] = []
            for file in f:
                if '.csv' in file:
                    files[r].append(file) 

        print('f {} d {} r {}\n'.format(f,d,r))

            
        # data = pd.read_csv('A_2017.11.24_14.34.43.csv', na_values=['-']).dropna()
        # data['State'] = data['State'].replace('D', 1)
        # data['State'] = data['State'].replace('I', 0)
        # #context
        # speed_series = data['Speed']
        # distance_series = data['ServingCell_Distance']
        # #channel
        # cqi_series = data['CQI']
        # #coverage
        # rsrp_series = data['RSRP']
        # rsrq_series = data['RSRQ']
        # snr_series = data['SNR']
        # rssi_series = data['RSSI']
        # #throughtput    
        # dl_series = data['DL_bitrate']
        # ul_series = data['UL_bitrate']

        # print('speed: {}, distance: {}, cqi: {}, rsrp: {}, rsrq: {}, snr: {}, rssi: {}, dl: {}, ul: {} '.format(speed_series.mean(skipna = True),distance_series.mean(skipna = True),cqi_series.mean(skipna = True)
        # ,rsrp_series.mean(skipna = True),rsrq_series.mean(skipna = True),snr_series.mean(skipna = True),rssi_series.mean(skipna = True),dl_series.mean(skipna = True),ul_series.mean(skipna = True)))

        # while(True):
        #     self.getPlot(data)
        #     plt.show()

    def getPlot(self, data):
        #get user input
        for idx, col in enumerate(data.columns.values):
            print('{}: {}\n'.format(idx,col))
        col1 = int(input('Selecione 2 colunas para vizualização:'))
        for idx, col in enumerate(data.columns.values):
            print('{}: {}\n'.format(idx,col))
        col2 = int(input('Selecione 1 coluna para vizualização:'))

        order_col_index = int(input('qual coluna será ordenada?(1 ou 2)'))
        colx = col1 if order_col_index == 1 else col2
        coly = col1 if order_col_index == 2 else col2

        data = data.sort_values(data.columns.values[colx])
        data.plot(x=data.columns.values[colx], y=data.columns.values[coly])

if __name__ == "__main__":
    m = DataMinning4G()
    m.start()

