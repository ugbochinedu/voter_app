import unittest

from src.myMain.data.model.Address import Address
from src.myMain.data.repositories.AddressRepositoryImpl import AddressRepositoryImpl
from src.myMain.data.repositories.AddressRepositoryInterface import AddressRepositoryInterface


class MyTestCase(unittest.TestCase):

    def test_address_can_save(self):
        address_repo: AddressRepositoryInterface = AddressRepositoryImpl()
        address: Address = Address()
        saved_address: Address = address_repo.save(address)
        self.assertIsNotNone(saved_address)

    def test_address_delete_by_id(self):
        address_repo: AddressRepositoryInterface = AddressRepositoryImpl()
        address: Address = Address()
        saved_address: Address = address_repo.save(address)
        self.assertIsNotNone(saved_address)
        print(len(address_repo.findAll()))
        address_repo.deleteById(saved_address.get_id())
        print(len(address_repo.findAll()))
        self.assertEqual(0, len(address_repo.findAll()))

    def test_find_all(self):
        address_repo: AddressRepositoryInterface = AddressRepositoryImpl()
        address1: Address = Address()
        address2: Address = Address()
        saved_address1: Address = address_repo.save(address1)
        saved_address2: Address = address_repo.save(address2)
        self.assertIsNotNone(saved_address1)
        self.assertIsNotNone(saved_address2)
        self.assertEqual(2, len(address_repo.findAll()))

    def test_find_id(self):
        address_repo: AddressRepositoryInterface = AddressRepositoryImpl()
        address1: Address = Address()
        address2: Address = Address()
        saved_address1: Address = address_repo.save(address1)
        saved_address2: Address = address_repo.save(address2)
        self.assertIsNotNone(saved_address1)
        self.assertIsNotNone(saved_address2)
        print(len(address_repo.findAll()))
        self.assertIsNotNone(address_repo.findById(saved_address1.get_id()))
