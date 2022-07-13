
#slide show
# from tkinter import Tk, Label, Button, StringVar, Canvas, PhotoImage, NW
#
#
# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("Earthquake AI")
#
#         self.label_text = StringVar()
#         self.label_text.set("This is our first GUI!")
#         self.label = Label(master, textvariable=self.label_text)
#         self.label.pack()
#
#         self.star_trek_image = PhotoImage(file="images/eq_map.png")
#         self.star_trek_label = Label(root, image=self.star_trek_image)
#         self.star_trek_label.pack()
#
#         self.greet_button = Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()
#
#         self.change_image_button = Button(master, text="Change Image", command=self.change_image)
#         self.image = "eq_map.png"
#         self.change_image_button.pack()
#
#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()
#
#     def greet(self):
#         self.label_text.set("Greetings!")
#         self.label.pack()
#
#     def change_image(self):
#
#         if self.image == "eq_map.png":
#             self.label_text.set("Earthquake Map")
#             self.star_trek_image=PhotoImage(file="images/eq_map.png")
#             self.image = "heat_map.png"
#         elif self.image == "heat_map.png":
#              self.label_text.set("Heat Map")
#              self.star_trek_image=PhotoImage(file="images/heat_map.png")
#              self.image = "scale.png"
#         elif self.image == "scale.png":
#              self.label_text.set("Scale and magnitude")
#              self.star_trek_image=PhotoImage(file="images/scale.png")
#              self.image = "results.png"
#         else:
#             self.label_text.set("Test results")
#             self.star_trek_image = PhotoImage(file="images/results.png")
#             self.image = "eq_map.png"
#         self.star_trek_label.configure(image=self.star_trek_image)
#
# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()
from mpl_toolkits.basemap import Basemap
from DataControler import datawizerd


data = datawizerd.datawiz()

#map
m = Basemap(projection='mill', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, lat_ts=20, resolution='c')
longitudes = data["Longitude"].tolist()
latitudes = data["Latitude"].tolist()
x, y = m(longitudes, latitudes)
#
# for column in numeric_columns:
#     sns.kdeplot(standardized_df[column], ax=ax4, legend=True, shade=True, clip=(-3, 3))
# #     axfour = sns.kdeplot(standardized_df[column], ax=ax4, legend=True, shade=True, clip=(-3, 3))
# #     predictEarthquake.eqfour = axfour