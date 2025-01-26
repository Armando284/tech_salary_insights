# Tech Salary Insights 🚀

**Tech Salary Insights** is a project showcasing advanced skills in data engineering, CI/CD, and system design. The primary goal is to process, clean, and analyze data related to salaries in the tech industry, providing key insights through visualizations. The project also emphasizes strong modularization practices and design patterns.

## 📋 Table of Contents
- [Description](#-description)
- [Features](#-features)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [Next Steps](#-next-steps)
- [Contributing](#-contributing)

## 🖥️ Description
This project processes a dataset about tech industry salaries to:
- Clean and enrich data through a custom pipeline.
- Store the cleaned data in **Google BigQuery**.
- Visualize trends and insights using interactive graphs.

The focus is on applying data engineering principles and best practices while demonstrating a complete CI/CD pipeline with **GitHub Actions**.

## ✨ Features
- **Data Cleaning:** Algorithms to transform and enrich data, handling inconsistencies and missing values.
- **Visualizations:** Interactive graphs to explore salary trends.
- **BigQuery:** Structured storage and efficient querying.
- **CI/CD:** Automated development and deployment pipeline using **GitHub Actions**.
- **Best Practices:** Modularized code, design patterns, and comprehensive documentation.

## 💻 System Requirements
- **Python** 3.7+
- Up-to-date **pip**
- Google Cloud account with **BigQuery** permissions
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) configured (optional)
- Text editor/IDE (recommended: VS Code)

## 🚀 Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/tech-salary-insights.git
    cd tech-salary-insights
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Google Cloud credentials**:
   - Download your JSON credentials file from Google Cloud.
   - Export the environment variable (on Linux/MacOS):
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
     ```
     On Windows:
     ```cmd
     set GOOGLE_APPLICATION_CREDENTIALS=path\to\credentials.json
     ```

## 🛠️ Usage
1. **Run the data cleaning script**:
    ```bash
    python src/data_cleaning.py
    ```

2. **Upload the cleaned data to BigQuery**:
    ```bash
    python src/upload_to_bigquery.py
    ```

3. **Generate visualizations**:
    ```bash
    python src/generate_visualizations.py
    ```

4. **Automate with CI/CD**:
    - Ensure you have a `.github/workflows` file configured.
    - Pipelines will run automatically on every commit/push.

## 🌟 Next Steps
- Implement additional validations during data cleaning.
- Enhance visualizations with interactive dashboards.
- Integrate storage with **Google Cloud Storage** for backups.
- Document technical decisions and design patterns used.

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request to suggest improvements.

---

Thank you for visiting this repository!
