def list_serializer(bosses):
    result = []

    for boss in bosses:
        item = {
            'id': boss['id'],
            'label': boss['label'],
            'is_activate': boss['is_activate']
        }

        result.append(item)

    return result

def show_serializer(boss):
    return {
        'id': boss.id,
        'label': boss.label,
        'is_activate': boss.is_activate
    }