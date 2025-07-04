# Dein Kundenmanagement-System

kunden = {} # Ein Dictionary zum Speichern der Kunden. Schlüssel: Kundenname, Wert: Dictionary mit Details

def kunden_anzeigen():
    if not kunden:
        print("Der Katalog ist leer.")
        return

    print("\n--- Deine Kundenliste ---")
    for name, details in kunden.items():
        print(f"Name: {name}")
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

#-----------------------------------------------------------------
def kunde_hinzufuegen():
    print("\n--- Kunden hinzufügen ---")
    name = input("Name des Kunden: ")
    email = input("E-Mail des Kunden: ")
    telefon = input("Telefonnummer des Kunden: ")

    if name in kunden:
        print(f"Fehler: Kunde '{name}' existiert bereits im Katalog.")
        return

    kunden[name] = {
        "email": email,
        "telefon": telefon
    }
    print(f"Kunde '{name}' wurde hinzugefügt.")
#------------------------------------------------------------------
def kunde_suchen():
    print("\n--- Kunden suchen ---")
    suchbegriff = input("Geben Sie einen Suchbegriff (Name oder E-Mail) ein: ").lower()
    gefundene_kunden = {}

    for name, details in kunden.items():
        if suchbegriff in name.lower() or suchbegriff in details.get('email', '').lower():
            gefundene_kunden[name] = details

    if not gefundene_kunden:
        print(f"Keine Kunden gefunden, die '{suchbegriff}' im Namen oder in der E-Mail enthalten.")
        return

    print(f"\n--- Gefundene Kunden für '{suchbegriff}' ---")
    for name, details in gefundene_kunden.items():
        print(f"Name: {name}")
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

#------------------------------------------------------------------

def zeige_menue():
    print("\n--- CRM Menü ---")
    print("1. Kunde hinzufügen")
    print("2. Kunden anzeigen")
    print("3. Beenden")
    print("----------------")

def main():
    while True:
        zeige_menue()
        wahl = input("Ihre Wahl: ")

        if wahl == '1':
            kunde_hinzufuegen()
        elif wahl == '2':
            kunden_anzeigen()
        elif wahl == '3':
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

# Startet das Hauptprogramm, wenn die Datei direkt ausgeführt wird
if __name__ == "__main__":
    main()
