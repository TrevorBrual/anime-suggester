from flask import Flask, request, jsonify
from flask_cors import CORS
from anime_data import anime_list

# Initialize Flask app (The Home Route, as shows the form)
app = Flask(__name__)
CORS(app)
# Need to enable CORS to allow React frontend to communicate with Flask backend

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
    