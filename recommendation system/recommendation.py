import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/root/ratings.csv")
df.head()

ratings_matrix = df.pivot(
    index="user",
    columns="movie",
    values="rating"
).fillna(0)

ratings_matrix.head()
user_similarity = ratings_matrix.T.corr()
user_similarity.head()

def recommend(user_id, ratings, similarity, top_n=5):
    similar_users = similarity[user_id].drop(user_id)
    similar_users = similar_users[similar_users > 0]

    scores = {}

    for other_user, sim in similar_users.items():
        for movie in ratings.columns:
            if ratings.loc[user_id, movie] == 0:
                scores[movie] = scores.get(movie, 0) + ratings.loc[other_user, movie] * sim

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
user = input("Enter the user name:")
print(f"Recommendation for {user}:")
recommendations = recommend(user, ratings_matrix, user_similarity)
recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)


top_n = 5
top_recs = recommendations[:top_n]

movies = [m[0] for m in top_recs]
scores = [m[1] for m in top_recs]


plt.figure(figsize=(8, 5))
plt.bar(movies, scores)
plt.xlabel("Movies")
plt.ylabel("Recommendation Score")
plt.title(f"Top {top_n} Recommendations for {user}")

plt.text(
    0.5, -0.25,
    "Recommendations generated using Pearson Correlation",
    ha='center',
    transform=plt.gca().transAxes
)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()