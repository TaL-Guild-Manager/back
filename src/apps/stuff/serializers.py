def list_serializer(stuffs):
    result = []

    for stuff in stuffs:
        item = {
            'id': stuff.id,
            'label': stuff.label,
            'is_raid_loot': stuff.is_raid_loot,
            'loot_type': {
                'id': stuff.loot_type.id,
                'label': stuff.loot_type.label,
            } if stuff.loot_type else None,
            'boss': {
                'id': stuff.boss.id,
                'label': stuff.boss.label,
            } if stuff.boss else None,
            'is_activate': stuff.is_activate
        }

        result.append(item)

    return result

def show_serializer(stuff):
    return {
            'id': stuff.id,
            'label': stuff.label,
            'is_raid_loot': stuff.is_raid_loot,
            'loot_type': {
                'id': stuff.loot_type.id,
                'label': stuff.loot_type.label,
            } if stuff.loot_type else None,
            'boss': {
                'id': stuff.boss.id,
                'label': stuff.boss.label,
            } if stuff.boss else None,
            'created_at': stuff.created_at.strftime('%Y-%m-%d') if stuff.created_at else "",
            'updated_at': stuff.updated_at.strftime('%Y-%m-%d') if stuff.updated_at else "",
            'is_activate': stuff.is_activate
        }