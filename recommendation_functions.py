import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# loading Dataset
course_details = pd.read_csv("course_details.csv")
user_activity = pd.read_csv("user_activity.csv")


# Merging both csv files on column: course_id 
df = pd.merge(course_details, user_activity, on = 'course_id')

# converting categorical values into numerical codes 
df['course_category'] = df['course_category'].astype('category').cat.codes


def Popularity():
    """
        The function returns the top trending courses
        based on average ratings and no of ratings of the courses.
    """
    trending = df.groupby('course_name').mean()['rating'].reset_index()
    no_rating = df.groupby('course_name').sum()['rating'].reset_index()
    trending.rename(columns = {'rating': 'avg_rating'},inplace=True)
    trending = pd.merge(trending, no_rating, on = 'course_name')
    tt = trending.sort_values('avg_rating', ascending = False).reset_index()
    return tt


def recommend(course,similarity,pt):

  index = np.where(pt.index == course)[0][0]
  similar_items = sorted(list(enumerate(similarity[0])), key = lambda x:x[1], reverse=True)[1:4]

  return similar_items


def recommendation(course):
    """
    Input: Course name
    Returns list of recommended courses based on collaborative filtering
    """

    pt = df.pivot_table(index= 'course_name', columns = 'user_id', values = 'rating')  
    pt.fillna(0, inplace = True)
    similarity = cosine_similarity(pt)
    final_list = recommend(course, similarity, pt)
    fl = []
    for i in final_list:
        fl.append(pt.index[i[0]])
    print(fl)
    return fl


# recommendation('Mobile App Development with React Native')

