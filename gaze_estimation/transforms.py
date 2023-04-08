from typing import Any

import cv2
import numpy as np
import torch
import torchvision
import yacs.config

from .types import GazeEstimationMethod


def create_transform(config: yacs.config.CfgNode) -> Any:
    return _create_mpiigaze_transform(config)

def tmp_fun1(x):
    return x.astype(np.float32) / 255

def _create_mpiigaze_transform(config: yacs.config.CfgNode) -> Any:
    scale = torchvision.transforms.Lambda(tmp_fun1)
    transform = torchvision.transforms.Compose([
        scale,
        torch.from_numpy,
        torchvision.transforms.Lambda(tmp_fun6),
    ])
    return transform

def tmp_fun6(x):
    return x[None, :, :]


