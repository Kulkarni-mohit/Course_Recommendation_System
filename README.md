# Course Recommendation System
Welcome to the Course Recommendation System project! This project aims to provide personalized course recommendations based on user activity and preferences.

## Overview

The Course Recommendation System is designed to recommend online courses to users based on their activity and responses. It includes a machine learning model, implemented using collaborative filtering, to provide personalized course suggestions.

## Features

- Trending Courses: Display a list of trending courses based on user ratings.
- Course Recommendation: Allow users to input a course, and recommend 5 other courses using collaborative filtering.

## Dataset

The dataset used in this project is generated using ChatGPT, a language model developed by OpenAI. It includes user activity data and user responses, which are essential for training the recommendation model.

#### The dataset consists of two main files:

1. **Course Dataset:**
   - `course_id`: Unique identifier for each course.
   - `course_name`: Name of the course.
   - `course_category`: Category or topic of the course.
2. **User Activity Dataset:**
    - `user_id`: Unique identifier for each user.
    - `course_id`: Identifier for the course the user interacted with.
    - `time_spent`: Time spent by the user on the course (in hours).
    - `views_clicks`: Number of views or clicks on the course.
    - `course_completed`: Boolean indicating if the user completed the course.
    - `quiz_score`: User's score in quizzes related to the course.
    - `ratings`: User's rating for the course on a scale of 0 to 5.

## Installation and Usage

* pip install -r requirements.txt
* streamlit run app.py

## Demo
