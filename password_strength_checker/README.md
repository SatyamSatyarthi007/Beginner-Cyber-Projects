# 🔐 Password Strength Checker – Flask Web App

> A modern web application built with **Flask** that evaluates password strength using visual indicators, percentage scores, and time-to-crack estimation.

---

## 📌 Overview

The **Password Strength Checker** helps users understand how secure their passwords are by analyzing:

- Length
- Character variety
- Complexity patterns
- Entropy
- Common weaknesses

It provides **real-time visual feedback** and an **estimated brute-force cracking time** — making it perfect for cybersecurity education and awareness.

---

## ✨ Features

### 🔎 Password Strength Analysis

Comprehensive evaluation based on:

- 📏 Password length  
- 🔠 Uppercase letters  
- 🔡 Lowercase letters  
- 🔢 Numbers  
- 🔣 Special characters  
- 🧠 Entropy calculation  
- 🚫 Common pattern detection  
- 🔄 Sequential character detection  

---

### 🎨 Visual Feedback

- 📊 Strength percentage (0–100%)  
- 🎨 Color-coded indicators:
  - Red → Orange → Green  
- 📈 Animated progress bar  
- 🏷️ Strength label:
  - Very Weak → Very Strong  

---

### ⏳ Time-to-Crack Estimation

Estimates how long a brute-force attack would take to crack the password based on:

- 1 billion guesses per second (modern GPU capability)
- Brute-force methodology
- Average-case scenario (50% of combinations)

---

### ✅ Criteria Checklist

Displays which security requirements are met:

- ✔ Lowercase letters  
- ✔ Uppercase letters  
- ✔ Numbers  
- ✔ Special characters  

---

## 📦 Requirements

- Python **3.6+**
- Flask

---

## ⚙️ Installation

Install Flask:

```bash
pip install flask
