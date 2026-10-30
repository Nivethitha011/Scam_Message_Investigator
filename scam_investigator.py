import streamlit as st
import requests
import json

# Configuration
MODEL = "gemma3:1b"
URL = "http://localhost:11434/api/generate"

st.set_page_config(
    page_title="Scam Message Investigator",
    page_icon="🔍",
    layout="wide"
)

# Design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e0e7ff, #f5f3ff, #dbeafe);
    color: #172554;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

h1 {
    color: #312e81 !important;
    text-align: center;
    font-size: 38px !important;
    font-weight: bold;
}

h2, h3 {
    color: #3730a3 !important;
}

p, label, .stMarkdown {
    color: #1e293b;
}

.stTextArea textarea {
    background-color: white !important;
    color: #172554 !important;
    border: 2px solid #6366f1 !important;
    border-radius: 12px !important;
    font-size: 17px !important;
}

.stTextArea label {
    color: #312e81 !important;
    font-weight: bold;
}

.stButton > button {
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 12px 25px;
    font-size: 17px;
    font-weight: bold;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #3730a3, #6d28d9);
    border: 1px solid white;
}

.stExpander {
    background: white;
    border: 1px solid #a5b4fc;
    border-radius: 10px;
}

.stAlert {
    border-radius: 12px;
}

.footer {
    text-align: center;
    color: #475569;
    padding: 15px;
}
</style>
""", unsafe_allow_html=True)


# Header
st.title("SCAM MESSAGE INVESTIGATOR")

st.markdown("""
<p style="text-align:center; color:#475569; font-size:18px;">
Transform suspicious messages into clear AI-powered reports
</p>
""", unsafe_allow_html=True)

st.divider()


# Message Input
st.subheader("Enter Your Message")

message = st.text_area(
    "Paste your suspicious message here:",
    height=170,
    placeholder="Example: Your bank account will be blocked. Enter your OTP immediately."
)

st.caption("Never enter real passwords, PINs or OTPs.")


# AI Analysis
if st.button("🔎 INVESTIGATE MESSAGE"):

    if not message.strip():
        st.warning("Please enter a message first.")

    else:
        prompt = f"""
You are a scam message investigation assistant.

Analyze the message and return ONLY valid JSON.

Use this structure:

{{
 "risk_level": "Low, Medium, or High Concern",
 "message_type": "Type of message",
 "summary": "Short explanation",
 "warning_signs": [
   {{
     "evidence": "Suspicious words",
     "reason": "Why they are suspicious"
   }}
 ],
 "recommended_actions": [
   "Action 1",
   "Action 2"
 ],
 "limitations": "AI analysis may not always be accurate."
}}

Rules:
- warning_signs must be a list of objects.
- recommended_actions must be a list of strings.
- Do not invent facts.
- Return JSON only.

Message:
{message}
"""

        with st.spinner("Gemma AI is investigating your message..."):

            try:
                response = requests.post(
                    URL,
                    json={
                        "model": MODEL,
                        "prompt": prompt,
                        "format": "json",
                        "stream": False,
                        "options": {"temperature": 0.2}
                    },
                    timeout=300
                )

                response.raise_for_status()

                data = response.json()
                result = json.loads(data["response"])

                if not isinstance(result, dict):
                    st.error("Invalid report received from AI.")
                    st.stop()

                st.success("Message analysis completed successfully!")

                # Risk Assessment
                st.subheader("Risk Assessment")

                risk = str(result.get("risk_level", "Unknown")).strip()

                if risk.lower() == "high concern":
                    st.error("🚨 HIGH CONCERN")
                elif risk.lower() == "medium":
                    st.warning("⚠️ MEDIUM RISK")
                elif risk.lower() == "low":
                    st.success("✅ LOW RISK")
                else:
                    st.info(risk)

                # Message Details
                st.subheader("Message Details")

                with st.container(border=True):
                    st.markdown("### Message Type")
                    st.write(result.get("message_type", "Not available"))

                with st.container(border=True):
                    st.markdown("### Summary")
                    st.write(result.get("summary", "Not available"))

                # Warning Signs
                st.subheader("Warning Signs")

                warnings = result.get("warning_signs", [])

                if isinstance(warnings, str):
                    warnings = [warnings]

                if not isinstance(warnings, list):
                    warnings = []

                if warnings:
                    for item in warnings:

                        if isinstance(item, dict):
                            evidence = item.get("evidence", "Warning sign")
                            reason = item.get("reason", "Possible warning sign identified.")
                        else:
                            evidence = str(item)
                            reason = "Identified as a possible warning sign."

                        with st.expander(str(evidence)):
                            st.write(str(reason))
                else:
                    st.write("No warning signs identified.")

                # Recommended Actions
                st.subheader("Recommended Actions")

                actions = result.get("recommended_actions", [])

                if isinstance(actions, str):
                    actions = [actions]

                if isinstance(actions, list):
                    for action in actions:
                        st.write("✓", str(action))

                # Limitations
                st.subheader("Limitations")

                st.info(result.get(
                    "limitations",
                    "AI analysis cannot guarantee complete accuracy."
                ))

                # Download Report
                report = json.dumps(
                    result,
                    indent=4,
                    ensure_ascii=False
                )

                st.download_button(
                    "📥 Download Analysis Report",
                    data=report,
                    file_name="scam_analysis.json",
                    mime="application/json"
                )

            except requests.exceptions.ConnectionError:
                st.error("Ollama is not running. Please open Ollama.")

            except requests.exceptions.Timeout:
                st.error("AI response timed out. Please try again.")

            except requests.exceptions.HTTPError:
                st.error("Ollama server error:")
                st.code(response.text)

            except (json.JSONDecodeError, KeyError):
                st.error("Invalid response received from AI. Please try again.")

            except Exception as e:
                st.error("Unexpected error:")
                st.code(str(e))


# Footer
st.divider()

st.markdown("""
<div class="footer">
SCAM MESSAGE INVESTIGATOR<br>
Powered by Ollama + Gemma 3 1B
</div>
""", unsafe_allow_html=True)
