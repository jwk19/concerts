from database import get_connection, get_cursor

class Concert:
    def __init__(self, concert_id):
        self.concert_id = concert_id
        self.connection = get_connection()
        self.cursor = get_cursor(self.connection)

    def band(self):
        query = """
            SELECT bands.*
            FROM bands
            JOIN concert ON concert.bands_id = bands.id
            WHERE concert.id = %s;
        """
        self.cursor.execute(query, (self.concert_id,))
        return self.cursor.fetchone()

    def venue(self):
        query = """
            SELECT venues.*
            FROM venues
            JOIN concert ON concert.venues_id = venues.id
            WHERE concert.id = %s;
        """
        self.cursor.execute(query, (self.concert_id,))
        return self.cursor.fetchone()

    def hometown_show(self):
        query = """
            SELECT CASE
                WHEN bands.hometown = venues.city THEN true
                ELSE false
            END AS hometown_show
            FROM concert
            JOIN bands ON concert.bands_id = bands.id
            JOIN venues ON concert.venues_id = venues.id
            WHERE concert.id = %s;
        """
        self.cursor.execute(query, (self.concert_id,))
        return self.cursor.fetchone()[0]

    def introduction(self):
        query = """
            SELECT venues.city, bands.name, bands.hometown
            FROM concert
            JOIN bands ON concert.bands_id = bands.id
            JOIN venues ON concert.venues_id = venues.id
            WHERE concert.id = %s;
        """
        self.cursor.execute(query, (self.concert_id,))
        city, band_name, band_hometown = self.cursor.fetchone()
        return f"Hello {city}!!!!! We are {band_name} and we're from {band_hometown}"

    def __del__(self):
        self.cursor.close()
        self.connection.close()
