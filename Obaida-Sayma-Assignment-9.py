#!/usr/bin/python3

import matplotlib # Importing the matplotlib library
print("Matplotlib version: {}".format(matplotlib.__version__)) # Printing the version of matplotlib

#line graph
import matplotlib.pyplot as plt # Importing the pyplot module from matplotlib and calling it 'plt'
plt.plot([0, 2, 4, 6, 8, 10], [0,20, 40, 60, 80, 100]) # Plotting a line graph
plt.show()
plt.savefig('pyplot.png') # Saving the plot as a PNG file


#multiple points
plt.plot([1,1,10,10], [1,100, 100,1]) # Plotting multiple points
plt.show()
plt.savefig('multi_points.png')

import numpy as np # Importing the numpy library and calling it 'np'

xpoints = np.array([1, 3, 5, 8]) # Creating a numpy array for x points
ypoints = np.array([1, 100, 20, 100]) # Creating a numpy array for y points

#markers
plt.plot(xpoints, ypoints, marker = 'o') # Plotting the points with a marker 'o' (circle)
plt.show()
plt.savefig('markers.png')


#markers with designed line
plt.plot(xpoints, ypoints, linestyle = 'dotted', marker = 'o', color = 'r') # Plotting the points with a dotted line, marker 'o' (circle), and red color
plt.show()
plt.savefig('markers.png')

x = np.array([2, 4, 6, 8, 10]) # Creating a numpy array for x points
y = np.array([20, 40, 60, 80, 100]) # Creating a numpy array for y points


#Labels
plt.plot(x,y) # Plotting the points
plt.xlabel('Year') # Adding label for x-axis
plt.ylabel('Rise') # Adding label for y-axis
plt.show()
plt.savefig('Labels.png')


#Grid
plt.plot(x,y) # Plotting the points
plt.xlabel('Year') # Adding label for x-axis
plt.ylabel('Rise') # Adding label for y-axis
plt.title('Apple Watch Data') # Adding a title to the plot
plt.grid()
plt.show() 
plt.savefig('Grid.png')

#subplot
x = np.array([1, 2, 3, 4])
y = np.array([1.0, 2.0, 3.0, 4.0])

plt.subplot(1, 2, 1)
plt.plot(x,y)

x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
plt.savefig('Subplot.png')

#Color
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red", "green", "blue", "yellow", "pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()
plt.savefig('Color.png')

#Bar graph
x = np.array(["Python", "Ruby", "Java", "C++"])
y = np.array([10, 9, 8, 7])

plt.bar(x,y) #plotting a bar graph with x as the categories and y as the values
plt.show()
plt.savefig('Bar.png')

#Histogram
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 
plt.savefig('Histogram.png')

#Pie chart

y = np.array([35, 25, 25, 15]) # Creating a numpy array for the values of the pie chart
mylabels = ["Python", "Ruby", "C++", "Java"] 
myexplode = [0.2, 0, 0, 0] #1st slice will be exploded

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()
plt.savefig('Pie.png')