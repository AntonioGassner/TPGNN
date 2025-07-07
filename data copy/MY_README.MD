# Dependency fixes

To install scikit:
>scikit_learn==0.24.2

```shell
pip install scikit-learn --only-binary :all:

```

To install torch w CUDA:
>torch==1.12.1+cu113

```shell
pip install torch==1.12.1+cu113 \
            torchvision==0.13.1+cu113 \
            torchaudio==0.12.1 \
            --extra-index-url https://download.pytorch.org/whl/cu113
```

Sklearn seems to be missing
```shell
pip install -U scikit-learn
```

pip install numpy==1.24.4
pip install tensorboard


Cuda error
```shell
nvidia-smi
cat /proc/driver/nvidia/version

```

```shell
export CUDA_VISIBLE_DEVICES=0
```

set device to zero in scripts/multi.sh





