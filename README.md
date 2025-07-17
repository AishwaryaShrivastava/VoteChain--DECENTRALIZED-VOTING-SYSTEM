# 🗳️ VoteChain – A Decentralized Voting DApp

VoteChain is a secure, transparent, and blockchain-powered voting system built with **Solidity**, **Streamlit**, **Web3.py**, **MetaMask**, and optionally using **Ganache for local development**. It empowers **Admins** to create and manage elections while **Voters** securely cast their votes on-chain.

---

## 🚀 Features

- 🔐 Secure Admin & Voter Authentication (bcrypt-secured)
- 🧑‍💼 Admin Dashboard – Create elections, add candidates, register voters
- 👤 Voter Dashboard – Cast secure, encrypted votes
- ⛓️ Smart Contract Integration (Remix, MetaMask, Ganache)
- 📜 Audit Trail for voting actions (`audit_log.json`)
- 📈 Real-Time Results Display
- 🛡️ Blockchain-based, tamper-proof records

---

## 🧩 Tech Stack

| Layer              | Technology             |
|--------------------|------------------------|
| 👨‍💻 Smart Contract | Solidity (Remix IDE)     |
| 🧠 Backend         | Python, Streamlit       |
| 🔗 Blockchain Comm.| Web3.py                 |
| 🌐 Frontend        | HTML, CSS, Streamlit, JS|
| 👛 Wallet          | MetaMask                |
| 🔐 Auth System     | bcrypt + JSON DB        |

---

## 🏗️ Folder Structure


decentralized_voting_app/
├── app/
│   ├── app.py                   # Streamlit frontend
│   ├── web3_config.py           # Web3 connection logic
│   ├── contract_interaction.py  # Smart contract calls
│   ├── users.json               # Admin/Voter data
│   ├── audit_log.json           # Voting trail log
│   ├── .env                     # Secrets file
│   └── abi.json                 # Smart contract ABI
├── contracts/
│   └── Voting.sol               # Solidity contract
├── frontend/
│   ├── index.html               # MetaMask-integrated UI
│   ├── app.js                   # Frontend contract interaction
│   └── style.css                # Basic styling
├── README.md
├── LICENSE
└── requirements.txt
🔐 .env Configuration
Create an .env file inside the app/ folder:


ADMIN_ADDRESS=0xYourRemixDeployedAdminAddress
ADMIN_PRIVATE_KEY=0xYourPrivateKeyFromRemix
CONTRACT_ADDRESS=0xYourDeployedContractAddress
🦊 Connecting MetaMask with Ganache (Local Blockchain)
✅ Prerequisites
Ganache – Local Ethereum chain

MetaMask – Browser extension wallet

Remix IDE – Online Solidity IDE

🔧 Step-by-Step Setup
1️⃣ Install and Run Ganache
Launch Ganache → Click Quickstart

You get:

10 test accounts with 100 ETH each

RPC Server: http://127.0.0.1:7545

Chain ID: 1337 or 5777

2️⃣ Add Ganache to MetaMask
MetaMask → Add Network Manually:

Field	Value
Network Name	Ganache Local
RPC URL	http://127.0.0.1:7545
Chain ID	1337 or 5777
Currency	ETH

Click Save and switch to the Ganache Local network.

3️⃣ Import a Ganache Account
In Ganache → Click 🔑 icon → Copy Private Key

In MetaMask:

Click avatar → Import Account

Paste private key → Click Import

✅ Now MetaMask is connected to your local chain with fake test ETH!

🧱 Smart Contract Deployment
Open Remix IDE

Create Voting.sol and paste:

solidity

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Voting {
  address public admin;
  string[] public candidates;
  mapping(string => uint256) public votes;
  mapping(address => bool) public hasVoted;

  constructor() {
      admin = msg.sender;
  }

  function addCandidate(string memory name) public {
      require(msg.sender == admin, "Only admin can add candidates");
      candidates.push(name);
  }

  function vote(string memory name) public {
      require(!hasVoted[msg.sender], "Already voted");
      votes[name]++;
      hasVoted[msg.sender] = true;
  }

  function getVotes(string memory name) public view returns (uint256) {
      return votes[name];
  }

  function getAllCandidates() public view returns (string[] memory) {
      return candidates;
  }
}
Compile using Solidity v0.8.20

Deploy using Injected Web3 (MetaMask)

Copy the Contract Address and ABI

🧑‍💻 Run the App
For Streamlit Backend:

pip install -r requirements.txt
streamlit run app/app.py
For HTML/JS Frontend:
Just open frontend/index.html in your browser and connect MetaMask.

⚠️ Common Errors & Fixes
Error Message	Fix
from field must match key	MetaMask address ≠ Remix deployer
Gas estimation failed	Invalid form data or unauthorized account
not a valid hex	Check .env format (contract address)
audit_log.json not found	Create an empty {} manually

✨ Features (JS Frontend)
Admin can add candidates

Voters can vote once only

Vote counts stored on-chain

No Node.js, no backend needed

📊 Future Enhancements
Result visualization with pie/bar charts

Role-based election types (Govt, Edu, Corporate)

OTP/email-based voter verification

Deploy to Goerli/Sepolia/Testnets

Add voter anonymity via Zero-Knowledge Proofs

🙌 Credits
Built  by Aishwarya Shrivastava


📄 License
This project is licensed under the MIT License. See LICENSE for full text.

📸 Screenshots
Screenshots will be added after successful deployment & voting demonstration.


---

### ✅ LICENSE File (MIT)


MIT License

Copyright (c) 2025 Aishwarya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

