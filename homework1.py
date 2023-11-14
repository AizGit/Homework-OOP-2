cook_book = {}
with open("omlet.txt",  "rt", encoding="utf-8",) as file:
    for l in file:
        department_name = l.strip()
        dictic = []
        listik = {}
        employees_count = file.readline()
        for i in range (int(employees_count)):
            emp = file.readline()
            ingredient_name, quantity, measure = emp.strip().split(" | ")
            dictic.append({"ingredient_name": ingredient_name, "quantity": quantity,"measure":measure})
            dep = {department_name: dictic}
        blank_line = file.readline()
        cook_book.update(dep)
print(f"cook_book = {cook_book}")