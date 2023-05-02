# Eye-Gaze-Estimation
Implementation of existing project, here is the [source code](https://github.com/hysts/pytorch_mpiigaze).
Code refactoring to improve readability and maintainability.

## Datasets
Please refer to [this](https://github.com/hysts/pytorch_mpiigaze) to download and prepare the MPIIGaze dataset.

## Training and Evaluation
By running the following code, you can train a model using all the data except the person with ID 0, and run test on that person.
```
python train.py --config configs/lenet_train.yaml
python evaluate.py --config configs/lenet_eval.yaml
```
Using [configs/resnet_preact_train.yaml](https://github.com/Mekkkky/Eye-Gaze-Estimation/blob/main/configs/resnet_preact_train.yaml), you can run training and evaluation for ResNet-8 with default parameters.

## Demo
Specify the model path and the path of the camera calibration results in the configuration file as in [configs/demo_resnet.yaml](https://github.com/Mekkkky/Eye-Gaze-Estimation/blob/main/configs/demo_resnet.yaml).
```
python demo.py --config configs/demo_resnet.yaml
```
