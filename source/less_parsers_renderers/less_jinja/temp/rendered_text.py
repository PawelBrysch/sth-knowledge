
# some_dict.items()
# >>> dict_items([('first_key', Object with ID=2B), ('second_key', Object with ID=9Z)])

# some_dict.items()|map('last')
# >>> <generator object do_map at 0x000000000499D888>
# some_dict.items()|map('last')|list
# >>> [Object with ID=2B, Object with ID=9Z]

# some_dict.items()|map('last')|selectattr('name', 'equalto', '2B')
# >>> <generator object select_or_reject at 0x000000000499D048>
# some_dict.items()|map('last')|selectattr('name', 'equalto', '2B')|list
# >>> [Object with ID=2B]

# some_dict.items()|map('last')|selectattr('name', 'equalto', 'MC2')|list
# >>>[]