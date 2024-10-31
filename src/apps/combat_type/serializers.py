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
        'created_at': combat_type.created_at.strftime('%Y-%m-%d') if combat_type.created_at else "",
        'updated_at': combat_type.updated_at.strftime('%Y-%m-%d') if combat_type.updated_at else "",
        'is_activate': combat_type.is_activate
    }