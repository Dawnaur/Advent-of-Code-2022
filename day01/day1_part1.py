#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day1_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/02 03:32:10 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/02 03:32:16 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

max_calories = 0
act_calories = 0

fd = open(sys.argv[1], "r")
for line in fd.readlines():
	if (len(line) == 1):
		max_calories = max_calories if max_calories > act_calories else act_calories
		act_calories = 0
	else:
		act_calories += int(line[:-1])

max_calories = max_calories if max_calories > act_calories else act_calories
print(max_calories)
