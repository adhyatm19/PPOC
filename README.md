# PolitiPulse: Public Policy Sentiment Analysis

## Overview

**PolitiPulse** is an NLP-based analytics platform developed under the **Public Policy and Opinion Cell (PPOC), IIT Kanpur** to analyze public sentiment toward newly implemented government policies. The project leverages Natural Language Processing (NLP), sentiment analysis, and interactive visualization to quantify policy reception and generate actionable insights for policymakers.

As a **Project Mentor**, I guided the project development, mentored team members on NLP methodologies, system architecture, and analytics workflow, while ensuring the successful implementation of an end-to-end policy sentiment analysis framework.

## Objectives

* Analyze large-scale public opinion on government policies.
* Quantify policy reception using sentiment analysis techniques.
* Provide real-time visualization of public sentiment.
* Generate data-driven recommendations for evidence-based policymaking.

## Key Features

* **NLP-based sentiment analysis** for large-scale public opinion mining.
* **Rule-based sentiment scoring** using the **VADER** framework.
* **Interactive Streamlit Dashboard** for real-time visualization.
* **Policy Approval Index** to measure public reception.
* **Automated data pipeline** for collecting, preprocessing, and analyzing public opinion data.
* **Clause-level sentiment mapping** to identify strengths and weaknesses of individual policy provisions.
* **Recommendation engine** that generates structured reports based on sentiment trends.

## System Architecture

1. Data Collection
   - Collects public opinion from multiple digital platforms.

2. Data Preprocessing
   - Text cleaning
   - Tokenization
   - Stop-word removal
   - Text normalization

3. Sentiment Analysis
   - VADER-based sentiment scoring
   - Classification into Positive, Neutral, and Negative sentiments

4. Policy Analytics
   - Clause-level sentiment mapping
   - Policy Approval Index computation
   - Trend analysis

5. Visualization
   - Interactive Streamlit dashboard
   - Real-time analytics
   - Comparative policy insights

## Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Streamlit
- NLTK
- VADER Sentiment Analyzer

## Mentor Responsibilities

* Mentored project members on **Natural Language Processing** and **Sentiment Analysis** techniques.
* Guided the design of the overall **NLP architecture** and analytics workflow.
* Assisted in developing the **automated data pipeline** for scalable sentiment analysis.
* Supervised the implementation of the **Policy Approval Index** and recommendation framework.
* Reviewed technical progress and provided guidance on dashboard development and data visualization.

## Repository Structure

```
PolitiPulse/
│
├── data/
│   ├── raw_data/
│   └── processed_data/
│
├── notebooks/
│
├── src/
│   ├── preprocessing.py
│   ├── sentiment_analysis.py
│   ├── policy_mapping.py
│   ├── dashboard.py
│   └── recommendation_engine.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Future Improvements

* Fine-tuning Transformer-based models (BERT/RoBERTa)
* Multilingual sentiment analysis
* Real-time social media integration
* Topic modeling for policy discussions
* Interactive comparative policy analytics
* Deployment on cloud platforms

## Outcomes

* Successfully developed a scalable NLP framework for public policy sentiment analysis.
* Enabled real-time monitoring of public opinion through an interactive dashboard.
* Generated structured, data-driven policy recommendation reports.
* Demonstrated the effectiveness of NLP in supporting evidence-based public policy decisions.

## Acknowledgements

This project was developed under the **Public Policy and Opinion Cell (PPOC), IIT Kanpur**.

Special thanks to all project contributors for their dedication and collaborative efforts.
