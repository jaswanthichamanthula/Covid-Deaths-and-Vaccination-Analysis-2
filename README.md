# Covid Deaths and Vaccination Analysis

This project analyzes the relationship between **Covid-19 deaths** and **vaccination rates** across different countries using **MySQL, Python, and Excel**.

##  Features
- MySQL database for storing deaths and vaccination data
- SQL queries for analysis
- Python script for visualization
- Data exploration with Pandas & Matplotlib

##  Project Structure
- `covid_analysis.sql` → MySQL schema & queries
- `covid_analysis.py` → Python analysis script
- `data/covid_data.csv` → Dataset
- `requirements.txt` → Required Python libraries

##  Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/username/covid-analysis.git
   cd covid-analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Import SQL file into MySQL:
   ```sql
   SOURCE covid_analysis.sql;
   ```
4. Run the Python script:
   ```bash
   python covid_analysis.py
   ```

## Sample Analysis
- Total deaths per country
- Vaccination rate vs. death rate
- Trends over time
