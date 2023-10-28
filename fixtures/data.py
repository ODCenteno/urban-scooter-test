VALID_DATA = {
    "user_details": {
        "name_2char": "Su",
        "name_3char": "Ana",
        "name_9char": "Sebastian",
        "name_14char": "Constantinople",
        "name_15char": "Alexandriabella",
        "last_name": "Montalvo",
        "phone_10char": "1123234345",
        "phone_11char": "+1123234345",
        "phone_12char": "+11232343450",
    },
    "address_5char": "12 St",
    "address_6char": "12 St.",
    "address_23char": "123 Main Street, Apt 4B",
    "address_49char": "3213 Oak Drive, Apt E2031, West Side, Los Angeles",
    "address_50char": "3213 Oak Drive, Apt. E2031, West Side, Los Angeles",
}

INVALID_DATA = {
    "empty_str": "",
    "user_details": {
        "name_1char": "A",
        "name_16char": "Maximilianthomas",
        "name_special_char": "Ana$",
        "name_with_num": "S3bastian",
        "address": "Camelias 123",
        "phone_9char": "112323434",
        "phone_13char": "+112323434501",
    },
    "address_4char": "A 12",
    "address_51char": "3213 Oaks Drive, Apt. E2031, West Side, Los Angeles",
}

dato1 = {
    "name": "Rigo",
    "age": 24,
    "band": "Los papuchos"
}
dato2 = {
    "name": "Daniel",
    "age": 28,
    "band": "Los Strokes"
}
dato3 = {
    "name": "Alex",
    "age": 42,
    "band": "Los Aguas Aguas"
}
