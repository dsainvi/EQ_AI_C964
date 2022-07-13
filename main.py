import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Label, Button, Frame
from DataControler.predictEarthquake import epochs_range, train_loss, val_loss, train_auc, val_auc, corr, numeric_columns, standardized_df
from Pages import slides

m = slides.m
root=Tk()


class MyFirstGUI:
    def __init__(self, window):
        self.window = window
        window.title(" Earthquake Forecasting AI ")
        window.geometry("900x900")
        window.protocol("WM_DELETE_WINDOW", window.quit)
        pane = Frame(window, background='white')
        pane.pack(fill='both')
        self.label = Label(pane, text=' Significant EarthQuakes from 1996-2016 ', background='snow', fg='snow')
        self.label.pack(fill='both', expand=True)
        self.eqmap_button = Button(pane, text="Earthquake Map ", command=self.eqmap, background='black', fg='gold')
        self.eqmap_button.pack(side='left', fill='both', expand=True)
        self.everyplot_button = Button(pane, text="TestResults, Heatmap, Graph", command=self.everyplot,background='gold', fg='black')
        self.everyplot_button.pack(side='left', fill='both', expand=True)

    def eqmap(self):
        fig = plt.figure(figsize=(18, 15))
        plt.title("Significant Earthquake Map")
        m.plot(slides.x, slides.y, "o", markersize=3, color='gold')
        m.drawcoastlines(color='aqua')
        m.fillcontinents(color='green', lake_color='aqua')
        m.drawmapboundary(fill_color='blue')
        m.drawcountries()
        m.drawcounties(facecolor='green')
        canvas = FigureCanvasTkAgg(fig, master=Tk())
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both')

    def everyplot(self):
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(19, 15))
        fig.suptitle('Test Results and Data Chats')
        ax1.plot(epochs_range, train_loss, label="Training Loss")
        ax1.plot(epochs_range, val_loss, label="Validation Loss")
        ax1.legend()
        ax1.set_title('Loss Over Time ')
        ax2.plot(epochs_range, train_auc, label="Training AUC")
        ax2.plot(epochs_range, val_auc, label="Validation AUC")
        ax2.legend()
        ax2.set_title(' AUC Over Time')
        ax2.sharex(ax1)
        ax3 = sns.heatmap(corr, ax=ax3, annot=True, vmin=-1.0, vmax=1.0)
        ax3.set_title('Heatmap')
        for column in numeric_columns:
            sns.kdeplot(standardized_df[column], ax=ax4, legend=True, shade=True, clip=(-3, 3))
        ax4.plot(0,3 )
        ax4.legend(numeric_columns)
        ax4.set_title(' Scale of Featured Variables')
        fig.subplots_adjust(bottom=0.2, hspace=0.2)
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both')

my_gui = MyFirstGUI(root)
root.mainloop()
