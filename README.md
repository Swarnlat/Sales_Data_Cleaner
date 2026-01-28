
#  Sales Data Cleaner & Currency Converter

## 1. Project Title & Goal
This project is a Python-based data cleaning pipeline that processes raw sales CSV data, removes duplicate records, standardizes price formats, converts prices from USD to INR, and exports the cleaned data into a structured JSON file.

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
- Used `csv.DictReader` to access CSV rows using column names, improving readability and reducing indexing errors.
- Implemented a `set()` to efficiently detect and remove duplicate product records.
- Cleaned and normalized price values before conversion to handle real-world messy data.
- Used a fixed USD to INR conversion rate (83) to ensure consistent and reproducible results.
- Exported the final output in JSON format for easy integration with APIs, databases, and frontend systems.

### What was the hardest bug I faced, and how did I fix it?
The hardest issue was handling price values that contained currency symbols, extra quotes, and whitespace, which caused float conversion errors.
I fixed this by sanitizing the price string before converting it to a float, ensuring consistent numeric formatting and preventing runtime errors.

---

## 4. Output Screenshots
![Clean Sales JSON Output](screenshots/clean_sales_output.png)

---

## 5. Future Improvements
If I had two more days, I would:
- Integrate real-time currency exchange rates using an external API.
- Add advanced error handling and logging for invalid CSV rows.
- Build a command-line interface to accept dynamic input and output paths.
- Write automated unit tests for validation and currency conversion.
- Support exporting cleaned data to Excel and database formats.

