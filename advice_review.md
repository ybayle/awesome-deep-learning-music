# Advices for reviewers of dl4m articles

Regarding conflicts of interest, confidentiality, anonymity, ethical guidelines, commitment, respect and scheduling please refer to the guidelines provided by the MIR community on the dedicated conference websites:
- [ISMIR 2016](https://wp.nyu.edu/ismir2016/call-for-participation/guidelines-for-reviewers/)
- [ISMIR 2017](https://ismir2017.smcnus.org/guidelines-for-reviewers/)

For technical guidelines on deep learning and music you can use this humble following advices.
Check for completeness of details about:

- **Music aspects**
  - datasets used, please refer to [datasets.md](https://github.com/ybayle/awesome-deep-learning-music/blob/master/datasets.md)
  - data augmentation (Pitch shift, Time-stretch, Mixing, Circular shift, Noise addition, Filter, Dropout, ...)
  - input type (Raw signal, Time-frequency representation, ...)
  - number of dimension used as input (1D, 2D, ...) 

- **Deep learning aspects**:
  - architectures, please refer to [architectures.md](https://github.com/ybayle/awesome-deep-learning-music/blob/master/architectures.md)
  - learning rate (Fixed or changing and range)
  - framework, please refer to [frameworks.md](https://github.com/ybayle/awesome-deep-learning-music/blob/master/frameworks.md)
  - reproducibility, please refer to [reproducibility.md](https://github.com/ybayle/awesome-deep-learning-music/blob/master/reproducibility.md)
  - activation function (ReLU, Leaky ReLU, Sigmoid, Softmax, ...)
  - number of epochs
  - batch size (the bigger the better but generally between 16 and 150)
  - loss function (RMSE, Cross-entropy, ...)
  - number of layers
  - dropout ratio
  - cpu or gpu usage and description
  - computation time (Global or per epoch)
  - optimizer (Adam, SGD, ...)

- **General aspects**:
  - source code provided
  - description of the task similar to existing ones
  - citing relevant literature from [dl4m.bib](https://github.com/ybayle/awesome-deep-learning-music/blob/master/dl4m.bib)
