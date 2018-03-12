"""
import numpy as np
a = np.array([1, 2, 5, 6, 8, 9])
for i in a:
    print(i)
b = a.reshape((3, 2))

print(b.ndim)

print(a.ndim)

"""
import numpy
import timeit

normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))', number=10000)
naive_np_sec = timeit.timeit('sum(na*na)', setup="import numpy as np; na=np.arange(1000)", number=10000)
good_np_sec = timeit.timeit('na.dot(na)', setup="import numpy as np;na=np.arange(1000)", number=10000)
print("normal python: %f sec" % normal_py_sec)
print("Naive Numpy: %f" % naive_np_sec)
print("Good Numpy: %f" % good_np_sec)
