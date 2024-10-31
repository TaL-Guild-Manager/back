def list_serializer(weapons):
    result = []

    for weapon in weapons:
        item = {
            'id': weapon['id'],
            'label': weapon['label'],
            'is_activate': weapon['is_activate']
        }

        result.append(item)

    return result

def show_serializer(weapon):
    return {
        'id': weapon.id,
        'label': weapon.label,
        'is_activate': weapon.is_activate
    }