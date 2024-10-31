def list_serializer(grades):
    result = []

    for grade in grades:
        item = {
            'id': grade['id'],
            'label': grade['label'],
            'is_activate': grade['is_activate']
        }

        result.append(item)

    return result

def show_serializer(grade):
    return {
        'id': grade.id,
        'label': grade.label,
        'created_at': grade.created_at.strftime('%Y-%m-%d') if grade.created_at else "",
        'updated_at': grade.updated_at.strftime('%Y-%m-%d') if grade.updated_at else "",
        'is_activate': grade.is_activate
    }