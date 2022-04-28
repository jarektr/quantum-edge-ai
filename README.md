# <ins>Overview</ins>
### 2021 - 2022 CU Boulder Engineering Capstone - Sponsored by Northrop Grumman.<br>
Simple classifiers are starting to show promise on quantum processors, and these 
classifiers are deployable on edge nodes for inference. The goal of this 
project was to apply Quantum AI to train a simple classifier network and then 
use that network for inference on an emulated embedded platform. If the quantum 
piece does not show improvement over traditional techniques, then traditionally 
trained models will be used for inference on the emulator. <br>

We trained our models across three datasets. The quantum dataset used in the
paper [ Supervised Learning With Quantum-Enhanced Feature Spaces](https://www.nature.com/articles/s41586-019-0980-2#MOESM1),
the MNIST dataset, and the Qiskit ad_hoc dataset.<br><br>


## Team:
* [Adam Hoerger](https://github.com/adamhoerger) - Software Engineer
* [Alan Yu](https://github.com/huaaoyu) - Software Engineer
* [Cade Gorman](https://github.com/cgorman-cu) - Software Engineer
* [Giovanni Visco](https://github.com/givi0519) - Software Engineer
* [Jarek Smith](https://github.com/JarekTS) - Project & Repo Manager
* [John Ortiz](https://github.com/OrtizJohn) - Software Engineer
* [Jorge Ortiz](https://github.com/joor2163) - Software Engineer
* [Noah Svensson](https://github.com/Gholion) - Software Engineer
<br><br>


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
`C_MLP_Analysis.ipynb`: Analysis of classical MLPs across all three datasets.<br>
`C_SVM_Analysis.ipynb`: Analysis of classical SVM's across all three datasets.<br>
`Initial_Notebook.ipynb`: Initial notebook for loading the quantum datset.<br>
`Q_MLP_Analysis.ipynb`: Analysis of quantum MLPs across all three datasets.<br>
`Q_SVM_Analysis.ipynb`:Analysis of quantum SVMs across all three datasets.<br><br>


# <ins>Data</ins>
Quantum Dataset, Source:[ Supervised Learning With Quantum-Enhanced Feature Spaces](https://www.nature.com/articles/s41586-019-0980-2#MOESM1).<br>
MNIST Dataset, Source:[ The MNIST Database Of Handwritten Digits](http://yann.lecun.com/exdb/mnist/).<br>
AD_HOC Dataset, Source:[ qiskit_machine_learning.datasets.ad_hoc](https://qiskit.org/documentation/machine-learning/_modules/qiskit_machine_learning/datasets/ad_hoc.html).<br><br>


# <ins>Technical Challenges</ins>
* Vitis hardware emulation is not well documented.<br>

* Qiskit documentation for certain workflows is scarce.<br>

* Vitis AI does not currently support Scikit Learn workflows.<br>

* Vitis AI does not currently support deep learning processor unit (DPU) hardware 
emulation. [ Source](https://support.xilinx.com/s/question/0D52E000073wxTdSAI/unable-to-create-a-runner-for-hardware-emulation-using-vitisai-2001103-cpu-and-tensorflow2?language=en_US&t=1647608876546).<br>

* Transitioning from classical models to quantum models, while trying best 
to maintain similarity between layers proved challenging.
