from unittest import TestCase
from src.myMain.data.model.Voter import Voter
from src.myMain.data.repositories.VoterInterface import VoterInterface
from src.myMain.data.repositories.VoterRepoImpl import VoterRepoImpl


class Voter_Repository_Test(TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.voter = Voter()
        cls.voter_repo: VoterInterface = VoterRepoImpl()

    def test_save_new_voter(self):
        self.voter_repo.save(self.voter)
        self.assertEqual(1, len(self.voter_repo.findAll()))

    def test_save_voter_multiple_times_count_does_not_increment(self):
        self.voter_repo.save(self.voter)
        self.voter_repo.save(self.voter)
        self.assertEqual(1, len(self.voter_repo.findAll()))

    def test_find_voter_by_id(self):
        saved_voter = self.voter_repo.save(self.voter)
        print(saved_voter.get_id())
        found_voter = self.voter_repo.findById(self.voter.get_id())
        self.assertIsNotNone(found_voter)
        self.assertIsNotNone(found_voter.get_id())

    def test_delete_voter_by_id(self):
        saved_voter = self.voter_repo.save(self.voter)
        print(saved_voter)
        is_deleted = self.voter_repo.deleteById(self.voter.get_id())
        self.assertTrue(is_deleted)
        self.assertEqual(0, len(self.voter_repo.findAll()))
