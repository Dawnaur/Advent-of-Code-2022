#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day1_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/02 03:32:10 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/02 03:32:16 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

first_elve = 0
second_elve = 0
third_elve = 0
act_calories = 0

fd = open(sys.argv[1], "r")
for line in fd.readlines():
	if (len(line) == 1):
		if (act_calories > first_elve):
			third_elve = second_elve
			second_elve = first_elve
			first_elve = act_calories
		elif (act_calories > second_elve):
			third_elve = second_elve
			second_elve = act_calories
		elif (act_calories > third_elve):
			third_elve = act_calories
		act_calories = 0
	else:
		act_calories += int(line[:-1])

if (act_calories > first_elve):
	third_elve = second_elve
	second_elve = first_elve
	first_elve = act_calories
elif (act_calories > second_elve):
	third_elve = second_elve
	second_elve = act_calories
elif (act_calories > third_elve):
	third_elve = act_calories
print(first_elve + second_elve + third_elve)
