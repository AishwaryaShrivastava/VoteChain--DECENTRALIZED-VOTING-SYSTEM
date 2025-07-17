import streamlit as st
from auth import register_user, authenticate_user  # ✅ fixed import
from contract_interaction import (
    start_election, end_election, add_candidate, register_voter,
    vote, get_candidate, get_total_candidates
)
from utils import log_action, format_time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

admin_address = os.getenv("ADMIN_ADDRESS")
admin_private_key = os.getenv("ADMIN_PRIVATE_KEY")

st.set_page_config(page_title="VoteChain", layout="wide")

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False
if "role" not in st.session_state:
    st.session_state.role = None
if "username" not in st.session_state:
    st.session_state.username = ""

def show_login():
    st.title("🔐 Login to Voting System")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        success, user = authenticate_user(username, password)  # ✅ updated function call
        if success:
            st.session_state.is_logged_in = True
            st.session_state.role = user["role"]
            st.session_state.username = username
            st.session_state.wallet = user["wallet"]
            st.session_state.private_key = user["private_key"]
            log_action("Login", username, f"{username} logged in as {user['role']}")
            st.success("Login successful!")
        else:
            st.error(user)

def show_register():
    st.title("📝 Register")
    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")
    role = st.selectbox("Register As", ["admin", "voter"])
    wallet = st.text_input("Wallet Address")
    private_key = st.text_input("Private Key", type="password")
    if st.button("Register"):
        success, msg = register_user(username, password, role, wallet, private_key)
        if success:
            st.success(msg)
        else:
            st.error(msg)

def admin_dashboard():
    st.title("👨‍💼 Admin Dashboard")
    election_name = st.text_input("Election Name")
    if st.button("Start Election"):
        start_election(election_name)
        log_action("Election Started", st.session_state.username, election_name)
        st.success("Election started!")

    st.subheader("📅 Add Candidate")
    cname = st.text_input("Candidate Name")
    if st.button("Add Candidate"):
        add_candidate(cname)
        log_action("Candidate Added", st.session_state.username, cname)
        st.success(f"Candidate '{cname}' added!")

    st.subheader("🧲 Register Voter")
    voter_addr = st.text_input("Voter Wallet Address")
    if st.button("Register Voter"):
        register_voter(voter_addr)
        log_action("Voter Registered", st.session_state.username, voter_addr)
        st.success(f"Voter {voter_addr} registered.")

    if st.button("End Election"):
        end_election()
        log_action("Election Ended", st.session_state.username, "Election closed.")
        st.success("Election ended.")

def voter_dashboard():
    st.title("🗳️ Voter Dashboard")

    total = get_total_candidates()
    candidates = []
    for i in range(1, total + 1):
        name, votes = get_candidate(i)
        candidates.append((i, name))

    selected = st.radio("Choose a candidate to vote for:", [f"{cid}: {name}" for cid, name in candidates])
    selected_id = int(selected.split(":")[0])

    if st.button("Cast Vote"):
        receipt = vote(
            selected_id,
            st.session_state.wallet,
            st.session_state.private_key
        )
        log_action("Vote Cast", st.session_state.username, f"Voted for {selected}")
        st.success("✅ Vote submitted successfully!")

    st.subheader("📊 Live Results")
    for cid, name in candidates:
        _, count = get_candidate(cid)
        st.write(f"{name}: {count} votes")

def main():
    if st.session_state.is_logged_in:
        st.sidebar.success(f"Welcome, {st.session_state.username} ({st.session_state.role})")

        # ✅ Optional: Add Logout Button
        if st.sidebar.button("Logout"):
            st.session_state.is_logged_in = False
            st.session_state.username = ""
            st.session_state.role = None
            st.experimental_rerun()

        # Show dashboards
        if st.session_state.role == "admin":
            admin_dashboard()
        elif st.session_state.role == "voter":
            voter_dashboard()
    else:
        menu = ["Login", "Register"]
        choice = st.sidebar.selectbox("Navigation", menu)

        if choice == "Login":
            show_login()
        elif choice == "Register":
            show_register()


if __name__ == "__main__":
    main()
