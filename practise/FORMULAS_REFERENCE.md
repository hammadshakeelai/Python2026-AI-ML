# Regression Models - Formulas & Parameters Reference Card

## 1. Linear Regression
**Formula:**
```
ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
Minimize: Σ(yᵢ - ŷᵢ)²
```

**Parameters:**
- `fit_intercept`: Include bias term (default: True)

**Interpretation:**
- β₀: Intercept (value when all features = 0)
- βᵢ: Change in y per unit increase in xᵢ

---

## 2. Ridge Regression (L2 Regularization)
**Formula:**
```
Cost = Σ(yᵢ - ŷᵢ)² + λ * Σ(βⱼ²)

Where:
λ (alpha) = regularization parameter (0 ≤ λ < ∞)
```

**Parameters:**
- `alpha`: Regularization strength
  - α=0: Linear Regression
  - α→∞: All coefficients → 0
  - Suggested: 0.1 to 100

**Key Features:**
- Shrinks large coefficients (but doesn't zero them)
- Handles multicollinearity well
- Always keeps all features

---

## 3. Lasso Regression (L1 Regularization)
**Formula:**
```
Cost = Σ(yᵢ - ŷᵢ)² + λ * Σ|βⱼ|

Where:
λ (alpha) = regularization parameter
```

**Parameters:**
- `alpha`: Regularization strength
  - Suggested: 0.001 to 1.0
- `max_iter`: Maximum iterations (default: 1000)

**Key Features:**
- Can shrink coefficients exactly to ZERO
- Automatic feature selection
- Use when expecting some features irrelevant

**When to Use:**
- High-dimensional data
- Features might be irrelevant
- Want sparse solution

---

## 4. Elastic Net (L1 + L2)
**Formula:**
```
Cost = Σ(yᵢ - ŷᵢ)² + λ[(1-ρ)*Σ|βⱼ|/2 + ρ*Σ(βⱼ²)/2]

Where:
λ = regularization strength
ρ (l1_ratio) = balance between L1 and L2
```

**Parameters:**
- `alpha`: Regularization strength (λ)
- `l1_ratio`: Mix of L1 vs L2
  - 0 = Pure Ridge
  - 0.5 = 50% L1, 50% L2
  - 1 = Pure Lasso
  - Suggested: 0.3 to 0.7

**Key Features:**
- Best of both Ridge and Lasso
- Feature selection + correlation handling
- Most flexible regularization

---

## 5. Polynomial Regression
**Formula:**
```
ŷ = β₀ + β₁x + β₂x² + β₃x³ + ... + βₙxⁿ

Degree d = polynomial order
```

**Parameters:**
- `degree`: Polynomial order (1=linear, 2=quadratic, 3=cubic)
- `include_bias`: Include intercept (default: True)

**Complexity vs Degree:**
| Degree | Complexity | Use Case |
|--------|-----------|----------|
| 1      | Low       | Linear relationships |
| 2      | Medium    | Curved trends |
| 3-4    | High      | Complex curves |
| >4     | Very High | Risk of overfitting |

**Warning:** Degree > 4 often overfits unless regularized

---

## 6. K-Nearest Neighbors (KNN)
**Formula:**
```
Uniform: ŷ = (1/k) * Σ(yᵢ of k-nearest)
Distance: ŷ = Σ(wᵢ * yᵢ) where wᵢ = 1/dᵢ

Distance metric: d = √(Σ(x₁ᵢ - x₂ᵢ)²) [Euclidean]
```

**Parameters:**
- `n_neighbors`: k (number of neighbors)
  - k=1: Flexible but noisy
  - k=5: Common default
  - k=10+: Smoother but underfits
- `weights`: 'uniform' or 'distance'
  - 'uniform': All neighbors equal
  - 'distance': Closer neighbors weighted more

**Key Insights:**
- Non-parametric (no model training)
- Lazy learner (work during prediction)
- Sensitive to feature scaling
- Slow for large datasets

**k Selection:**
- Small k: Low bias, high variance (overfitting)
- Large k: High bias, low variance (underfitting)
- Sweet spot: √(n_samples)

---

## 7. Support Vector Machine (SVM) Regression
**Formula:**
```
f(x) = wᵀφ(x) + b

Minimize: (1/2)||w||² + C*Σ(ξᵢ)

Where:
w = weight vector
φ(x) = kernel transformation
ξᵢ = slack variables (error tolerance)
```

**Parameters:**
- `C`: Penalty for errors
  - Small C: Tolerates errors, smoother boundary
  - Large C: Fits training data tightly
  - Suggested: 1 to 1000
- `kernel`: Type of kernel
  - 'linear': Linear boundary
  - 'rbf': Gaussian, flexible curves
  - 'poly': Polynomial features
  - Default: 'rbf'
- `epsilon`: Margin of tolerance
  - ε=0.1: Accept errors < 0.1
  - Suggested: 0.01 to 0.5

**Kernel Comparison:**
| Kernel | Complexity | Speed | Use Case |
|--------|-----------|-------|----------|
| linear | Low       | Fast  | Simple relationships |
| rbf    | High      | Slow  | Complex patterns |
| poly   | Medium    | Medium| Specific structure |

---

## 8. Random Forest Regressor
**Formula:**
```
ŷ = (1/B) * Σ(T_b(x)) for b = 1 to B

Where:
B = number of trees
T_b = prediction from tree b
```

**Parameters:**
- `n_estimators`: Number of trees
  - Suggested: 50-500
  - More = better but slower
  - Rule: Start with 100
- `max_depth`: Maximum tree depth
  - None: Grow until pure
  - Typical: 5-20
  - Higher = more complex
- `min_samples_split`: Minimum samples to split
  - Default: 2
  - Higher = simpler trees
  - Suggested: 3-10
- `max_features`: Features per split
  - 'sqrt': √(n_features)
  - 'log2': log₂(n_features)
  - Suggested: 'sqrt' or 'log2'
- `random_state`: Reproducibility seed

**Feature Importance:**
```
importance = fraction of samples using feature
Higher importance = more predictive
```

**Advantages:**
- Handles non-linear relationships
- Feature importance ranking
- Robust to outliers
- No scaling needed

---

## 9. Gradient Boosting Regressor
**Formula:**
```
F_m(x) = F_{m-1}(x) + ν * h_m(x)

Where:
F_m = ensemble after m iterations
ν = learning rate (step size)
h_m = new tree correcting residuals
```

**Parameters:**
- `n_estimators`: Number of boosting stages
  - Suggested: 50-500
  - More accurate but slower
  - Rule: 100-200
- `learning_rate`: Shrinkage parameter
  - Small ν (0.01-0.05): More robust, more iterations
  - Large ν (0.1-0.3): Faster learning, risk overfitting
  - ν < 0.1 generally safer
- `max_depth`: Tree depth
  - Typical: 3-8
  - Smaller = simpler = less overfit
  - GB uses shallow trees
- `min_samples_split`: Minimum samples to split
  - Default: 2
  - Suggested: 5-20
- `subsample`: Fraction of samples per tree
  - 0.8: Use 80% of data per tree
  - Reduces overfitting
  - Typical: 0.5-1.0

**Learning Rate × N_Estimators Trade-off:**
```
lr=0.01, n_est=1000 → Accurate, slow
lr=0.1,  n_est=100  → Fast, risk overfit
lr=0.05, n_est=200  → Balanced
```

**Feature Importance:**
```
Based on frequency and effectiveness of feature
in correcting residuals
```

---

## Evaluation Metrics

### Mean Squared Error (MSE)
```
MSE = (1/n) * Σ(yᵢ - ŷᵢ)²

Units: Squared target units
Lower is better
Penalizes large errors heavily
```

### Root Mean Squared Error (RMSE)
```
RMSE = √MSE = √[(1/n) * Σ(yᵢ - ŷᵢ)²]

Units: Same as target variable
Lower is better
Same penalty as MSE but interpretable
```

### R² Score
```
R² = 1 - (SS_res / SS_tot)

Where:
SS_res = Σ(yᵢ - ŷᵢ)²  [residual sum of squares]
SS_tot = Σ(yᵢ - ȳ)²   [total sum of squares]

Range: (-∞, 1]
0 = model as good as mean baseline
1 = perfect fit
Negative = worse than baseline
```

---

## Quick Selection Guide

| Goal | Model | Why |
|------|-------|-----|
| **Interpretability** | Linear, Ridge, Lasso | Easy to understand coefficients |
| **Handling Correlation** | Ridge, ElasticNet | Built-in regularization |
| **Feature Selection** | Lasso, ElasticNet | Can zero out features |
| **Non-linear** | Polynomial, KNN, SVM | Capture curves/patterns |
| **Accuracy** | Random Forest, GB | Ensemble methods |
| **Speed** | Linear models | Fast training & prediction |
| **Large Data** | Linear, SVM | Scale well |
| **Small Data** | Tree-based | Works with less data |
| **Outliers** | Tree-based | Robust |

---

## Hyperparameter Tuning Tips

1. **Start with Defaults**: sklearn defaults are usually reasonable
2. **Grid Search**: Test combinations systematically
3. **Cross-Validation**: Use k-fold for robust evaluation
4. **One at a Time**: Vary one parameter, fix others
5. **Visualize**: Plot training vs test error vs parameter value

**Typical Tuning Range:**
```python
# Linear models
alphas = [0.001, 0.01, 0.1, 1, 10, 100]

# KNN
ks = [3, 5, 7, 9, 11, 15, 20]

# Trees
depths = [3, 5, 7, 10, 15, 20]
estimators = [50, 100, 200, 500]

# Learning rate (Gradient Boosting)
lrs = [0.001, 0.01, 0.05, 0.1, 0.2]
```

---

## Bias-Variance Trade-off

```
Total Error = Bias² + Variance + Noise

HIGH BIAS (Underfitting):
- Simple model, high training error
- Solutions: More features, complex model, more data

HIGH VARIANCE (Overfitting):
- Simple training error, high test error
- Solutions: Regularization, less features, simpler model
```

**Check Your Model:**
```python
if train_r2 ≈ test_r2:
    ✓ Good generalization
elif train_r2 >> test_r2:
    ⚠️ Overfitting → Regularize or simplify
elif train_r2 ≈ test_r2 and both low:
    ⚠️ Underfitting → Add features or complexity
```

---

## Formula Cheat Sheet Summary

| Model | Cost Function | Regularization | Key Parameter |
|-------|---------------|-----------------|----------------|
| OLS | Σ(yᵢ - ŷᵢ)² | None | - |
| Ridge | Σ(yᵢ - ŷᵢ)² + λΣ(βⱼ²) | L2 | α (lambda) |
| Lasso | Σ(yᵢ - ŷᵢ)² + λΣ\|βⱼ\| | L1 | α (lambda) |
| ElasticNet | Σ(yᵢ - ŷᵢ)² + λ[...] | L1+L2 | α, l1_ratio |
| Polynomial | (features² then OLS) | None (add ridge) | degree |
| KNN | (1/k)Σneighbors | Implicit k | k |
| SVM | \|\|w\|\|² + Cξ | Margin | C, kernel |
| RF | Σ(tree avg) | Tree depth | n_estimators |
| GB | Σ(residual fit) | Learning rate | learning_rate |
