import matplotlib.pyplot as plt
regions=['North','South','West','East']
revenue=[3400,3500,1500,1000]
plt.pie(revenue,labels=regions,autopct='%1.1f%%',colors=['gold','skyblue','lightgreen','coral'])


plt.show()