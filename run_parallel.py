import subprocess
from concurrent.futures import ThreadPoolExecutor
import argparse

commissioners = [
    ("881", "Ursula von der Leyen"),
    ("166", "Valdis Dombrovskis"),
    ("183", "Maroš Šefčovič"),
    ("982", "Dubravka Šuica"),
    ("998", "Olivér Várhelyi"),
    ("1881", "Wopke Hoekstra"),
    ("2086", "Maria Luís Albuquerque"),
    ("2087", "Magnus Brunner"),
    ("2088", "Raffaele Fitto"),
    ("2089", "Christophe Hansen"),
    ("2090", "Dan Jørgensen"),
    ("2091", "Kaja Kallas"),
    ("2092", "Andrius Kubilius"),
    ("2093", "Marta Kos"),
    ("2094", "Costas Kadis"),
    ("2095", "Hadja Lahbib"),
    ("2096", "Roxana Mînzatu"),
    ("2097", "Michael McGrath"),
    ("2098", "Glenn Micallef"),
    ("2099", "Teresa Ribera"),
    ("2100", "Jessika Roswall"),
    ("2101", "Stéphane Séjourné"),
    ("2102", "Jozef Síkela"),
    ("2103", "Piotr Serafin"),
    ("2104", "Apostolos Tzitzikostas"),
    ("2105", "Henna Virkkunen"),
    ("2106", "Ekaterina Zaharieva"),
]

def run_scraper(code, name, start_date=None, end_date=None, policy_area=None, headed=False):
    cmd = [
        "python", "scraper.py",
        "--commissioner", code,
        "--commissioner-name", name
    ]
    if start_date:
        cmd += ["--start-date", start_date]
    if end_date:
        cmd += ["--end-date", end_date]
    if policy_area:
        cmd += ["--policy-area", policy_area]
    if headed:
        cmd += ["--headed"]
    print(f"Starting: {name} ({code})")
    subprocess.run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--include", nargs="*", default=[], help="Commissioner names to include")
    parser.add_argument("--start-date", help="Start date in DD-MM-YYYY format")
    parser.add_argument("--end-date", help="End date in DD-MM-YYYY format")
    parser.add_argument("--policy-area", help="Policy area name (e.g. 'Animal Welfare')")
    parser.add_argument("--headed", action="store_true")
    args = parser.parse_args()

    if args.include:
        filtered = [(code, name) for code, name in commissioners if name in args.include]
    else:
        filtered = commissioners

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for code, name in filtered:
            futures.append(executor.submit(
                run_scraper, code, name, args.start_date, args.end_date, args.policy_area, args.headed
            ))
        for f in futures:
            f.result()
