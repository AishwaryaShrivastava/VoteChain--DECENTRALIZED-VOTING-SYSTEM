// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract VotingSystem {
    address public admin;

    struct Candidate {
        string name;
        address candidateAddress;
    }

    struct Vote {
        uint256 voteId;
        address voterAddress;
        string candidateName;
        bool isApproved;
    }

    Candidate[] public candidates;
    mapping(string => address) public candidateAddressMap;
    mapping(uint256 => Vote) public votes;
    uint256[] public approvedVoteIds;

    constructor() {
        admin = msg.sender;
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only the admin can perform this action");
        _;
    }

    modifier onlyVoter() {
        require(msg.sender != admin, "Admin cannot vote");
        _;
    }

    function addCandidate(string memory _name, address _candidateAddress)
        public
        onlyAdmin
    {
        require(bytes(_name).length > 0, "Candidate name is required");
        require(_candidateAddress != address(0), "Invalid address");

        candidates.push(Candidate(_name, _candidateAddress));
        candidateAddressMap[_name] = _candidateAddress;
    }

    function castVote(uint256 _voteId, string memory _candidateName, bool _isApproved)
        public
        onlyVoter
    {
        require(candidateAddressMap[_candidateName] != address(0), "Candidate does not exist");

        votes[_voteId] = Vote(_voteId, msg.sender, _candidateName, _isApproved);

        if (_isApproved) {
            approvedVoteIds.push(_voteId);
        }
    }

    function getVote(uint256 _id)
        public
        view
        returns (uint256, address, string memory, bool)
    {
        Vote memory v = votes[_id];
        return (v.voteId, v.voterAddress, v.candidateName, v.isApproved);
    }

    function getAllApprovedVoteIds() public view returns (uint256[] memory) {
        return approvedVoteIds;
    }

    function getVoteCountForCandidate(string memory _candidateName)
        public
        view
        returns (uint256 count)
    {
        require(candidateAddressMap[_candidateName] != address(0), "Candidate does not exist");

        uint256 counter = 0;
        for (uint256 i = 0; i < approvedVoteIds.length; i++) {
            Vote memory v = votes[approvedVoteIds[i]];
            if (
                keccak256(bytes(v.candidateName)) == keccak256(bytes(_candidateName)) &&
                v.isApproved
            ) {
                counter++;
            }
        }
        return counter;
    }

    function getAllCandidates() public view returns (Candidate[] memory) {
        return candidates;
    }
}

