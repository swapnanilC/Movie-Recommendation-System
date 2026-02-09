# Statistical Recommendation System

A statistical movie recommendation system built using **user-based collaborative filtering** and **Pearson correlation**, implemented with **NumPy**, **Pandas**, and **Matplotlib**.

This project demonstrates how recommendation systems work at a fundamental level using statistical techniques rather than black-box machine learning models.

---

## 📌 Features
- User–user similarity calculation using **Pearson Correlation**
- Collaborative filtering–based recommendations
- Data handling using **Pandas**
- Numerical computation using **NumPy**
- Visualization of top recommendations using **Matplotlib**
- Beginner-friendly and fully explainable implementation

---

## 📊 Dataset
The dataset consists of user ratings for different movies.

**Format:**
User, Movie, Rating
U1, Movie_A, 4
U1, Movie_B, 5
U2, Movie_A, 3
...


- Each user can rate multiple movies
- Missing ratings are handled during matrix creation

---

## ⚙️ How It Works
1. Convert the ratings data into a **user–item matrix**
2. Compute **Pearson correlation** between users
3. Identify users most similar to the target user
4. Predict scores for unseen movies using weighted ratings
5. Generate top-N movie recommendations
6. Visualize the recommendations using a bar chart

---

## 📈 Output
The system displays:
- A list of recommended movies with scores
- A bar chart visualizing the top recommendations for a selected user

---

## 🛠️ Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Google Colab

---

## ▶️ How to Run
1. Clone or download this repository
2. Open the notebook in **Google Colab** or **Jupyter Notebook**
3. Run all cells in sequence
4. Change the user ID to get recommendations for different users

---

## 🎯 Learning Outcomes
- Understanding collaborative filtering concepts
- Applying Pearson correlation for similarity measurement
- Handling and analyzing data using Pandas
- Visualizing recommendation results
- Building a complete end-to-end recommendation pipeline

---

## 🚀 Future Enhancements
- Use a larger dataset
- Implement item-based collaborative filtering
- Normalize user ratings
- Deploy as a web application using Streamlit

---

## 📄 License
This project is licensed under the MIT License.

## 👤 Author
Swapnanil Chakraborty
