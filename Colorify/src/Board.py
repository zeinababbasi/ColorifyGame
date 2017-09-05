# -*- coding: utf-8 -*-


from __future__ import unicode_literals
import sys
import string
import random


__author__ = "Zeinab Abbasimazar -> https://github.com/zeinababbasi"


class Board(object):

    def __init__(self, dimension, color_count):
        self.dimension = dimension
        self.color_count = color_count
        self.board_colors = random.sample(string.ascii_uppercase, color_count)
        self.plate = [random.sample(self.board_colors, self.dimension) for _ in range(self.dimension)]

    def draw_board(self):
        sys.stdout.write('\n%s\n' % '\n'.join(['\t'.join(row) for row in self.plate]))

    def has_differences(self):
        return len(set(''.join([''.join(row) for row in self.plate]))) > 1

    def get_origin(self):
        return self.plate[0][0]

    def get_plate(self):
        return self.plate

    def set_plate(self, plate):
        self.plate = plate

    def update_plate(self, cur_color, pre_color=None, x=0, y=0):
        pre_color = pre_color if pre_color else self.plate[x][y]

        if x == self.dimension or y == self.dimension:
            return

        if self.plate[x][y] != pre_color:
            return

        self.plate[x][y] = cur_color
        self.update_plate(x=x + 1, y=y, pre_color=pre_color, cur_color=cur_color)
        self.update_plate(x=x, y=y + 1, pre_color=pre_color, cur_color=cur_color)
