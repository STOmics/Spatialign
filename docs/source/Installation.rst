Installation
==============
The Spatialign package is developed based on the pytorch framework and can be implemented on both CPU and GPU.

We recommend running the package on GPU. Please ensure that pytorch and CUDNN are installed correctly.

To run Spatialign, all dependencies included in the file 'requirement.txt' need to be installed.

We provide two ways to install the package of Spatialign.

Please note that the current Spatialign version offers full support of Linux operating system. Further version for other operating systems would be released soon.


1. Python
----------------
Downloading the package from `GitHub repository <https://github.com/zhangchao162/Spatialign/blob/wheel/spatialign-0.1.2-py3-none-linux_x86_64.whl>`_.

.. code-block:: python

    pip install spatialign-0.1.2-py3-none-linux_x86_64.whl

or

.. code-block:: python

    git clone -b release https://github.com/zhangchao162/Spatialign.git

    cd Spatialign

    python setup.py install


2. Anaconda
---------------
For convenience, we suggest using a separate conda environment for running Spatialign. Please ensure Annaconda3 is installed.

Create conda environment and install Spatialign package.

.. code-block:: python

   # create an environment called Spatialign
   conda create -n Spatialign python=3.8

   # activate your environment
   conda activate Spatialign

   # install package

   pip install spatialign

   or

   git clone -b release https://github.com/zhangchao162/Spatialign.git

   cd Spatialign

   python setup.py build

   python setup.py install --user

   #To use the environment in jupyter notebook, add python kernel for this environment.

   pip install ipykernel

   python -m ipykernel install --user --name=spatialign
