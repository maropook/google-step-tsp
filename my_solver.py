#!/usr/bin/env python3

import sys

from common import print_tour, read_input

"""
citiesは[(x,y)....]という形式のlistである、

"""
class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


def solve(cities_pos_list):
    cities = create_city_list(cities_pos_list)
    print(cities)
    # 交差したものを探すがどうやって探すのか？
    # Citiesをansとして持っておいて、appendしたときに探索する？cities[i], cities[i] = cities[i], cities[i]
    # 交差したもの A→B C→Dだったら、  A→C B→Dにしたいので  BとCをひっくり返す
    # 交差することを判定する方法
    # min(a_x, b_x) < c_x < max(a_x, b_x) or min(a_x, b_x) < d_x < max(a_x, b_x) 　and
    # min(a_y, b_y) < c_y < max(a_y, b_y) or min(a_y, b_y) < d_y < max(a_y, b_y) 
    # のときに交差してると言えるので、BとCをひっくりかえす
    # 今までのcitiesをひとつひとつ見ていって、
    # まずは貪欲法だけ考えてみる

    # indexを返さないといけないので、formatを変えたい(0, (x, y))... というように変更する
    ans_cities = []
    current_city = cities.pop(0)
    ans_cities.append(current_city)

    while cities:
        city_pos = find_nearest_city_pos(cities, current_city)
        current_city = cities.pop(city_pos)
        ans_cities.append(current_city)
        
    ans = create_city_ids(ans_cities)
    return ans

def create_city_list(cities_pos_list):
    cities = []
    for i in range(len(cities_pos_list)):
        cities.append(City(i, cities_pos_list[i][0], cities_pos_list[i][1]))
    return cities

def find_nearest_city_pos(cities, current_city):
    min_distance = float("inf")
    min_city_pos = -1
    for i in range(len(cities)):
        current_distance = (cities[i].x -current_city.x)**2 + (cities[i].y -current_city.y)**2
        if min_distance > current_distance:
            min_distance = current_distance
            min_city_pos = i
    return  min_city_pos

def create_city_ids(cities):
    ids = []
    for city in cities:
        ids.append(city.id)
    return ids
    
if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
