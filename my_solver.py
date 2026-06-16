#!/usr/bin/env python3

import sys

from common import print_tour, read_input

"""
solve関数
cities_pos_listは[(x,y)....]という形式のlistをinputとして受け取り、探索順にcities_pos_listでのindexのlistを返す

"""
class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

def solve(cities_pos_list):
    cities = create_city_list(cities_pos_list)
    optimized_cities = two_opt(greedy(cities))
    ans = create_city_ids(optimized_cities)
    return ans


def create_city_list(cities_pos_list):
    cities = []
    for i in range(len(cities_pos_list)):
        cities.append(City(i, cities_pos_list[i][0], cities_pos_list[i][1]))
    return cities


def greedy(cities):
    opt_cities = []
    current_city = cities.pop(0)
    opt_cities.append(current_city)
    while cities:
        city_pos = find_nearest_city_pos(cities, current_city)
        current_city = cities.pop(city_pos)
        opt_cities.append(current_city)
    return opt_cities



def find_nearest_city_pos(cities, current_city):
    min_distance = float("inf")
    min_city_pos = -1
    for i in range(len(cities)):
        current_distance = (cities[i].x -current_city.x)**2 + (cities[i].y -current_city.y)**2
        if min_distance > current_distance:
            min_distance = current_distance
            min_city_pos = i
    return  min_city_pos

def two_opt(cities):
    # listの最初と最後を含んでの大まかなswapの方法がわからない
    is_optimized = True
    while is_optimized:
        is_optimized = False
        N = len(cities)
        for i in range(1, N-2):
            a1, a2 = cities[i-1], cities[i]
            for j in range(i+2, N):
                b1, b2 =  cities[j-1], cities[j]
                current_distance = (a1.x-a2.x)**2 + (a1.y-a2.y)**2 + (b1.x-b2.x)**2 + (b1.y-b2.y)**2
                candidate_distance = (a1.x-b1.x)**2 + (a1.y-b1.y)**2 + (a2.x-b2.x)**2 + (a2.y-b2.y)**2
                if current_distance > candidate_distance:
                    cities[i:j] = reversed(cities[i:j]) 
                    is_optimized = True
    return cities

def create_city_ids(cities):
    ids = []
    for city in cities:
        ids.append(city.id)
    return ids
    
if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
