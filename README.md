# Load Forecasting and Demand Analysis of Indian Power Grid

This project presents a data-driven analysis and forecast of electricity consumption patterns in India. The main objective is to understand national, state-wise, and sector-wise electricity usage trends and make short-term forecasts using Python and data science tools. The project was carried out by four team members as part of a data science internship.

## Team Members and Responsibilities

- Member 1 – National-Level Analysis  
  Analyzed total electricity consumption in India from 2013 to 2022 and used linear regression to forecast national power demand for 2023 to 2025. Created line plots and saved output charts.

- Member 2 – State-Wise Analysis  
  Collected and cleaned data for all Indian states from 2013 to 2022. Identified the top 5 electricity-consuming states and visualized their trends using bar plots and heatmaps. Forecasted electricity demand for Maharashtra using regression.

- Member 3 – Sector-Wise Analysis  
  Focused on electricity consumption by different sectors such as Residential, Industrial, and Agricultural. Created trendlines for each sector and forecasted future consumption for the Residential sector.

- Member 4 – Growth Rate Analysis  
  Calculated and visualized the year-on-year growth rates of electricity consumption for:
  - India (overall)
  - Top 5 states
  - Each sector

## Project Structure

load_forecasting_india/

data/

-->official_india_power_demand.csv


-->state_wise_consumption_2013_to_2022.csv


--->sector_wise_consumption_2013_to_2022.csv

main.py

requirements.txt

README.md

consumption_trend.png

forecast.png

## Technologies Used

- Python 3
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn (Linear Regression)
- Visual Studio Code
- Git and GitHub

## Output Visualizations

### National Electricity Consumption (2013–2022)
Saved as: `consumption_trend.png`

### Forecast for 2023–2025
Saved as: `forecast.png`

Other plots such as sector-wise and state-wise trends are generated during runtime when the script is executed.

## How to Run the Project

1. Clone the repository  
git clone https://github.com/Sarthakpatel05/load_forecasting_india.git
cd load_forecasting_india

2. Create and activate a virtual environment  
python3 -m venv .venv
source .venv/bin/activate # For Mac/Linux
.venv\Scripts\activate # For Windows

3. Install the required Python packages  
pip install -r requirements.txt

4. Run the script  
python main.py

## Key Insights

- Maharashtra has remained the highest electricity-consuming state.
- Residential electricity usage shows a rising trend and is expected to grow.
- National demand shows a consistent increase over the past decade.
- Growth rate trends offer insights into regional and sector-wise demand shifts.
