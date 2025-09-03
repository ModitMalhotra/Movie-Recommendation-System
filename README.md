# 🎬 Movie Recommendation System

A simple **movie recommendation system** built with the [MovieLens dataset](https://grouplens.org/datasets/movielens/).  
The system suggests movies similar to a user’s chosen movie, ranked by **correlation and average ratings**.


## Features
- Built using **MovieLens ratings and movies datasets** (`ratings.csv`, `movies.csv`).  
- Recommends movies based on **collaborative filtering (correlation)**.  
- Filters out movies with very few ratings to ensure quality.  
- Ranks recommended movies by similarity and overall rating.  

## Languages and Libraries
- **Python 3**  
- **Pandas, NumPy** → data handling  

## How It Works
1. Load and clean the dataset.  
2. Build a **user–movie ratings matrix**.  
3. When a user inputs a movie:  
   - Find movies with the highest rating correlations.  
   - Rank them by similarity and rating.  
   - Return **Top N recommendations**.  

## Example

**Input Movie:** `Toy Story (1995)`  

**Top 5 Recommendations:**  
1. Finding Nemo (2003)  
2. Monsters, Inc. (2001)  
3. Shrek (2001)  
4. Aladdin (1992)  
5. The Lion King (1994)  


## Future Improvements
- Add **matrix factorization (SVD)** for better personalization.  
- Support **user-based collaborative filtering**.  
- Extend to **content-based recommendations** (genres, tags).  

## Dataset
This project uses the **MovieLens dataset** by [GroupLens Research](https://grouplens.org/datasets/movielens/).  
Make sure to place `ratings.csv` and `movies.csv` in the project directory.
