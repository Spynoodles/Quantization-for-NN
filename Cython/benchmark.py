
import timeit
import torch
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# print("Using device:", device)

# torch.set_default_tensor_type(torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor)

data=torch.randn(40,40,100,7).tolist()
print("DONE")
cython_time = timeit.timeit("Quantise_Cython.SublistIterator(data)", setup="import Quantise_Cython; data = {}".format(data), number=10)

# Time pure Python implementation
python_time = timeit.timeit("quantise_py(data)", setup="from my_python_module import quantise_py; data = {}".format(data), number=10)
print("Cython Time:", cython_time)
print("Python Time:", python_time)
print("Performance difference (Cython vs Python):", python_time / cython_time)


#__init__.py