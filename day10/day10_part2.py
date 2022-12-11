#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day10_part2.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/11 03:37:25 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/11 03:37:25 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from termcolor import colored

cycle = 1
remaining_cycles = 1
instruction = "noop"
register = 1

fd = open(sys.argv[1], "r")

while True:
	remaining_cycles -= 1

	if (remaining_cycles == 0):
		if (instruction[0:4] == "addx"):
			register += int(instruction[5:])
		instruction = fd.readline()[:-1]
		if (len(instruction) < 2):
			exit()
		if (instruction[0:4] == "addx"):
			remaining_cycles = 2
		else:
			remaining_cycles = 1
	if ((((cycle - 1) % 40) + 1) in range(register, register + 3)):
		print(colored('#', 'green'), end='')
	else:
		print(colored('.', 'grey'), end='')

	if (cycle % 40 == 0):
		print("")
	cycle += 1

