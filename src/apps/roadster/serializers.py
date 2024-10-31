def list_serializer(roadsters):
    result = []

    for roadster in roadsters:
        item = {
            'id': roadster.id,
            'label': roadster.label,
            'is_pvp': roadster.is_pvp
        }

        result.append(item)

    return result

def show_serializer(roadster):
    return {
        'id': roadster.id,
        'label': roadster.label,
        'is_pvp': roadster.is_pvp,
        'created_at': roadster.created_at.strftime('%Y-%m-%d'),
        'updated_ad': roadster.updated_at.strftime('%Y-%m-%d'),
        'is_activate': roadster.is_activate,
    }
