# ABHI – Artificial Brain for Harm Identification

🛡️ A Browser based extension built to detect phishing & fraud sites using Machine Learning.  
💬 Integrated with AI – Real time response from GPT. 
👨‍💻 Developed by Abhijeet Khanzode

# 🛡️ ABHI-SHIELD – Artificial Brain for Harm Identification

`ABHI-SHIELD` is a real-time AI-powered Browser application that detects **phishing websites**, alerts users with notifications, and enables **interactive conversation** with an intelligent chatbot – ABHI AI. It's backed by a trained machine learning model and designed for **cybersecurity awareness**.

---

## 🔥 Features

- ✅ Real-time phishing URL detection
- 🔔 Continuous alerts while tab is open
- 🤖 ABHI AI Chat Assistant for user education
- 🧠 Auto-learning via user feedback (false positive handling)
- 💬 Clean and modern chat UI
- 🟢 Toggle: Turn protection ON/OFF anytime
- 🔗 Social links & extension support built-in

---



## 🚀 How It Works

1. **Phishing Detection**  
   Extension monitors active tab URLs every 3 seconds and sends them to a Flask server hosting the trained ML model.

2. **Model Prediction**  
   If phishing is detected with confidence > 70%, it triggers a visual alert with a button to mark as "Not Phishing".

3. **User Feedback Loop**  
   Feedback is stored in `false_positive.csv` and used to **auto-retrain the model** via `auto_update_model.py`.

4. **ABHI AI Chat**  
   Clicking the alert opens a chat window powered by OpenAI API where users can interact with an assistant trained for cybersecurity.

---

## 🧠 Technologies Used

- 🐍 Python (Flask)
- 🎯 Machine Learning
- 🤖 OpenAI (ChatGPT API)
- 🌐 HTML / CSS / JS (Chrome Extension)
- 📦 Scikit-learn, Pandas, Joblib

---

## 🛠️ Setup Instructions

### ⚙️ 1. Clone this repository

```bash
git clone https://github.com/Abhijeet-Khanzode/ABHI-SHIELD.git
cd ABHI-SHIELD
Install Python dependencies

Run the Flask server
bash
Copy
Edit
python app.py
Make sure phishing_model.pkl and feature_extraction.py are present.

🧪 4. Load Extension in Chrome
Open chrome://extensions

Enable "Developer Mode"

Click "Load Unpacked"

Select the /extension folder

🧪 Test Data
Try these URLs to test:

✅ Safe: https://www.google.com/, https://github.com/, https://linkedin.com/

⚠️ Phishing: https://login-microsoft-secure.com/, https://mysecureportal.fake-domain.com/

https://lastminute-dealzclose.shop/livesale/ProductManager/202?fbclid=PAQ0xDSwKMVyVleHRuA2FlbQEwAGFkaWQBqxxWsmSR1QGnduLWPYem31BlFPwTZ8z8oVoKyXg_b1xjpCxOKNJ96Ka3Wq8Wf-Y6FenpylA_aem_fLYEAkM3VNO6NI4ECPYCGA

👨‍💻 Developer Info
👤 Abhijeet Khanzode
👤 Parth Dhande
👤 Ayush Bangare
B.Tech Computer Science (Cybersecurity)
📍 Nagpur, Maharashtra
🎓 G.H. Raisoni College Of Engineering And Management, Nagpur.
📆 Graduating: 2026


🌐 My Links
🔗 GitHub - https://github.com/Abhijeet-Khanzode

💼 LinkedIn - https://www.linkedin.com/in/abhijeet-khanzode-232925370

🌍 Portfolio - https://protofolio-devabhi.netlify.app/

📸 Instagram - https://www.instagram.com/abhijeet_khanzode

🙌 Support
If you found this extension helpful:

⭐ Rate the extension

🛠️ Contributions welcome!

📄 License
This project is licensed under the MIT License.

💡 ABHI-SHIELD is not just an extension; it's a mission to make the web a safer place using AI.
