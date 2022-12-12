#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day9_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/11 05:29:05 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/12 23:36:39 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from termcolor import colored

def print_map():
	for y in reversed(range(map_height)):
		for x in range(map_width):
			if (map[y][x] == '.'):
				print(colored('.', 'grey'), end='')
			elif (map[y][x] == 's'):
				print(colored(map[y][x], 'blue'), end='')
			else:
				print(colored(map[y][x], 'green'), end='')
		print("")

def count_map():
	count = 0
	for y in range(map_height):
		for x in range(map_width):
			if (map[y][x] != "."):
				count += 1
	return count

def get_diff_sign(value, ref):
	if (value > ref):
		return (1)
	elif (value < ref):
		return (-1)
	return (0)

def refresh_tail_position():
	for i in range(knots_number - 1):
		if (knots_position[i + 1]["x"] > knots_position[i]["x"] + 1):
			knots_position[i + 1]["x"] -= 1
			knots_position[i + 1]["y"] += get_diff_sign(knots_position[i]["y"], knots_position[i + 1]["y"])
		elif (knots_position[i + 1]["x"] < knots_position[i]["x"] - 1):
			knots_position[i + 1]["x"] += 1
			knots_position[i + 1]["y"] += get_diff_sign(knots_position[i]["y"], knots_position[i + 1]["y"])
		elif (knots_position[i + 1]["y"] > knots_position[i]["y"] + 1):
			knots_position[i + 1]["y"] -= 1
			knots_position[i + 1]["x"] += get_diff_sign(knots_position[i]["x"], knots_position[i + 1]["x"])
		elif (knots_position[i + 1]["y"] < knots_position[i]["y"] - 1):
			knots_position[i + 1]["y"] += 1
			knots_position[i + 1]["x"] += get_diff_sign(knots_position[i]["x"], knots_position[i + 1]["x"])
	map[knots_position[knots_number - 1]["y"]][knots_position[knots_number - 1]["x"]] = chr(ord('0') + knots_number - 1)

def execute_action(instruction):
	direction = instruction.split()[0]
	for i in range(int(instruction.split()[1])):
		if (direction == "U"):
			knots_position[0]["y"] += 1
		elif (direction == "D"):
			knots_position[0]["y"] -= 1
		elif (direction == "R"):
			knots_position[0]["x"] += 1
		elif (direction == "L"):
			knots_position[0]["x"] -= 1
		refresh_tail_position()

knots_number = int(sys.argv[2]) if (len(sys.argv) > 2) else 10

# Adjusted to input file for better visualization
map_height = 350
map_width = 320
start_x = 130
start_y = 280
knots_position = [ {"x": start_x, "y": start_y} for i in range(knots_number) ]

map = [ [] for y in range(map_height) ]
for y in range(map_height):
	for x in range(map_width):
		map[y].append(".")

fd = open(sys.argv[1], "r")

for line in fd.readlines():
	execute_action(line[:-1])

map[start_y][start_x] = "s"
print_map()
print(count_map())
