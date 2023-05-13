import pytest 
from musicians import Musician, Guitarist, Bassist, Drummer, Band
import unittest


class TestMusician(unittest.TestCase):
    def setUp(self):
        self.musician = Musician("John", "guitar")

    def test_str(self):
        self.assertEqual(str(self.musician), "John (guitar)")

    def test_repr(self):
        self.assertEqual(repr(self.musician), "Musician('John', 'guitar')")

    def test_get_instrument(self):
        self.assertEqual(self.musician.get_instrument(), "guitar")

    def test_play_solo(self):
        self.assertEqual(self.musician.play_solo(), "Playing a solo!")


class TestGuitarist(unittest.TestCase):
    def setUp(self):
        self.guitarist = Guitarist("Jimi")

    def test_str(self):
        self.assertEqual(str(self.guitarist), "Jimi (guitar)")

    def test_repr(self):
        self.assertEqual(repr(self.guitarist), "Guitarist('Jimi', 'guitar')")

    def test_play_solo(self):
        self.assertEqual(self.guitarist.play_solo(), "Playing an awesome guitar solo!")


class TestBassist(unittest.TestCase):
    def setUp(self):
        self.bassist = Bassist("Flea")

    def test_str(self):
        self.assertEqual(str(self.bassist), "Flea (bass)")

    def test_repr(self):
        self.assertEqual(repr(self.bassist), "Bassist('Flea', 'bass')")

    def test_play_solo(self):
        self.assertEqual(self.bassist.play_solo(), "Playing a groovy bass solo!")


class TestDrummer(unittest.TestCase):
    def setUp(self):
        self.drummer = Drummer("Neil")

    def test_str(self):
        self.assertEqual(str(self.drummer), "Neil (drums)")

    def test_repr(self):
        self.assertEqual(repr(self.drummer), "Drummer('Neil', 'drums')")

    def test_play_solo(self):
        self.assertEqual(self.drummer.play_solo(), "Playing an epic drum solo!")


class TestBand(unittest.TestCase):
    def setUp(self):
        self.musician1 = Musician("John", "guitar")
        self.musician2 = Musician("Paul", "bass")
        self.musician3 = Musician("Ringo", "drums")
        self.guitarist = Guitarist("Jimi")
        self.bassist = Bassist("Flea")
        self.drummer = Drummer("Neil")
        self.band1 = Band("The Beatles", [self.musician1, self.musician2, self.musician3])
        self.band2 = Band("The Jimi Hendrix Experience", [self.guitarist, self.bassist, self.drummer])

    def test_name(self):
        self.assertEqual(self.band1.name, "The Beatles")
        self.assertEqual(self.band2.name, "The Jimi Hendrix Experience")

    def test_members(self):
        self.assertEqual(len(self.band1.members), 3)
        self.assertTrue(isinstance(self.band1.members[0], Musician))
        self.assertTrue(isinstance(self.band1.members[1], Musician))
        self.assertTrue(isinstance(self.band1.members[2], Musician))
        self.assertEqual(len(self.band2.members), 3)
        self.assertTrue(isinstance(self.band2.members[0], Guitarist))
        self.assertTrue(isinstance(self.band2.members[1], Bassist))
        self.assertTrue(isinstance(self.band2.members[2], Drummer))

    def test_play_solos(self):
        self
