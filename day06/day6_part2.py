#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day6_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/08 23:47:31 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/08 23:47:31 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def is_som(values):
	for i in range(13):
		for j in range(i + 1, 14):
			if values[i] == values[j]:
				return 0
	return 1

fd = open(sys.argv[1], "r")

line = fd.readline()
for index in range(14, len(line)):
	if is_som(line[index - 14:index]):
		print(index)
		exit()

