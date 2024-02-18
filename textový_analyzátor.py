# -*- coding: utf-8 -*-
"""Textový analyzátor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z-Ph3mGMDU64yTHgc44t9-JT8VUSKl-A
"""

"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Hedvika Drechslerová
email: hedvika.drechsler@seznam.cz
discord: hedvika_62633
"""

cara = 40 * "-"

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
username = input("username: ").lower()
password = input("password: ").lower()

print(cara)

if users.get(username) == password:
    print(f"Welcome to the app, {username}.","\nWe have 3 texts to be analyzed.")
else:
    print("Unregistered user, terminating the program...")
    exit()

print(cara)

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

cislo_textu = input("Enter a number btw. 1 and 3 to select: ")
if cislo_textu.isnumeric() and (1 <= int(cislo_textu) <= 3):
    print(cara)
else:
    print("Your selection was not a number btw. 1 and 3")
    exit()

TEXT = TEXTS[int(cislo_textu) - 1]
pocet_slov = TEXT.split()
print("There are", len(pocet_slov), "words in the selected text.")

prvni_velke = 0
vsechna_velka = 0
vsechna_mala = 0
pocet_cisel = 0
suma_cisel = 0

for slovo in pocet_slov:
  if slovo.istitle():
    prvni_velke = prvni_velke + 1
  if slovo.isupper():
    vsechna_velka = vsechna_velka + 1
  if slovo.islower():
    vsechna_mala = vsechna_mala + 1
  if slovo.isdigit():
    pocet_cisel = pocet_cisel + 1
    suma_cisel = suma_cisel + int(slovo)

print("There are", prvni_velke, "titlecase words.")
print("There are", vsechna_velka, "uppercase words.")
print("There are", vsechna_mala, "lowercase words.")
print("There are", pocet_cisel, "numeric strings.")
print(f"The sum of all the numbers is {suma_cisel}.")

print(cara)

print("{:>4}|{:<18}| {}".format("LEN","   OCCURENCES", "NR."))

pocet_delek_slov = {}
for slovo in pocet_slov:
    delka_slova = len(slovo)
    pocet_delek_slov[delka_slova] = pocet_delek_slov.get(delka_slova, 0) + 1

for klic in sorted(pocet_delek_slov.keys()):
  print("{:>4}|{:<18}| {}".format(klic, "*" * pocet_delek_slov[klic], pocet_delek_slov[klic]))

