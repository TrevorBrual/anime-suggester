from flask import Flask, request, jsonify
from flask_cors import CORS
from anime_data import anime_list

# Initialize Flask app (The Home Route, as shows the form)
app = Flask(__name__)
CORS(app)
# Need to enable CORS to allow React frontend to communicate with Flask backend

# Want to add description for each anime later on and have be able to pick different vibes if needed (Done)
# Make the website a lil better to look at. Look into react frameworks, want to use CSS libraries like TailwindCSS or Bootstrap
# Could add more filtering options like length of anime, year released, rating, etc.
# Maybe add a watchlist feature where users can save anime to watch later
# Could add user accounts and let users rate anime and get recommendations based on their ratings
# Could add a search feature to search for specific anime
# Could add a feature to recommend similar anime based on a selected anime
# Could add a feature to recommend anime based on mood or activities (e.g. studying, relaxing, etc.)
# Could add a feature to recommend anime based on time available (e.g. short anime for quick breaks, long anime for weekends, etc.)
# Could add a feature to recommend anime based on previously watched anime
# Want to deploy the app online using Heroku or another service
# Want to a feature that interacts with an external anime API to get more detailed information about each anime?
# Want to add a feature that allows to have users to have an external link to watch the anime on their preferred streaming service (e.g., Crunchyroll, Funimation, Netflix, etc.) if available 


@app.route('/recommend', methods=['POST'] )
def recommend():
    # React sends data as JSON, not a Form
    data = request.get_json()
    user_genre = data.get('genre')
    user_vibe = data.get('vibe')
    user_ratings = data.get('rating') 
    
    recommendations = []
    # for anime in anime_list:
    #     if user_genre in anime['genre'] or user_genre == 'Any':
    #         if user_vibe == "Any" or user_vibe == anime['vibe']:
    #             recommendations.append(anime)

    for anime in anime_list:
        match_genre = (user_genre in anime['genre'] or user_genre == anime['genre'])
        match_vibe = (user_vibe == "Any" or user_vibe == anime['vibe'])
        # Check if the anime matches the user's rating preferences
        # If the user slected No rating (empty list), then match all rating animes 
        # Otherwise, we check if the anime's rating is the one of the user's 
        if not user_ratings:
            match_rating = True
        else:
            match_rating = (anime.get('rating') in user_ratings)
        
        if match_genre and match_vibe and match_rating:
            recommendations.append(anime)
    # Return the list as JSON (JavaScript Object Notation)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
    