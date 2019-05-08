# Selenium Scraper - 360blue
<a href="https://codeclimate.com/github/Firiyuu/selenium-360blue/maintainability"><img src="https://api.codeclimate.com/v1/badges/cdacc7260bb66dc379b0/maintainability" /></a>
Order made script - Selenium + bs4 scraper for 460 blue.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install app script dependencies, it is recommended to use a new virtualenv on running it.

```bash
pip install -r requirements.txt
```

## Download [Spreadsheet](https://docs.google.com/spreadsheets/d/1xhb472B93C35tVMKwZG3nHYETT3QMWqVE5CfP9tPCW8/edit?usp=sharing)

## How it works
It saves scraped and needed parameters on dataframes and saves them on csv for alter use. After every csv's are taken from the website ```combine()``` function takes all inputs from these functions and combines them to one dataframe and saves them to CSV.

## Usage
In fast servers, run main script, for slower connections you can comment/uncomment functions to make progress with every scrape. 

