import importlib

modules = {
    "1": "Files.module1",
    "2": "Files.module2",
    "3": "Files.module3",
    "4": "Files.module4",
    "5": "Files.module5",
    "6": "Files.module6",
    "7": "Files.module7",
    "8": "Files.module8",
    "9": "Files.module9",
    "10": "Files.module10"
}

def peamenüü():
    while True:
        print("Vali number, mille mooduli soovid laadida ja käivitada:")
        for key in modules:
            print(f"{key}. Moodul {key}")

        valik = input("Sisesta number (või 'q' väljumiseks): ")

        if valik.lower() == 'q':
            break
        elif valik in modules:
            try:
                mooduli_nimi = modules[valik]
                moodul = importlib.import_module(mooduli_nimi)

                if hasattr(moodul, 'main'):
                    moodul.main()
                else:
                    print(f"Moodul {mooduli_nimi} ei sisalda funktsiooni main().")
            except ImportError:
                print(f"Ei õnnestu importida moodulit {mooduli_nimi}.")
        else:
            print("Vigane valik, proovi uuesti.")

if __name__ == "__main__":
    peamenüü()