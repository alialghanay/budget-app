def create_spend_chart(categories):
    total_spent = 0
    category_spent = []

    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        category_spent.append(spent)
        total_spent += spent

    category_spent_percent = [int((spent / total_spent) * 100) // 10 * 10 for spent in category_spent]

    chart = 'Percentage spent by category\n'

    for i in range(100, -1, -10):
        chart += f'{i:>3}| '
        for percent in category_spent_percent:
            chart += 'o  ' if percent >= i else '   '
        chart += '\n'

    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        chart += '    '
        for category in categories:
            if i < len(category.name):
                chart += ' ' + category.name[i] + ' '
            else:
                chart += '   '
        chart += ' \n' if i < max_length - 1 else ' '

    return chart