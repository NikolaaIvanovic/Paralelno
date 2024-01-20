from multiprocessing import Pool
import time
import math

def izracunaj_kvadrat_faktorijala(broj):
    r_faktorijela = math.factorial(broj)
    kvadrat_faktorijela = r_faktorijela * r_faktorijela

    # Simulacija zadatka koji oduzima vreme
    time.sleep(1)

    return kvadrat_faktorijela

def segmentiraj_brojeve(brojevi, djelilac):
    segmentirani_brojevi = {i: [] for i in range(djelilac)}
    for broj in brojevi:
        segmentirani_brojevi[broj % djelilac].append(broj)
    return segmentirani_brojevi

if __name__ == "__main__":
    pocetno_vrijeme = time.time()  # Pokreni tajmer

    
    brojevi = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ,17, 18, 19, 20, 21, 22, 23, 24, 25]

    # Broj procesa koje zelim iskoristiti

    broj_procesa = 4

    djelilac = 3  

    # Segmentiraj brojeve na osnovu ostatka pri deljenju sa djeliocem

    segmentirani_brojevi = segmentiraj_brojeve(brojevi, djelilac)

    with Pool(processes=broj_procesa) as bazen:

        rezultati = bazen.map(izracunaj_kvadrat_faktorijala, brojevi)

    for broj, rezultat in zip(brojevi, rezultati):
        print(f"Kvadrat faktorijela od {broj}: {rezultat}")

    konacno_vrijeme = time.time()  # Zaustavi tajmer

    # Izračunaj i prikazi ukupno vrijeme izvršavanja


    ukupno_vrijeme = konacno_vrijeme - pocetno_vrijeme
    print(f"Ukupno vrijeme izvršavanja: {ukupno_vrijeme} sekundi")

    # Prikazi segmentirane brojeve
    print(f"Segmentovani brojevi na osnovu ostatka pri djijeljenju sa {djelilac}:")
    for ostatak, segmentirana_lista in segmentirani_brojevi.items():
        print(f"Ostatak {ostatak}: {segmentirana_lista}")