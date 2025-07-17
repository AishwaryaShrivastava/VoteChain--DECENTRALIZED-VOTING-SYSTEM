// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    address public admin;
    string public electionName;
    bool public electionStarted;
    bool public electionEnded;

    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }

    struct Voter {
        bool isRegistered;
        bool hasVoted;
        uint votedCandidateId;
    }

    mapping(uint => Candidate) public candidates;
    mapping(address => Voter) public voters;
    uint public candidatesCount;

    event Voted(address indexed voter, uint candidateId);
    event ElectionStarted(string electionName);
    event ElectionEnded();

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this.");
        _;
    }

    modifier electionOngoing() {
        require(electionStarted && !electionEnded, "Election is not ongoing.");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    function startElection(string memory _name) public onlyAdmin {
        electionName = _name;
        electionStarted = true;
        emit ElectionStarted(_name);
    }

    function endElection() public onlyAdmin {
        electionEnded = true;
        emit ElectionEnded();
    }

    function addCandidate(string memory _name) public onlyAdmin {
        require(!electionStarted, "Cannot add candidates once election starts.");
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }

    function registerVoter(address _voter) public onlyAdmin {
        voters[_voter].isRegistered = true;
    }

    function vote(uint _candidateId) public electionOngoing {
        Voter storage sender = voters[msg.sender];
        require(sender.isRegistered, "You must be a registered voter.");
        require(!sender.hasVoted, "You have already voted.");
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate.");

        sender.hasVoted = true;
        sender.votedCandidateId = _candidateId;
        candidates[_candidateId].voteCount++;

        emit Voted(msg.sender, _candidateId);
    }

    function getCandidate(uint _id) public view returns (string memory, uint) {
        Candidate memory c = candidates[_id];
        return (c.name, c.voteCount);
    }
}
