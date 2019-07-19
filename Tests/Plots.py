import matplotlib.pyplot as plt
import numpy as np
import matplotlib

class Plotter():

    def plot_files(self, *args: str, **kwargs):

        sample_time = kwargs.get('period')

        for file in args:
            fh = open(file, 'r')
            positions = [line.split() for line in fh]

            curve = []
            curve2 = []

            key1 = kwargs.get('key')
            key2 = kwargs.get('key2')

            for x in positions:
                for y in range(len(x)):

                    if key1 and x[y] == key1:
                        curve.append(float(x[y+1]))
                    if key2 and x[y] == key2:
                        curve2.append(float(x[y + 1])*100/255)

            x = np.arange(0, (len(curve)) * sample_time-0.00000000000001, sample_time)

            fig, ax1 = plt.subplots()
            ax1.set_xlabel('Time [min]',fontsize = 20)

            if key1:
                y_1 = np.array(curve)
                ax1.plot(x,y_1,'b')
                ax1.set_ylabel('Temperature [°C]', fontsize = 20)
                ax1.yaxis.label.set_color('b')
                
            if key2:
                ax2 = ax1.twinx()
                y_2 = np.array(curve2)
                ax2.plot(x, y_2, 'r')
                ax2.set_ylabel('Control Action [%]', fontsize = 20)
                ax2.yaxis.label.set_color('r')

            fig.tight_layout()
            plt.title(file)

        plt.show()

files_list ={
    'file1' : 'Test 1 _4deg_defaultPID.txt',
    'file2' : 'Test 2 _4deg_autotunedPID.txt',
    'file3' : 'Test 3 _4deg _10 deg_15deg_6deg_1deg.txt',
    'file4' : 'Test 5_4deg_40deg syringe_fire screwdriver.txt',
    'file5' : 'Test_Syringe_4deg_5deg_10deg_15deg.txt',
    'file6' : 'PID_Autotuning_4deg.txt',
    'file7' : 'PID_Autotuning_15deg.txt',
    'file8' : 'PID_Autotuning_20deg.txt',
    'file9' : 'Test 4 _10deg_timeout.txt',
	'file10' : 'Test 6_Cool_and_Heating_15_30_37_4deg.txt'
}

if __name__ == "__main__":
    
    matplotlib.use("TkAgg")

    plot = Plotter()

    #plot.plot_files(files_list['file1'], files_list['file2'], files_list['file3'], files_list['file4']
     #               , files_list['file5'], key="Input", key2="Output", period=0.16 / 60)
	
    #plot.plot_files(files_list['file6'],files_list['file7'],files_list['file8'],files_list['file9'],
                    #key="T:", key2 = "@:", period = 1.8/60)
        
    plot.plot_files(files_list['file5'], key="Input", key2="Output", period=0.16 / 60)

	