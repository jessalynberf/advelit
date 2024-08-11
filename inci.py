dict_all = {key: dict1.get(key, []) + dict2.get(key, []) for key in dict2.keys()}
