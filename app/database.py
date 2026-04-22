import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def save_weather(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO weather_readings 
        (city, country, temp, humidity, description, wind_speed)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        data["city"],
        data["country"],
        data["temp"],
        data["humidity"],
        data["description"],
        data["wind_speed"]
    ))
    conn.commit()
    cur.close()
    conn.close()

def get_history(city):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT temp, humidity, description, wind_speed, recorded_at
        FROM weather_readings
        WHERE city = %s
        ORDER BY recorded_at DESC
        LIMIT 24
    """, (city,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows