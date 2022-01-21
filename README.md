# FiNCAT: Financial Numeral Claim Analysis Tool

A tool to detect whether numerals present in Financial Texts are in-claim or out-of-claim

## How to use? <br>
<br>**Training**<br>
For training you need to execute the *FiNCAT_training.ipynb* notebook the present in the training folder. It needs *fincat_utils.py* present in the main folder and the embeddings/labels present in the training folder as .csv files. *X_train_df.zip* needs to be unzipped to get the X_train_df.csv file. <br>
<br>**Using the tool**<br>
For using the tool you need to execute the *FiNCAT_tool.ipynb* notebook the present in the tool folder. It needs *fincat_utils.py* present in the main folder and the *lr_clf_FiNCAT.pickle* artifact present in the tool folder

Tool citation:
```bibtex 
@misc{ghosh-fiNCAT,
    title = "FiNCAT: Financial Numeral Claim Analysis Tool",
    author = "Sohom Ghosh, Sudip Kumar Naskar",
    booktitle = "",
    month = "",
    year = "",
    publisher = "",
    url = "forthcoming",
    intype = {submitted},
}
```

Dataset:
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
