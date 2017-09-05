# -*- coding: utf-8 -*-


from __future__ import unicode_literals
import random
import string
import unittest
from main import m, n
from src.Board import Board
from src.Player import Player


__author__ = "Zeinab Abbasimazar -> https://github.com/zeinababbasi"


class TestBoardMethods(unittest.TestCase):

    def test_has_difference_false(self):
        test_board = Board(dimension=n, color_count=m)
        test_plate = [['A' for i in range(n)] for j in range(n)]
        test_board.set_plate(plate=test_plate)
        self.assertEqual(False, test_board.has_differences())

    def test_has_difference_true(self):
        test_board = Board(dimension=n, color_count=m)
        test_plate = [[random.choice(string.ascii_uppercase) for i in range(n)] for j in range(n)]
        test_plate[0][0] = '1'
        test_board.set_plate(plate=test_plate)
        self.assertEqual(True, test_board.has_differences())

    def test_get_plate(self):
        test_board = Board(dimension=n, color_count=m)
        test_plate = [['A', 'B'], ['C', 'D']]
        test_board.set_plate(plate=test_plate)
        self.assertEqual(test_plate, test_board.get_plate())


class TestPlayerMethods(unittest.TestCase):

    def test_choose_with_no_pre_choice(self):
        test_player = Player()
        test_plate = [['A', 'B', 'A'], ['C', 'D', 'A'], ['A', 'X', 'X']]
        self.assertEqual('A', test_player.choose(plate=test_plate))

    def test_choose_with_pre_choice(self):
        test_player = Player()
        test_plate = [['A', 'B', 'A'], ['C', 'D', 'A'], ['A', 'X', 'X']]
        test_player.set_cur_choice(test_plate[0][0])
        self.assertEqual('B', test_player.choose(plate=test_plate))


if __name__ == '__main__':
    unittest.main()
