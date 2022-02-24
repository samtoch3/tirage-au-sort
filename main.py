# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:57:37 2022

@author: Samson N.
"""
import random
import PySimpleGUI as sg


def tirage(personnes):
    isChoisi = {}
    ListNumero = []
    numeroAttribue = {}

    for i in personnes.keys():
        isChoisi[i]=False
        ListNumero.append(i)
        
    s = 0
    
    for i in ListNumero:
        while  True:
            while True:
                s = random.choice(ListNumero)
                if isChoisi[s]==False:
                    break
            if s!=i:
                break
        
        numeroAttribue[i] = s
        isChoisi[s] = True

    return numeroAttribue    
    
    
def affichage(personnes, numeroAttribue):
    for i in numAttribue.keys():
    sg.popup('Resultat - Tirage au sort', f'\n{personnes[i]}, ----->>> {personnes[numAttribue[i]]}.')


nb = ''
while not(nb.isnumeric()):
    nb = sg.popup_get_text(f'Entrer le nombre de personnes', 'Tirage au sort')

dico_pers = {}
#dico_pers = personnes
for i in range(1,int(nb)+1):
    n = sg.popup_get_text(f'Entrer le nom et le numero de la personne {i} séparé d\'un espace', f'Personne {i}')
    x = n.split()
    dico_pers[int(x[1])] = x[0]

numAtt = {}
numAtt = tirage(dico_pers)
affichage(dico_pers, numAtt)
