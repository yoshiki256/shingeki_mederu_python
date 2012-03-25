# -*- coding: utf-8 -*-
import models
import csv

character_reader = csv.reader(open('character.csv','rb'),delimiter=',')

character_list = list()
for row in character_reader:
    character_list.append(row)

new_character_list = list()
for row in character_list[1:]:
    character_dict = dict()
    for i,v in enumerate(row):
        character_dict[character_list[0][i]]= unicode(v,'utf-8')
    new_character_list.append(character_dict)

for hoge in new_character_list:
    character = models.characters.Character()
    for k,v in hoge.iteritems():
        character[k] = v
    character.save()
