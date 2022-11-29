FROM pengchuanzhang/pytorch:ubuntu20.04_torch1.9-cuda11.3-nccl2.9.9

COPY . /workspace/GLIP
WORKDIR /workspace/GLIP
RUN pip install einops shapely timm yacs tensorboardX ftfy prettytable pymongo transformers pycocotools
RUN python setup.py build develop --user
