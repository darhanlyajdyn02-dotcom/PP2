import psycopg2
from datetime import datetime

# ---CONNECTION SETTINGS ---
DB_CONFIG = {
    "dbname": "Snake",     
    "user": "postgres",       
    "password": "12345678", 
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    """Creates a connection to the database."""
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    """Creates the players and game_sessions tables if they do not already exist."""
    conn = get_connection()
    cur = conn.cursor()
    
    #Players table (username is unique)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    """)
    
    # Table of game sessions (linked to a player via player_id)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS game_sessions (
            id SERIAL PRIMARY KEY,
            player_id INTEGER REFERENCES players(id) ON DELETE CASCADE,
            score INTEGER NOT NULL,
            level_reached INTEGER NOT NULL,
            played_at TIMESTAMP DEFAULT NOW()
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()

def get_or_create_player(username):
    """
    Checks if the player exists in the database.
If not, creates one. Returns the player's ID.
    """
    conn = get_connection()
    cur = conn.cursor()
    
    # We try to insert a player, if the name is taken - we just do nothing (ON CONFLICT)
    cur.execute("""
        INSERT INTO players (username) VALUES (%s)
        ON CONFLICT (username) DO NOTHING;
    """, (username,))
    
    # Get the player ID (existing or newly created)
    cur.execute("SELECT id FROM players WHERE username = %s;", (username,))
    player_id = cur.fetchone()[0]
    
    conn.commit()
    cur.close()
    conn.close()
    return player_id

def save_result(player_id, score, level):
    """Saves the game result to the database."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO game_sessions (player_id, score, level_reached)
        VALUES (%s, %s, %s);
    """, (player_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

def get_personal_best(player_id):
    """Returns the maximum record of a specific player."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id = %s;", (player_id,))
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return result if result is not None else 0
def get_top_scores(limit=10):
    """Gets top 10 best results without crashing."""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT p.username, s.score, s.level_reached, s.played_at
            FROM game_sessions s
            JOIN players p ON s.player_id = p.id
            ORDER BY s.score DESC
            LIMIT %s;
        """, (limit,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows # Returns a list of tuples
    except Exception as e:
        print(f"Ошибка БД в Leaderboard: {e}")
        return []