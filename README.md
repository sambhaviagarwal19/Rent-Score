# RentScore: ML-Based Risk Assessment for Car Rentals

A Random Forest-powered machine learning solution for customer risk evaluation in the car rental industry, offering enhanced decision-making, risk mitigation, and operational efficiency.

---

## 🚗 Project Overview

*RentScore* is a predictive system that leverages machine learning to analyze customer data (e.g., driving history, fines, license status, accident records) and generate a risk score. This enables car rental providers to make informed, data-driven decisions before approving rentals, helping to reduce defaults, losses, and fraud.

---

## 🎯 Features

- Random Forest-based risk scoring model
- Frontend UI for entering customer details
- Flask backend for processing and serving predictions
- Google Colab for training the ML model
- MySQL (via Excel-based schema) for database storage
- Risk classification visualization similar to credit scoring systems

---

## ⚙ Technologies Used

- Python, Flask, HTML, CSS
- Scikit-learn (Random Forest)
- Google Colab (training environment)
- Pandas, NumPy (data handling)
- Excel & MySQL for database
- Matplotlib, Seaborn (visualizations)

---

## 🔄 System Workflow

1. *Data Ingestion*: User inputs customer info through a web form.
2. *Data Processing*: Backend preprocesses inputs for ML model.
3. *Prediction Engine*: Random Forest model predicts customer risk class.
4. *Response Output*: Risk score is returned and displayed on the UI.
5. *Storage*: Data is stored for future review and analysis.

---

## 📈 Performance Metrics

| Component     | Avg Response Time |
|---------------|-------------------|
| Frontend UI   | <1 second         |
| Backend API   | 100–500 ms        |
| ML Model (Colab) | 2–5 seconds    |
| Database      | 10–500 ms         |

---

## 🖥 Display Output

| Input (Example)                      | Output                   |
|-------------------------------------|--------------------------|
| Driving History: 2 fines, no accidents | *Low Risk*            |
| License Status: Valid               |                          |
| Age: 28                             |                          |

---

<table>
  <tr>
    <td><img src="Rent Score output/backend_time_response.jpeg" alt="UI" width="400"/></td>
    <td><img src="Rent Score output/Database_response.jpeg" alt="Risk Score Bar" width="400"/></td>
  </tr>
  <tr>
    <td><img src="Rent Score output/heatmap.jpeg" alt="API Response" width="400"/></td>
  </tr>
</table>

---

## 🚀 Future Enhancements

- Real-time risk assessment using IoT data from rental vehicles
- Integration with government APIs for license validation
- Blockchain-backed transaction logs for fraud prevention
- AI-driven personalized recommendations for renters
- Expansion to bike/scooter rentals and international markets

---

## 📌 Limitations

- Dependent on quality and completeness of user data
- Initial model trained on synthetic and limited data
- Scalability challenges with Excel as backend DB
- Requires user training for adoption in traditional rental setups

---

## 📚 References

- Google Co-lab
- Scikit-learn Documentation
- Medium & Reddit (for practical insights)
- Figma (for frontend UI prototyping)
- Harvard Business Review & ScienceDirect (for industry context)
