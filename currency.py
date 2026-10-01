import os
import xml.dom.minidom as minidom
import csv

XML_FILENAME = 'currency.xml'
CSV_FILENAME = 'books.csv'

# 0. Создание файла currency.xml с корректной кодировкой UTF-8
if not os.path.exists(XML_FILENAME):
    xml_content = """<?xml version="1.0" encoding="utf-8"?>
<ValCurs Date="17.09.2026" name="Foreign Currency Market">
    <Valute ID="R01010">
        <NumCode>036</NumCode>
        <CharCode>AUD</CharCode>
        <Nominal>1</Nominal>
        <Name>Австралийский доллар</Name>
        <Value>62,4512</Value>
    </Valute>
    <Valute ID="R01035">
        <NumCode>826</NumCode>
        <CharCode>GBP</CharCode>
        <Nominal>1</Nominal>
        <Name>Фунт стерлингов Соединенного королевства</Name>
        <Value>115,3210</Value>
    </Valute>
    <Valute ID="R01090">
        <NumCode>933</NumCode>
        <CharCode>BYN</CharCode>
        <Nominal>1</Nominal>
        <Name>Белорусский рубль</Name>
        <Value>28,1420</Value>
    </Valute>
    <Valute ID="R01235">
        <NumCode>840</NumCode>
        <CharCode>USD</CharCode>
        <Nominal>1</Nominal>
        <Name>Доллар США</Name>
        <Value>92,5014</Value>
    </Valute>
    <Valute ID="R01239">
        <NumCode>978</NumCode>
        <CharCode>EUR</CharCode>
        <Nominal>1</Nominal>
        <Name>Евро</Name>
        <Value>100,1235</Value>
    </Valute>
    <Valute ID="R01375">
        <NumCode>156</NumCode>
        <CharCode>CNY</CharCode>
        <Nominal>1</Nominal>
        <Name>Китайский юань</Name>
        <Value>12,8540</Value>
    </Valute>
    <Valute ID="R01820">
        <NumCode>392</NumCode>
        <CharCode>JPY</CharCode>
        <Nominal>100</Nominal>
        <Name>Японских иен</Name>
        <Value>61,2540</Value>
    </Valute>
    <Valute ID="R01535">
        <NumCode>398</NumCode>
        <CharCode>KZT</CharCode>
        <Nominal>100</Nominal>
        <Name>Казахстанских тенге</Name>
        <Value>19,5410</Value>
    </Valute>
    <Valute ID="R01020">
        <NumCode>944</NumCode>
        <CharCode>AZN</CharCode>
        <Nominal>1</Nominal>
        <Name>Азербайджанский манат</Name>
        <Value>54,4120</Value>
    </Valute>
    <Valute ID="R01335">
        <NumCode>356</NumCode>
        <CharCode>INR</CharCode>
        <Nominal>10</Nominal>
        <Name>Индийских рупий</Name>
        <Value>11,1020</Value>
    </Valute>
</ValCurs>
"""
    with open(XML_FILENAME, 'w', encoding='utf-8') as f:
        f.write(xml_content)

print("=== ЗАДАНИЕ 4 (XML, Вариант 3: Список Name при Nominal = 1) ===")

# Считывание и парсинг XML через parseString
with open(XML_FILENAME, 'r', encoding='utf-8') as xml_file:
    xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

valutes = dom.getElementsByTagName('Valute')
names_with_nominal_one = []

for valute in valutes:
    nominal_node = valute.getElementsByTagName('Nominal')[0]
    name_node = valute.getElementsByTagName('Name')[0]
    
    # Приведение типов: номинал к целому числу (int), название к строке (str)
    nominal_val = int(nominal_node.firstChild.data.strip())
    name_val = str(name_node.firstChild.data.strip())
    
    if nominal_val == 1:
        names_with_nominal_one.append(name_val)

print(f"Всего найдено валют с номиналом 1: {len(names_with_nominal_one)}")
for idx, name in enumerate(names_with_nominal_one, 1):
    print(f"  {idx}. {name}")
print()

print("=== ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ ===")

# 1. Список авторов без повторений и 2. Топ-20 популярных книг
if os.path.exists(CSV_FILENAME):
    with open(CSV_FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        header = next(reader)
        unique_authors = set()
        all_books = []
        for row in reader:
            if row:
                unique_authors.add(row[1])
                all_books.append({
                    'author': row[1],
                    'title': row[2],
                    'downloads': int(row[5])
                })
        
        print("1. Перечень авторов без повторений:")
        for author in sorted(unique_authors):
            print(f"   • {author}")
        print()
        
        all_books.sort(key=lambda x: x['downloads'], reverse=True)
        top_20 = all_books[:20]
        
        print("2. Топ самых популярных книг (по числу выдач):")
        for i, b in enumerate(top_20, 1):
            print(f"   {i:2d}. «{b['title']}» ({b['author']}) — {b['downloads']} выдач")