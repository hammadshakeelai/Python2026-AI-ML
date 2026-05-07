# Student Performance Regression Models - Setup Guide

## Overview
This project implements 9 different regression algorithms to predict student performance with detailed explanations of formulas and parameters.

## Models Included

### Linear Models (Interpretable)
1. **Linear Regression** - Basic OLS fitting
2. **Ridge Regression (L2)** - Penalizes coefficient magnitude
3. **Lasso Regression (L1)** - Feature selection through zero coefficients
4. **Elastic Net** - Combines Ridge + Lasso benefits
5. **Polynomial Regression** - Non-linear relationships

### Tree-Based Models (Powerful)
6. **K-Nearest Neighbors (KNN)** - Instance-based learning
7. **Support Vector Machine (SVM)** - Kernel-based regression
8. **Random Forest** - Ensemble of decision trees
9. **Gradient Boosting** - Sequential error correction

## Setup Instructions

### Step 1: Install Required Packages
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Step 2: Download Dataset

#### Option A: Using Kaggle CLI (Automatic)
```bash
# Install kaggle CLI
pip install kaggle

# Get your API credentials from https://www.kaggle.com/account
# Create ~/.kaggle/kaggle.json with your credentials
# Set permissions: chmod 600 ~/.kaggle/kaggle.json

# Run the download script
python download_kaggle_data.py
```

#### Option B: Manual Download
1. Visit: https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression
2. Download the CSV file
3. Place `Student_Performance.csv` in the `practise/` directory

### Step 3: Run the Notebook
```bash
jupyter notebook test.ipynb
```

## Notebook Structure

### Data Loading & Preprocessing
- Load data from CSV
- Check for missing values
- Split into features (X) and target (y)
- Train-test split (80-20)
- Feature scaling (StandardScaler)

### Models & Explanations
Each model section includes:
- **Mathematical Formula**: The equation governing the model
- **Parameters**: Key hyperparameters and their meanings
- **Training**: Fitting the model on training data
- **Code**: Implementation with scikit-learn

### Key Formulas Explained

#### Linear Regression
```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε
```
- Minimizes Sum of Squared Errors (SSE)

#### Ridge Regression (L2)
```
Cost = SSE + λ * Σ(βᵢ²)
```
- λ (alpha): Controls regularization strength
- Prevents overfitting by penalizing large coefficients

#### Lasso Regression (L1)
```
Cost = SSE + λ * Σ|βᵢ|
```
- Can shrink coefficients to exactly zero
- Performs automatic feature selection

#### Polynomial Regression
```
y = β₀ + β₁x + β₂x² + β₃x³ + ... + βₙxⁿ
```
- Degree parameter controls polynomial complexity

#### KNN Regressor
```
ŷ = (1/k) * Σ(nearest_k_neighbors)
```
- k: Number of neighbors to consider
- Prediction is average of k nearest points

#### SVM Regressor
```
f(x) = wᵀφ(x) + b
```
- C: Penalty for errors
- kernel: Linear, RBF, or Polynomial
- ε: Acceptable margin of error

#### Random Forest
```
ŷ = (1/B) * Σ(Tree_b(x)) for b=1 to B
```
- B: Number of trees
- Aggregates predictions from multiple trees

#### Gradient Boosting
```
F_m(x) = F_{m-1}(x) + ν * h_m(x)
```
- ν (learning_rate): Step size for updates
- Sequentially reduces prediction errors

### Evaluation Metrics

#### Mean Squared Error (MSE)
```
MSE = (1/n) * Σ(yᵢ - ŷᵢ)²
```

#### Root Mean Squared Error (RMSE)
```
RMSE = √MSE
```
- Same units as target variable

#### R² Score (Coefficient of Determination)
```
R² = 1 - (SSₑₛ / SSₜₒₜ)
```
- 0 = poor fit, 1 = perfect fit
- Indicates proportion of variance explained

## Parameters Guide

### Common Parameters

**Random State**: Ensures reproducibility
```python
random_state=42
```

**Test Size**: Train-test split ratio
```python
test_size=0.2  # 20% testing, 80% training
```

**Alpha (Regularization)**: Controls penalty strength
- Ridge: `alpha_ridge = 1.0`
- Lasso: `alpha_lasso = 0.01`
- ElasticNet: `alpha_elasticnet = 0.01`

### Model-Specific Parameters

**KNN**
- `n_neighbors=5`: Number of neighbors
- `weights='distance'`: Weight scheme

**SVM**
- `C=100`: Penalty parameter
- `kernel='rbf'`: Kernel function
- `epsilon=0.1`: Margin of tolerance

**Random Forest**
- `n_estimators=100`: Number of trees
- `max_depth=10`: Maximum tree depth
- `max_features='sqrt'`: Features per split

**Gradient Boosting**
- `n_estimators=100`: Number of boosting stages
- `learning_rate=0.1`: Shrinkage parameter
- `max_depth=5`: Tree depth
- `subsample=0.8`: Sample fraction per tree

## Expected Output

The notebook will generate:
1. **Model Coefficients**: For linear models
2. **Feature Importance**: For tree-based models
3. **Evaluation Metrics**: MSE, RMSE, R² for all models
4. **Comparison Charts**: R² and RMSE visualizations
5. **Best Model**: Summary of top-performing model

## Understanding the Results

### High R² (>0.8)
✓ Model explains most variance in the data
✓ Good fit

### R² between 0.5-0.8
△ Reasonable fit
△ May need feature engineering or hyperparameter tuning

### Low R² (<0.5)
✗ Poor fit
✗ Consider different model or more/better features

### Train R² >> Test R² 
⚠️ Overfitting - model memorized training data
⚠️ Solutions: Reduce complexity, add regularization, more data

### Train R² ≈ Test R²
✓ Good generalization
✓ Model will likely perform well on new data

## Tips for Best Results

1. **Feature Engineering**: Create meaningful features from raw data
2. **Feature Scaling**: Normalize features for distance-based models (KNN, SVM)
3. **Hyperparameter Tuning**: Use GridSearchCV for optimal parameters
4. **Cross Validation**: Use k-fold CV for more robust evaluation
5. **Ensemble Methods**: Combine multiple models for better predictions

## Troubleshooting

### Kaggle Download Issues
- Ensure kaggle.json is in ~/.kaggle/
- Check file permissions: `chmod 600 ~/.kaggle/kaggle.json`
- Test with: `kaggle datasets list`

### Missing Data
- Check CSV encoding (usually UTF-8)
- Verify CSV path is correct
- Ensure CSV has headers in first row

### Model Performance Issues
- Check for data leakage
- Ensure proper train-test split
- Verify feature scaling is applied
- Try different hyperparameters

## References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Kaggle Datasets](https://www.kaggle.com/datasets/)
- [Regression Algorithms](https://en.wikipedia.org/wiki/Regression_analysis)

## License & Attribution

Student Performance Dataset: https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression
