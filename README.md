# Battery Report Generator and Parser

This Python script generates a battery report using `powercfg` and parses it to display relevant information such as report date, time, designed capacity, full charge capacity, and battery health percentage.

## Prerequisites

- Python 3.x (should be installed on your system)
- BeautifulSoup (`pip install beautifulsoup4`)

## Usage

1. Clone the repository:
git clone https://github.com/Osama-Alathwari/Battery_Report_Generator.git


2. Navigate to the project directory:
cd Battery_Report_Generator


3. Run the script:
python main.py


## Output

The script generates an HTML battery report file (`battery-report.html`) and prints the following information:

- Report Date
- Report Time
- Designed Capacity (mWh)
- Full Charge Capacity (mWh)
- Battery Health (%)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
