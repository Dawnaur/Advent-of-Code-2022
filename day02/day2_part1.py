#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day2_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/02 06:23:58 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/02 06:23:59 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

points = 0

fd = open(sys.argv[1], "r")
for line in fd.readlines():
	if len(line) > 2:
		points += (ord(line[2]) - ord('W'))
		points += (((ord(line[2]) - ord(line[0]) - 1) % 3) * 3)

print(points)
