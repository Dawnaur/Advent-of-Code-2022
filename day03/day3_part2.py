#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day3_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/03 06:17:35 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/03 06:17:36 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

score = 0
group_elve = 0
rucksack = [[],[],[]]
list = []
priority = 0

fd = open(sys.argv[1], "r")

for line in fd.readlines():
	if len(line) > 2:
		if group_elve > 2:
			group_elve = 0
			rucksack = [[],[],[]]

		rucksack[group_elve] = line
		group_elve += 1

		if group_elve > 2:
			list = []
			for item in line[:-1]:
				if rucksack[1].find(item) >= 0 and rucksack[0].find(item) >= 0:
					list.append(item)
			for item in dict.fromkeys(list):
				priority = ord(item)
				priority -= 96 if priority > 90 else 38
				score += priority

print(score)
