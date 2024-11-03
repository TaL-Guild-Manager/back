
def list_serializer(contributions):
    result = []

    for contribution in contributions:        
        item = {
            'id': contribution.id,
            'member': {
                'id': contribution.member.id,
                'username': contribution.member.username,
            },
            'start': contribution.start,
            'end': contribution.end,
            'contribution_start': contribution.contribution_start.strftime('%Y-%m-%d') if contribution.created_at else "",
            'contribution_end': contribution.contribution_end.strftime('%Y-%m-%d') if contribution.updated_at else "",
        }

        result.append(item)

    return result

def show_serializer(contribution):
    return {
        'id': contribution.id,
        'member': {
            'id': contribution.member.id,
            'username': contribution.member.username,
        },
        'start': contribution.start,
        'end': contribution.end,
        'contribution_start': contribution.contribution_start.strftime('%Y-%m-%d') if contribution.created_at else "",
        'contribution_end': contribution.contribution_end.strftime('%Y-%m-%d') if contribution.updated_at else "",
        'created_at': contribution.created_at.strftime('%Y-%m-%d') if contribution.created_at else "",
        'updated_at': contribution.updated_at.strftime('%Y-%m-%d') if contribution.updated_at else "",
        'is_activate': contribution.is_activate,
    }

