import random

from domain.client import Client


class ServiceClienti:
    def __init__(self, clienti, vclienti):
        """
        initializam service clienti
        :param clienti: RepositoryClienti
        :param vclienti: ValidatorClienti
        """
        self.__clienti = clienti
        self.__val = vclienti

    def adaugaClient(self, id, nume, cnp):
        """
        adauga clientul determinat de parametrii id, nume si cnp in lista de clienti clienti, daca clientul este valid
        si daca id-ul acestuia nu se regaseste in lista
        :param id: int
        :param nume: string
        :param cnp: string
        :return: -
        :raises: ValueError cu mesajul "id invalid!\n", daca id-ul nu este un numar intreg
                                        "nume invalid!\n", daca numele clientului este vid
                                        "cnp invalid!\n", daca cnp-ul nu este un string format din 13 cifre
                                        "client invalid!\n", daca id-ul clientului client se afla deja in lista de
                                                             clienti
        """
        client = Client(id, nume, cnp)
        self.__val.valideazaClient(client)
        self.__clienti.adaugaClientLista(client)

    def stergeClient(self, id):
        """
        sterge clientul cu id-ul intreg id din lista de clienti clienti, daca id-ul acestuia se regaseste in lista
        :param id: int
        :return: -
        :raises: ValueError cu mesajul "clientul nu se regaseste in lista!\n", daca id-ul nu se regaseste in lista
                 ValueError cu mesajul "id invalid!\n", daca id < 0
        """
        client = Client(id, "nume", "1029345876198")
        self.__val.valideazaClient(client)
        self.__clienti.stergeClientLista(id)

    def getAllClienti(self):
        """
        returneaza lista de clienti
        :return: rez - lista
        """
        return self.__clienti.getAllClienti()

    def getClient(self, id):
        """
        returneaza clientul cu id-ul intreg id din lista de clienti
        :param id: int
        :return: Client
        :raises: ValueError cu mesajul "clientul nu se afla in lista!\n", daca id-ul intreg al clientului nu se
                                                                          regaseste in lista
        """
        return self.__clienti.getClientLista(id)

    def updateClient(self, id, nume_nou, cnp_nou):
        """
        seteaza parametrii clientului cu id-ul intreg id la noii parametrii string nume_nou si cnp_nou, daca acesta se
        afla in lista si parametrii noi sunt valizi
        :param id: int
        :param nume_nou: string
        :param cnp_nou: string
        :return: -
        :raises: ValueError cu mesajul "clientul nu se afla in lista!\n", daca id-ul nu se regaseste in lista
                                       "nume invalid!\n", daca numele clientului este vid
                                       "cnp invalid!\n", daca cnp-ul nu este un string format din 13 cifre
        """
        client_nou = Client(id, nume_nou, cnp_nou)
        self.__val.valideazaClient(client_nou)
        self.__clienti.updateClientLista(client_nou)

    def genereazaClienti(self, nr_clienti):
        """
        functia genereaza nr_clienti clienti, pe care ii adauga in lista
        :param nr_clienti: int
        :return: -
        """

        nume_persoane = ["Andrei Ursu", "Madalina Vasilica", "Georgiana Ciocirlan", "Ovidiu Munteanu",
                         "Carla Dobrica", "Adrian Popescu", "Lucian Sava", "Narcisa Chirita"]

        coduri_cnp = ["2930927415021", "2990203434243", "2980509273072", "2950810391534", "2990722293672",
                      "1940318270203", "2970331362907", "1900116411619", "6031029361361"]

        for i in range(nr_clienti):
            id = 1

            while self.__clienti.inLista(id):
                id = random.randint(0, 100)

            nume = random.choice(nume_persoane)
            cnp = random.choice(coduri_cnp)

            self.adaugaClient(id, nume, cnp)
