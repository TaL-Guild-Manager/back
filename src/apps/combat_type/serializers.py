def list_serializer(combat_types):
    result = []

    for combat_type in combat_types:
        item = {
            'id': combat_type['id'],
            'label': combat_type['label'],
            'is_activate': combat_type['is_activate']
        }

        result.append(item)

    return result

def show_serializer(combat_type):
    return {
        'id': combat_type.id,
        'label': combat_type.label,
        'is_activate': combat_type.is_activate
    }