from helper import *
from presentatie import * 
import csv

inkomsten={
    "Aardbeien-ijs-totaal": 1000,
    "vanille-ijs-totaal": 2000,
    "chocolade-ijs-totaal": 1500,
    "waterijsje-totaal": 750
}

totaal_inkomsten = som(inkomsten)
presenteer(inkomsten, totaal_inkomsten)

with open("boekhouding.csv", "w",newline="") as csvfile:
     writer = csv.writer(csvfile, delimiter=";")

     for key, value in inkomsten.items():
         writer.writerow([key, value])
