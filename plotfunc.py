import matplotlib.pyplot as plt

month=[1,2,3,4]
sales=[1200,1500,1000,1800]
plt.plot(month,sales,color="green",linestyle='--',linewidth=2,marker="o",label='2025 sales data')
plt.xlabel("Month")
plt.ylabel("sales")
plt.title("Monthly Sales Date Report")
plt.legend(loc="upper left",fontsize=12)
plt.grid(color='gray', linestyle=":",linewidth=1)
plt.xtick([1,2,3,4],['m1','m2','m3','m4'])

plt.show()










