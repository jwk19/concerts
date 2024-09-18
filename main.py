from venue import Venue
from band import Band
from concert import Concert
def main():
    # Example: Get concerts for a venue
    venue = Venue(1)  # Assuming venue with id=1 exists
    print("Concerts at Venue 1:", venue.concerts())

    # Example: Get all concerts a band has played
    band = Band(1)  # Assuming band with id=1 exists
    print("Concerts played by Band 1:", band.concerts())

    # Example: Add a new concert for Band 1 at "The Shrine" on "2024-09-18"
    new_concert = band.play_in_venue("The Shrine", "2024-09-18")
    print("New Concert added:", new_concert)

    # Example: Get band information for a specific concert
    concert = Concert(1)  # Assuming concert with id=1 exists
    print("Band performing at Concert 1:", concert.band())

main()
