from copy import deepcopy
import random
from utils.default_config import *


class Config(object):
    def __init__(self, max_capacity=MAX_CAPACITY, depot_cnt=DEPOT_CNT, randomize=False):
        self._max_capacity = max_capacity
        self._depot_cnt = depot_cnt
        self._depots = self._get_depots(rnd=randomize)
        self._distance_matrix = self._get_distance_matrix(rnd=randomize)

    @property
    def max_capacity(self):
        return deepcopy(self._max_capacity)

    @property
    def depot_cnt(self):
        return deepcopy(self._depot_cnt)

    @property
    def depots(self):
        return deepcopy(self._depots)

    @property
    def distance_matrix(self):
        return deepcopy(self._distance_matrix)

    @staticmethod
    def _get_distance_matrix(rnd=False, max_distance=10):
        size = DEPOT_CNT
        result = deepcopy(EX_DISTANCE_MATRIX)
        if rnd:
            result = [[0 for x in range(size)] for x in range(size)]
            for row in range(size):
                for col in range(row + 1, size):
                    result[row][col] = random.randrange(1, max_distance + 1)
                    result[col][row] = result[row][col]
        return result

    @staticmethod
    def _get_depots(rnd=False):
        result = deepcopy(EX_DEPOTS)
        if rnd:
            result = []
            for i in range(1, DEPOT_CNT):
                result.append(Depot(i, random.randrange(1, MAX_CAPACITY + 1)))
        return result

