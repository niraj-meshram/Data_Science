# Data Science Exercises and Projects

A curated collection of notebooks and small projects across machine learning, deep learning, EDA, and statistics/probability. Each folder includes a short README with setup and run instructions.

## Getting Started

- Recommended: Python 3.9+
- Create a virtual environment
  - Windows (PowerShell): `python -m venv .venv; .\\.venv\\Scripts\\Activate.ps1`
- Install JupyterLab: `pip install jupyterlab`
- If a `requirements.txt` exists in a project: `pip install -r requirements.txt`

## Repo Structure

- `Deep Learning/` — TensorFlow-focused experiments and demos
- `Machine Learning/Exercise/` — classic ML algorithms and workflows
- `EDA/` — exploratory data analysis notebooks
- `Statics-And_Probability-Exercise-CC/` — statistics and probability exercises

## How to Run

- Notebooks: open in JupyterLab and run cells top-to-bottom.
- Scripts: run `python <script>.py` from the project directory.
- Artifacts (models, outputs, runs) are gitignored by default; see `.gitignore`.

## Projects Index

### Deep Learning / TensorFlow
- [CNN_Image](Deep Learning/TensorFlow/CNN_Image/README.md)
- [Customer_Churn_Prediction_Using_ANN](Deep Learning/TensorFlow/Customer_Churn_Prediction_Using_ANN/README.md)
- [Data_Augumentation](Deep Learning/TensorFlow/Data_Augumentation/README.md)
- [Dropout Regularization](Deep Learning/TensorFlow/Dropout Regularization/README.md)
- [GPU_Benchmarking](Deep Learning/TensorFlow/GPU_Benchmarking/README.md)
- [Gradient_Descent](Deep Learning/TensorFlow/Gradient_Descent/README.md)
- [Handling_Imbalance](Deep Learning/TensorFlow/Handling_Imbalance/README.md)
- [Loss_or_Cost_Funtion_MAE_MSE](Deep Learning/TensorFlow/Loss_or_Cost_Funtion_MAE_MSE/README.md)
- [Matrix](Deep Learning/TensorFlow/Matrix/README.md)
- [Neural Network For Handwritten Digits Classification](Deep Learning/TensorFlow/Neural Network For Handwritten Digits Classification/README.md)
- [Precision_Recall_F1](Deep Learning/TensorFlow/Precision_Recall_F1/README.md)
- [Tensorboard](Deep Learning/TensorFlow/Tensorboard/README.md)

### Machine Learning / Exercise
- [Bagging_and_Boosting](Machine Learning/Exercise/Bagging_and_Boosting/README.md)
- [Decision_Tree](Machine Learning/Exercise/Decision_Tree/README.md)
- [Dummy_Variables](Machine Learning/Exercise/Dummy_Variables/README.md)
- [Gradient_Descent](Machine Learning/Exercise/Gradient_Descent/README.md)
- [Hyper_Parameter_Tunning](Machine Learning/Exercise/Hyper_Parameter_Tunning/README.md)
- [K_Fold_Cross_Verification](Machine Learning/Exercise/K_Fold_Cross_Verification/README.md)
- [K_Means](Machine Learning/Exercise/K_Means/README.md)
- [K_Nearest_Neighbor](Machine Learning/Exercise/K_Nearest_Neighbor/README.md)
- [L1_L2_Regularization](Machine Learning/Exercise/L1_L2_Regularization/README.md)
- [Linear_Regression](Machine Learning/Exercise/Linear_Regression/README.md)
- [Linear_Regression_Multivariate](Machine Learning/Exercise/Linear_Regression_Multivariate/README.md)
- [Logistic_Regression](Machine Learning/Exercise/Logistic_Regression/README.md)
- [Naive_Bayes](Machine Learning/Exercise/Naive_Bayes/README.md)
- [Principal_Component_Analysis](Machine Learning/Exercise/Principal_Component_Analysis/README.md)
- [Project_Banglore_Home_Prices](Machine Learning/Exercise/Project_Banglore_Home_Prices/README.md)
- [Random_Forest](Machine Learning/Exercise/Random_Forest/README.md)
- [Support_Vector_Machine](Machine Learning/Exercise/Support_Vector_Machine/README.md)
- [Training_And_Testing](Machine Learning/Exercise/Training_And_Testing/README.md)

### Machine Learning / PythonProject
- [Project_Banglore_Home_Prices_Flask_Server](Machine Learning/Exercise/PythonProject/Project_Banglore_Home_Prices_Flask_Server/README.md)
- [Project_Celebrity_Image_Detection](Machine Learning/Exercise/PythonProject/Project_Celebrity_Image_Detection/README.md)
- [Project_Wine_Quality](Machine Learning/Exercise/PythonProject/Project_Wine_Quality/README.md)

## Notes

- Data files are not committed; place datasets under `data/` inside each project.
- If you add new projects, copy a README template from an existing one.

## Datasets and Assets

- Keep large assets (datasets, model weights, archives) out of Git history by default; most are gitignored.
- Recommended for large binaries: use Git LFS.
  - `git lfs install`
  - `git lfs track "*.h5" "*.pkl" "*.pt" "*.zip" "*.onnx"`
  - Commit the generated `.gitattributes` and push normally.
- Examples excluded here:
  - `Deep Learning/TensorFlow/Data_Augumentation/datasets/flower_photos/`
  - `Machine Learning/Exercise/PythonProject/Project_Celebrity_Image_Detection/model/*` weights and dataset
- Alternative: add lightweight download scripts or links in each project README and keep only small samples under `data/sample/`.
