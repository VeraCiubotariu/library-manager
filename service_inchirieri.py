from domain.inchiriere import Inchiriere
import math

from utilities.bingo_sort import bingoSort
from utilities.merge_sort import mergeSort


class ServiceInchirieri():
    def __init__(self, inchirieri, vinchirieri, clienti, carti):
        """
        initializam service inchirieri
        :param inchirieri: RepositoryInchirieri
        :param vinchirieri: ValidatorInchirieri
        :param clienti: RepositoryClienti
        :param carti: RepositoryCarti
        """
        self.__inchirieri = inchirieri
        self.__val = vinchirieri
        self.__clienti = clienti
        self.__carti = carti

    def inchiriazaCarte(self, id_client, id_carte, data):
        """
        cartea cu id_carte este inchiriata de clientul cu id_client in data data, daca cele doua id-uri sunt valide si
        exista in lista, daca data este valida si daca cartea cu id_carte nu este inchiriata de un alt client in
        momentul interogarii
        :param id_client: int
        :param id_carte: int
        :param data: lista - [zi, luna, an]
        :return: - (inchirierea este adaugata in lista de inchirieri)
        :raises: ValueError cu mesajul "id_client invalid!\n", daca id_client < 0
                                       "id_carte invalid!\n", daca id_carte < 0
                                       "data invalida!\n", daca data nu este valida
                                       "client inexistent!\n", daca id_client nu se regaseste in lista de clienti
                                       "carte inexistenta!\n", daca id_carte nu se regaseste in lista de carti
                                       "carte deja inchiriata!\n", daca cartea cu id_carte este inchiriata de un alt
                                                                   client
        """

        id = 1
        while self.__inchirieri.inLista(id):
            id += 1

        inchiriere = Inchiriere(id, id_client, id_carte, data, 0)
        self.__val.valideazaInchiriere(inchiriere)

        if not self.__clienti.inLista(id_client):
            raise ValueError("client inexistent!\n")

        if not self.__carti.inLista(id_carte):
            raise ValueError("carte inexistenta!\n")

        for item in self.__inchirieri.getAll():
            if item.getIdCarte() == id_carte and item.getStatus() == 0:
                raise ValueError("carte deja inchiriata!\n")

        self.__inchirieri.adaugaInchiriere(inchiriere)

    def returneazaCarte(self, id_inchiriere):
        """
        returneaza cartea inchiriata cu id-ul id_inchiriere
        :param id_inchiriere: int
        :return: -
        :raises: ValueError cu mesajul "inchiriere inexisteanta!\n", daca id-ul acesteia nu se regaseste in
                 lista
        """
        self.__inchirieri.updateStatus(id_inchiriere)

    def getAllInchirieri(self):
        """
        returneaza lista de inchirieri
        :return: rez - lista
        """
        return self.__inchirieri.getAll()

    def getNumarInchirieri(self):
        """
        returneaza numarul de inchirieri din lista
        :return: rez - int
        """
        return self.__inchirieri.getNumarInchirieri()

    def getInchiriere(self, id):
        """
        returneaza inchirierea cu id-ul id din lista
        :param id: int
        :return: rez - Inchiriere
        :raises: ValueError cu mesajul "inchirierea nu se afla in lista!\n", daca id-ul acesteia nu se regaseste in
                 lista
        """
        return self.__inchirieri.getInchiriere(id)

    def celeMaiInchiriateCarti(self):
        """
        returneaza o lista cu carti ordonata dupa numarul de inchirieri
        :return: rez - lista
        :raises: ValueError cu mesajul "nu au fost efectuate inchirieri!\n", daca nu exista inchirieri in lista
        """
        if self.__inchirieri.getNumarInchirieri() == 0:
            raise ValueError("nu au fost efectuate inchirieri!\n")

        inchirieri = self.__inchirieri.getAll()

        for i in range(len(inchirieri)):
            inchirieri[i] = inchirieri[i].getIdCarte()

        carti = self.__carti.getAllCarti()
        rez = []
        for carte in carti:
            nr_inchirieri = inchirieri.count(carte.getId())
            if nr_inchirieri != 0:
                rez.append([carte, nr_inchirieri])

        # rez = sorted(rez, key=lambda x: x[1], reverse=True)
        # rez = mergeSort(rez, key=lambda x: x[1], reverse=True)
        rez = bingoSort(rez, key=lambda x: x[1], reverse=True)

        return rez

    def inchirieriNumeClient(self):
        """
        returneaza raportul clienților cu cărți închiriate ordonat după nume
        :return: rez - lista
        :raises: ValueError cu mesajul "nu au fost efectuate inchirieri!\n", daca nu exista inchirieri in lista
        """
        if self.__inchirieri.getNumarInchirieri() == 0:
            raise ValueError("nu au fost efectuate inchirieri!\n")

        inchirieri = self.__inchirieri.getAll()

        for i in range(len(inchirieri)):
            inchirieri[i] = inchirieri[i].getIdClient()

        clienti = self.__clienti.getAllClienti()
        rez = []

        for client in clienti:
            if client.getId() in inchirieri:
                rez.append(client)

        # rez = sorted(rez, key=lambda x: x.getNume())
        rez = mergeSort(rez, key=lambda x: x.getNume())

        return rez

    def inchirieriClientiNrCarti(self):
        """
        returneaza raportul clienților cu cărți închiriate ordonat după numărul de cărți închiriate
        :return: rez - lista
        :raises: ValueError cu mesajul "nu au fost efectuate inchirieri!\n", daca nu exista inchirieri in lista
        """
        if self.__inchirieri.getNumarInchirieri() == 0:
            raise ValueError("nu au fost efectuate inchirieri!\n")

        inchirieri = self.__inchirieri.getAll()

        for i in range(len(inchirieri)):
            inchirieri[i] = inchirieri[i].getIdClient()

        clienti = self.__clienti.getAllClienti()
        rez = []
        for client in clienti:
            nr_inchirieri = inchirieri.count(client.getId())
            nume_client = client.getNume()
            if nr_inchirieri != 0:
                rez.append([client, nr_inchirieri, nume_client])

        # rez = sorted(rez, key=lambda x: x[1], reverse=True)
        # rez = mergeSort(rez, key=lambda x: x[1], reverse=True)
        rez = mergeSort(rez, key=lambda x: (x[1], x[2]), reverse=True)

        return rez

    def inchirieriClientiNrCarti20(self):
        """
        returneaza raportul primiilor 20% dintre cei mai activi clienți
        :return: rez - lista
        :raises: ValueError cu mesajul "nu au fost efectuate inchirieri!\n", daca nu exista inchirieri in lista
        """
        clienti = self.inchirieriClientiNrCarti()

        nr_clienti = math.ceil(0.2 * len(clienti))

        # rez = []
        # for i in range(nr_clienti):
        #     rez.append(clienti[i])

        # return rez

        rez = []
        self.__inchirieriClientiNrCarti20Recursiv(clienti, rez, 0, nr_clienti)
        return rez

    def __inchirieriClientiNrCarti20Recursiv(self, clienti, rez, i, nr_clienti):
        if i == nr_clienti:
            return 0
        else:
            rez.append(clienti[i])
            self.__inchirieriClientiNrCarti20Recursiv(clienti, rez, i+1, nr_clienti)

    def nrCartiLiteraNume(self, litera):
        """
        returneaza numarul de carti pe care clientii al caror nume incep cu litera litera le-au inchiriat
        :param litera: char
        :return: rez - int
        """
        # rez = 0
        clienti = self.inchirieriClientiNrCarti()
        n = len(clienti)

        #for client in clienti:
        #    nume_client = client[0].getNume()
        #    if nume_client[0] == litera.lower() or nume_client[0] == litera.upper():
        #        rez += client[1]

        rez = self.__nrCartiLiteraNumeRecursiv(litera, clienti, 0, n)

        return rez

    def __nrCartiLiteraNumeRecursiv(self, litera, clienti, i, n):
        if i == n:
            return 0

        else:
            nume_client = clienti[i][0].getNume()
            if nume_client[0] == litera.lower() or nume_client[0] == litera.upper():
                return clienti[i][1] + self.__nrCartiLiteraNumeRecursiv(litera, clienti, i+1, n)
            else:
                return self.__nrCartiLiteraNumeRecursiv(litera, clienti, i+1, n)
