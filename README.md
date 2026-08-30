# Marketing Campaign Data Cleaning

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-2.0+-green.svg)](https://pandas.pydata.org/)

A data cleaning project for marketing campaign data that standardizes mixed date formats, fixes data inconsistencies, and prepares the data for analysis.

## 📋 Overview

This repository contains a Python script to clean messy marketing campaign data. The primary challenge addressed is standardizing date formats across the dataset, specifically converting mixed formats like `"2023-04-22 00:00:00"` and `"2023-10-30"` to a consistent `YYYY-MM-DD` format.

## 📁 Files

| File | Description |
|------|-------------|
| `marketing_campaign_data_messy.csv` | Raw, uncleaned data with mixed date formats |
| `cleaning.py` | Python script that processes and cleans the data |
| `cleaned_marketing_campaign_data.csv` | Output file with standardized dates and cleaned data |

## 🔧 Features

- **Date Standardization**: Converts mixed date formats (with/without timestamps) to consistent `YYYY-MM-DD` format
- **Error Handling**: Handles invalid dates gracefully with `errors='coerce'`
- **Logical Fixes**: Corrects "time travel" instances where end dates precede start dates
- **Data Quality**: Prepares data for downstream analysis and reporting

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pandas library

### Installation

```bash
# Clone the repository
git clone https://github.com/muteufit/marketing_campaign_cleaning.git
cd marketing_campaign_cleaning

# Install required packages
pip install pandas
