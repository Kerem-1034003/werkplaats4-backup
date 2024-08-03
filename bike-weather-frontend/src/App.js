import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
import './App.css'; // Importeer je CSS-bestand

const App = () => {
  const [settings, setSettings] = useState(null);
  const [weatherData, setWeatherData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const userId = Cookies.get('userId');
    if (userId) {
      fetchWeather(userId);
    } else {
      setLoading(false);
    }
  }, []);

  const saveSettings = async (newSettings) => {
    console.log('Saving settings:', newSettings);
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/weather', newSettings, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      console.log('Response:', response.data);
      const { id } = response.data;
      Cookies.set('userId', id);
      setSettings(newSettings);
      fetchWeather(id);
    } catch (err) {
      console.error('Failed to save settings:', err);
      setError('Failed to save settings');
    }
  };

  const fetchWeather = async (userId) => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/api/weather/${userId}`);
      setWeatherData(response.data);
      setLoading(false);
    } catch (err) {
      console.error('Failed to fetch weather data:', err);
      setError('Failed to fetch weather data');
      setLoading(false);
    }
  };

  const handleGoBack = () => {
    setSettings(null); // Reset settings to show the form again
    setWeatherData(null); // Clear weather data
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!settings) {
    return (
      <div className="form-container">
        <h1 className="form-title">Set Your Weather Preferences</h1>
        <form onSubmit={(e) => {
          e.preventDefault();
          const formData = new FormData(e.target);
          const newSettings = {
            location: formData.get('location'),
            departure: formData.get('departure'),
            max_wind_speed: parseFloat(formData.get('max_wind_speed')),
            max_rain_chance: parseFloat(formData.get('max_rain_chance')),
            min_temp: parseFloat(formData.get('min_temp')),
            max_temp: parseFloat(formData.get('max_temp')),
            max_snow_chance: parseFloat(formData.get('max_snow_chance'))
          };
          saveSettings(newSettings);
        }} className="settings-form">
          <div>
            <label>Location: <input name="location" type="text" required /></label>
          </div>
          <div>
            <label>Departure: <input name="departure" type="text" defaultValue="08:00" required /></label>
          </div>
          <div>
            <label>Max Wind Speed: <input name="max_wind_speed" type="number" step="0.1" defaultValue="3.0" required /></label>
          </div>
          <div>
            <label>Max Rain Chance: <input name="max_rain_chance" type="number" step="0.1" defaultValue="25" required /></label>
          </div>
          <div>
            <label>Min Temp: <input name="min_temp" type="number" step="0.1" defaultValue="5" required /></label>
          </div>
          <div>
            <label>Max Temp: <input name="max_temp" type="number" step="0.1" defaultValue="30" required /></label>
          </div>
          <div>
            <label>Max Snow Chance: <input name="max_snow_chance" type="number" step="0.1" defaultValue="10" required /></label>
          </div>
          <button type="submit">Save Settings</button>
        </form>
      </div>
    );
  }

  return (
    <div className="weather-container">
      <h1>Weather Forecast for {weatherData?.location}</h1>
      {weatherData && weatherData.okay_to_bike.map((day, index) => (
        <div key={index} className="weather-item">
          <p>{day.date}:</p>
          <img
            className="bike-image"
            src={day.bike_okay ? '/images/good_bike.jpg' : '/images/notgood_bike.png'}
            alt={day.bike_okay ? 'Good to bike' : 'Not good to bike'}
          />
        </div>
      ))}
      <div className="button-wrapper">
        <button onClick={handleGoBack} className="back-button">Go Back to Settings</button>
      </div>
    </div>
  );
};

export default App;
