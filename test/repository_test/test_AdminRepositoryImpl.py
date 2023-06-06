from unittest import TestCase

from src.myMain.data.model.Admin import Admin
from src.myMain.data.repositories.AdminRepositoryImpl import AdminRepositoryImpl
from src.myMain.data.repositories.AdminRepositoryInterface import AdminRepositoryInterface


class Test(TestCase):
    def test_admin_can_save(self):
        admin_repo: AdminRepositoryInterface = AdminRepositoryImpl()
        admin: Admin = Admin()
        saved_admin = admin_repo.save(admin)
        self.assertIsNotNone(saved_admin)

    def test_admin_delete_by_id(self):
        admin_repo1: AdminRepositoryInterface = AdminRepositoryImpl()
        admin: Admin = Admin()
        saved_admin: Admin = admin_repo1.save(admin)
        admin_repo1.deleteById(saved_admin.get_id())
        print(len(admin_repo1.findAll()))
        self.assertEqual(0,len(admin_repo1.findAll()))

    def test_find_by_id(self):
        admin_repo: AdminRepositoryInterface = AdminRepositoryImpl()
        admin: Admin = Admin()
        saved_admin: Admin = admin_repo.save(admin)
        self.assertIsNotNone(admin_repo.findById(saved_admin.get_id()))

    def test_find_all(self):
        admin_repo: AdminRepositoryInterface = AdminRepositoryImpl()
        admin: Admin = Admin()
        saved_admin: Admin = admin_repo.save(admin)
        admin1: Admin = Admin()
        saved_admin1: Admin = admin_repo.save(admin1)
        self.assertIsNotNone(saved_admin)
        self.assertIsNotNone(saved_admin1)
        self.assertEqual(2, len(admin_repo.findAll()))