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

def solve(cities_list):
    cities = []
    for i in range(len(cities_list)):
        cities.append(City(i, cities_list[i][0], cities_list[i][1])) # (0,(x,y)), (1,(x,y)) 
    # 並び替えしたらinputがおかしくなるのが問題ではと思うけど
    # indexとか関係なく座標を順番に返すだけだから大丈夫そう、
    # 上下の差がminimumのやつを一つ一つ選んでいけば良さそう
    # find_nearest_city(x, y) -> x,y でいいのかな
    # divx**2 + divy ** 2が一番小さいものを返せばいい
    # 交差したもの A→B C→Dだったら、  A→C B→Dにしたいので  BとCをひっくり返す
    # 交差することを判定する方法
    # min(a_x, b_x) < c_x < max(a_x, b_x) or min(a_x, b_x) < d_x < max(a_x, b_x) 　and
    # min(a_y, b_y) < c_y < max(a_y, b_y) or min(a_y, b_y) < d_y < max(a_y, b_y) 
    # のときに交差してると言えるので、BとCをひっくりかえす
    # 今までのcitiesをひとつひとつ見ていって、
    # まずは貪欲法だけ考えてみる

    # indexを返さないといけないので、formatを変えたい(0, (x, y))... というように変更する
    ans = []
    current_city = cities.pop(0)
    ans.append(current_city.id)

    while cities:
        city_index, city_pos = find_nearest_city(cities, current_city)
        current_city = cities.pop(city_pos)
        ans.append(city_index)
    return ans

def find_nearest_city(cities, current_city):
    min_distance = float("inf")
    min_city_id = -1
    min_city_pos = -1
    for i in range(len(cities)):
        current_distance = (cities[i].x -current_city.x)**2 + (cities[i].y -current_city.y)**2
        if min_distance > current_distance:
            min_city_id = cities[i].id
            min_distance = current_distance
            min_city_pos = i
    return  min_city_id, min_city_pos

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
