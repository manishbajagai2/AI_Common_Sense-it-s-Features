from matplotlib import pyplot as plt
plt.style.use("Solarize_Light2")
x=['0','1 (notsatisfied)','2 (good)',' 3 (verygood)','4 (excellent)','5 (outstanding)']
y= [0,3,5,4,1,2]
plt.plot(x,y)
plt.xlabel('Ratings ------>')
plt.ylabel('No. of Question Asked ----->')
plt.title('Efficiency of response though feedback ')

plt.show()
