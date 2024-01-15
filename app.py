import streamlit as st
import recommendation_functions

def main():

    # Set page configuration
    st.set_page_config(
        page_title="Your App Title",
        page_icon=":rocket:",
        # layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title(":rocket: Course Recommendation System")
    

    tab1, tab2 = st.tabs(["Trending 🔥", "Recommendation based on Course 🤩"])

    with tab1:
        
        st.write("""
            # Trending Courses based on Ratings

        Welcome to our platform! Discover the latest and most popular courses on our platform, curated based on user ratings for the best learning experience. Whether you want to upgrade your skills or explore a new field, these courses have received high praise from our users.

        ## How are these courses selected?

        Our trending courses are dynamically updated based on the ratings provided by our users. We analyze user feedback and ratings to bring you the top courses in various categories. This ensures that you have access to quality content that resonates with our learning community.

        ## Explore and Excel

        Take a closer look at the trending courses below, explore diverse topics, and find the perfect learning path for you. Dive into courses that have made an impact and join thousands of learners who have found success on our platform.

        Happy learning!
        """
        )

        tt = recommendation_functions.Popularity()
        st.write(tt.head(10))

    with tab2:
        
        st.write(
            """
        # Course Recommendation

        Curious to explore more courses similar to your favorite one? You're in the right place! Enter the name of a course you've enjoyed, and we'll use collaborative filtering to recommend five other courses that might pique your interest.

        ## How it works

        1. **Enter a Course Name:**
        Type the name of a course you've liked in the text box below.

        2. **Get Recommendations:**
        Click the "Get Recommendations" button, and we'll use collaborative filtering to suggest five courses that align with your interests.

        ## Ready to Discover?

        Give it a try! Enter the name of a course you enjoyed and explore new learning opportunities.

        **Note:** Our recommendation engine uses collaborative filtering to analyze user behavior and suggest courses based on similar preferences.
        """
        )

        current_course = st.text_input("Enter your current course...")

        # Button to trigger the recommendation
        if st.button("Get Recommendations"):
            # Call the recommend function with the input course and display the result
            recommendations = recommendation_functions.recommendation(current_course)
            
            st.write(recommendations)

if __name__ == '__main__':
    main()
