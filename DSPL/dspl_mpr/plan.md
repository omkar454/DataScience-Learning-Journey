# Re-Building Recommendation System on Big Data (`Coursera.csv`)

Building the recommendation engine on the real `Coursera.csv` (3,534 rows) instead of the synthetic custom `coursera_courses.csv` (42 rows) proves you can handle real-world big data at scale!

## ⚠️ User Review Required

Because `Coursera.csv` is missing `Enrolled Students`, `Duration (Hours)`, and `Topic` columns, our logic must be updated. We cannot logically predict a "Weighted Score" because we don't have popularity metrics. Below is the exact methodology to maintain the same 4-model architecture using only the columns natively available in `Coursera.csv`.

---

## 🛠️ Phase 1: Preprocessing & Exploratory Data Analysis (EDA)
- **Data Loading:** Read the massive 3,500-row `Coursera.csv` dataset.
- **Handling Missing Values:** Null values in `Skills` or `Course Description` will be replaced with `"Not Specified"` or blank strings to prevent NLP failures.
- **Feature Engineering:**
  - `Difficulty Level`: Applied One-Hot Encoding just like the previous build.
  - `Metadata Merging`: Combine `Course Name`, `Course Description`, and `Skills` into a massive `Combined_Tags` string for NLP.
- **EDA Generation:** Generate a distribution of `Course Ratings` and a count-plot of `Difficulty Levels`.

---

## 🤖 Phase 2: Model Training & Hyperparameter Tuning (The 4 Models)
- **Model 1: Content-Based Filtering (NLP TF-IDF)**
  - Vectorize the `Combined_Tags` using `TfidfVectorizer` (with `max_features=5000` to prevent RAM crashing on 3,500 rows).
  - Compute Cosine Similarity.

- **Model 2: Feature-Based Similarity (KNN) with Tuning**
  - Iterate through `k = [3, 5, 7, 10]` and `metric = ['euclidean', 'cosine', 'manhattan']` to mathematically find the best parameters before fitting the final model.

- **Model 3: Latent Factor Model (Truncated SVD) with Tuning**
  - Loop through `n_components = [10, 20, 50, 100]` to chart `explained_variance_ratio_` to scientifically determine the best threshold before fitting the final SVD.

- **Model 4: Predictive Modeling (Random Forest Regressor) with GridSearch**
  - **Proposed Pivot:** Since we don't have `Popularity`, we will train the Random Forest to predict **`Course Rating`** instead of Weighted Score.
  - Implement **`GridSearchCV`** to test dozens of combinations for `n_estimators`, `max_depth`, and `min_samples_split` to find the absolute best predictive parameters.
  - **Baseline Model Comparison:** Pit the Tuned Random Forest against `Ridge Regression`, `GradientBoostingRegressor`, and a `Popularity Baseline` (Mean Rating) to mathematically prove the RF is superior.
  - **5-Fold Cross Validation:** Run `KFold(n_splits=5)` to test the model 5 separate times, proving its stability over different chunks of the 3,500 row dataset.
  - Features used to predict Rating: `Difficulty Levels` and the top 20 most frequent `Skills` (One-Hot Encoded).

---

## 📊 Phase 2.5: Advanced Data Science Visualizations
To match the backend python scripts, we will plot:
- **SVD Scree Plot:** Visualizing Cumulative Explained Variance to justify our choice of `n_components`.
- **Model Comparison Chart:** Bar chart comparing MSE, MAE, and R² for Random Forest vs Ridge vs Gradient Boosting.
- **Cross-Validation Plot:** Showing the MSE variation across the 5 folds with ±1 Standard Deviation.
- **Random Forest Feature Importance:** Horizontal bar chart showing which features (skills/difficulty) dictate Course Ratings.

---

## ⚖️ Phase 3: Model Validation & Hypothesis Testing
- **Blind Test Evaluation Array:** We will run the exact same `evaluate_model()` function, fetching the Top 5 recommendations for a sample course across the 3 models and testing Precision@3 and NDCG@3.
- **Hypothesis Testing (Paired T-Test):** Compare the performance of Model 1 (TF-IDF) vs Model 3 (SVD) and output the P-Value to determine statistical difference on big data.

