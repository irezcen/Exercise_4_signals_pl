import numpy as np
import pandas as pd
import math
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import os


def gasnaca_sinusoida(xmin, xmax, liczba_punktow, amp, w, phi, y, b):
    t = np.linspace(xmin, xmax, liczba_punktow)
    f = math.e**(-y * t) * amp * np.sin(2 * math.pi * w * t + phi) + b + amp/10*(np.random.rand(len(t))-0.5)
    dane_funkcji = {"t": t, "f": f}
    pd.DataFrame(dane_funkcji).to_csv("dane gasnacej sinusoidy.csv", index=True, sep="\t")


def fitowanie_funkcji():
    try:
        dane_funkcji = pd.read_csv("dane gasnacej sinusoidy.csv", sep="\t")
        t = np.array(dane_funkcji["t"])
        f = np.array(dane_funkcji["f"])
        p0 = [1, 1, 1, 1, 1]
        dopasowane_parametry, covariance_matrix = curve_fit(funkcja, t, f, p0=p0)
        plt.scatter(t, f)
        plt.plot(t, funkcja(t, *dopasowane_parametry), 'b')
        plt.show()
    except FileNotFoundError:
        print('Najpierw podaj dane funkcji')
        interfejs()
    except TypeError:
        print('liczba orgumentów musi być większa od 5')


def funkcja(t, amp, w, phi, y, b):
    return math.e**(-y * t) * amp * np.sin(2 * math.pi * w * t + phi) + b


def start():
    print("witaj! W czym moge pomóc?")
    interfejs()


def interfejs():
    opcje = ['podaj parametry funkcji', 'pokaż funkcję', 'zamknij program']
    for i in range(0, len(opcje), 1):
        print(i+1, ": ", opcje[i], "-->", i+1)
    menu()


def menu():
    wybor_uzytkownika = input()
    if wybor_uzytkownika == '1':
        podawanie_parametrow()
        interfejs()
    elif wybor_uzytkownika == '2':
        try:
            fitowanie_funkcji()
        except RuntimeError:
            print("podaj parametry, dla których funkcja przyjmuje wartości rzeczywiste")
        interfejs()
    elif wybor_uzytkownika == '3':
        os.remove("dane gasnacej sinusoidy.csv")
        exit(0)
    else:
        print("nieznana opcja", wybor_uzytkownika, "spróbuj jeszcze raz")
        menu()


def podawanie_parametrow():
    parametry = []
    nazwa_parametrow = ['najmnijeszy argument', 'najwiekszy argument', 'liczba argumentow', 'amplitudaa sinusoidy',
                        'pulsacja', 'przesuniecie fazowe', 'wspolczynnik tlumienia', 'offset']
    for i in range(0, len(nazwa_parametrow), 1):
        print(nazwa_parametrow[i], ": ")
        parametry.append(tylkoliczby())
    gasnaca_sinusoida(float(parametry[0]), float(parametry[1]), int(parametry[2]), float(parametry[3]),
                      float(parametry[4]), float(parametry[5]), float(parametry[6]), float(parametry[7]))


def tylkoliczby():
    while 1 == 1:
        podane = input()
        try:
            numer = float(podane)
            return numer
        except ValueError:
            print('podaj numer!')


start()
