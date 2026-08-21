# 🎓 Enterprise Course Recommendation System

**A Two-Stage Hybrid AI Recommendation Engine built on the real-world Coursera dataset (3,500+ courses).**

---

## 📖 Project Overview
This project constructs a production-grade Data Science and Machine Learning pipeline designed to mimic the architectural scale of top-tier algorithmic platforms (like Netflix, YouTube, and Coursera). 

Instead of relying on a single, isolated algorithm, this system mathematically evaluates user queries and executes a **Two-Stage Hybrid Architecture**:
1. **Candidate Generation (Stage 1):** Utilizes Unsupervised Natural Language Processing (SVD / LSA) to instantly retrieve conceptually relevant courses from a massive database.
2. **Predictive Quality Ranking (Stage 2):** Utilizes a Supervised Ensemble model (Random Forest) to scientifically predict course ratings based on their curriculum, actively eliminating the "Cold-Start" bias that plagues new courses with zero reviews.

---

## 🛠️ The Data Engineering Pipeline
Before AI was applied, the raw `Coursera.csv` (containing over 3,500 rows) underwent rigorous preprocessing and Exploratory Data Analysis (EDA):
* **Noise Imputation:** Handled missing categorical values and duplicated URLs.
* **Feature Engineering:** One-Hot Encoded `Difficulty Levels` and utilized `CountVectorizer` to transpose the Top 20 most frequent technological `Skills` into binary tracking matrices.
* **Bias Identification:** EDA visualizations proved a massive platform bias (the vast majority of courses default to a `4.6` rating). This necessitated the pivot to predicting ratings via Deep Trees to identify true quality.

---

## 🧠 The AI Architectures (Model Implementations)

### Model 1 & 2: TF-IDF & K-Nearest Neighbors (KNN)
* **Goal:** Establish a baseline strict keyword matcher.
* **Implementation:** An uncapped `TfidfVectorizer` was deployed against course descriptions, followed by a `NearestNeighbors` model utilizing Brute-Force **Cosine Similarity**. 
* **Tuning:** A Grid Search over `K` and Distance Metrics mathematically proved that Cosine distances operate superiorly on sparse, high-dimensional matrices compared to Euclidean/Manhattan distances.

### Model 3: Truncated SVD (Latent Semantic Analysis)
* **Goal:** Elevate the Search Engine from matching exact "Keywords" to matching broader "Hidden Concepts" (Synonyms).
* **Implementation:** `TruncatedSVD` condensed the massive sparse matrix into dense arrays.
* **Tuning:** An automated **Scree Plot** was generated to visualize the "Cumulative Explained Variance", mathematically proving the "Elbow" at `n_components=100`, successfully condensing data without memorizing noise.

### Model 4: Random Forest Regressor (Predictive Quality)
* **Goal:** Solve the "Cold-Start" problem by mathematically predicting what a course's rating *should be* based purely on its 'Difficulty' and 'Skills'.
* **Implementation:** A highly tuned Supervised Decision Tree ensemble. 
* **Tuning:** Deployed `GridSearchCV` to optimize `n_estimators`, `max_depth`, and `min_samples_split` across hundreds of iterations. Tested against Naive, Ridge, and Gradient Boosting baselines. 

---

## ⚖️ Scientific Validation & Inference
To prove statistical significance rather than relying on assumed accuracy, Phase 3 executed:
1. **Blind Test Evaluation Array:** Simultaneously fed 50 blind queries into both the SVD and KNN models.
2. **Paired T-Testing:** Outputted a P-Value (0.659) failing to reject the null hypothesis. This successfully proved that the SVD model retains identical heuristic relevance (matching Difficulty/University) to KNN, defending the business pivot to the much faster, computationally cheaper Dense SVD architecture.
3. **5-Fold Cross Validation:** Ran K-Fold validation to guarantee the stability of the Random Forest across the massive dataset.

---

## 🚀 The Grand Finale: Hybrid Pipeline Execution
All models are serialized to the `exports/` folder via `joblib`. The final API function (`hybrid_recommender()`) wires the unsupervised and supervised brains together:

1. **User requests a course.**
2. **The SVD Engine** rapidly scans all 3,500 rows and pools the Top 30 conceptually relevant matches.
3. **The Random Forest** intercepts these 30 matches, predicting their true, objective rating, bypassing human review bias.
4. **The Pipeline** sorts the pool by the RF Prediction Score, outputting the absolute top 5 courses to the user.

---
*Created as a capstone exploration into Enterprise-Grade Natural Language Processing and Hybrid Recommendation Systems.*
