def calculate_total(quantity, unit_price):
    return unit_price * quantity


first_input_values = input().split()

first_code = int(first_input_values[0])
first_quantity = int(first_input_values[1])
first_price = float(first_input_values[2])
first_result = calculate_total(first_quantity, first_price)

second_input_values = input().split()

second_code = int(second_input_values[0])
second_quantity = int(second_input_values[1])
second_price = float(second_input_values[2])
second_result = calculate_total(second_quantity, second_price)

total = first_result + second_result

print(f"VALOR A PAGAR: R$ {total:.2f}")
