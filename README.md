# 🚀 DCA Calculator by LVKSH ©

A simple **Dollar Cost Averaging** calculator built with **Python** and **Streamlit**.

This project simulates monthly investing with **compound interest** and shows how consistent contributions grow over time. You can choose whether investments are made at the beginning or at the end of each month, and see the **total portfolio value**, **invested capital**, **profit** and **ROI**.

The calculation is based on a standard **compound interest model**:

**monthly_rate = (1 + APY)^(1/12) - 1**

🌍 **Live app**:
https://dca-calculator-by-lvksh.streamlit.app/

To run locally:
git clone https://github.com/volodymyrlevkusha/dca-calculator.git
cd dca-calculator
pip install -r requirements.txt
streamlit run src/dca_calculator/app.py

/// Improvements in progress.

⚠️ *This simulation does not take into account inflation, taxes, fees or market volatility. It is intended for educational and illustrative purposes only.*

Built by 
Volodymyr Levkusha 
/ LVKSH ©
