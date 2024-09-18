from database import get_connection, get_cursor

class Band:
    def __init__(self, band_id):
        self.band_id = band_id
        self.connection = get_connection()
        self.cursor = get_cursor(self.connection)

    def concerts(self):
        query = "SELECT * FROM concert WHERE bands_id = %s;"
        self.cursor.execute(query, (self.band_id,))
        return self.cursor.fetchall()

    def venues(self):
        query = """
            SELECT DISTINCT venues.*
            FROM venues
            JOIN concert ON concert.venues_id = venues.id
            WHERE concert.bands_id = %s;
        """
        self.cursor.execute(query, (self.band_id,))
        return self.cursor.fetchall()

    
    
    
    def play_in_venue(self, venue_title, date):
        query = """
            INSERT INTO concert (bands_id, venues_id, date)
            SELECT %s, venues.id, %s
            FROM venues
            WHERE venues.title = %s
            RETURNING *;
        """
        self.cursor.execute(query, (self.band_id, date, venue_title))
        self.connection.commit()
        return self.cursor.fetchone()



    def all_introductions(self):
        query = """
            SELECT venues.city, bands.name, bands.hometown
            FROM concert
            JOIN bands ON concert.bands_id = bands.id
            JOIN venues ON concert.venues_id = venues.id
            WHERE bands.id = %s;
        """
        self.cursor.execute(query, (self.band_id,))
        introductions = self.cursor.fetchall()
        return [
            f"Hello {city}!!!!! We are {band_name} and we're from {band_hometown}"
            for city, band_name, band_hometown in introductions
        ]

    @staticmethod
    def most_performances():
        connection = get_connection()
        cursor = get_cursor(connection)
        query = """
            SELECT bands.*, COUNT(concert.id) AS performance_count
            FROM bands
            JOIN concert ON concert.bands_id = bands.id
            GROUP BY bands.id
            ORDER BY performance_count DESC
            LIMIT 1;
        """
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result

    def __del__(self):
        self.cursor.close()
        self.connection.close()
