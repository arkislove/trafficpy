import db_connection
import mariadb

def add_vehicle(vehicle_type, plate_number, location_id):
    conn = db_connection.get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO vehicles (vehicle_type, model, color, image_path, created_at, plate_number, locations_id) VALUES (?, ?, ?, ?, NOW(), ?, ?)",
            (vehicle_type, "", "", "", plate_number, location_id)
        )
        conn.commit()
        print("New row inserted successfully.")
    except mariadb.Error as e:
        print(f"Error: {e}")

    conn.close()

def delete_vehicle(vehicle_id):
    conn = db_connection.get_connection()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM vehicles WHERE id = ?", (vehicle_id,))
        conn.commit()
        print("Vehicle deleted successfully.")
    except mariadb.Error as e:
        print(f"Error: {e}")

    conn.close()

def refresh_vehicle_list(tree):
    for i in tree.get_children():
        tree.delete(i)

    conn = db_connection.get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT v.id, v.type, v.model, v.color, v.image_path, v.created_at, v.plate_number, l.name as location
        FROM vehicles v 
        JOIN locations l 
        ON v.locations_id = l.id
    """)
    for row in cur:
        tree.insert("", "end", values=row)
    conn.close()

