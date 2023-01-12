import unittest
from teste.teste_domain import *
from teste.teste_validator import *
from teste.teste_repo import *
from teste.teste_file_repo import *
from teste.teste_service import *
from teste.teste_sort import *

from business.service_carti import ServiceCarti
from business.service_clienti import ServiceClienti
from business.service_inchirieri import ServiceInchirieri
from infrastructura.file_repository_carti import FileRepositoryCarti
from infrastructura.file_repository_clienti import FileRepositoryClienti
from infrastructura.file_repository_inchirieri import FileRepositoryInchirieri
from prezentare.ui import UI
from validare.validator_carte import ValidatorCarte
from validare.validator_client import ValidatorClient
from validare.validator_inchirieri import ValidatorInchiriere


def main():
    unittest.main(exit=False)

    repo_carti = FileRepositoryCarti("carti.txt")
    val_carti = ValidatorCarte()
    serv_carti = ServiceCarti(repo_carti, val_carti)
    repo_carti.getAllCarti()

    repo_clienti = FileRepositoryClienti("clienti.txt")
    val_clienti = ValidatorClient()
    serv_clienti = ServiceClienti(repo_clienti, val_clienti)
    repo_clienti.getAllClienti()

    repo_inchirieri = FileRepositoryInchirieri("inchirieri.txt")
    val_inchirieri = ValidatorInchiriere()
    serv_inchirieri = ServiceInchirieri(repo_inchirieri, val_inchirieri, repo_clienti, repo_carti)
    repo_inchirieri.getAll()

    ui = UI(serv_carti, serv_clienti, serv_inchirieri)
    ui.runUI()


main()