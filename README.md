# 📈 Customer Segmentation Analysis Using KMeans
## 📌 Overview

This project applies KMeans Clustering to segment customers based on their demographics, income, spending behavior, and engagement features.
It helps businesses identify distinct customer groups and build personalized marketing strategies.

## 🛠 Tools & Technologies

Python

NumPy & Pandas → Data manipulation

Matplotlib & Seaborn → Data visualization

Scikit-learn → Machine learning (KMeans, PCA, StandardScaler)

Joblib → Model saving/loading

Jupyter Notebook → Analysis environment

## 📂 Project Structure
├── customer_segmentation.ipynb     # Jupyter Notebook with full analysis  

├── customer_segmentation.csv       # Dataset  

├── Kmeans_model.pkl                # Saved KMeans model  

├── scaler.pkl                      # Saved StandardScaler  

├── requirements.txt                # Dependencies  

└── .gitignore                      # Ignored files  

## ⚙️ Model Workflow

**Data Collection** → Import and clean customer dataset.

**Preprocessing** → Handle missing values, create new features (Age, Total Spending, Children, etc.).

**EDA (Exploratory Data Analysis)** → Histograms, Boxplots, Correlation Matrix.

**Feature Engineering** → Select key features for clustering.

**Scaling** → Standardize features using StandardScaler.

**Clustering** → Apply KMeans (Elbow Method to choose optimal k).

**PCA Visualization** → Reduce dimensions to 2D for visualization.

**Cluster Profiling** → Summarize each cluster by average Income, Age, Spending, etc.

**Model Saving** → Save trained KMeans model and Scaler using joblib.

## 🚀 How to Run
**Clone repository**

`git clone https://github.com/your-username/Customer-Segmentation.git`

`cd Customer-Segmentation`

**Install dependencies**

`pip install -r requirements.txt`

**Run Jupyter Notebook**

`jupyter notebook customer_segmentation.ipynb`

---

### **Create New virtual environment**

**🔹 Step 1: Open terminal (Command Prompt / PowerShell / Git Bash / VS Code Terminal)**

**Navigate to your project folder:**

`cd path\to\your\project`

**🔹 Step 2: Create the virtual environment**


`python -m venv .venv`


`python -m venv → creates a virtual environment`

.venv → the folder name (you can also name it env, but .venv is common for GitHub projects)

**🔹 Step 3: Activate the environment**

**On Windows (CMD)**


`.venv\Scripts\activate`

**On Windows (PowerShell)**

`.venv\Scripts\Activate.ps1`

**On Mac/Linux**

`source .venv/bin/activate`

**On Windows (PowerShell)**


`.venv\Scripts\Activate.ps1`

---

# 📸 Custumer Segmentation By PCA
<img width="559" height="449" alt="image" src="https://github.com/user-attachments/assets/749898ba-3289-43e1-ab9c-bddbc8747750" />


## 📊 Results

**Customers were grouped into 6 clusters with different profiles:**

**Cluster 0:** Younger, low spending, low income

**Cluster 1:** Middle-aged, high spending, high income

**Cluster 2:** Older, average spending

**Cluster 3:** Younger, medium income, online shoppers

**Cluster 4:** Families with higher store purchases

**Cluster 5:** Low engagement & low acceptance of campaigns

PCA visualization shows clear separation of clusters.

## 📸 Example:

Age Distribution, Income by Education, Campaign Acceptance by Marital Status

2D PCA Plot with Cluster Coloring

## 📧 Support

**For questions or collaborations, feel free to connect:**

📩 **Email:** zuhairzia1@gmail.com

💼 **LinkedIn:** www.linkedin.com/in/zuhairzia
