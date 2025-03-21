import numpy as np;

""" arr=np.array([12,20,30,40,50,60])
print(arr)
print(type(arr)) """

""" brr=np.arange(0,21,3)
print(brr) """

""" crr,step_s=np.linspace(0,20,10,endpoint=False,retstep=True)
print(crr)
print(crr.size)
print('the step size is '+str(step_s))#計算出該陣列每次移動的距離 """
""" drr=np.random.rand(3,4)
print(drr)#生成隨機0~1的n*n陣列 """
""" err=np.zeros((2,3))
print(err)#生成0的n*n陣列
frr=np.ones((3,2))
print(frr)#生成1的n*n陣列 """
""" grr=[[1,2,3],[4,5,6]]
ones=np.ones_like(grr)#將原始陣列n*n複製一個全部為1的n*n陣列
print(ones) """
""" emp=np.empty((2,2))
print(emp)#隨機分配記憶體位置以及隨機數值 """
""" grr=np.array([[10,20,30],[40,50,60]],dtype=np.int64)
empp=np.empty_like(grr)#複製一個隨機分配n*n數值的陣列
print(empp) """
""" ful=np.full((4,4),'*')
print(ful)#生成一個n*n指定數值或字串的陣列 """