# FiNCAT: Financial Numeral Claim Analysis Tool

A tool to detect whether numerals present in Financial Texts are in-claim or out-of-claim

![alt text](https://github.com/sohomghosh/FiNCAT_Financial_Numeral_Claim_Analysis_Tool/blob/main/FiNCAT_intro.png)

## Architecture
![alt text](https://github.com/sohomghosh/FiNCAT_Financial_Numeral_Claim_Analysis_Tool/blob/main/system-diagram.png)

## How to use? <br>

Please refer to requirements.txt for versions of the Python libaries used while developing this tool.

<br>**Training**<br>
For training you need to execute the *FiNCAT_training.ipynb* notebook the present in the training folder. It needs *fincat_utils.py* present in the main folder and the embeddings/labels present in the training folder as .csv files. *X_train_df.zip* needs to be unzipped to get the X_train_df.csv file. You can obtain the raw data from [here](https://sites.google.com/nlg.csie.ntu.edu.tw/finnum3/data) .<br>

<br>**Using the tool**<br>
For using the tool you do not need to train it as we have already provided the model artifacts. You can simply execute the *FiNCAT_tool.ipynb* notebook the present in the tool folder. It needs *fincat_utils.py* present in the main folder and the *lr_clf_FiNCAT.pickle* artifact present in the tool folder
![alt text](https://github.com/sohomghosh/FiNCAT_Financial_Numeral_Claim_Analysis_Tool/blob/main/FiNCAT.png)

## FiNCAT-2 (an enhanced version)
![alt text](https://github.com/sohomghosh/FiNCAT_Financial_Numeral_Claim_Analysis_Tool/blob/main/FiNCAT-2_short_demo.gif)
### Video Demonstration on YouTube [![Video Demonstration](https://img.youtube.com/vi/5GmtiOKWSwc/0.jpg)](https://www.youtube.com/watch?v=5GmtiOKWSwc)


This tool has been built using [Google Colab](https://colab.research.google.com/) and [Gradio](https://gradio.app/) .

Tool citation:
```bibtex 
@misc{ghosh-fiNCAT,
    title = "FiNCAT: Financial Numeral Claim Analysis Tool",
    author = "Sohom Ghosh, Sudip Kumar Naskar",
    year = "2022",
    eprint={2202.00631},
    archivePrefix={arXiv},
    primaryClass={q-fin.GN},
    url = "https://arxiv.org/abs/2202.00631",
}
```

Dataset and shared task citation:
```bibtex
@inproceedings{finum3,
  title={Overview of the NTCIR-16 FinNum-3 Task: Investor’s and Manager’s 
Fine-grained Claim Detection},
  author={Chen, Chung-Chi and Huang, Hen-Hsen and Huang, Yu-Lieh and Takamura, Hiroya and Chen, Hsin-Hsi},
  journal={Proceedings of the 15th NTCIR Conference on Evaluation of Information Access Technologies, Tokyo Japan},
  year={2022}
}
```

```bibtex 
@inbook{numclaim,
author = {Chen, Chung-Chi and Huang, Hen-Hsen and Chen, Hsin-Hsi},
title = {NumClaim: Investor's Fine-Grained Claim Detection},
year = {2020},
isbn = {9781450368599},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3340531.3412100},
booktitle = {Proceedings of the 29th ACM International Conference on Information &amp; Knowledge Management},
pages = {1973–1976},
numpages = {4}
}
```
