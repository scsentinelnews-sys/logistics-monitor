# 🚢 Personal Port Incident Monitor

## 🎯 Purpose & Scope

**A personal, non-commercial tool for monitoring port incident intelligence through publicly available news sources.**

### 🇦🇪 UAE Legal Compliance

**Personal Use Only**: This tool is designed exclusively for private, non-commercial research and personal information gathering. The developer does not provide news services to the public and does not distribute content to third parties.

**Educational Purpose**: This project serves as an educational demonstration of news API integration and automated monitoring systems for personal learning purposes only.

**Content Accuracy**: Summaries and alerts are generated automatically via news API feeds. The developer is not responsible for the accuracy of the extracted content or any AI-generated content. Users must verify all information via official sources before taking any action.

**Compliance Framework**: This project is intended to comply with:
- UAE Federal Decree-Law No. 34 of 2021 (Cybercrime Law)
- UAE Federal Decree-Law No. 38 of 2021 (Copyright)
- UAE Personal Data Protection Regulation (PDPR) principles
- Federal Law No. 3 of 1987 (Penal Code provisions on defamation)

### 🔒 Security & Privacy Protection

**No Credentials in Code**: All email credentials, API keys, and secrets are stored exclusively in GitHub Secrets. No hardcoded credentials exist in the codebase.

**Public News Sources Only**: This tool only extracts data from publicly available news sources provided by authorized news organizations. No scraping or unauthorized data extraction occurs.

**Data Minimization**: The system processes only minimal news content required for personal monitoring purposes. No personal data, emails, or credentials are stored in the code or repository.

**Secure Handling**: All sensitive information is handled through secure environment variables and GitHub Secrets encryption.

**No Social Media Sharing**: This tool is explicitly designed for personal use only and does not include any social media sharing or public distribution features.

## 📋 System Overview

### 🎯 Personal Monitoring Focus
- Personal port incident monitoring
- Non-commercial research and analysis
- Educational demonstration of news API processing
- Private intelligence gathering for personal decision-making

### 🔧 Technology Stack
- **News API Processing**: NewsAPI.org integration
- **Email Notifications**: Gmail SMTP (personal use only)
- **Automation**: GitHub Actions (30-minute intervals)
- **Filtering**: Precision targeting for port incident intelligence

### 📊 Data Sources
All data sources are publicly available news sources from authorized news organizations:
- NewsAPI.org aggregated sources (150,000+ authorized publications)
- Maritime and logistics industry news
- Regional news sources
- International business news

### 🎯 Monitoring Parameters
- **Materials Focus**: Polyethylene, Polypropylene, Polymers, Crude Oil, LNG, Chemicals
- **Infrastructure Focus**: Port operations, maritime incidents, supply chain disruptions
- **Geographic Focus**: GCC ports and maritime operations
- **Content Filtering**: Excludes consumer, retail, and automotive content

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10+
- GitHub account with repository access
- Gmail account with App Password
- NewsAPI.org account (free tier)

### Setup Instructions
1. Create NewsAPI.org account and obtain API key
2. Fork/clone this repository
3. Configure GitHub Secrets:
   - `NEWS_API_KEY`: Your NewsAPI.org key
   - `LOGISTICS_EMAIL_USER`: Your Gmail address
   - `LOGISTICS_EMAIL_PASSWORD`: Gmail App Password
   - `LOGISTICS_EMAIL_RECIPIENT`: Email recipient
4. Enable GitHub Actions
5. Manual trigger test via Actions tab

### ⚖️ Usage Restrictions

**Permitted Uses**:
- Personal monitoring and research
- Educational learning and demonstration
- Private decision-making support
- Non-commercial analysis

**Prohibited Uses**:
- Commercial news distribution
- Public content sharing
- Social media posting
- Third-party data provision
- Commercial resale of content
- Automated content redistribution

## 🛡️ Data Protection Measures

### Personal Data Protection
- No personal data collection or processing
- No user behavior tracking
- No personal information storage
- No third-party data sharing

### Content Handling
- Minimal data processing for personal use
- No long-term content storage
- No content redistribution
- No commercial exploitation

### Security Measures
- Encrypted credential storage
- Secure API communication
- No data logging
- Private deployment only

## ⚖️ Legal Disclaimer

**Educational & Personal Use Only**

This project is provided for educational and personal use only. The developer is not responsible for any misuse, commercial application, or illegal use of this tool.

**User Responsibility**: Users are responsible for ensuring compliance with applicable laws and regulations in their jurisdiction.

**Content Verification**: Users must independently verify all information through official sources before making any decisions based on automated alerts.

**No Warranty**: This software is provided "as is" without any warranty, express or implied.

## 📞 Support

For questions about educational use or technical issues, please create an issue in this repository.

---

**Last Updated**: $(date)
**Purpose**: Personal port incident monitoring (non-commercial, educational)
**Compliance**: UAE Cybercrime Law, Copyright Law, PDPR principles
**Usage**: Personal and educational use only
**Distribution**: Private use only - no public sharing
