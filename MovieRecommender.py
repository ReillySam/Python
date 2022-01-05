# ================================================= Movie Recommender =================================================
'''
	Short and simple project to understand the fundamentals of machine learning.
	This program reads data from a csv file and recommends movies with common features to the movie title
	 that is searched by the user. It uses the cosine similarity to compute the weighting of most common
	 movies in the data set, based on these features.

	 Yet to add vote average as a weighting.
'''

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Read CSV File
df = pd.read_csv("movie_dataset.csv")
# print(df.head())
# print(df.columns)

# #Select Features
features = ['keywords', 'cast', 'director', 'genres', 'vote_average']

# #Create a column in DF which combines all selected features
for feature in features:
	df[feature] = df[feature].fillna('___')

# vote average function, not working yet
# def vote_processing(vote_average):
# 	return vote_average/vote_average.max()
#
# for feature in features:
# 	df[feature] = df[feature].apply(vote_processing)
#
# 	#df[feature].apply(lambda x: x / x.max(), axis=0)

def combine_features(row):
	try:
		return row['keywords'] +" "+ row['cast'] +" "+ row['director'] +" "+ row['genres'] #+" "+ row['vote_average']
	except:
		print("Error: ", row)


df["combined_features"] = df.apply(combine_features, axis=1)
# print("Combined Features:\n",df["combined_features"].head())

#Create count matrix from this new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

#Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)
# print("Cosine Similarity:\n",cosine_sim)

movie_user_likes = str(input("Enter a movie to search the recommendation list (Must begin with a capital letter): "))

#Get index of this movie from its title
movie_index = get_index_from_title(movie_user_likes)

similar_movies = list(enumerate(cosine_sim[movie_index]))		#creates list of tuples by count(enumerate) & index (0,0)

#Get a list of similar movies in descending order of similarity score
sort_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)


#Print titles of first 10 movies
i = 0
print("Top 10 Movie recommendations similar to", movie_user_likes, "are;")
for movie in sort_similar_movies:
	i += 1
	print(i, get_title_from_index(movie[0]))
	if i >= 10:
		break

		
###### helper functions to be for getting title and index #######
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
