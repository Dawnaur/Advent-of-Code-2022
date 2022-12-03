#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day3_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/03 06:01:12 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/03 06:01:14 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

score = 0

fd = open(sys.argv[1], "r")

for line in fd.readlines():
	if len(line) > 2:
		first_compartment = line[:int(len(line) / 2)]
		second_compartment = line[int(len(line) / 2):]
		list = []
		for item in first_compartment:
			if second_compartment.find(item) >= 0:
				list.append(item)
		for item in dict.fromkeys(list):
			priority = ord(item)
			priority -= 96 if priority > 90 else 38
			score += priority

print(score)