# PhoneTrace-OSINT

**A Python-based Phone Number OSINT Toolkit for Educational and Research Purposes.**

## About

PhoneTrace-OSINT is a lightweight Python project designed to demonstrate basic phone-number intelligence using the `phonenumbers` library.

It extracts publicly available numbering metadata and presents the results in a simple terminal interface.

## Features

- Phone number validation
- International number formatting
- Country and region identification where available
- Carrier information where available
- CSV report export
- Modular Python architecture
- Error handling and input validation

## Technology Stack

- Python 3
- phonenumbers
- CSV
- Visual Studio Code

## Project Structure

```text
PhoneTrace-OSINT/
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ lookup.py
â”‚   â””â”€â”€ exporter.py
â”œâ”€â”€ data/
â”œâ”€â”€ docs/
â”‚   â””â”€â”€ FEATURES.md
â”œâ”€â”€ tests/
â”‚   â””â”€â”€ test_lookup.py
â”œâ”€â”€ Phone_Location.py
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ README.md
â””â”€â”€ .gitignore
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd PhoneTrace-OSINT
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python Phone_Location.py
```

## Limitations

This project does not provide:

- Live GPS tracking
- Exact physical location
- Subscriber identity or private records
- Guaranteed district-level identification

Country, region and carrier information depend on the available numbering metadata. Mobile number portability may affect accuracy.

## Educational Disclaimer

This project is developed for educational, academic and authorized cybersecurity research purposes only.

Use only your own phone numbers or numbers for which you have explicit permission. Do not use this project to harass, monitor or invade anyone's privacy.

The developer is not responsible for misuse of this software.





## Author

Aditya Singh Thakur

## License

