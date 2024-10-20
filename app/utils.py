def calculate_split(split_type, participants, total_amount):
    split_data = []
    if split_type == 'equal':
        amount_per_person = total_amount / len(participants)
        for participant in participants:
            split_data.append({
                'user_id': participant['user_id'],
                'amount_owed': amount_per_person
            })
    elif split_type == 'exact':
        for participant in participants:
            split_data.append({
                'user_id': participant['user_id'],
                'amount_owed': participant['exact_amount']
            })
    elif split_type == 'percentage':
        total_percentage = sum(p['percentage'] for p in participants)
        if total_percentage != 100:
            raise ValueError('Total percentages must add up to 100')
        for participant in participants:
            split_data.append({
                'user_id': participant['user_id'],
                'amount_owed': (participant['percentage'] / 100) * total_amount
            })
    return split_data
