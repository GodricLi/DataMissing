# _*_ coding=utf-8 _*_

import pandas as pd

"""数据缺失的处理"""
data1 = pd.Series([12, 23, 10], index=['a', 'b', 'c'])
data2 = pd.Series([11, 22, 33], index=['d', 'c', 'a'])
data = data1 + data2

# 　使用NaN (not a number)来表示缺失数据，相当于np.nan,None也会当作NaN处理
"""-----处理方法-----"""
# dropna() 删除掉存在值为NaN的行，整行删除
res = data.dropna()
print(res)

# fillna()填充缺失数据,传入用来填充的参数
res1 = data.fillna(0)
print(res1)

# isnull()返回bool数组，缺失值对应True
res2 = data.isnull()
print(res2)

# notnull()返回bool数组，缺失值对应为False
res3 = data.notnull()
print(res3)

# 过滤缺失数据可以使用data.dropna()或者data[data.notnull()]
res4 = data[data.notnull()]
print(res4)
