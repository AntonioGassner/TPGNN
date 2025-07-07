# import torch, sys
# print("sys.executable:", sys.executable)
# print("torch.__file__:", torch.__file__)
# print("CUDA available:", torch.cuda.is_available())
#
#
import torch
# print(torch.cuda.is_available())      # Expect True if GPU is visible
# print(torch.cuda.device_count())      # Number of GPUs PyTorch sees
# if torch.cuda.is_available():
#     print(torch.cuda.get_device_name(0))
#     print(torch.version.cuda)  # CUDA version PyTorch was compiled with
#
# import os
# print(os.environ.get('CUDA_VISIBLE_DEVICES'))  # Should be unset or list of valid GPU IDs
#

print(torch.version.cuda)   # Should be "11.3"
print(torch.__version__)    # Ensure this matches the GPU-enabled wheel you installed
