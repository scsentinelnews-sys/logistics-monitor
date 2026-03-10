# AI Logistics Monitor

## 🚢 Personal Logistics Intelligence Monitor

**A personal, non-commercial tool for monitoring global logistics intelligence through publicly available RSS feeds.**

## ⚠️ Legal Disclaimer & Compliance

### 🇦🇪 UAE Legal Compliance

**Personal Use Only**: This tool is designed for private, non-commercial research and personal information gathering. The developer does not provide news services to the public.

**Content Accuracy**: Summaries are generated automatically via AI/RSS feeds. The developer is not responsible for the accuracy of the extracted content or any "hallucinations" caused by the AI model. Users should verify all information via official sources (e.g., WAM, The National) before taking any action.

**Compliance**: This project is intended to comply with the UAE Federal Decree-Law No. 34 of 2021 (Cybercrime Law) and Decree-Law No. 38 of 2021 (Copyright). It does not store or redistribute copyrighted full-text articles.

### 🔒 Security & Privacy

**No Credentials in Code**: All email credentials, API keys, and secrets are stored exclusively in GitHub Secrets. No hardcoded credentials exist in the codebase.

**Public RSS Sources Only**: This tool only extracts data from publicly available RSS feeds provided by authorized news organizations. No scraping or unauthorized data extraction occurs.

**Data Storage**: No personal data, emails, or credentials are stored in the code or repository. All sensitive information is handled through secure environment variables.

## 📋 System Overview

### 🎯 Purpose
- Personal logistics intelligence monitoring
- Non-commercial research and analysis
- Educational demonstration of RSS feed processing

### 🔧 Technology Stack
- **RSS Feed Processing**: feedparser library
- **Email Notifications**: Gmail SMTP (personal use only)
- **Automation**: GitHub Actions (30-minute intervals)
- **Filtering**: Precision targeting for logistics intelligence

### 📊 Data Sources
All data sources are publicly available RSS feeds from authorized news organizations:
- Financial Times, BBC Business, Guardian Business
- Bloomberg, CNBC, Yahoo Finance, MarketWatch
- JOC, Hellenic Shipping, ICIS, Splash247
- Reuters Commodities

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11+
- GitHub account with repository access
- Gmail account with App Password

### Setup Instructions
1. Fork/clone this repository
2. Configure GitHub Secrets:
   - `LOGISTICS_EMAIL_USER`: Your Gmail address
   - `LOGISTICS_EMAIL_PASSWORD`: Gmail App Password
3. Enable GitHub Actions
4. Manual trigger test via Actions tab

## ⚖️ License

**Educational & Personal Use Only**

This project is provided for educational and personal use only. The developer is not responsible for any misuse or commercial application of this tool.

## 📞 Support

For questions about educational use or technical issues, please create an issue in this repository.

---
**Last Updated**: $(date)
**Purpose**: Personal logistics intelligence monitoring (non-commercial)
**Compliance**: UAE Cybercrime Law & Copyright Law
# Schedule activation update - Tue Mar 10 15:46:29 UTC 2026
# Schedule activation update - Tue Mar 10 15:47:07 UTC 2026
