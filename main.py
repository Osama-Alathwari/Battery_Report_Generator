import os
import subprocess
from bs4 import BeautifulSoup
from datetime import date


def generate_battery_report():
    subprocess.run(['powercfg', '/batteryreport'], capture_output=True)


def parse_battery_report():
    report_path = 'battery-report.html'
    with open(report_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        report_date = soup.find(string=str(date.today()) + " ")
        report_time = soup.find(string=str(date.today()) + " ").find_next('span').text
        designed_capacity = int(soup.find(string="DESIGN CAPACITY").find_next('td').text.strip().split()[0].replace(",", ""))
        full_charge_capacity = int(soup.find(string="FULL CHARGE CAPACITY").find_next('td').text.strip().split()[0].replace(",", ""))
    return report_date, report_time, designed_capacity, full_charge_capacity


def calculate_remaining_capacity_percentage(designed_capacity, full_charge_capacity):
    remaining_capacity_percentage = (full_charge_capacity/designed_capacity)*100
    return remaining_capacity_percentage


def main():
    generate_battery_report()

    report_date, report_time, designed_capacity, full_charge_capacity = parse_battery_report()

    remaining_capacity_percentage = calculate_remaining_capacity_percentage(designed_capacity, full_charge_capacity)

    print("Report Date : ", report_date)
    print("Report Time : ", report_time)
    print("Designed Capacity = ", designed_capacity, "mWh")
    print("Full Charge Capacity = ", full_charge_capacity, "mWh")
    print("Battery Health = {:.2f}% ".format(remaining_capacity_percentage))


if __name__ == "__main__":
    main()