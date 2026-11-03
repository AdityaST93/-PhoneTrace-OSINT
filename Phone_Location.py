from src.lookup import lookup_number
from src.exporter import export_result


def main():
    print("\n================================")
    print("       PHONE OSINT TOOLKIT")
    print("================================")

    while True:
        print("\n1. Phone Number Lookup")
        print("2. Exit")

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            number = input(
                "\nEnter phone number with country code: "
            ).strip()

            result = lookup_number(number)

            print("\n===== LOOKUP REPORT =====")

            for key, value in result.items():
                print(f"{key.replace('_', ' ').title()}: {value}")

            if "error" not in result and result.get("valid"):
                save = input("\nExport result to CSV? (y/n): ")

                if save.lower() == "y":
                    export_result(result)

        elif choice == "2":
            print("\nExiting Phone OSINT Toolkit...")
            break

        else:
            print("\nInvalid option. Try again.")


if __name__ == "__main__":
    main() 