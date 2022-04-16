# <ins>Overview</ins>
### 2021 - 2022 CU Boulder Engineering Capstone - Sponsored by Northrop Grumman.<br>
Simple classifiers are starting to show promise on quantum processors, and these 
classifiers are deployable on edge processors for inference. The goal of this 
project was to apply Quantum AI to train a simple classifier network and then 
use that network for inference on an emulated embedded platform. If the quantum 
piece does not show improvement over traditional techniques, then traditionally 
trained models will be used for inference on the emulator. <br><br>

We trained our models across three datasets. The quantum dataset used in the
paper [ Supervised Learning With Quantum-Enhanced Feature Spaces](https://www.nature.com/articles/s41586-019-0980-2#MOESM1),
the MNIST Dataset, and the Qiskit ad_hoc dataset via `qiskit_machine_learning.datasets.ad_hoc`.
# <ins>Structure</ins>
`administration/`: Contains status reports and time sheets for project status tracking.<br>
`data/`: Quantum training data. Source:[ Supervised Learning With Quantum-Enhanced Feature Spaces](https://www.nature.com/articles/s41586-019-0980-2#MOESM1).<br>
`documentation/`: Project management and development environment documentation.<br>
`vitis`: Vitis testing files, generated when trying to run models on emulated Vitis DPU's.<br>
`.gitignore`: Git ignore file for ignoring Python virtual environments and other files.<br>
`capstone_poster.pdf`: Project poster used to present during the engineering expo.<br>
`requirements.txt`: Python project dependencies.<br>
`README.md`: Project description and overview.<br><br>


# <ins>Jupyter Notebooks</ins>
`CMLP_Analysis.ipynb`: Analysis of classical MLPs across all three datasets.<br>
`CSVM_Analysis.ipynb`: Analysis of classical SVM's across all three datasets.<br>
`Initial_Notebook.ipynb`: Initial notebook for loading the quantum datset.<br>
`QMLP_Analysis.ipynb`: Analysis of quantum MLPs across all three datasets.<br>
`QSVM_Analysis.ipynb`:Analysis of quantum SVMs across all three datasets.<br><br>

# <ins>Data</ins>
Quantum Dataset, Source:[ Supervised Learning With Quantum-Enhanced Feature Spaces](https://www.nature.com/articles/s41586-019-0980-2#MOESM1).<br>
MNIST Dataset, Source:[ The MNIST Database Of Handwritten Digits](http://yann.lecun.com/exdb/mnist/).<br>
AD_HOC Dataset, Source:[ qiskit_machine_learning.datasets.ad_hoc ](https://qiskit.org/documentation/machine-learning/_modules/qiskit_machine_learning/datasets/ad_hoc.html).