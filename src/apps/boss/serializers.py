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
    loots = []

    for loot in boss.loot_set.all():
        loots.append({
            'id': loot.id,
            'label': loot.label,
            'loot_type': {
                'id': loot.loot_type.id,
                'label': loot.loot_type.label,
            },
        })

    return {
        'id': boss.id,
        'label': boss.label,
        'loots': loots,
        'created_at': boss.created_at.strftime('%Y-%m-%d') if boss.created_at else "",
        'updated_at': boss.updated_at.strftime('%Y-%m-%d') if boss.updated_at else "",
        'is_activate': boss.is_activate
    }