def extract_name(data: dict) -> str:
    name = data["name"]
    return f"{name['first']} {name['last']}"


def extract_gender(data: dict) -> str:
    return data["gender"]


def extract_email(data: dict) -> str:
    return data["email"]


def extract_birth_info(data: dict) -> dict:
    dob = data["dob"]
    return {
        "birth_date": dob["date"],
        "age": dob["age"]
    }


def extract_location(data: dict) -> dict:
    location = data["location"]
    return {
        "city": location["city"],
        "state": location["state"],
        "country": location["country"],
        "postcode": location["postcode"]
    }

def parse_user(data: dict) -> dict:
    user = {
        "full_name": extract_name(data),
        "gender": extract_gender(data),
        "email": extract_email(data)
    }

    user.update(extract_birth_info(data))
    user.update(extract_location(data))

    return user