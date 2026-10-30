# SCAM MESSAGE INVESTIGATOR

## Project Overview

Scam Message Investigator is an AI-powered web application developed using Python and Streamlit. It helps users identify suspicious messages such as fake bank alerts, phishing messages, fraudulent job offers, and online scams.

The application uses the Gemma 3 1B model through Ollama to analyze messages and generate a detailed investigation report.

## Features

- Analyze suspicious SMS, emails, and online messages.
- Identify risk levels: Low, Medium, and High Concern.
- Detect possible warning signs in messages.
- Generate a short message summary.
- Provide recommended safety actions.
- Display AI analysis limitations.
- Download the investigation report in JSON format.
- Attractive and user-friendly interface.

## Technologies Used

- Python
- Streamlit
- Ollama
- Gemma 3 1B
- Requests
- JSON
- HTML and CSS

## Project Structure

```text
SCAM-MESSAGE-INVESTIGATOR/
│
├── scam_investigator.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### Step 1: Install Python

Install Python 3.10 or above on your computer.

### Step 2: Install Ollama

Download and install Ollama from:

https://ollama.com/

### Step 3: Download the AI Model

Open the terminal and execute:

```bash
ollama pull gemma3:1b
```

### Step 4: Install Required Libraries

Open the project folder in VS Code and execute:

```bash
python -m pip install -r requirements.txt
```

### Step 5: Run the Application

Execute the following command:

```bash
python -m streamlit run scam_investigator.py
```

The application will open in your web browser at:

```text
http://localhost:8501
```

## How to Use

1. Open the Scam Message Investigator application.
2. Paste a suspicious message into the input box.
3. Click the Investigate Message button.
4. Wait for the AI model to analyze the message.
5. View the risk assessment and message details.
6. Check the warning signs and recommended actions.
7. Download the analysis report in JSON format if required.

## Sample Input

```text
Your bank account will be blocked.
Enter your OTP immediately.
```

## Expected Output

The application generates an investigation report containing:

- Risk Assessment
- Message Type
- Summary
- Warning Signs
- Recommended Actions
- Limitations

The actual results depend on the AI model's analysis.

<img width="887" height="391" alt="image" src="https://github.com/user-attachments/assets/c4a4e6c3-8cc7-44fc-9d40-c739266dbb21" />

<img width="817" height="362" alt="image" src="https://github.com/user-attachments/assets/3a52fd03-7bd0-4adf-86b1-b4355e9dd5fa" />

<img width="850" height="352" alt="image" src="https://github.com/user-attachments/assets/d0dafbeb-093e-4498-9db1-ea1482a84ecf" />

<img width="850" height="386" alt="image" src="https://github.com/user-attachments/assets/a8152525-a863-443d-956a-3a9ecb884430" />

## Limitations

- AI-generated results may not always be accurate.
- An internet connection is not required for local Ollama inference, but initial model download requires internet access.
- Ollama must be running on the local computer.
- The application cannot guarantee that a message is safe or fraudulent.
- Users should independently verify suspicious messages through official channels.

## Future Enhancements

- Support for multiple languages.

Improved scam detection accuracy.

Message history and analysis records.

Additional AI models.

More detailed fraud detection reports.

Conclusion

Scam Message Investigator demonstrates how Artificial Intelligence can help identify suspicious messages and improve digital awareness. By combining Streamlit, Python, Ollama, and Gemma 3 1B, the application provides a simple interface for analyzing potentially fraudulent messages.

Developed using Python, Streamlit, Ollama, and Gemma 3 1B.
