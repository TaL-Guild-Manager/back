
def list_serializer(loots):
    result = []

    for loot in loots:        
        item = {
            'id': loot.id,
            'label': loot.label,
            'boss': {
                'id': loot.boss.id,
                'label': loot.boss.label,
            },
            'loot_type': {
                'id': loot.loot_type.id,
                'label': loot.loot_type.label,
            },
        }

        result.append(item)

    return result

def show_serializer(loot):
    return {
        'id': loot.id,
        'label': loot.label,
        'boss': {
            'id': loot.boss.id,
            'label': loot.boss.label,
        },
        'loot_type': {
            'id': loot.loot_type.id,
            'label': loot.loot_type.label,
        },
        'created_at': loot.created_at.strftime('%Y-%m-%d') if loot.created_at else "",
        'updated_at': loot.updated_at.strftime('%Y-%m-%d') if loot.updated_at else "",
        'is_activate': loot.is_activate,
    }

