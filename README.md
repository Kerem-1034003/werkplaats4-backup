## Bike Weather App

The Bike Weather App helps users determine if the weather is suitable for biking based on their personal preferences.

## Developers

Kerem Yildiz (1034004)

## Installation Requirements

Ensure you have the following software installed:

- Python 3.x
- Node.js
- npm (Node Package Manager)

## Installation

Backend:

Install the required Python packages:

- pip install -r requirements.txt

- be sure that requests and flask-cors are installed.

Frontend:

Navigate to the frontend directory:

- cd bike-weather-frontend

Install the required npm packages:

- npm install
- npm install axios js-cookie

## Starting the Application

Backend:

- flask run (terminal cmd)
- The application is now accessible at: http://127.0.0.1:5000

frontend:

Navigate to the frontend directory (if not already done):

- cd bike-weather-frontend (terminal bash)

- npm start(terminal bash)
- The frontend is now accessible at: http://localhost:3000

## Test

Setting Weather Preferences

- Open the application in your browser.
- Fill out the form with your weather preferences and location.
- Click the "Save Settings" button to save your preferences.

Viewing Weather Results

- After saving your preferences, the application will fetch the weather forecast for your location and preferences.
- The results will be displayed with a date and a bike image (green if it is good to bike, red if it is not good to bike).
- To return to the settings form, click the "Go Back to Settings" button.

## Setting Up OpenWeatherMap API Key

Go to the OpenWeatherMap website: https://openweathermap.org/

Create an account:

- Click on "Sign Up" or "Get Started" in the top right corner of the website.
- Fill in the registration form with your details (username, email, password, etc.).
- Click on the "Create Account" button to complete your registration.
- After registration, you will receive a confirmation email. Follow the instructions in the email to activate your account.

Log in to your account:

- Go back to the OpenWeatherMap website and click on "Sign In" in the top right corner.
- Log in with your registered email and password.

Obtain an API key:

- After logging in, navigate to the "API keys" section under your account settings. This can usually be found by clicking on your profile in the top right corner and then on "API keys" in the dropdown menu.
- Click on the "Generate" or "Create API Key" button.
- Name your API key, for example, "WeatherApp".
- Click on "Generate" or "Create" to create the API key.
  Copy your API key:

- After generating the API key, it will be displayed in your list of API keys.
- Copy the API key, you will need it to request weather data in your application.
- Config.py: paste the api key in the following line OPENWEATHERMAP_API_KEY = 'YOUR_API_KEY_HERE'

## Resources

python:

- https://flask.palletsprojects.com/en/3.0.x/
- https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing
- https://www.youtube.com/watch?v=qbLc5a9jdXo

React:

- https://www.youtube.com/watch?v=SqcY0GlETPk
- https://react.dev/learn/installation
- https://react.dev/learn

Html+css:

- https://www.w3schools.com/js/

Api:

- https://openweathermap.org/

## Version

- Current version: v1.0
- Release date: 14-06-2023
