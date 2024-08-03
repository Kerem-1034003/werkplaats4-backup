import sqlite3

def init_db():
    conn = sqlite3.connect('weather_app.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS settings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT,
        departure TEXT,
        max_wind_speed REAL,
        max_rain_chance REAL,
        min_temp REAL,
        max_temp REAL,
        max_snow_chance REAL
    )
    ''')
    conn.commit()
    conn.close()

def save_settings_to_db(data):
    conn = sqlite3.connect('weather_app.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO settings (location, departure, max_wind_speed, max_rain_chance, min_temp, max_temp, max_snow_chance)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (data['location'], data['departure'], data['max_wind_speed'], data['max_rain_chance'], data['min_temp'], data['max_temp'], data['max_snow_chance']))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def get_settings_from_db(id):
    conn = sqlite3.connect('weather_app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM settings WHERE id = ?', (id,))
    settings = cursor.fetchone()
    conn.close()
    if settings:
        return {
            "location": settings[1],
            "departure": settings[2],
            "max_wind_speed": settings[3],
            "max_rain_chance": settings[4],
            "min_temp": settings[5],
            "max_temp": settings[6],
            "max_snow_chance": settings[7]
        }
    return None
