def list_serializer(bises):
    result = []

    for bis in bises:
        stuffs = []
        
        for stuff in bis.stuffs.all():
            stuffs.append({
                'id': stuff.id,
                'label': stuff.label,
                'has_been_acquired': stuff.has_been_acquired if stuff.is_raid_loot else False,
                'acquired_at': stuff.acquired_at if stuff.has_been_acquired else None,
            })

        item = {
            'id': bis.id,
            'members': {
                'id': bis.member.id,
                'username': bis.member.username,
                'weapon': {
                    'id': bis.member.weapon.id,
                    'label': bis.member.weapon.label,
                },
                'combat_type': {
                    'id': bis.member.combat_type.id,
                    'label': bis.member.combat_type.label,
                },
            },
            'stuffs': stuffs,
            'is_primary': bis.is_primary,
        }

        result.append(item)

    return result

def show_serializer(bis):
    stuffs = []

    for stuff in bis.stuffs.all():
        stuffs.append({
            'id': stuff.id,
            'label': stuff.label,
            'is_raid_loot': stuff.is_raid_loot,
            'boss': {
                'id': stuff.boss.id,
                'label': stuff.boss.label,
            } if stuff.is_raid_loot else None,
            'loot_type': {
                'id': stuff.loot_type.id,
                'label': stuff.loot_type.label
            } if stuff.loot_type else None,
            'has_been_acquired': stuff.has_been_acquired if stuff.is_raid_loot else False,
            'acquired_at': stuff.acquired_at if stuff.has_been_acquired else None,
            'is_activate': stuff.is_activate
        })

    return {
        'id': bis.id,
        'member': {
            'id': bis.member.id,
            'username': bis.member.username,
            'weapon': {
                'id': bis.member.weapon.id,
                'label': bis.member.weapon.label,
            },
            'combat_type': {
                'id': bis.member.combat_type.id,
                'label': bis.member.combat_type.label,
            },
        },
        'stuffs': stuffs,
        'is_primary': bis.is_primary,
        'created_at': bis.created_at.strftime('%Y-%m-%d') if bis.created_at else "",
        'updated_at': bis.updated_at.strftime('%Y-%m-%d') if bis.updated_at else "",
        'is_activate': bis.is_activate,
    }

