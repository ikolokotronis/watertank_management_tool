from utils.most_common import most_common

history = {
    'refill': {'operation_name': 'refill', 'tank': 'tank_01', 'operation_type': 'Pour water', 'status': 1, 'date_time': '31/08/2022 15:37:49'},
    'use': {'operation_name': 'refill', 'tank': 'tank_01', 'operation_type': 'Pour out water', 'status': 0, 'date_time': '31/08/2022 15:37:49'},
    'reuse': {'operation_name': 'refill', 'tank': 'tank_01', 'operation_type': 'Pour water', 'status': 1, 'date_time': '31/08/2022 15:37:49'},
           }


def find_most_used_types():
    types = []
    for key, value in history.items():
        for props_key, props_value in value.items():
            if props_key == 'operation_type':
                types.append(props_value)
    print(f'Most common type: {most_common(types)}')
    return most_common(types)


find_most_used_types()