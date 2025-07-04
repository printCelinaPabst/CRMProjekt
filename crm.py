import json
# Dein Kundenmanagement-System

kunden = {} # Ein Dictionary zum Speichern der Kunden. Schlüssel: Kundenname, Wert: Dictionary mit Details
DATEINAME = "kunden.json" # NEU: Dateiname für die Speicherung des Katalogs

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
def kunde_aktualisieren():
    print("\n--- Kunden aktualisieren ---")
    name_zu_aktualisieren = input("Name des zu aktualisierenden Kunden: ")

    if name_zu_aktualisieren not in kunden:
        print(f"Fehler: Kunde '{name_zu_aktualisieren}' nicht im Katalog gefunden.")
        return

    print(f"Aktuelle Daten für {name_zu_aktualisieren}:")
    print(f"  E-Mail: {kunden[name_zu_aktualisieren]['email']}")
    print(f"  Telefon: {kunden[name_zu_aktualisieren]['telefon']}")

    neue_email = input("Neue E-Mail (leer lassen für keine Änderung): ")
    neue_telefon = input("Neue Telefonnummer (leer lassen für keine Änderung): ")

    if neue_email:
        kunden[name_zu_aktualisieren]['email'] = neue_email
    if neue_telefon:
        kunden[name_zu_aktualisieren]['telefon'] = neue_telefon

    print(f"Kunde '{name_zu_aktualisieren}' wurde aktualisiert.")
#------------------------------------------------------------------
def kunde_loeschen():
    print("\n--- Kunden löschen ---")
    name_zu_loeschen = input("Name des zu löschenden Kunden: ")
    if name_zu_loeschen in kunden:
        del kunden[name_zu_loeschen]
        print(f"Kunde '{name_zu_loeschen}' wurde aus dem Katalog entfernt.")
    else:
        print(f"Fehler: Kunde '{name_zu_loeschen}' nicht im Katalog gefunden.")
#------------------------------------------------------------------
def katalog_speichern():
    try:
        with open(DATEINAME, 'w', encoding='utf-8') as f:
            json.dump(kunden, f, indent=4, ensure_ascii=False)
        print(f"Katalog erfolgreich in '{DATEINAME}' gespeichert.")
    except IOError as e:
        print(f"Fehler beim Speichern des Katalogs: {e}")

def katalog_laden():
    global kunden
    try:
        with open(DATEINAME, 'r', encoding='utf-8') as f:
            kunden.update(json.load(f))
        print(f"Katalog erfolgreich aus '{DATEINAME}' geladen.")
    except FileNotFoundError:
        print("Keine vorhandene Katalogdatei gefunden. Starte mit leerem Katalog.")
        kunden.clear()
    except json.JSONDecodeError as e:
        print(f"Fehler beim Laden des Katalogs (ungültiges JSON): {e}. Starte mit leerem Katalog.")
        kunden.clear()
    except Exception as e:
        print(f"Ein unerwarteter Fehler beim Laden ist aufgetreten: {e}. Starte mit leerem Katalog.")
        kunden.clear()
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
