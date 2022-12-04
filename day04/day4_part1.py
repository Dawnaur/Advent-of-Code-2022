#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day4_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/04 13:13:18 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/04 13:13:19 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

score = 0

fd = open(sys.argv[1], "r")

for line in fd.readlines():
	if len(line) > 2:
		ranges = line[:-1].split(',')
		if ((int(ranges[0].split('-')[0]) <= int(ranges[1].split('-')[0])
				and int(ranges[0].split('-')[1]) >= int(ranges[1].split('-')[1]))
			or (int(ranges[0].split('-')[0]) >= int(ranges[1].split('-')[0])
				and int(ranges[0].split('-')[1]) <= int(ranges[1].split('-')[1]))):
			score += 1
			print(ranges)

print(score)
