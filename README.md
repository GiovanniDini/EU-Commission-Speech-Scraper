# European Commission Press Corner Scraper

This Python tool automates downloading speeches and statements from the European Commission Press Corner website.  
You can filter by commissioner, policy area, and date range. Downloads are organized by commissioner, policy area, and date range.

---

## Features

- Filters by commissioner (name and code)
- Filters by policy area (from a predefined list)
- Filters by date range (start and end dates)
- Downloads PDFs for speeches and statements
- Handles cookie banners automatically
- Organizes downloads in directories:  
  `[commissioner_name]_[commissioner_code]/[policy_area]/[start_date]_to_[end_date]/`

---

## Requirements

- Python 3.8+
- [Selenium](https://pypi.org/project/selenium/)
- [requests](https://pypi.org/project/requests/)
- Google Chrome browser
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (must match your Chrome version and be in your PATH)

Install dependencies:
```powershell
pip install selenium requests
```
Install environment
---

## Terminal Environment

You can run the scraper from:

- **Windows Command Prompt** (`cmd`)
- **Windows PowerShell**
- **macOS Terminal**
- **Linux Terminal**
- **VS Code integrated terminal**

Make sure:
- Python is installed and available in your PATH.
- ChromeDriver is installed and available in your PATH.
- You are in the project directory (where `scraper.py` and `run_parallel.py` are located).

**Example (Windows):**
```powershell
cd "C:\Users\xxx\\Desktop\EU Politics Paper\selenium scraper"
python scraper.py --commissioner 881 --commissioner-name "Ursula von der Leyen" --start-date 01-03-2026 --end-date 07-03-2026 --policy-area "Climate action" --headed
```

**Example (macOS/Linux):**
```bash
cd ~/Desktop/EU\ Politics\ Paper/selenium\ scraper
python3 scraper.py --commissioner 881 --commissioner-name "Ursula von der Leyen" --start-date 01-03-2026 --end-date 07-03-2026 --policy-area "Climate action" --headed
```

---
---

## Usage

Run the scraper with command-line arguments:

```powershell
python scraper.py --commissioner <code> --commissioner-name "<name>" --start-date <DD-MM-YYYY> --end-date <DD-MM-YYYY> --policy-area "<policy area>" --headed
```

Or use the parallel runner to scrape multiple commissioners at once:

```powershell
python run_parallel.py --include "Ursula von der Leyen" "Henna Virkkunen" --start-date 01-01-2025 --end-date 31-12-2025 --policy-area "Climate action" --headed
```

**Arguments:**
- `--commissioner`: Commissioner code (required)
- `--commissioner-name`: Commissioner name (required)
- `--start-date`: Start date (DD-MM-YYYY)
- `--end-date`: End date (DD-MM-YYYY)
- `--policy-area`: Policy area name (optional, see list below)
- `--headed`: Run browser in headed mode (optional, default is headless)
- `--include`: (run_parallel.py only) List of commissioner names to include

**Example:**
```powershell
python scraper.py --commissioner 881 --commissioner-name "Ursula von der Leyen" --start-date 01-03-2026 --end-date 07-03-2026 --policy-area "Climate action" --headed
```

---

## Output Directory Structure

Downloads are saved as:
```
<commissioner_name>_<commissioner_code>/
    <policy_area>/
        <start_date>_to_<end_date>/
            [PDF files]
```
Example:
```
Ursula von der Leyen_881/
    Climate_action/
        01-03-2026_to_07-03-2026/
            881_p1_1.pdf
            881_p1_2.pdf
            ...
```

---

## Commissioners

Supported commissioners (use the exact name and code):

| Code   | Name                    |
|--------|------------------------|
| 881    | Ursula von der Leyen   |
| 166    | Valdis Dombrovskis     |
| 183    | Maroš Šefčovič         |
| 982    | Dubravka Šuica         |
| 998    | Olivér Várhelyi        |
| 1881   | Wopke Hoekstra         |
| 2086   | Maria Luís Albuquerque |
| 2087   | Magnus Brunner         |
| 2088   | Raffaele Fitto         |
| 2089   | Christophe Hansen      |
| 2090   | Dan Jørgensen          |
| 2091   | Kaja Kallas            |
| 2092   | Andrius Kubilius       |
| 2093   | Marta Kos              |
| 2094   | Costas Kadis           |
| 2095   | Hadja Lahbib           |
| 2096   | Roxana Mînzatu         |
| 2097   | Michael McGrath        |
| 2098   | Glenn Micallef         |
| 2099   | Teresa Ribera          |
| 2100   | Jessika Roswall        |
| 2101   | Stéphane Séjourné      |
| 2102   | Jozef Síkela           |
| 2103   | Piotr Serafin          |
| 2104   | Apostolos Tzitzikostas |
| 2105   | Henna Virkkunen        |
| 2106   | Ekaterina Zaharieva    |

---

## Policy Areas

Supported policy areas (use the exact name):

- Agriculture and rural development
- Animal Welfare
- Antitrust
- Artifical intelligence
- Banking and financial services
- Borders
- Brexit
- Budget
- Business and industry
- Climate action
- Cohesion Policy
- Commission Juncker 2014 -2019
- Competition
- Competitiveness
- Consumers
- Culture and media
- Customs
- Cybersecurity
- Defence
- Democracy
- Demography
- Digital economy and society
- Disinformation
- EU enlargement
- Economy, finance and the euro
- Education and training
- Employment and social affairs
- Energy
- Environment
- Equality
- European Green Deal
- European neighbourhood policy
- Food safety
- Foreign affairs and security policy
- General information
- Global Gateway
- Home affairs
- Housing
- Humanitarian aid and civil protection
- Institutional affairs
- Interinstitutional relations and foresight
- International partnerships
- Justice and fundamental rights
- Maritime affairs and fisheries
- Mediterranean
- Mergers
- Middle East
- Migration and asylum
- New European Bauhaus
- NextGenerationEU
- Presidency
- Public health
- Recovery and Resilience Facility
- Reforms
- Research and innovation
- Security
- Single market
- Space
- Sport
- State aid
- State of the Union
- Taxation
- Technology
- Trade
- Transport
- UN Climate Change Conference (COP)
- Ukraine
- Vaccines
- Youth

---

## Troubleshooting

- Make sure ChromeDriver matches your Chrome version.
- If you get a TimeoutException, try increasing wait times or running with `--headed` for debugging.
- If downloads are not appearing, check directory structure and permissions.

---

## License

MIT License
