# coding: utf-8

import pandas as pd
import matplotlib.pyplot
import numpy
import matplotlib.pyplot as pd
import numpy as np
df1=pd.DataFrame(np.random.randn(6,3), columns=['A','B','C'])
import matplotlib.pyplot as mt
df1=pd.DataFrame(np.random.randn(6,3), columns=['A','B','C'])
import pandas as pd
df1=pd.DataFrame(np.random.randn(6,3), columns=['A','B','C'])
df2=pd.DataFrame(np.random.randn(6,3), columns=['D','E','F'])
df=pd.concat([df1,df2])
df
df3=df1.copy()
df3
get_ipython().magic(u'save Test_panda.py 0-16')
df=pd.concat([df1,df2], axis=1)
df
get_ipython().magic(u'save Test_panda1 0-19')
