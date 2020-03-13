Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> def gradient_descent(x,y):
    m_c = b_c = 0
    n = len(x)
    l_r = 0.08
    plt.scatter(x,y,color='red',marker='+',linewidth='5')
    for i in range (10):
        y_p = m_c * x + b_c
        plt.plot(x,y_p,color='green')
        plt.show()
        cost = (1/n) * sum([val**2 for val in (y-y_p)])
        md = -(2/n)*sum(x*(y-y_p))
        bd = -(2/n)*sum(y-y_p)
        m_c = m_c - l_r*md
        b_c = b_c - l_r*bd
        print(f"m={m_c}, b={b_c},cost={cost}")

        
>>> x = np.array([1,2,3,4])
>>> y = np.array([5,7,9,11])
>>> gradient_descent(x,y)
m=3.6, b=1.28,cost=69.0
m=2.3680000000000003, b=0.9152,cost=8.398399999999999
m=2.7603199999999997, b=1.1015679999999999,cost=1.5260390399999975
m=2.6073088, b=1.1011891200000001,cost=0.7226137354239996
m=2.638062592, b=1.1620753408,cost=0.6058398123884546
m=2.60755734528, b=1.200918249472,cost=0.5678412279692813
m=2.5981212311551998, b=1.24574839144448,cost=0.5399129421480667
m=2.582076397191168, b=1.2871801563512832,cost=0.5142406004831324
m=2.568712658021253, b=1.3284007724586107,cost=0.48988878990676865
m=2.554897159412305, b=1.3683715856567316,cost=0.46670143376227535
>>> 