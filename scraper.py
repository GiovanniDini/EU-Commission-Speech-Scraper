import argparse
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://ec.europa.eu/commission/presscorner/home/en"

# Full list of policy areas and codes
POLICY_AREAS = {
    "Agriculture and rural development": "AGRURAL",
    "Animal Welfare": "ANIWELFARE",
    "Antitrust": "ANTITRUST",
    "Artifical intelligence": "AI",
    "Banking and financial services": "FINSTAB",
    "Borders": "BORDER",
    "Brexit": "BREXIT",
    "Budget": "BUDFINPROG",
    "Business and industry": "BUSINDUS",
    "Climate action": "CLIMACTION",
    "Cohesion Policy": "REGIONAL",
    "Commission Juncker 2014 -2019": "JUNCKER-CABINET",
    "Competition": "COMPETY",
    "Competitiveness": "COMPETITIVE",
    "Consumers": "CONSUMPOL",
    "Culture and media": "CULTMED",
    "Customs": "CUSTOMS",
    "Cybersecurity": "CYBER",
    "Defence": "DEFENCE",
    "Democracy": "DEMOCRACY",
    "Demography": "DEMOGRAPHY",
    "Digital economy and society": "DIGAG",
    "Disinformation": "DISINFO",
    "EU enlargement": "ENLNEIG",
    "Economy, finance and the euro": "ECOMONAFF",
    "Education and training": "ECMY",
    "Employment and social affairs": "ESAI",
    "Energy": "ENERGY",
    "Environment": "ENVIRO",
    "Equality": "EQUALITY",
    "European Green Deal": "PR-GREENDEAL",
    "European neighbourhood policy": "NEIGHB",
    "Food safety": "FOODSAF",
    "Foreign affairs and security policy": "HREXTRELS",
    "General information": "GENINFO",
    "Global Gateway": "GLOBGA",
    "Home affairs": "HOMEAFF",
    "Housing": "HOUSE",
    "Humanitarian aid and civil protection": "ICHACR",
    "Institutional affairs": "INTRELADM",
    "Interinstitutional relations and foresight": "INRELATION",
    "International partnerships": "DEVEL",
    "Justice and fundamental rights": "JFRC",
    "Maritime affairs and fisheries": "MARAFFISH",
    "Mediterranean": "MED",
    "Mergers": "MERGERS",
    "Middle East": "MIDDLE",
    "Migration and asylum": "MIGR",
    "New European Bauhaus": "NEBAUHAUS",
    "NextGenerationEU": "NGEU",
    "Presidency": "PRESIDENCY",
    "Public health": "HEALTHPOL",
    "Recovery and Resilience Facility": "RECOVERY",
    "Reforms": "STRUREF",
    "Research and innovation": "RESINSC",
    "Security": "SECU",
    "Single market": "GROWTH",
    "Space": "SPACE",
    "Sport": "SPORT",
    "State aid": "STATAID",
    "State of the Union": "SOTEU",
    "Taxation": "TAXCUAA",
    "Technology": "TECH",
    "Trade": "TRADEPOL",
    "Transport": "TRANSPORT",
    "UN Climate Change Conference (COP)": "COP",
    "Ukraine": "UKRAINE",
    "Vaccines": "VACC",
    "Youth": "YOUTH"
}

def setup_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)

def apply_filters(driver, commissioner_code, commissioner_name, start_date=None, end_date=None, policy_area=None):
    wait = WebDriverWait(driver, 30)
    driver.get(BASE_URL)

    # Dismiss cookie banner
    try:
        cookie_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'Accept all cookies')]")
        ))
        driver.execute_script("arguments[0].click();", cookie_btn)
        time.sleep(1)
    except Exception:
        try:
            cookie_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(), 'Accept only essential cookies')]")
            ))
            driver.execute_script("arguments[0].click();", cookie_btn)
            time.sleep(1)
        except Exception:
            pass

    # Optional date filter (type dates directly)
    if start_date:
        date_input_from = wait.until(EC.element_to_be_clickable((By.ID, "datepicker1")))
        date_input_from.clear()
        date_input_from.send_keys(start_date)
        time.sleep(1)
    if end_date:
        date_input_to = wait.until(EC.element_to_be_clickable((By.ID, "datepicker2")))
        date_input_to.clear()
        date_input_to.send_keys(end_date)
        time.sleep(1)

    # Click "More criteria"
    more_criteria_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(), 'More criteria')]")
    ))
    driver.execute_script("arguments[0].click();", more_criteria_btn)
    time.sleep(1)

    # Document type: click first select (by ID)
    doc_type_select = wait.until(EC.element_to_be_clickable((By.ID, "filter-documentType-toggle")))
    driver.execute_script("arguments[0].click();", doc_type_select)
    time.sleep(1)

    # Tick "Speech" and "Statement" checkboxes
    for label in ["Speech", "Statement"]:
        try:
            option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{label}']")))
            driver.execute_script("arguments[0].click();", option)
            time.sleep(0.5)
        except Exception:
            print(f"Could not find or click option: {label}")

    # Close document type dropdown
    close_btns = driver.find_elements(By.XPATH, "//button[contains(@class, 'ecl-popover__close')]")
    for btn in close_btns:
        try:
            btn.click()
        except Exception:
            pass

    # Commissioner: click third select (by ID)
    comm_select = wait.until(EC.element_to_be_clickable((By.ID, "filter-commissioner-toggle")))
    driver.execute_script("arguments[0].click();", comm_select)
    time.sleep(1)

    # Select commissioner by code or name
    try:
        comm_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[contains(text(), '{commissioner_name}')]")
        ))
    except Exception:
        comm_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[contains(text(), '{commissioner_code}')]")
        ))
    driver.execute_script("arguments[0].click();", comm_option)
    time.sleep(0.5)

    # Click "Apply" button inside the commissioner dropdown only
    apply_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@id='filter-commissioner-dropdown']//button[contains(@class, 'ecl-button--primary') and contains(., 'Apply')]")
    ))
    driver.execute_script("arguments[0].click();", apply_btn)
    time.sleep(2)

    # Policy area selection (inserted after commissioner selection, before filter)
    if policy_area:
        # Click second select menu for policy area
        policy_select = wait.until(EC.element_to_be_clickable((By.ID, "filter-policy-toggle")))
        driver.execute_script("arguments[0].click();", policy_select)
        time.sleep(1)
        # Tick the checkbox for the policy area
        try:
            option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{policy_area}']")))
            driver.execute_script("arguments[0].click();", option)
            time.sleep(0.5)
        except Exception:
            print(f"Could not find or click policy area option: {policy_area}")
        # Click "Apply" button inside the policy area dropdown
        try:
            apply_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@id='filter-policy-dropdown']//button[contains(@class, 'ecl-button--primary') and contains(., 'Apply')]")
            ))
            driver.execute_script("arguments[0].click();", apply_btn)
            time.sleep(1)
        except Exception:
            print("Could not find or click Apply button for policy area.")

    # Click "Filter" to conduct the search
    filter_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(), 'Filter')]/ancestor::button")
    ))
    driver.execute_script("arguments[0].click();", filter_btn)
    time.sleep(2)

def get_result_links(driver):
    wait = WebDriverWait(driver, 20)
    # Wait for the search result heading to appear
    heading = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'ecl-heading--h2') and contains(text(), 'Search result')]")
        )
    )
    # Find all result links below the heading
    result_links = []
    # Find all h3 elements after the heading
    h3s = driver.find_elements(By.XPATH,
        "//div[contains(@class, 'ecl-heading--h2') and contains(text(), 'Search result')]/following::h3[contains(@class, 'ecl-list-item__title')]"
    )
    for h3 in h3s:
        parent = h3.find_element(By.XPATH, "./ancestor::a[1]")
        url = parent.get_attribute("href")
        if url:
            result_links.append(url)
    return result_links

def find_pdf_link(driver, detail_url):
    wait = WebDriverWait(driver, 7)  # Shorter timeout
    driver.get(detail_url)
    # Try to click "Print friendly pdf" if present
    try:
        print_btn = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(), 'Print friendly pdf')]")
        ))
        driver.execute_script("arguments[0].click();", print_btn)
        time.sleep(2)
    except Exception:
        pass
    # Try to find "Download" link
    try:
        download_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(), 'Download')]/ancestor::a")
        ))
        pdf_url = download_btn.get_attribute("href")
        return pdf_url
    except Exception:
        return None

def download_pdf(pdf_url, out_path):
    import requests
    r = requests.get(pdf_url, timeout=60)
    r.raise_for_status()
    with open(out_path, "wb") as f:
        f.write(r.content)

def run(commissioner_code, commissioner_name, headless, start_date=None, end_date=None, policy_area=None):
    # Commissioner directory
    commissioner_dir = f"{commissioner_name}_{commissioner_code}"
    os.makedirs(commissioner_dir, exist_ok=True)
    # Policy area subdirectory
    policy_area_str = policy_area.replace(" ", "_") if policy_area else "speech_statement"
    policy_area_dir = os.path.join(commissioner_dir, policy_area_str)
    os.makedirs(policy_area_dir, exist_ok=True)
    # Date range subdirectory
    date_range_str = f"{start_date}_to_{end_date}" if start_date and end_date else "all_dates"
    output_dir = os.path.join(policy_area_dir, date_range_str)
    os.makedirs(output_dir, exist_ok=True)
    print(f"[START] commissioner={commissioner_code} ({commissioner_name}), policy_area={policy_area}, date_range={date_range_str}")
    driver = setup_driver(headless)
    try:
        apply_filters(driver, commissioner_code, commissioner_name, start_date, end_date, policy_area)
        page = 1
        total_downloaded = 0
        results_url = driver.current_url
        while True:
            links = get_result_links(driver)
            print(f"Found {len(links)} detail links on page {page}")
            print(f"Links found on page {page}:")
            for l in links:
                print(l)
            for idx, detail_url in enumerate(links, 1):
                print(f"Opening: {detail_url}")
                # Use a separate driver for detail pages
                detail_driver = setup_driver(headless=True)
                pdf_url = find_pdf_link(detail_driver, detail_url)
                if pdf_url:
                    filename = f"{commissioner_code}_p{page}_{idx}.pdf"
                    out_path = os.path.join(output_dir, filename)
                    download_pdf(pdf_url, out_path)
                    print(f"Downloaded: {filename}")
                    total_downloaded += 1
                else:
                    print("No PDF link found")
                detail_driver.quit()
                time.sleep(1)
            # DO NOT reload results_url here!
            # Click "Next" for pagination (only once per page)
            try:
                next_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ecl-pager__link') and contains(text(), 'Next')]"))
                )
                print("Next button found, clicking...")
                driver.execute_script("arguments[0].click();", next_btn)
                page += 1
                WebDriverWait(driver, 30).until(EC.staleness_of(next_btn))
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".ecl-list-item__title"))
                )
                time.sleep(2)
                results_url = driver.current_url
            except Exception as e:
                print(f"No Next button found or not clickable on page {page}. Stopping. Exception: {e}")
                break
    finally:
        driver.quit()
    print(f"[DONE] Total PDFs downloaded: {total_downloaded}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--commissioner", required=True, help="Commissioner code (e.g. 2105)")
    parser.add_argument("--commissioner-name", required=True, help="Commissioner name (e.g. Henna Virkkunen)")
    parser.add_argument("--headed", action="store_true")
    parser.add_argument("--start-date", help="Start date in DD-MM-YYYY format")
    parser.add_argument("--end-date", help="End date in DD-MM-YYYY format")
    parser.add_argument("--policy-area", help="Policy area name (e.g. 'Animal Welfare')")
    args = parser.parse_args()
    run(args.commissioner, args.commissioner_name, headless=not args.headed, start_date=args.start_date, end_date=args.end_date, policy_area=args.policy_area)

if __name__ == "__main__":
    main()
