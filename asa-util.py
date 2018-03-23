from ciscoconfparse import CiscoConfParse
import pprint
parse = CiscoConfParse('test.txt')

object_group = parse.find_objects('object network')
members = []

for line in object_group:
    if line.re_search_children('eee'):
        members.append(line)



pprint.pprint(object_group)
pprint.pprint(members)


#object_group = parse.find_objects_w_child('object network')


