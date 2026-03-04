import re
import json
from datetime import datetime

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()


item_pattern = re.compile(
    r"\d+\.\s*\n"                  
    r"(.+?)\n"                     
    r"([\d,]+)\s*x\s*([\d\s]+,\d+)\n"  
    r"([\d\s]+,\d+)\n"             
    r"Стоимость\n"
    r"([\d\s]+,\d+)",               
    re.MULTILINE
)

products = []

for match in item_pattern.findall(text):
    name = match[0].strip()
    quantity = float(match[1].replace(",", "."))
    unit_price = float(match[2].replace(" ", "").replace(",", "."))
    total_price = float(match[3].replace(" ", "").replace(",", "."))

    products.append({
        "name": name,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_price": total_price
    })


total_pattern = re.search(r"ИТОГО:\s*\n([\d\s]+,\d+)", text)
overall_total = float(
    total_pattern.group(1).replace(" ", "").replace(",", ".")
) if total_pattern else sum(item["total_price"] for item in items)


payment_pattern = re.search(r"(Банковская карта|НАЛИЧНЫЕ|КАРТА)", text)
payment_method = payment_pattern.group(1) if payment_pattern else "Не указано"

date_pattern = re.search(r"Время:\s*([\d\.]+\s+[\d:]+)", text)

if date_pattern:
    receipt_datetime = datetime.strptime(
        date_pattern.group(1), "%d.%m.%Y %H:%M:%S"
    ).strftime("%Y-%m-%d %H:%M:%S")
else:
    receipt_datetime = "Не найдено"

receipt_data = {
    "products": products,
    "overall_total": overall_total,
    "payment_method": payment_method,
    "receipt_datetime": receipt_datetime,
    "parsed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

print(json.dumps(receipt_data, ensure_ascii=False, indent=4))