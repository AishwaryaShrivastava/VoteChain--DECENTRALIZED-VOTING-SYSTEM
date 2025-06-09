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

