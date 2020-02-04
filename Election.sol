pragma solidity>=0.4.25 <0.6.2;

contract Ballot{
    
    address public admin;
    mapping (string => uint) candidates;
    mapping (string =>bool) isVoted;
    string public currentWinner;
    uint public maxVotes;
	string public Name;
    
    enum StateType { Started,Ended}
    
    StateType public  State;
    
    constructor(string memory name) public {
        admin = msg.sender;
        State = StateType.Started;
		Name = name;
    }
    
    function addCandidate(string memory _name) public {
        if(msg.sender != admin){
            revert();
        }
        candidates[_name] = 0;
    }
    
    function vote(string memory _name,string memory _addhar) public {
        if(isVoted[_addhar]==true){
            revert();
        }
        isVoted[_addhar] = true;
        candidates[_name]+=1;
        if(candidates[_name]>maxVotes){
            currentWinner = _name;
            maxVotes = candidates[_name];
        }
    }
    
    function addVoter(string memory _addhar) public {
        if(msg.sender != admin){
            revert();
        }
        isVoted[_addhar] = false;
    }
    
    function end() public {
        if(msg.sender != admin){
            revert();
        }
        State = StateType.Ended;
    }
    
}
