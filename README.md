
#   The "Sales Data" Cleaner

## 1. Project Title & Goal
This project is a Python-based ETL pipeline that processes messy sales CSV data, removes duplicates, standardizes price formats, converts prices from USD to INR, and exports a clean JSON report.  
It demonstrates practical **data cleaning, transformation, and Python programming skills**, making it a real-world data engineering showcase.

---

## 2. Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Install dependencies
pip install -r requirements.txt

### Run the program
python clean_sales.py

### Output
After successful execution, the following file will be generated:
clean.json

---

## 3. The Logic (How I Thought)

### Why did I choose this approach?
- Used csv.DictReader to read CSV rows using column names for better readability and fewer indexing errors.
- Used a set() to efficiently detect and remove duplicate product records.
- Cleaned and normalized price values before conversion to handle messy real-world data.
- Applied a fixed USD → INR conversion rate (83) for consistent, reproducible results.
- Exported output in JSON format for easy integration with APIs, databases, and frontend systems.

### What was the hardest bug I faced, and how did I fix it?
The most challenging issue was handling inconsistent price formats — some had $ signs, extra quotes, or spaces — which caused float conversion errors.
Solution: Sanitized price strings by removing special characters and whitespace before converting to float. This ensured consistent numeric formatting and prevented runtime errors.

---

## 4. Output Screenshots
The screenshot below shows the final clean_sales.json file opened in a text editor, demonstrating that the data was cleaned, deduplicated, and converted correctly.
![Clean Sales JSON Output](screenshots/clean_sales_output.png)
---

## 5. Future Improvements
If I had two more days, I would:
- Integrate real-time currency exchange rates using an external API.
- Add advanced error handling and logging for invalid CSV rows.
- Build a command-line interface to accept dynamic input and output file paths.
- Write automated unit tests for data validation and currency conversion.
- Support exporting cleaned data to Excel and database formats.

