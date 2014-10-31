# -*- coding: utf-8 -*-

import math


class Integrator(object):

    """
    Klasa która implementuje całki metodą Newtona Cotesa z użyciem interpolacji
    N-tego stopnia :math:`n\in<2, 11>`.

    .. note::

        Używamy wzorów NC nie dlatego że są super przydatne (zresztą gorąco
        zniechęcam Państwa przed pisaniem własnych podstawowych algorytmów
        numerycznych --- zbyt łatwo o głupi błąd) ale dlatego żebyście
        jescze raz napisali jakiś algorytm w którym nie opłaca się zrobić 11
        ifów.

    """

    tab_coeff = {2:[1, 1],
                 3:[1,4,1],
                 4:[1,3,3,1],
                 5:[7,32,12,32,7],
                 6:[19,75,50,50,75,19],
                 7:[41,216,27,272,27,216,41],
                 8:[751,3577,1323,2989,2989,1323,3577,751],
                 9:[989,5888,-928,10496,-4540,10496,-928,5888,989],
                 10:[2857,15741,1080,19344,5778,5778,19344,1080,15741,2857],
                 11:[16067,106300,-48525,272400,-260550,427368,-260550,272400,-48525,106300,16067]}

    @classmethod
    def get_level_parameters(cls, level):
        """
       
        :param int level: Liczba całkowita większa od jendości.
        :return: Zwraca listę współczynników dla poszczególnych puktów
                 w metodzie NC. Na przykład metoda NC stopnia 2 używa punktów
                 na początku i końcu przedziału i każdy ma współczynnik 1,
                 więc metoda ta zwraca [1, 1]. Dla NC 3 stopnia będzie to
                 [1, 3, 1] itp.
        :rtype: List of integers
        """
        if level < 2: raise ValueError
        
        return cls.tab_coeff.get(level) 

    def __init__(self, level):
        """
        Funkcja ta inicjalizuje obiekt do działania dla danego stopnia metody NC
        Jeśli obiekt zostanie skonstruowany z parametrem 2 używa metody trapezów.
        :param level: Stopień metody NC
        """
        self.level = level

    def integrate(self, func, func_range, num_evaluations):
        """
        Funkcja dokonuje całkowania metodą NC.

        :param callable func: Całkowana funkcja, funkcja ta ma jeden argument,
                              i jest wołana w taki sposób: `func(1.0)`.
        :param Tuple[int] func_range: Dwuelementowa krotka zawiera początek i koniec
                                 przedziału całkowania.
        :param int num_evaluations: Przybliżona lość wywołań funkcji ``func``,
            generalnie algorytm jest taki:

            1. Dzielimy zakres na ``num_evaluations/self.level`` przdziałów.
               Jeśli wyrażenie nie dzieli się bez reszty, należy wziąć najmiejszą
               liczbę całkowitą większą od `num_evaluations/self.level``. 
            2. Na każdym uruchamiamy metodę NC stopnia ``self.level``
            3. Wyniki sumujemy.

            W tym algorytmie wykonamy trochę więcej wywołań funkcji niż ``num_evaluations``,
            dokłanie ``num_evaluations`` byłoby wykonywane gdyby keszować wartości
            funkcji na brzegach przedziału całkowania poszczególnych przedziałów.

        :return: Wynik całkowania.
        :rtype: float
        """
        coeff = self.get_level_parameters(self.level)
        _range = math.ceil(num_evaluations/self.level)

        a, b = func_range
        h = (b-a)/_range
        _sum = 0.0
        for x1, x2 in self.generate_step(a, b, _range):
            step = (x2-x1) / (self.level - 1)
            _sum += sum( a*func( x1 + i*step ) for i, a in enumerate(coeff) )

        # _sum *= (self.level-1)?
        _sum *= h/sum(coeff)
            
        return _sum
        
    def generate_step(self, a, b, N):
        step = (b-a)/N
        for i in range(1, N+1):
            yield ( a+(i-1)*step, a+i*step )


if __name__ == '__main__':
    i = Integrator(11)
    def tst(x):
        print(x)
        return math.sin(x)
    print("res = %f" % i.integrate(lambda x: math.exp(-x**2), (-100000, 100000), 300000))

    # print(i.integrate(lambda x: x*x, (0, 1), 30))
