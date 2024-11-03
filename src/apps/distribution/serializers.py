
def list_serializer(distributions):
    result = []

    for distribution in distributions:    
        members = []

        for member in distribution.members.all():
            members.append({
                'id': member.id,
                'username': member.username
            })

        item = {
            'id': distribution.id,
            'loot': {
                'id': distribution.loot.id,
                'label': distribution.loot.label,
            },
            'members': members,
        }

        result.append(item)

    return result

def show_serializer(distribution):
    members = []

    for member in distribution.members.all():
        members.append({
            'id': member.id,
            'username': member.username
    })

    return {
        'id': distribution.id,
        'loot': {
            'id': distribution.loot.id,
            'label': distribution.loot.label,
        },
        'members': members,
        'created_at': distribution.created_at.strftime('%Y-%m-%d') if distribution.created_at else "",
        'updated_at': distribution.updated_at.strftime('%Y-%m-%d') if distribution.updated_at else "",
        'is_activate': distribution.is_activate,
    }

