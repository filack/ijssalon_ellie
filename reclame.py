from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak{smaak},van {prijs} euro voor {nieuwe_prijs:.2f}euro."

def inkomsten_totaal(inkomsten, btw):
   totaal = sum(inkomsten)
   bedrag_btw = totaal * btw
   return f"het totaal van alle inkomsten van deze week is {totaal} euro, waarvover {bedrag_btw} euro betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"de gemiddelde inkomsten deze week zijn {bedrag} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])