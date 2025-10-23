import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,15,25]
# plt.subplot(1,2,1)  #1row,2col,2nd suplot
# plt.plot(x,y)
# plt.title("Line chart")

# plt.subplot(1,2,2)
# plt.bar(x,y)
# plt.title("Bar Chart")

# # plt.tight_layout()
# plt.show()

# in proffesional way:
fig,ax=plt.subplots(1,2,figsize=(10,5))

ax[0].plot(x,y)
ax[0].set_title('Line Plot')

ax[1].bar(x,y,color='green')
ax[1].set_title("Bar Plot")
fig.suptitle("Comparision of Line and Bar Charts")
plt.tight_layout()
plt.show()