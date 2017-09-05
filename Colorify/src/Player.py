# -*- coding: utf-8 -*-


from __future__ import unicode_literals
import itertools
import operator
import copy


__author__ = "Zeinab Abbasimazar -> https://github.com/zeinababbasi"


class Player(object):

    def __init__(self, player_name='ZiZi'):
        self.name = player_name
        self.cur_choice = None

    def choose(self, plate):
        copy_plate = copy.copy(plate)
        if self.cur_choice:
            for index, p in enumerate(copy_plate):
                copy_plate[index] = [pm for pm in p if pm != self.cur_choice]
        copy_plate = [p for p in copy_plate if len(p)]
        choice = Player.most_common([mcp for mcp in Player.most_common(copy_plate)])
        self.cur_choice = choice
        return choice

    @staticmethod
    def most_common(input_list):
        sorted_list = sorted((x, i) for i, x in enumerate(input_list))
        groups = itertools.groupby(sorted_list, key=operator.itemgetter(0))

        def _auxfun(g):
            item, iterable = g
            count = 0
            min_index = len(input_list)
            for _, where in iterable:
                count += 1
                min_index = min(min_index, where)
            return count, -min_index

        return max(groups, key=_auxfun)[0]

    def set_cur_choice(self, choice):
        self.cur_choice = choice
