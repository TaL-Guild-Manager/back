def list_serializer(blacklists):
    result = []

    for blacklist in blacklists:
        item = {
            'id': blacklist.id,
            'username': blacklist.username,
            'previous_guild': blacklist.previous_guild if blacklist.previous_guild else None,
            'reason': blacklist.reason if blacklist.reason else None,
        }

        result.append(item)

    return result

def show_serializer(blacklist):
    return {
        'id': blacklist.id,
        'username': blacklist.username,
        'previous_guild': blacklist.previous_guild if blacklist.previous_guild else None,
        'reason': blacklist.reason if blacklist.reason else None,
        'created_at': blacklist.created_at.strftime('%Y-%m-%d') if blacklist.created_at else "",
        'updated_at': blacklist.updated_at.strftime('%Y-%m-%d') if blacklist.updated_at else "",
        'is_activate': blacklist.is_activate,
    }

