from database import get_connection, get_cursor

class Venue:
    def __init__(self, venue_id):
        self.venue_id = venue_id
        self.connection = get_connection()
        self.cursor = get_cursor(self.connection)

    def concerts(self):
        query = "SELECT * FROM concert WHERE venues_id = %s;"
        self.cursor.execute(query, (self.venue_id,))
        return self.cursor.fetchall()

    def bands(self):
        query = """
            SELECT DISTINCT bands.*
            FROM bands
            JOIN concert ON concert.bands_id = bands.id
            WHERE concert.venues_id = %s;
        """
        self.cursor.execute(query, (self.venue_id,))
        return self.cursor.fetchall()

    def concert_on(self, date):
        query = "SELECT * FROM concert WHERE venues_id = %s AND date = %s LIMIT 1;"
        self.cursor.execute(query, (self.venue_id, date))
        return self.cursor.fetchone()

    def most_frequent_band(self):
        query = """
            SELECT bands.*, COUNT(concert.id) AS performance_count
            FROM bands
            JOIN concert ON concert.bands_id = bands.id
            WHERE concert.venues_id = %s
            GROUP BY bands.id
            ORDER BY performance_count DESC
            LIMIT 1;
        """
        self.cursor.execute(query, (self.venue_id,))
        return self.cursor.fetchone()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
