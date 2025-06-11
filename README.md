# DECENTRALIZED-VOTING-SYSTEM

🧾 README: Connecting MetaMask with Ganache (Local Blockchain)
This guide walks through setting up a local Ethereum blockchain using Ganache and connecting it to MetaMask using fake test ETH for development — with zero real money involved.

✅ Prerequisites
Ganache Desktop App (Free): Download Ganache

MetaMask Extension (Free): Install MetaMask

Browser (like Chrome or Firefox)

🔧 Step-by-Step Setup
1. Install and Run Ganache
Launch the Ganache desktop app.

Click Quickstart to create a default local blockchain.

This gives you:

10 test accounts

Each preloaded with 100 fake ETH

Local RPC server at http://127.0.0.1:7545

Chain ID: usually 5777 or 1337

2. Set Up MetaMask
Install the MetaMask extension in your browser.

Create a new wallet (you will get a Secret Recovery Phrase — store it safely!).

MetaMask defaults to Ethereum Mainnet — we’ll change that.

3. Add Ganache Network to MetaMask
In MetaMask:

Click the network dropdown at the top → Select “Add network manually”

Fill in:

yaml
Copy
Edit
Network Name: Ganache Local
RPC URL:      http://127.0.0.1:7545
Chain ID:     5777  (or 1337 based on Ganache)
Currency:     ETH
Click Save

Now switch to the new Ganache Local network in MetaMask

4. Import Ganache Test Account into MetaMask
To access the fake ETH:

In Ganache, click the key icon next to an account → Copy Private Key

In MetaMask:

Click your account icon (top-right)

Choose Import Account

Paste the private key

Click Import

You will now see:

The Ganache account in MetaMask

The corresponding test ETH balance

✅ Done! 🎉
You are now fully connected:

MetaMask is linked to your local blockchain.

You can deploy smart contracts, send fake ETH, and test your DApp with no real money involved.

🛠 Next Steps
Write and deploy your Voting Smart Contract using Remix IDE or Hardhat.

Use MetaMask to sign transactions.

Optionally connect your frontend (HTML/JS) using Web3.js or Ethers.js.


# 🗳️ Decentralized Voting DApp (Local Blockchain Setup)

This guide walks through setting up a **local Ethereum blockchain using Ganache** and connecting it to **MetaMask**. You’ll then deploy a smart contract using **Remix IDE** and run a frontend web app using **HTML/JS** without requiring `npm` or Truffle.

---

## ✅ Prerequisites

- **Ganache Desktop App** → [Download Ganache](https://trufflesuite.com/ganache/)
- **MetaMask Extension** → [Install MetaMask](https://metamask.io/)
- Browser (Chrome or Firefox)
- **Remix IDE** → [Open Remix](https://remix.ethereum.org)

---

## 🔧 Step-by-Step: Connecting MetaMask with Ganache

### 1. Install and Run Ganache
- Launch the Ganache desktop app
- Click **Quickstart**
- Ganache provides:
  - 10 test accounts with 100 ETH each
  - Local RPC Server: `http://127.0.0.1:7545`
  - Chain ID: `1337` or `5777`

### 2. Set Up MetaMask
- Install the MetaMask browser extension
- Create a new wallet
- Save your **Secret Recovery Phrase** securely

### 3. Add Ganache Network in MetaMask
- Click the network dropdown → **Add network manually**
- Fill in:
Network Name: Ganache Local
RPC URL: http://127.0.0.1:7545
Chain ID: 1337 or 5777
Currency Symbol: ETH

- Click **Save** and switch to the Ganache network

### 4. Import a Ganache Account into MetaMask
- In Ganache: Click the 🔑 icon next to an account → **Copy Private Key**
- In MetaMask:
- Click your avatar → **Import Account**
- Paste the private key → Click **Import**

✅ Now MetaMask is linked to your local blockchain with fake test ETH.

---

## ⚙️ Deploy the Smart Contract (Without Truffle)

1. Open [Remix IDE](https://remix.ethereum.org)
2. Create a file: `Voting.sol`
3. Paste the following code:

```solidity
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

Compile using Solidity 0.8.20

In Deploy tab:

Select Injected Provider - MetaMask

Deploy the contract

Copy the deployed Contract Address

Expand the deployed contract → Copy the ABI (click {} icon)

Project Structure

voting-dapp/
├── contracts/
│   └── Voting.sol
├── index.html
├── app.js
└── style.css

✅ How to Run
Open the folder in your system

Open index.html in your browser (just double-click)

Connect MetaMask to Ganache

Use the DApp to add candidates, vote, and see results

✨ Features
Admin can add candidates

Voters can vote once

Vote results are stored on-chain

No backend or Node.js required

🧠 Next Steps
Add vote deadline feature

Add voter registration system

Deploy on a public testnet (Goerli, Sepolia)

Add chart visualization for votes

🔗 Resources
Web3.js Docs

Remix IDE

Ganache

MetaMask

