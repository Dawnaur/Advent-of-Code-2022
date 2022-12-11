#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day10_part1.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/11 03:15:41 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/11 03:15:41 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

cycle = 1
remaining_cycles = 1
instruction = "noop"
register = 1
result = 0

fd = open(sys.argv[1], "r")

while True:
	remaining_cycles -= 1

	if (remaining_cycles == 0):
		if (instruction[0:4] == "addx"):
			register += int(instruction[5:])
		instruction = fd.readline()[:-1]
		if (len(instruction) < 2):
			print(result)
			exit()
		if (instruction[0:4] == "addx"):
			remaining_cycles = 2
		else:
			remaining_cycles = 1

	if (cycle in [20, 60, 100, 140, 180, 220]):
		result += (cycle * register)
	cycle += 1

