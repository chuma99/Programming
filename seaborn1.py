#On my honor, I have neither given or received unauthorized aid.
#1-16-19
#For this project, I explored and experimented with some of the 
#capabilities and functionalities of Seaborn, a data visualization package.

#started by importing some neccesary packages
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#import numpy as np
#from pandas import Series, DataFrame
#from pandas.tools.plotting import scatter matrix

from pylab import rcParama


#rcParama['figurerfigsize'] = 5, 4
sns.set_style('whitegrid')

df = pd.read_csv('elements.csv', index_col=0)
df.head()
#cars = pd.read_csv(address)
#cars.columns = []
#cars.index = cars.car_names