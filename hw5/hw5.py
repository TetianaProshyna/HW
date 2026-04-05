import os
import requests
import certifi
from collections import Counter
from itertools import combinations, chain


def download_document(file_name, document_url):
    if os.path.exists(file_name):
        return
    response = requests.get(document_url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
    else:
        raise RuntimeError('Failed to download file')


def fetch_data_from_url(url):
    response = requests.get(url, verify=certifi.where())
    response.raise_for_status()
    return response.text


def parse_orders_from_text(text):
    orders = []
    raw_orders = text.split('\n\n')

    for row in raw_orders:
        row = row.strip()
        if row:
            products = [p.strip() for p in row.split('@@@') if p.strip()]
            orders.append(products)

    return orders


def parse_orders_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
    return parse_orders_from_text(text)


def count_products(orders):
    return Counter(chain.from_iterable(orders))


def count_product_pairs(orders):
    pair_counter = Counter()

    for order in orders:
        unique_products = set(order)
        for pair in combinations(sorted(unique_products), 2):
            pair_counter[pair] += 1

    return pair_counter


def find_association_rules(products, product_pairs, min_support=15, min_confidence=45):
    rules = []
    rule_id = 1

    for (x, y), support in product_pairs.items():
        if support < min_support:
            continue

        confidence_x_y = support / products[x] * 100
        confidence_y_x = support / products[y] * 100

        if confidence_x_y >= min_confidence:
            rules.append(
                f'p{rule_id} {x} => {y} ({confidence_x_y:.2f}% confidence), {support} support'
            )
            rule_id += 1

        if confidence_y_x >= min_confidence:
            rules.append(
                f'p{rule_id} {y} => {x} ({confidence_y_x:.2f}% confidence), {support} support'
            )
            rule_id += 1

    return rules


def main():
    file_name = 'orders.txt'
    url = 'https://drive.google.com/uc?id=1IOPTVq2ooQfZRkF3rAjGkTjRtbotG7FF'

    # 1
    download_document(file_name, url)
    orders = parse_orders_from_file(file_name)

    # 2
    # text = fetch_data_from_url(url)
    # orders = parse_orders_from_text(text)

    products = count_products(orders)
    product_pairs = count_product_pairs(orders)

    print(f'Довжина списку = {len(orders)}')
    print(f'Кількість унікальних товарів = {len(products)}')
    print(f'Знайдено {len(product_pairs)} пар товарів із {len(orders)} замовлень\n')

    rules = find_association_rules(
        products,
        product_pairs,
        min_support=15,
        min_confidence=45
    )

    print(f'Знайдено правил: {len(rules)}\n')
    for rule in rules:
        print(rule)


if __name__ == "__main__":
    main()