import random

from domain.carte import Carte


class ServiceCarti:
    def __init__(self, carti, vcarti):
        """
        initializam service carti
        :param carti: RepositoryCarti
        :param vcarti: ValidatorCarti
        """
        self.__carti = carti
        self.__val = vcarti

    def adaugaCarte(self, id, titlu, descriere, autor):
        """
        adauga cartea determinata de parametrii id, titlu, descriere si autor in lista de carti, daca Cartea
        carte este valida si daca id-ul acesteia nu se regaseste in lista
        :param id: int
        :param titlu: string
        :param descriere: string
        :param autor: string
        :return: -
        :raises: ValueError cu mesajul "id invalid!\n", daca id-ul nu este un numar intreg
                                        "titlu invalid!\n", daca titlu este vid
                                        "descriere invalida!\n", daca descrierea este vida
                                        "autor invalid!\n", daca autorul este vid
                                        "carte invalida!\n", daca id-ul cartii carte se afla deja in lista de carti
        """
        carte = Carte(id, titlu, descriere, autor)
        self.__val.valideazaCarte(carte)
        self.__carti.adaugaCarteLista(carte)

    def stergeCarte(self, id):
        """
        sterge cartea cu id-ul intreg id din lista de carti, daca id-ul se regaseste in lista
        :param id: int
        :return: -
        :raises: ValueError cu mesajul "cartea nu se regaseste in lista!\n", daca id-ul nu se regaseste in lista
        """
        carte = Carte(id, "titlu", "descriere", "autor")
        self.__val.valideazaCarte(carte)
        self.__carti.stergeCarteLista(id)

    def getAllCarti(self):
        """
        returneaza lista de carti
        :return: rez - lista
        """
        return self.__carti.getAllCarti()

    def getCarte(self, id):
        """
        returneaza cartea cu id-ul intreg id din lista de carti
        :param id: int
        :return: Carte
        :raises: ValueError cu mesajul "cartea nu se afla in lista!\n", daca id-ul cartii nu se afla in lista
        """
        return self.__carti.getCarteLista(id)

    def updateCarte(self, id, titlu_nou, descriere_noua, autor_nou):
        """
        seteaza parametrii cartii cu id-ul intreg id la noii parametrii string titlu_nou, descriere_noua si autor_nou,
        daca aceasta se afla in lista si daca parametrii noi sunt valizi
        :param id: int
        :param titlu_nou: string
        :param descriere_noua: string
        :param autor_nou: string
        :return: -
        :raises: ValueError cu mesajul "cartea nu se afla in lista!\n", daca id-ul cartii nu se regaseste in lista
                                       "titlu invalid!\n", daca titlu este vid
                                       "descriere invalida!\n", daca descrierea este vida
                                       "autor invalid!\n", daca autorul este vid
        """
        carte = Carte(id, titlu_nou, descriere_noua, autor_nou)
        self.__val.valideazaCarte(carte)
        self.__carti.updateCarteLista(carte)

    def genereazaCarti(self, nr_carti):
        """
        functia genereaza nr_carti carti, pe care le adauga in lista
        :param nr_carti: int
        :return: -
        """

        titluri = ["Mandrie si prejudecata", "Anna Karenina", "Jane Eyre", "Stapanul inelelor",
                   "Un veac de singuratate", "Femeia in alb", "Casa de langa lac", "Si ma intunec"]

        descrieri = ["Actiune", "SF", "Fantasy", "Romance", "Istoric"]

        autori = ["Jane Austen", "Lev Tolstoi", "Chartoltte Bronte", "J.R.R. Tolkien", "Gabriel Garcia Marquez",
                  "Wilkie Collins", "Kiersten White"]

        for i in range(nr_carti):
            id = 1

            while self.__carti.inLista(id):
                id = random.randint(0, 100)

            titlu = random.choice(titluri)
            descriere = random.choice(descrieri)
            autor = random.choice(autori)

            self.adaugaCarte(id, titlu, descriere, autor)

