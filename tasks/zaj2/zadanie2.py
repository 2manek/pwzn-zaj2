# -*- coding: utf-8 -*-

import pickle
import pathlib
from pprint import pprint

def load_animals(large_dataset=False):
    """

    :param bool large_dataset: Jeśli wartość to True zwraca 1E6 zwierząt, w
                               przeciwnym razie 1E5. Test będzie odbywał się
                               przy 1E6 zwierząt.

    :return: Lista zwierząt
    """
    file_name = 'animals-small.bin' if not large_dataset else 'animals.bin'
    file = pathlib.Path(__file__).parent / file_name
    with open(str(file), 'rb') as f:
        return pickle.load(f)

count_female = 0
def mass(data): 
    global count_female
    conv = {'Mg':1.0e6, 'kg':1.0e3, 'g':1.0, 'mg':1.0e-3}
    mass, unit = data['mass']
    if data['sex'] == 'female': count_female += 1
    return (mass*conv[unit], data['sex'])

def filter_animals(animal_list):
    """
    Jesteś informatykiem w firmie Noe Shipping And Handling. Firma ta zajmuje
    się międzykontynentalnym przewozem zwierząt.

    Dostałeś listę zwierząt które są dostępne w pobliskim zoo do transportu.

    Mususz z tej listy wybrać listę zwierząt które zostaną spakowane na statek,

    Lista ta musi spełniać następujące warunki:

    * Docelowa lista zawiera obiekty reprezentujące zwierzęta (tak jak animal_list)
    * Z każdego gatunku zwierząt (z tej listy) musisz wybrać dokładnie dwa
      egzemplarze.
    * Jeden egzemplarz musi być samicą a drugi samcem.
    * Spośród samic i samców wybierasz te o najmniejszej masie.
    * Dane w liście są posortowane względem gatunku a następnie nazwy zwierzęcia

    Wymaganie dla osób aspirujących na ocenę 5:

    * Ilość pamięci zajmowanej przez program musi być stała względem
      ilości elementów w liście zwierząt.
    * Ilość pamięci może rosnąć liniowo z ilością gatunków.

    Nie podaje schematu obiektów w tej liście, musicie radzić sobie sami
    (można podejrzeć zawartość listy w interaktywnej sesji interpretera).

    Do załadowania danych z listy możesz użyć metody `load_animals`.

    :param animal_list:
    """


    take_animal = []
    genus =  { animal['genus'] for animal in animal_list }
    for g in genus:
        global count_female
        one_genus = [ animal for animal in animal_list if animal['genus'] == g ]
        one_genus = sorted(one_genus, key=mass)
        take_animal.append(one_genus[0])
        take_animal.append(one_genus[count_female])
        count_female = 0
        
    return sorted(take_animal, key=lambda x: (x['genus'], x['name'], x['sex']))



if __name__ == "__main__":
    animals = load_animals(False)
    selected = filter_animals(animals)

    print(selected[0])
    # female = 0
    # male = 0
    # for i in selected:
    #   if i['sex'] == 'female':
    #     female += 1
    #   else:
    #     male += 1

    # print(female)
    # print(male)