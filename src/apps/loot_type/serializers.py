def list_serializer(loot_types):
    result = []

    for loot_type in loot_types:
        item = {
            'id': loot_type['id'],
            'label': loot_type['label'],
            'is_activate': loot_type['is_activate']
        }

        result.append(item)

    return result

def show_serializer(loot_type):
    return {
        'id': loot_type.id,
        'label': loot_type.label,
        'is_activate': loot_type.is_activate
    }