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

---

## Usage

Run the scraper with command-line arguments:

```powershell
python scraper.py --commissioner <code> --commissioner-name "<name>" --start-date <DD-MM-YYYY> --end-date <DD-MM-YYYY> --policy-area "<policy area>" --headed
```

**Arguments:**
- `--commissioner`: Commissioner code (required)
- `--commissioner-name`: Commissioner name (required)
- `--start-date`: Start date (DD-MM-YYYY)
- `--end-date`: End date (DD-MM-YYYY)
- `--policy-area`: Policy area name (optional, see list below)
- `--headed`: Run browser in headed mode (optional, default is headless)

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
