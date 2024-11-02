def list_serializer(roadsters):
    result = []

    for roadster in roadsters:
        members = []

        for member in roadster.members.all():
            members.append({
                'id': member.id,
                'username': member.username,
                'weapon': {
                    'id': member.weapon.id,
                    'label': member.weapon.label
                } if member.weapon else None,
                'combat_type': {
                    'id': member.combat_type.id,
                    'label': member.combat_type.label
                } if member.combat_type else None,
            })
        
        item = {
            'id': roadster.id,
            'label': roadster.label,
            'members': members,
            'is_pvp': roadster.is_pvp,
        }

        result.append(item)

    return result

def show_serializer(roadster):
    members = []

    for member in roadster.members.all():
        members.append({
            'id': member.id,
            'username': member.username,
            'weapon': {
                'id': member.weapon.id,
                'label': member.weapon.label
            } if member.weapon else None,
            'combat_type': {
                'id': member.combat_type.id,
                'label': member.combat_type.label
            } if member.combat_type else None,
            'is_on_discord': member.is_on_discord,
            'is_activate': member.is_activate
        })

    return {
        'id': roadster.id,
        'label': roadster.label,
        'is_pvp': roadster.is_pvp,
        'members': members,
        'created_at': roadster.created_at.strftime('%Y-%m-%d') if roadster.created_at else "",
        'updated_at': roadster.updated_at.strftime('%Y-%m-%d') if roadster.updated_at else "",
        'is_activate': roadster.is_activate,
    }

