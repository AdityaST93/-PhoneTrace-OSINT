import phonenumbers
from phonenumbers import geocoder, carrier


def lookup_number(number):
    try:
        phone = phonenumbers.parse(number, None)

        result = {
            "number": phonenumbers.format_number(
                phone,
                phonenumbers.PhoneNumberFormat.INTERNATIONAL
            ),
            "valid": phonenumbers.is_valid_number(phone),
            "possible": phonenumbers.is_possible_number(phone),
            "country_code": phone.country_code,
            "region_code": phonenumbers.region_code_for_number(phone),
            "country_region": geocoder.description_for_number(
                phone, "en"
            ),
            "carrier": carrier.name_for_number(phone, "en"),
        }

        return result

    except phonenumbers.NumberParseException as error:
        return {"error": str(error)}


if __name__ == "__main__":
    number = input("Enter number with country code: ")
    result = lookup_number(number)

    print("\n===== PHONE OSINT REPORT =====")

    for key, value in result.items():
        print(f"{key.replace('_', ' ').title()}: {value}")