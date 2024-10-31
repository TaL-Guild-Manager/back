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
        'created_at': boss.created_at.strftime('%Y-%m-%d') if boss.created_at else "",
        'updated_at': boss.updated_at.strftime('%Y-%m-%d') if boss.updated_at else "",
        'is_activate': boss.is_activate
    }