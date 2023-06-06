from unittest import TestCase

from src.myMain.data.model.Party import Party
from src.myMain.data.repositories.PartyRepositoryImpl import PartyRepositoryImpl
from src.myMain.data.repositories.PartyRepositoryInterface import PartyRepositoryInterface


class TestPartyRepositoryImpl(TestCase):
    def test_find_all(self):
        party_repo: PartyRepositoryInterface = PartyRepositoryImpl()
        party: Party = Party()
        party1: Party = Party()
        saved_party1: Party = party_repo.save(party)
        saved_party2: Party = party_repo.save(party1)
        self.assertIsNotNone(saved_party1)
        self.assertIsNotNone(saved_party2)
        self.assertEqual(2, len(party_repo.findAll()))

    def test_party_can_save(self):
        party_repo: PartyRepositoryInterface = PartyRepositoryImpl()
        party1: Party = Party()
        party2: Party = Party()
        saved_party: Party = party_repo.save(party1)
        saved_party1: Party = party_repo.save(party2)
        self.assertEqual(2,len(party_repo.findAll()))

    def test_party_can_delete_by_id(self):
        party_repo: PartyRepositoryInterface = PartyRepositoryImpl()
        party: Party = Party()
        party1: Party = Party()
        saved_party: Party = party_repo.save(party)
        saved_party1: Party = party_repo.save(party1)
        party_repo.deleteById(party.get_id())
        self.assertEqual(1, len(party_repo.findAll()))

    def test_find_party_by_id(self):
        party_repo: PartyRepositoryInterface = PartyRepositoryImpl()
        party: Party = Party()
        saved_party : Party = party_repo.save(party)
        self.assertIsNotNone(saved_party.get_id())

