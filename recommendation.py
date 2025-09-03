import pandas as pd
ratings = pd.read_csv(
    r"C:\Users\Modit\Desktop\Recommendation Model\ratings.csv")
movies = pd.read_csv(r"C:\Users\Modit\Desktop\Recommendation Model\movies.csv")

data = pd.merge(ratings, movies, on="movieId")

filtered_movies = data.groupby("title").filter(lambda x: len(x) >= 500)
movie_matrix = filtered_movies.pivot_table(
    index='userId', columns='title', values='rating')


def recommend_movies(movie_name, top_n=10):
    if movie_name not in movie_matrix.columns:
        return f"Movie '{movie_name}' not found in dataset."

    target_movie_ratings = movie_matrix[movie_name]
    similar_target = movie_matrix.corrwith(target_movie_ratings)
    corr_movies = pd.DataFrame(similar_target, columns=['correlation'])
    corr_movies.dropna(inplace=True)
    movie_stats = data.groupby('title')['rating'].agg(['mean', 'count'])
    corr_movies = corr_movies.join(movie_stats)
    recommendation = corr_movies.drop(movie_name, errors='ignore')
    recommendation = recommendation.sort_values(
        ['correlation', 'mean'], ascending=False)
    return recommendation.head(top_n)


user_input = input(
    "Enter a movie you like! (ex. ""Matrix (1999): ")
recommended_movies = recommend_movies(user_input, top_n=10)

print("\n Recommended Movies for you:")
print(recommended_movies)
