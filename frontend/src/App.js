import React, {useState} from 'react';
import './App.css';

function App() {
  const [genre, setGenre] = useState("Any");
  const [vibe, setVibe] = useState("Any");
  const [selectedRatings, setSelectedRatings] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const ratingOptions = ["G", "PG", "PG-13", "R"];
  //const [description, setDescription] = useState("");

  // Funtion to handle checking/unchecking rating checkboxes
  function handleRatingChange(e) {
    const value = e.target.value;
    const isChecked = e.target.checked;
    if (isChecked) {
      setSelectedRatings([...selectedRatings, value]);
    } else {
      setSelectedRatings(selectedRatings.filter((item) => item !== value));
    }
  }

  // This function runs when you click the button
  const getRecommendations = async () => {
    const response = await fetch('http://127.0.0.1:5000/recommend', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({genre: genre, vibe: vibe, ratings: selectedRatings}),
    });
  
    const data = await response.json();
    setRecommendations(data);
  };

  return ( // Drop down selects for genre and vibe
    <div className = "App" style={{ padding: "20px", fontFamily: "Arial, sans-serif"}}>
      <h1>Anime Suggestor</h1>
      {/*INPUT SECTION*/}
      <div style={{marginBottom: "20px"}}>
        <label><strong>Genre:</strong></label>
        <select onChange ={(e) => setGenre(e.target.value)}>
          <option value = "Any">Any</option>
          <option value = "Action">Action</option>
          <option value = "Adventure">Adventure</option>
          <option value = "Comedy">Comedy</option>
          <option value = "Horror">Horror</option>
          <option value = "Romance">Romance</option>
          <option value = "Sports">Sports</option>
          <option value = "Sci-Fi">Sci-Fi</option>
        </select>
        <label style={{ marginLeft: "10px"}}><strong>Vibe: </strong></label>
        <select onChange = {(e) => setVibe(e.target.value)}>
          <option value = "Any">Any</option>
          <option value = "Dark">Dark</option>
          <option value = "Emotional">Emotional</option>
          <option value = "Exciting">Exciting</option>
          <option value = "Funny">Funny</option>
          <option value = "Storytelling">Storytelling</option>
        </select>
      <div style={{ display: "inline-block", marginLeft: "10px"}}>

      {/* RATING CHECKBOXES */}
      <div style = {{marginBottom: "20px", padding: "10px", border: "1px solid #ddd"}}>
        <strong>Filter by rating </strong><br/>  

        {ratingOptions.map((rating) => (
          <label key = {rating} style = {{ marginRight: "15px", cursor: "pointer"}}>
            <input 
              type = "checkbox"
              value = {rating}
              onChange = {handleRatingChange}
              />
              {rating}
          </label>
        ))}
      </div>

      <button onClick = {getRecommendations} style = {{ padding: "10px 20px" }}>
          Get Anime Recommendations
      </button>
      </div>

      {/* RESULTS SECTION */}
      <div style = {{ marginTop: "30px"}}>
        {recommendations.map((anime, index) => (
          <div key = {index} style = {{ borderBottom: "1px solid #ccc", padding: "10px 0" }}>
            <h3>{anime.title} <span style = {{ fontSize: "0.8em", color: "#666" }}>({anime.rating})</span></h3>
          <p><em>{anime.genre} • {anime.vibe}</em></p>
          <p>{anime.Description}</p>
          </div>
        ))}
        </div>
      </div>
    </div>
  );
}
export default App;