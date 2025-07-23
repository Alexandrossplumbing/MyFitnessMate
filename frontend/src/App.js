// src/App.js
import React, { useState } from "react";
import "./App.css";
import "react-circular-progressbar/dist/styles.css";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";

function App() {
  const [date, setDate] = useState(new Date().toISOString().split("T")[0]);
  const [food, setFood] = useState("");
  const [calories, setCalories] = useState([]);
  const [error, setError] = useState(null);

  const calorieGoal = 3839;
  const totalCalories = calories.reduce((sum, entry) => sum + entry.calories, 0);
  const percentage = Math.min((totalCalories / calorieGoal) * 100, 100);

  const handleSearch = async () => {
    try {
      const response = await fetch(`https://solid-chainsaw-69v99pgv5jvp2qij-8001.app.github.dev/food/${food}`);
      const data = await response.json();

      if (response.ok) {
        setCalories([...calories, { name: food, calories: data.calories }]);
        setError(null);
        setFood("");
      } else {
        setError("Food not found.");
      }
    } catch (err) {
      setError("Error fetching data.");
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1 style={{ color: "#1976d2" }}>MyFitnessMate</h1>

      <div>
        <label>Date: </label>
        <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
      </div>

      <h2>Today's Progress</h2>
      <div style={{ width: 120, margin: "20px auto" }}>
        <CircularProgressbar
          value={percentage}
          text={`${Math.round(percentage)}%`}
          styles={buildStyles({ textColor: "#1976d2", pathColor: "#1976d2" })}
        />
        <p style={{ textAlign: "center" }}>{totalCalories} / {calorieGoal} cal</p>
      </div>

      <h3>Remaining Calories</h3>
      <p style={{ color: "green", fontSize: "24px" }}>{calorieGoal - totalCalories}</p>

      <div>
        <input
          type="text"
          value={food}
          placeholder="Search food"
          onChange={(e) => setFood(e.target.value)}
        />
        <button onClick={handleSearch}>Add Food</button>
        <button disabled style={{ marginLeft: "10px" }}>Scan Barcode</button>
      </div>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <div>
        <h4>Macronutrients</h4>
        <p><span style={{ color: "blue" }}>●</span> Protein (placeholder)</p>
      </div>
    </div>
  );
}

export default App;
