def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag / personen
    return f"het bedrag per persoon is {berdrag_pp} euro."

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def som(mijn_dict):
    totaal = 0

    for value in mijn_dict.values():
        totaal += value

    return totaal