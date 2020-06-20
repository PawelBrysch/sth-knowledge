import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(100, 2), columns=['X', 'Y'])
df.plot(kind='scatter', x='X', y='Y', color='r')
