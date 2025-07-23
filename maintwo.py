import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Dialog, DialogTrigger, DialogContent } from "@/components/ui/dialog";

const foodDatabase = {
  "banana": { calories: 89, protein: 1.1, carbs: 23, fat: 0.3 },
  "chicken breast": { calories: 165, protein: 31, carbs: 0, fat: 3.6 },
  "rice": { calories: 130, protein: 2.4, carbs: 28, fat: 0.3 },
  "broccoli": { calories: 55, protein: 3.7, carbs: 11, fat: 0.6 },
  "egg": { calories: 68, protein: 6, carbs: 0.6, fat: 4.8 },
  "apple": { calories: 52, protein: 0.3, carbs: 14, fat: 0.2 },
};

export default function MacroTracker() {
  const [foodInput, setFoodInput] = useState("");
  const [log, setLog] = useState([]);

  const [weight, setWeight] = useState(70);
  const [height, setHeight] = useState(175);
  const [goalCalories, setGoalCalories] = useState(3839);

  const addFood = () => {
    const food = foodInput.toLowerCase();
    if (foodDatabase[food]) {
      setLog([...log, { name: food, ...foodDatabase[food] }]);
    }
    setFoodInput("");
  };

  const handleBarcodeScan = () => {
    const barcodeFood = "apple"; // Simulated barcode result
    if (foodDatabase[barcodeFood]) {
      setLog([...log, { name: barcodeFood, ...foodDatabase[barcodeFood] }]);
    }
  };

  const filteredFoods = Object.keys(foodDatabase).filter(food =>
    food.includes(foodInput.toLowerCase())
  );

  const totals = log.reduce(
    (acc, food) => {
      acc.calories += food.calories;
      acc.protein += food.protein;
      acc.carbs += food.carbs;
      acc.fat += food.fat;
      return acc;
    },
    { calories: 0, protein: 0, carbs: 0, fat: 0 }
  );

  const percentage = ((totals.calories / goalCalories) * 100).toFixed(1);

  return (
    <div className="max-w-3xl mx-auto p-6 font-sans">
      <header className="flex justify-between items-center py-4 border-b mb-6">
        <h1 className="text-2xl font-bold text-blue-600">FitTracker</h1>
        <Dialog>
          <DialogTrigger asChild>
            <Button variant="outline">Profile</Button>
          </DialogTrigger>
          <DialogContent className="space-y-4">
            <h2 className="text-lg font-semibold">User Profile</h2>
            <div className="space-y-2">
              <label className="block text-sm">Body Weight (kg)</label>
              <Input
                type="number"
                value={weight}
                onChange={(e) => setWeight(Number(e.target.value))}
              />
            </div>
            <div className="space-y-2">
              <label className="block text-sm">Height (cm)</label>
              <Input
                type="number"
                value={height}
                onChange={(e) => setHeight(Number(e.target.value))}
              />
            </div>
            <div className="space-y-2">
              <label className="block text-sm">Calorie Goal</label>
              <Input
                type="number"
                value={goalCalories}
                onChange={(e) => setGoalCalories(Number(e.target.value))}
              />
            </div>
          </DialogContent>
        </Dialog>
      </header>

      <section className="bg-white shadow rounded-2xl p-6 mb-6">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-semibold">Today's Progress</h2>
          <p className="text-gray-500 text-sm">{new Date().toDateString()}</p>
        </div>
        <div className="flex items-center justify-center">
          <div className="text-center">
            <div className="text-4xl font-bold">{totals.calories}</div>
            <div className="text-gray-500 text-sm">of {goalCalories} cal</div>
            <div className="text-blue-600 text-sm">{percentage}% complete</div>
          </div>
        </div>
        <div className="text-center mt-4 text-green-600 font-semibold">
          Remaining Calories: {goalCalories - totals.calories}
        </div>
        <div className="flex gap-4 justify-center mt-6">
          <Button onClick={addFood} className="bg-blue-600 hover:bg-blue-700">+ Add Food</Button>
          <Button variant="outline" onClick={handleBarcodeScan}>Scan Barcode</Button>
        </div>
        <div className="flex justify-center mt-4">
          <Input
            placeholder="Enter food (e.g., banana)"
            value={foodInput}
            onChange={(e) => setFoodInput(e.target.value)}
            className="w-1/2"
          />
        </div>
        {foodInput && (
          <ul className="mt-2 text-sm text-gray-600">
            {filteredFoods.map((item, i) => (
              <li key={i} onClick={() => setFoodInput(item)} className="cursor-pointer hover:underline">
                {item}
              </li>
            ))}
          </ul>
        )}
      </section>

      <section className="bg-white shadow rounded-2xl p-6">
        <h3 className="text-lg font-semibold mb-4">Macronutrients</h3>
        <div className="space-y-2 text-sm">
          <p><span className="text-blue-600 font-semibold">Protein:</span> {totals.protein.toFixed(1)}g</p>
          <p><span className="text-blue-600 font-semibold">Carbs:</span> {totals.carbs.toFixed(1)}g</p>
          <p><span className="text-blue-600 font-semibold">Fat:</span> {totals.fat.toFixed(1)}g</p>
        </div>
        <div className="mt-6 border-t pt-4">
          <h4 className="text-sm font-medium mb-2">Food Log</h4>
          <ul className="text-sm space-y-1">
            {log.map((item, index) => (
              <li key={index} className="capitalize">
                {item.name} - {item.calories} kcal, {item.protein}g P, {item.carbs}g C, {item.fat}g F
              </li>
            ))}
          </ul>
        </div>
      </section>
    </div>
  );
}

