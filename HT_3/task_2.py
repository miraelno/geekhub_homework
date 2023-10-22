# 2. Write a script to remove an empty elements from a list.
#     Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

test_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

result_list = [i for i in test_list if i]
print(result_list)
