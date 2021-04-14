results = list(container.query_items(
    'query': 'SELECT * FROM Incomes t WHERE udf.Tax(t.income) > 20000'))
