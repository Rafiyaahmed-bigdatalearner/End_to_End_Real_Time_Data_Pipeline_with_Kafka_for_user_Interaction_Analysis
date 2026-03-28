# dashboard.py
import streamlit as st
import json
import time

THRESHOLD = 100
REFRESH_INTERVAL = 5

st.set_page_config(page_title="Real-Time Interaction Dashboard", layout="wide")
st.title("Real-Time Interaction Dashboard")

placeholder = st.empty()

while True:
    try:
        with open("aggregated_data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"users": {}, "items": {}}

    users = data.get("users", {})
    items = data.get("items", {})

    top_users = dict(sorted(users.items(), key=lambda x: x[1], reverse=True)[:10])
    top_items = dict(sorted(items.items(), key=lambda x: x[1], reverse=True)[:10])
    alert_items = [item for item, count in items.items() if count > THRESHOLD]

    with placeholder.container():
        st.subheader("Top 10 Users by Event Count")
        st.bar_chart(top_users if top_users else {"No Data": 0})

        st.subheader("Top 10 Items by Interaction Count")
        st.bar_chart(top_items if top_items else {"No Data": 0})

        st.subheader(f"Items Exceeding Threshold ({THRESHOLD})")
        st.write(", ".join(alert_items) if alert_items else "No items exceeding threshold.")

    time.sleep(REFRESH_INTERVAL)