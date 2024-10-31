def list_serializer(members):
    result = []
    
    for member in members:
        item = {
            'id': member.id,
            'username': member.username,
            'grade': {
                'id': member.grade.id,
                'label': member.grade.label,
            },
            'weapon': {
                'id': member.weapon.id,
                'label': member.weapon.label,
            },
            'combat_type': {
                'id': member.combat_type.id,
                'label': member.combat_type.label,
            },
            'added_at': member.added_at,
            'is_activate': member.is_activate
        }

        result.append(item)

    return result

def show_serializer(member):
    return {
        'id': member.id,
        'username': member.username,
        'grade': {
            'id': member.grade.id,
            'label': member.grade.label
        },
        'weapon': {
                'id': member.weapon.id,
                'label': member.weapon.label,
        },
        'combat_type': {
                'id': member.combat_type.id,
                'label': member.combat_type.label,
        },
        'added_at': member.added_at.strftime('%Y-%m-%d') if member.added_at else "",
        'removed_at': member.removed_at.strftime('%Y-%m-%d') if member.removed_at else "",
        'is_on_discord': member.is_on_discord,
        'is_active': member.is_active,
        'has_privilege': member.has_privilege,
        'is_activate': member.is_activate,
    }