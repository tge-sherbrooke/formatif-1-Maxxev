# /// script
# requires-python = ">=3.9"
# dependencies = ["adafruit-circuitpython-ahtx0", "adafruit-blinka", "rpi.gpio"]
# ///
"""
Premiere lecture de capteur - AHT20
Cours 243-413-SH, Semaine 1
"""
import time
import board
import adafruit_ahtx0


def main():
    
    # Configuration du bus I2C
    i2c = board.I2C()

    try:
        # Creation de l'objet capteur AHT20
        sensor = adafruit_ahtx0.AHTx0(i2c)
        
        # Lecture des donnees
        print("=" * 50)
        print(" Capteur AHT20- Temperature et Humidite")
        print("=" * 50)
        
        # Faire 3 lectures pour demontrer la stabilite
        for i in range(3):
            temperature = sensor.temperature
            humidite = sensor.relative_humidity
            
            print(f"\nLecture {i+1}:")
            print(f" Temperature : {temperature:6.2f} C")
            print(f" Humidite : {humidite:7.1f} %")
            
            if i < 2:
                time.sleep(2)
        print("\n" + "=" * 50)
        print("Lecture terminee avec succes !")
        print("=" * 50)
        
    except Exception as e:
        print(f"\nERREUR: Impossible de lire le capteur")
        print(f"Detail: {e}")
        print("\nVerifications:")
        print(" 1. Le capteur est-il bien connecte ?")
        print(" 2. L'adresse I2C est-elle correcte ? (i2cdetect-y 1)")
        print(" 3. La bibliotheque adafruit-circuitpython-ahtx0 est-elle installee ?")

if __name__ == "__main__":
    main()