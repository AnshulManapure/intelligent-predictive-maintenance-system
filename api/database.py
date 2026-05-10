import sqlite3

DB_NAME = "predictive_maintenance.db"

conn = sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():
    conn.execute("""
                CREATE TABLE IF NOT EXISTS predictions(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                 engine_id INTEGER,
                 failure_probability REAL,
                 prediction TEXT,
                 threshold REAL,
                 model_version TEXT
                 )
                 """)
    
def save_prediction(values):
    conn.execute(
        """
        INSERT INTO predictions(
        engine_id,
        failure_probability,
        prediction,
        threshold,
        model_version
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (values['engine_id'], values['failure_probability'], values['prediction'], values['threshold'], values['model_version'])
    )
    conn.commit()

def get_predictions():
    res = conn.execute(
        """
        SELECT * FROM predictions
        ORDER BY timestamp DESC
        """
    )

    columns = [col[0] for col in res.description]
    return [dict(zip(columns, row)) for row in res.fetchall()]

def get_predictions_by_engine_id(engine_id):
    res = conn.execute(
        """
        SELECT * FROM predictions
        WHERE engine_id = ?
        ORDER BY timestamp DESC
        """,
        (engine_id,)
    )

    columns = [col[0] for col in res.description]
    return [dict(zip(columns, row)) for row in res.fetchall()]

