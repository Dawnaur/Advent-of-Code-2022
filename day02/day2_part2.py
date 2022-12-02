#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day2_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/02 06:29:01 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/02 06:29:02 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

points = 0

fd = open(sys.argv[1], "r")
for line in fd.readlines():
	if len(line) > 2:
		win = ord(line[2]) - ord('X')
		points += (ord(line[0]) + 2 + win - ord('A')) % 3 + 1
		points += (win * 3)

print(points)
