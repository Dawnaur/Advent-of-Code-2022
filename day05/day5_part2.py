#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day5_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/08 01:07:34 by Dawnaur           #+#    #+#              #
#    Updated: 2022/12/08 01:07:35 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

fd = open(sys.argv[1], "r")

stacks_complete = 0

line = fd.readline()
stacks_nb = int(len(line) / 4)
content = [ [] for x in range(stacks_nb) ]
for i in range(0, stacks_nb):
	if line[4 * i + 1] != ' ':
		content[i].insert(0, line[4 * i + 1])

for line in fd.readlines():
	if len(line) > 2 and stacks_complete == 0:
		for i in range(0, stacks_nb):
			if line[4 * i + 1] != ' ':
				content[i].insert(0, line[4 * i + 1])
	elif len(line) > 2:
		fields = line.split()
		index = len(content[int(fields[5]) - 1])
		for i in range(int(fields[1])):
			value = content[int(fields[3]) - 1].pop()
			content[int(fields[5]) - 1].insert(index, value)
	else:
		for i in range(0, stacks_nb):
			content[i].pop(0)
		stacks_complete = 1

for i in range(0, stacks_nb):
	print(content[i][len(content[i]) - 1], end='')
print("")
