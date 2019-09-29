from typing import Callable, List

import attr
from tensorflow import keras


@attr.s(auto_attribs=True)
class ImageTrainingStep:
    n_epochs: int
    lr: float
    optimizer: keras.optimizers
    freeze: bool = False
    feature_pipeline: List[Callable] = []
    label_pipeline: List[Callable] = []
