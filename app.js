
const contractAddress = "0x1Bac3165eE33169Bc9946D469639A0DF72872DbD";

const contractABI = [
  {
    "inputs": [],
    "name": "getCandidates",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "id",
            "type": "uint256"
          },
          {
            "internalType": "string",
            "name": "name",
            "type": "string"
          },
          {
            "internalType": "uint256",
            "name": "voteCount",
            "type": "uint256"
          }
        ],
        "internalType": "struct VotingSystem.Candidate[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getVoterAddresses",
    "outputs": [
      {
        "internalType": "address[]",
        "name": "",
        "type": "address[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "_name",
        "type": "string"
      }
    ],
    "name": "addCandidate",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getAllVotesOfCastedPerson",
    "outputs": [
      {
        "internalType": "address[]",
        "name": "",
        "type": "address[]"
      },
      {
        "internalType": "string[]",
        "name": "",
        "type": "string[]"
      },
      {
        "internalType": "bool[]",
        "name": "",
        "type": "bool[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_person",
        "type": "address"
      }
    ],
    "name": "authorize",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_candidateId",
        "type": "uint256"
      }
    ],
    "name": "vote",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];

let contract;

window.addEventListener('load', async () => {
  if (window.ethereum) {
    const web3 = new Web3(window.ethereum);
    await window.ethereum.enable();

    contract = new web3.eth.Contract(contractABI, contractAddress);
    console.log("Contract loaded:", contract);

    const candidates = await contract.methods.getCandidates().call();
    console.log("Candidates:", candidates);
    document.getElementById("output").innerText = JSON.stringify(candidates, null, 2);
  } else {
    alert("Please install MetaMask!");
  }
});


async function connect() {
  if (window.ethereum) {
    const web3 = new Web3(window.ethereum);
    await window.ethereum.request({ method: 'eth_requestAccounts' });
    alert("Connected to MetaMask");
  }
}

async function addCandidate() {
  const name = document.getElementById("candidateName").value;
  const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
  await contract.methods.addCandidate(name).send({ from: accounts[0] });
  alert("Candidate added successfully");
}

async function vote() {
  const id = document.getElementById("candidateId").value;
  const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
  await contract.methods.vote(id).send({ from: accounts[0] });
  alert("Vote casted successfully");
}
