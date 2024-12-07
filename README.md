# Empirical Research on Governance Models in Open Source Software Communities

## Overview
This repository contains the research conducted for a master's thesis at Beijing Institute of Technology, which focuses on analyzing the governance models within open-source software communities. The study specifically examines three prevalent governance models—Meritocracy, Consortium, and Company-hosted—across 1,000 Java open-source projects to understand their impact on project sustainability and contributor engagement.

## Key Findings
- **Governance Model Distribution**: Meritocracy governance is most common at 62%, followed by Company-hosted at 26%, and Consortium at 12%.
- **Impact on Sustainability**: Our analysis reveals significant correlations between the governance model and the sustainability of projects. Projects governed by Meritocracy tend to exhibit better sustainability metrics.
- **Governance Model Recommendation System**: A system combining a random forest algorithm with the GPT-3.5 model was developed to recommend the most suitable governance model for new projects, achieving an accuracy rate of 80%.

## Methodology
The study leveraged a data-driven approach using statistical methods and machine learning techniques to analyze the data collected from GitHub.

### Data Collection
The data was collected using a custom Scrapy spider that extracted relevant details from GitHub repositories of Java projects based on activity levels, number of contributors, and other significant metrics since 2005.

### Statistical and Machine Learning Analysis
We conducted a comparative analysis of project characteristics under different governance models, utilizing methodologies like logistic regression and random forest algorithms to assess their impacts.

## Installation and Usage
To replicate the study or utilize the framework developed, follow these instructions:
```bash
git clone https://github.com/yourusername/yourprojectname.git
cd yourprojectname
pip install -r requirements.txt
python analyze.py
