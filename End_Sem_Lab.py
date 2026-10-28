def circulation_report():
    departments = {}

    while True:
        raw = input('Enter the circulation(or "Exit" to finish):')

        if raw.strip().lower() == "exit":
            break

        book_id, dept, timestamp, operation = [
            part.strip() for part in raw.split("#")
        ]

        if dept not in departments:
            departments[dept] = {
                "seen": set(),
                "books": set(),
                "active": 0,
                "duplicates": 0
            }

        data = departments[dept]
        transaction = (book_id, dept, timestamp, operation)

        if transaction in data["seen"]:
            data["duplicates"] += 1
            continue

        data["seen"].add(transaction)
        data["books"].add(book_id)

        if operation.upper() == "CHECKOUT":
            data["active"] += 1
        elif operation.upper() == "RETURN":
            data["active"] -= 1

    for dept, data in departments.items():
        name = dept.replace("_", "-").title()
        active = data["active"]

        if active > 5:
            print(
                f"Library Report : {name} -> Active Circ : "
                f"{active} | Status : Capacity-Exceeded"
            )
        else:
            print(
                f"Library Report : {name} -> Active Circ : "
                f"{active} | Unique : {len(data['books'])} "
                f"| Dup : {data['duplicates']}"
            )


circulation_report()