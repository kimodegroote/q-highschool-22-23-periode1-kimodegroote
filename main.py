# Maakt een variabele voor de while loop aan en maakt de lists waar de info in staat.
start = True
naam_list = []
geboorte_list = []
nummer_list = []
extra_list = []

while start is True:
    voeg_kijk_input = input("Typ 1 als u een contact wilt toevoegen, typ 2 als u uw contacten wilt bekijken, "
                            "typ 3 als u een contact wilt bewerken.")
# Voegt info toe aan de lists.
    if voeg_kijk_input == "1":
        start = False
        naam_input = input("Naam: ")
        geboorte_input = input("Geboortedatum: ")
        nummer_input = input("Telefoonnummer: ")
        extra_input = input("Extra informatie: ")
        naam_list.append(naam_input)
        geboorte_list.append(geboorte_input)
        nummer_list.append(nummer_input)
        extra_list.append(extra_input)
        print("Het contact is succesvol toegevoegd.")
        start = True
# Hiermee kan je de info bekijken.
    elif voeg_kijk_input == "2":
        if bool(naam_list):
            start = False
            print(", ".join(naam_list))
            naam_identificatie = input("Typ een naam uit deze lijst het te bekijken.")
            index_identificatie = naam_list.index(naam_identificatie)
            print("Naam: ", naam_list[index_identificatie])
            print("Geboorte datum: ", geboorte_list[index_identificatie])
            print("Telefoonnummer: ", nummer_list[index_identificatie])
            print("Extra informatie: ", extra_list[index_identificatie])

            start = True
        else:
            print("U heeft nog geen contacten toegevoegd.")
            start = True
# Detecteert of er iets in de lists staat,
    elif voeg_kijk_input == "3":
        start = False
        print(", ".join(naam_list))
        bewerk_start = True
        if bool(naam_list):
            bewerk_start = False
            naam_identificatie = input("Typ een naam uit deze lijst om het te bewerken.")
            index_identificatie = naam_list.index(naam_identificatie)
            bewerk_type_start = True
            while bewerk_type_start is True:
                bewerk_type_input = input(
                    "Typ 1 om de naam te bewerken, typ 2 om de geboortedatum te bewerken, typ 3 om het telefoonnummer "
                    "te "
                    "bewerken of typ 4 om de extra informatie te bewerken")
                # Hiermee kan je alle verschillende items bewerken.
                if bewerk_type_input == "1":
                    bewerk_type_start = False
                    naam_bewerk_input = input("Wat wordt de nieuwe informatie?")
                    naam_list[index_identificatie] = naam_bewerk_input
                    start = True
                elif bewerk_type_input == "2":
                    bewerk_type_start = False
                    geboorte_bewerk_input = input("Wat wordt de nieuwe informatie?")
                    geboorte_list[index_identificatie] = geboorte_bewerk_input
                    start = True
                elif bewerk_type_input == "3":
                    bewerk_type_start = False
                    nummer_bewerk_input = input("Wat wordt de nieuwe informatie?")
                    nummer_list[index_identificatie] = nummer_bewerk_input
                    start = True
                elif bewerk_type_input == "4":
                    bewerk_type_start = False
                    extra_bewerk_input = input("Wat wordt de nieuwe informatie?")
                    extra_list[index_identificatie] = extra_bewerk_input
                    start = True
                else:
                    bewerk_type_start = True
        else:
            print("U heeft nog geen contacten om te bewerken.")
            start = True
