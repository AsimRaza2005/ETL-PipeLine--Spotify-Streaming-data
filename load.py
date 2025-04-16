import pandas as pd
import mysql.connector

# Load CSV
df = pd.read_csv('data/Spotify_2024_Global_Streaming_Data.csv')

# Rename columns to match DB naming conventions
df.columns = [
    'country', 'artist', 'album', 'genre', 'release_year',
    'monthly_listeners_millions', 'total_streams_millions',
    'total_hours_streamed_millions', 'avg_stream_duration_min',
    'platform_type', 'streams_last_30_days_millions', 'skip_rate_percent'
]

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="datascience",
    database="my_db"
)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS spotify_streaming_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(100),
    artist VARCHAR(255),
    album VARCHAR(255),
    genre VARCHAR(100),
    release_year INT,
    monthly_listeners_millions FLOAT,
    total_streams_millions FLOAT,
    total_hours_streamed_millions FLOAT,
    avg_stream_duration_min FLOAT,
    platform_type VARCHAR(50),
    streams_last_30_days_millions FLOAT,
    skip_rate_percent FLOAT
);
""")

# Insert data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO spotify_streaming_data (
            country, artist, album, genre, release_year,
            monthly_listeners_millions, total_streams_millions,
            total_hours_streamed_millions, avg_stream_duration_min,
            platform_type, streams_last_30_days_millions, skip_rate_percent
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("Data loaded successfully.")
