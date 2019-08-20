# PyTorch Tutorial
presented on 21 Aug 2019 at the [MIT-Harvard Theoretical and Computational Neuroscience Journal Club](https://compneurojc.github.io/).

**Author**: Martin Schrimpf \[[github](https://github.com/mschrimpf)\] \[[scholar](https://scholar.google.com/citations?user=RiZ-RdwAAAAJ)\]

Link to notebook: https://nbviewer.jupyter.org/github/mschrimpf/pytorch_tutorial/blob/master/tutorial.ipynb


## Goals of this tutorial

1. You have been exposed to PyTorch, ideally even run it
2. When someone sends modeling code to you, you're comfortable going through it
3. You have a reference to look things up or start building your own models


## Setup
If you have [conda](https://docs.conda.io/en/latest/miniconda.html) (suggested), run
```
conda install numpy matplotlib seaborn jupyter tqdm
conda install pytorch torchvision -c pytorch
```
You can also `pip install "pytorch_tutorial @ git+https://github.com/mschrimpf/pytorch_tutorial"`, 
or `pip install` by hand.

In general, I also recommend using the [PyCharm IDE](https://www.jetbrains.com/pycharm/), but you can use whatever you are comfortable with.

For this tutorial, please have a [jupyter](https://jupyter.org/) notebook server running.


## More ressources

* [PyTorch examples](https://github.com/pytorch/examples), a collection of sample code for vision, text, RL etc.
* [fast.ai](https://www.fast.ai/), a practical deep learning course built with PyTorch
* [Andrew Ng's coursera course](https://www.coursera.org/learn/machine-learning), the first and still very relevant Machine Learning course with theory and practices
