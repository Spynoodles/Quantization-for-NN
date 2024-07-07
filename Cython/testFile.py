import Quantise_Cython
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print("Using device:", device)

torch.set_default_tensor_type(torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor)


import time

A = torch.randn(3,3,3)

print(A)
current=time.time()


B=(Quantise_Cython.QI(A.tolist()))


print(torch.tensor(B,dtype=torch.uint8))

print(torch.tensor(Quantise_Cython.DQI(B),dtype=torch.float32))


 

# Setup 
    # ->Reshape
    #Module
# Error 1D,2D,3D,4D
        # ->Small,Medium,Big
#Dtype 
        




"MAX SIZE [4,1280000]"