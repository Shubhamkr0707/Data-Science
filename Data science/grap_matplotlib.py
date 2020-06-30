# import pandas as pd 
# import numpy as np 
# import matplotlib.pyplot as plt
# # %matplotlib inline
# x=[1,2,3,4,5,6,7]
# y=[50,51,52,48,47,49,46]
# plt.xlabel("Day")
# plt.ylabel("Temperature")
# plt.title("Weather")
# plt.plot(x,y,color="red",linewidth=3,linestyle='dashdot')
# plt.show()
# print("successfull")


# Next tutorial
# import matplotlib.pyplot as plt
# x=[1,2,3,4,5,6,7]
# y=[50,51,52,48,47,49,46]
# plt.plot(x,y)
# plt.show()

# Bar Graph

import matplotlib.pyplot as plt
import numpy as np
company=["Google","Yahgoo","Fb","Msft"]
revenue=[12000,1300,1200,1500]
profit=[400,500,600,1000]
yposition=np.arange(len(company))
plt.xlabel("comapnay name")
plt.ylabel("Revenue billoin")
plt.title("Us Revenue")

plt.bar(yposition-0.2,revenue,width=0.4,label="Revenue")
plt.bar(yposition+0.2,profit,width=0.4,label="Profit")
plt.legend()
plt.show()


            #   Histogram Graph
