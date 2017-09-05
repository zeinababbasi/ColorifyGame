# -*- coding: utf-8 -*-


from __future__ import unicode_literals
import sys
from Colorify.src.Board import Board
from Colorify.src.Player import Player


__author__ = "Zeinab Abbasimazar -> https://github.com/zeinababbasi"


n, m = 3, 3


if __name__ == "__main__":
    board = Board(dimension=n, color_count=m)
    player = Player()
    player.set_cur_choice(choice=board.get_origin())
    sys.stdout.write("You've started it; board dimension is %d and color count is %d\n" % (n, m))
    round_count = 1

    while board.has_differences():
        sys.stdout.write("This is the board for round #%d..." % round_count)
        board.draw_board()
        plate = board.get_plate()
        choice = player.choose(plate=plate)
        board.update_plate(cur_color=choice)
        round_count += 1

    sys.stdout.write("It's finished!")
    board.draw_board()
