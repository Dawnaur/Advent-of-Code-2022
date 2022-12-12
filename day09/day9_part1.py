#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day9_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/11 04:17:43 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/11 04:17:43 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from termcolor import colored

def print_map():
	for y in reversed(range(map_height)):
		for x in range(map_width):
			if (map[y][x] == '.'):
				print(colored('.', 'grey'), end='')
			else:
				print(colored(map[y][x], 'green'), end='')
		print("")

def count_map():
	count = 0
	for y in range(map_height):
		for x in range(map_width):
			if (map[y][x] == "#"):
				count += 1
	return count

def refresh_tail_position():
	if (tail_position["x"] > head_position["x"] + 1):
		tail_position["x"] = head_position["x"] + 1
		tail_position["y"] = head_position["y"]
	elif (tail_position["x"] < head_position["x"] - 1):
		tail_position["x"] = head_position["x"] - 1
		tail_position["y"] = head_position["y"]
	if (tail_position["y"] > head_position["y"] + 1):
		tail_position["y"] = head_position["y"] + 1
		tail_position["x"] = head_position["x"]
	elif (tail_position["y"] < head_position["y"] - 1):
		tail_position["y"] = head_position["y"] - 1
		tail_position["x"] = head_position["x"]
	map[tail_position["y"]][tail_position["x"]] = "#"

def execute_action(instruction):
	direction = instruction.split()[0]
	for i in range(int(instruction.split()[1])):
		if (direction == "U"):
			head_position["y"] += 1
		if (direction == "D"):
			head_position["y"] -= 1
		if (direction == "R"):
			head_position["x"] += 1
		if (direction == "L"):
			head_position["x"] -= 1
		refresh_tail_position()

# Adjusted to input file for better visualization
map_height = 350
map_width = 310
head_position = {"x": 120, "y": 280}
tail_position = {"x": 120, "y": 280}
#head_position = {"x": int(map_width / 2), "y": int(map_height / 2)}
#tail_position = {"x": int(map_width / 2), "y": int(map_height / 2)}

map = [ [] for y in range(map_height) ]
for y in range(map_height):
	for x in range(map_width):
		map[y].append(".")

fd = open(sys.argv[1], "r")

for line in fd.readlines():
	execute_action(line[:-1])
print_map()
print(count_map())
