
# def starter_page():
#     window = Tk()
#     window.title("Earthquake Prediction App")
#     window.geometry("800x800")
#     window.configure(background='#CCCCFF')
#     vis = visualiztion
#     dtable = visualiztion.data
#     for i in range(10):
#         Frame(window, width=20, height=20, background='#CCCCFF').grid(row=0, column=i)
#         # Frame(dt, width=50, height=50).grid(row=20, column=i+5)
#     for j in range(10):
#         Frame(window, width=20, height=20, background='#CCCCFF').grid(column=0, row=j)
#         # Frame(dt, width=50, height=50).grid(row=j+5, column=20)
#     header = Label(window, text="Significant Earthquake forecaster, 1965-2016")
#     header.grid(row=0, column=4)
#     header.configure(background='#CCCCFF')
#     table = Label(window, text=dtable, anchor="center", justify="left")
#     image_names()
#     table.grid(row=4, column=6)
#
#     return window.mainloop()
#
#
# # App will  hold all the screen with in self
# # wanted to put window inside of App() like this App(window) but python sayed that not how this works
# class App(Tk):
#     def __init__(self, *args, **kwargs):
#         Tk.__init__(self, *args, **kwargs)
#
#         container = Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         # initializing frames to an empty array
#         self.frames = {}
#
#         for F in (StartPage, Page1, Page2):
#             frame = F(container, self)
#             # initializing frame of that object from
#             # startpage, page1, page2 respectively with
#             # for loop
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#             # frame.pack(fill='both')
#         self.show_frame(StartPage)
#
#         # to display the current frame passed as
#         # parameter
#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()
#
#
#     # button that displays the plot
# #StartPage will hold the splash page intro to the purpose of the app and a start button
# class StartPage(Frame):
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#
#         # label of frame Layout 2
#         label = ttk.Label(self, text="Startpage")
#
#         # putting the grid in its place by using
#         # grid
#         label.grid(row=0, column=4, padx=10, pady=10)
#         # label.pack(side='left')
#         button1 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(Page1))
#
#         # putting the button in its place by
#         # using grid
#         button1.grid(row=1, column=1, padx=10, pady=10)
#         # button1.pack(side='left')
#         # plot_button = Button(master=self, command=plot, height=1, width=10, text="Plot results")
#         # plot_button.pack()
#
#         # button to show frame 2 with text layout2
#         button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(Page2))
#
#         # putting the button in its place by
#         # using grid
#         button2.grid(row=2, column=1, padx=10, pady=10)
#         # button2.pack(side='left')
#         # pbt=ttk.Button(self, text="Plot", command=lambda: controller.show_frame(self))
#         # pbt= Button(self,command=plot,height=1, width=10, text="Plot results")
#         # pbt.pack()
#
# #Page 1 should hold the earthquake map and the heatmap
# class Page1(Frame):
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Page 1")
#         label.grid(row=0, column=4, padx=10, pady=10)
#         # label.pack(side='left')
#         plot()
#         # button to show frame 2 with text
#         # layout2
#         button1 = ttk.Button(self, text="StartPage", command=lambda: controller.show_frame(StartPage))
#
#         # putting the button in its place
#         # by using grid
#         button1.grid(row=1, column=1, padx=10, pady=10)
#         # button1.pack(side='left')
#         # button to show frame 2 with text
#         # layout2
#         button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(Page2))
#
#         # putting the button in its place by
#         # using grid
#         button2.grid(row=2, column=1, padx=10, pady=10)
#         # button2.pack(side='left')
#
# # third Tk frame page2 This Page should hold the results
# class Page2(Frame):
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Page 2")
#         label.grid(row=0, column=4, padx=10, pady=10)
#         # label.pack(side='left')
#         # button to show frame 2 with text
#         # layout2
#         button1 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(Page1))
#
#         # putting the button in its place by
#         # using grid
#         button1.grid(row=1, column=1, padx=10, pady=10)
#         # button1.pack(side='left')
#         # button to show frame 3 with text
#         # layout3
#         button2 = ttk.Button(self, text="Startpage", command=lambda: controller.show_frame(StartPage))
#         button2.grid(row=2, column=1, padx=10, pady=10)
#         # button2.pack(side='left')
#
#
# def plot():
#     # the figure that will contain the plot
#     fig = Figure(figsize=(19, 19))
#     # adding the subplot
#     plot1 = fig.add_subplot(1, 2, 1)
#     # # plotting the graph Loss Over time
#     plot1.plot(epochs_range, train_loss, label="Training Loss")
#     plot1.plot(epochs_range, val_loss, label="Validation Loss")
#     plot1.legend()
#     fig.suptitle("Loss Over Time " + "        " + " AUC Over Time", )
#     #plot 2 AUC OverTime
#     plot2 = fig.add_subplot(1, 2, 2)
#     plot2.plot(epochs_range, train_auc, label="Training AUC")
#     plot2.plot(epochs_range, val_auc, label="Validation AUC")
#     plot2.legend()
#
#     # creating the Tkinter canvas
#     # containing the Matplotlib figure
#     canvas = FigureCanvasTkAgg(fig, master=window)
#     canvas.draw()
#     # placing the canvas on the Tkinter Tk
#     canvas.get_tk_widget().pack(fill = 'both')
#     #
#     # creating the Matplotlib toolbar
#     toolbar = NavigationToolbar2Tk(canvas, window)
#     toolbar.update()
#     # placing the toolbar on the Tkinter Tk
#     canvas.get_tk_widget().pack()
#
# # This is the buttion that activates the plots both plot1 and plot2
# plot_button = Button(master=window, command=plot, height=1, width=10, text="Plot results")
# #this activates the button on the screen
# plot_button.pack()
# #this does the mainloop Amy says it just keeps it runing has nothing to do with main
# window.mainloop()
# #turns App into varable app
# app = App()
# #mainloops  app
# app.mainloop()
# #eveaultes the ai test results
# model.evaluate(X_test, y_test)
# #prints the ytest amount
# len(y_test)

#why does windows = list
# windows = []
#for a count of 2
#num of windows
# hide old window
# NUM_WINDOWS = 2
# for w in range (NUM_WINDOWS):
#     #windows adds Tk()
#     windows.append(Tk())
# #what does root do
#root window create new window

# results prints Greeting maybe add plot here
#     def eq_map(self):
#         fig = Figure(figsize=(19, 19))
#         mapplot = fig.add_subplot(1,2,1)
#         mapplot.plot(hotmap,label="Earthquake map")
#         mapplot.legend()
#         fig.suptitle("Map of recorded Earthquake with a magnitude of 5 or greater then 5")
#         fig =Figure(figsize=(19,19))
#         canvas = FigureCanvasTkAgg(fig, master=root)
#         canvas.draw()
#         canvas.get_tk_widget().pack(fill='both')
#         toolbar = NavigationToolbar2Tk(canvas, root)
#         toolbar.update()
#         canvas.get_tk_widget().pack()
# figi = matplotlib.image.AxesImage(im)
# figi.set_extent(self, extent=(4,5,6,7))
# ploti =fig.images.append(figi)
# pi =ploti[0]
# fig.draw(pi)


# results prints Greeting maybe add plot here
#     def eq_map(self):
#         fig = Figure(figsize=(19, 19))
#         mapplot = fig.add_subplot(1,2,1)
#         mapplot.plot(hotmap,label="Earthquake map")
#         mapplot.legend()
#         fig.suptitle("Map of recorded Earthquake with a magnitude of 5 or greater then 5")
#         fig =Figure(figsize=(19,19))
#         canvas = FigureCanvasTkAgg(fig, master=root)
#         canvas.draw()
#         canvas.get_tk_widget().pack(fill='both')
#         toolbar = NavigationToolbar2Tk(canvas, root)
#         toolbar.update()
#         canvas.get_tk_widget().pack()
# figi = matplotlib.image.AxesImage(im)
# figi.set_extent(self, extent=(4,5,6,7))
# ploti =fig.images.append(figi)
# pi =ploti[0]
# fig.draw(pi)

# cursor = mplcursors.cursor(plot0, hover=True)
# @cursor.connect("add")
# def on_add(sel):
#     i, j = sel.target.index
#     sel.annotation.set_text(plot0[i, j])

#
# numeric_columns.remove('Status')
# scaler = StandardScaler()
# plt.figure(figsize=(18, 10))
# standardized_df = pd.DataFrame(scaler.fit_transform(data[numeric_columns].copy()), columns=numeric_columns)
# for column in numeric_columns:
#     sns.kdeplot(standardized_df[column], shade=True)
# plt.xlim(-3, 3)
# plt.show()

# hmarray = np.array(standardized_df)
# print("hmarray ")
# print(hmarray)

# hmdata =np.array(data[numeric_columns].copy())
# print("hmdata ")
# print(hmdata)
#
# hmnumc =np.array(numeric_columns)
# print("hmnumc ")
# print(hmnumc)
#
# hmary = np.array([])
# np.resize(hmary, (12, 12))
# print("hmary ")
# print(hmary)
#
# arr = np.arange(144).reshape(12, 12)
# print("\n\n arr : \n", arr)
# print("shape : ", arr.shape)
#     np.append(hmarray, column, axis=1)
# print("\n\n hmarray after insert :", hmarray)
# print("hmarray after insert shape :", hmarray.shape)
    # hmary.insert(column)
    # hmarray.append(column, axis=0)
# im = Image.open('images/heatmap.png')

# fig = plt.figure(figsize=(12,10))
        # plot0 = fig.add_subplot()
        # plot0 = plot0.imshow(corr, cmap="Blues", interpolation='nearest', vmin=-1.0, vmax=1.0)
        # cb = fig.colorbar(plot0)# plot0.legend()
# y3 = np.random.rand(10)



# self.close_button = Button(window, text="Close", command=window.quit)
# self.close_button.pack()

#
# def heatmap(self):
#     fig, (ax) = plt.subplots(figsize=(12, 10))
#     ax = sns.heatmap(corr, ax=ax, annot=True, vmin=-1.0, vmax=1.0)
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas.draw()
#     canvas.get_tk_widget().pack()
#     toolbar = NavigationToolbar2Tk(canvas, root)
#     toolbar.update()
#     canvas.get_tk_widget().pack()
#
# def results(self):
#     fig = plt.figure(figsize=(12, 12))
#     plot1 = fig.add_subplot(1, 2, 1)
#     plot1.plot(epochs_range, train_loss, label="Training Loss")
#     plot1.plot(epochs_range, val_loss, label="Validation Loss")
#     plot1.legend()
#     fig.suptitle("Loss Over Time " + "        " + " AUC Over Time", )
#     plot2 = fig.add_subplot(1, 2, 2)
#     plot2.plot(epochs_range, train_auc, label="Training AUC")
#     plot2.plot(epochs_range, val_auc, label="Validation AUC")
#     plot2.legend()
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas.draw()
#     canvas.get_tk_widget().pack(side='right')
#     toolbar = NavigationToolbar2Tk(canvas, root)
#     toolbar.update()
#     canvas.get_tk_widget().pack()

# def everyplots(self):
#     fig, (ax) = plt.subplots(2, 2, figsize=(18, 10) )
#     fig.suptitle('Earthquake Graphs')
#     ax[0,0].plot(epochs_range, train_loss, label="Training Loss")
#     ax[0,0].plot(epochs_range, val_loss, label="Validation Loss")
#     ax[0,0].set_title('Loss Over Time ')
#     ax[0,0].legend()
#
#     ax[0,1].plot(epochs_range, train_auc, label="Training AUC")
#     ax[0,1].plot(epochs_range, val_auc, label="Validation AUC")
#     ax[0,1].set_title(' AUC Over Time')
#     ax[0, 1].legend()
#
#     ax[1,0] = sns.heatmap(corr, ax=ax[1,0], annot=True, vmin=-1.0, vmax=1.0, linewidths=1)
#     ax[1, 0].set_title(' Heatmap')
#
#     for column in numeric_columns:
#         ax[1,1] = sns.kdeplot(standardized_df[column], ax=ax[1,1], shade=True)
#     ax[1,1] = ax[1,1]
#     ax[1,1].set_title(' Standardized Data')
#     fig.delaxes(ax[1,1])
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas.draw()
#     canvas.get_tk_widget().pack()
#     toolbar = NavigationToolbar2Tk(canvas, root)
#     toolbar.update()
#     canvas.get_tk_widget().pack()


# canvus = Canvas(
#     pane,
#     width=900,
#     height=900,
#     scrollregion=(0, 0, 900, 900)
# )
# vsb = Scrollbar(pane, orient='vertical')
# vsb.pack(side='right', fill='y')
# vsb.config(command=canvus.yview)
# horibar = Scrollbar(pane, orient="horizontal")
# horibar.pack(side='bottom', fill='x')
# horibar.config(command=canvus.xview)
# canvus.config(width=900, height=900)
# canvus.config(xscrollcommand=horibar.set, yscrollcommand=vsb.set)
# canvus.pack(expand=True, side='left', fill='both')


# self.results_button = Button(window, text="Test Results ", command=self.results)
# self.results_button.pack()
# self.heatmap_button = Button(window, text="HeatMap ", command=self.heatmap)
# self.heatmap_button.pack()


# plt.Figure(figsize=(19,19))
# plt.show()
# plt.xlim(-3, 3)


# def heatmap(self):
#     fig, (ax) = plt.subplots(figsize=(12, 10))
#     ax = sns.heatmap(corr, ax=ax, annot=True, vmin=-1.0, vmax=1.0)
#     ax.set_title(' Heatmap')
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas.draw()
#     canvas.get_tk_widget().pack(side='left')
#     toolbar = NavigationToolbar2Tk(canvas, root)
#     toolbar.update()
#     canvas.get_tk_widget().pack()
#
# def results(self):
#     fig = plt.figure(figsize=(12, 12))
#     plot1 = fig.add_subplot(1, 2, 1)
#     plot1.plot(epochs_range, train_loss, label="Training Loss")
#     plot1.plot(epochs_range, val_loss, label="Validation Loss")
#     plot1.set_title(' AUC Over Time')
#     plot1.legend()
#     fig.suptitle("Test Results", )
#     plot2 = fig.add_subplot(1, 2, 2)
#     plot2.plot(epochs_range, train_auc, label="Training AUC")
#     plot2.plot(epochs_range, val_auc, label="Validation AUC")
#     plot2.set_title(' AUC Over Time')
#     plot2.legend()
#     canvas = FigureCanvasTkAgg(fig, master=root)
#     canvas.draw()
#     canvas.get_tk_widget().pack(side='right')
#     toolbar = NavigationToolbar2Tk(canvas, root)
#     toolbar.update()
#     canvas.get_tk_widget().pack()


