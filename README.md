# Empirical Research on Governance Models in Open Source Software Communities

## Overview
This repository contains the datasets and analytical scripts used in a large-scale empirical study on governance models within open-source software communities. The research examines three prevalent governance models—Meritocracy, Consortium, and Company-hosted—across 1,000 Java open-source projects to evaluate their impact on project sustainability and contributor engagement.

## Key Findings
- **Governance Model Distribution**: The most common governance model is Meritocracy, found in 62% of the projects. Company-hosted models are present in 26% of the projects, while Consortium models are least common at 12%.
- **Impact on Sustainability**: The analysis reveals significant correlations between the governance model and the sustainability of projects. Projects governed by Meritocracy tend to exhibit better sustainability metrics.
- **Governance Model Recommendation System**: A system combining a random forest algorithm with the GPT-3.5 model was developed to recommend the most suitable governance model for new projects, achieving an accuracy rate of 80%.

## Methodology
The study utilized a data-driven approach employing statistical methods and machine learning techniques to analyze the data collected from GitHub.

### Data Collection
Data was collected using a custom Scrapy spider that extracted relevant details from GitHub repositories of Java projects, focusing on metrics such as activity levels and contributor numbers since 2005.
## Dataset
The dataset used in this project can be downloaded from https://docs.google.com/spreadsheets/d/1TxwrCXAatKgOr1I457TKgh-dVWIXWet0/edit?usp=sharing&ouid=118127860167148424482&rtpof=true&sd=true

### Statistical and Machine Learning Analysis
A comparative analysis of project characteristics under different governance models was conducted, using methodologies like logistic regression and random forest algorithms to assess their impacts.

## Installation and Usage
To set up and run the analysis contained in this repository, follow these steps:
```bash
git clone https://github.com/yourusername/yourprojectname.git
cd yourprojectname
pip install -r requirements.txt
python analyze.py

