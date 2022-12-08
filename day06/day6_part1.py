#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day6_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/08 19:18:37 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/08 19:18:37 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def is_sop(values):
	for i in range(3):
		for j in range(i + 1, 4):
			if values[i] == values[j]:
				return 0
	return 1

fd = open(sys.argv[1], "r")

line = fd.readline()
for index in range(4, len(line)):
	if is_sop(line[index - 4:index]):
		print(index)
		exit()

