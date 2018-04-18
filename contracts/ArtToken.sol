pragma solidity ^0.4.19;


/* test code

ArtToken.deployed().then(function(instance){return instance.balanceOf(0x627306090abab3a6e1400e9345bc60c78a8bef57);}).then(function(value){return value.toNumber()});

ArtToken.deployed().then(function(instance){return instance.balanceOf(0x627306090abab3a6e1400e9345bc60c78a8bef57);});

ArtToken.deployed().then(function(instance){return instance.mintNFT(0x627306090abab3a6e1400e9345bc60c78a8bef57);});

ArtToken.deployed().then(function(instance){return instance.ownerOf(1);});

ArtToken.deployed().then(function(instance){return instance.ownerOf(1);});

ArtToken.deployed().then(function(instance){return instance.messageSender();});

ArtToken.deployed().then(function(instance){return instance.totalSupply();}).then(function(value){return value.toNumber()});

(0) 0x627306090abab3a6e1400e9345bc60c78a8bef57
(1) 0xf17f52151ebef6c7334fad080c5704d77216b732
(2) 0xc5fdf4076b8f3a5357c5e395ab970b5b54098fef
(3) 0x821aea9a577a9b44299b9c15c88cf3087f3b5544
(4) 0x0d1d4e623d10f9fba5db95830f7d3839406c6af2
(5) 0x2932b7a2355d6fecc4b5c0b6bd44cc31df247a2e
(6) 0x2191ef87e392377ec08e7c08eb105ef5448eced5
(7) 0x0f4f2ac550a1b4e2280d04c21cea7ebd822934b5
(8) 0x6330a553fc93768f612722bb8c2ec78ac90b3bbc
(9) 0x5aeda56215b167893e80b4fe645ba6d5bab767de

SimpleStorage.deployed().then(function(instance){return instance.get.call();}).then(function(value){return value.toNumber()});


*/
/*

ArtToken Token contract
Designed to fit the ERC 721 standard
https://github.com/ethereum/eips/issues/721

*/


contract ArtToken {

	//fixed name of the token
	string constant private tokenName = "ArtToken token";
	//fixed symbol of the token
	string constant private tokenSymbol = "ART";
	//fixed supply of tokens
	uint256 private totalTokens = 1000;
    //first token ID
    uint256 private currentTokenID = 0;
    /* This creates an array with all balances */
    mapping (address => uint256) public balanceOf;
	// Mapping from token ID to owner
    mapping (uint256 => address) public tokenOwners;
    // Mapping from token ID to approved address
    mapping (uint256 => address) public tokenApprovals;
    // Mapping from owner to list of owned token IDs
    mapping (address => uint256[]) public ownedTokens;

    //address genesisAddress = 0x627306090abab3a6e1400e9345bc60c78a8bef57;
    /* Initializes contract with initial supply tokens to the creator of the contract */
    function ArtToken  (
        uint256 initialSupply
        ) {
        balanceOf[msg.sender] = initialSupply;              // Give the creator all initial tokens
        totalTokens = initialSupply;
    }

    //returns name of token
    function name() public constant returns (string) {
    	return tokenName;
    }

    //returns symbol of token
    function symbol() public constant returns (string) {
    	return tokenSymbol;
    }

    //returns total supply of token
    function totalSupply() constant returns (uint256 totalSupply) {
    	return totalTokens;
    }

    //returns balance of an owner
    function balanceOf(address _owner) constant returns (uint256 balance) {
        return balanceOf[_owner];
    }

    //return the owner of a token
    function ownerOf(uint256 _tokenID) constant returns (address owner) {
    	return tokenOwners[_tokenID];
    }

    //return tokens an address owns
    function listOfTokens(address _owner) constant returns (uint256[] listOfTokens) {
        return ownedTokens[_owner];
    }

    //get address of message sender
    function messageSender() constant returns (address) {
    	return msg.sender;
    }

    //get balance of message sender
    function messageSenderBalance() constant returns (uint256 balance) {
        return balanceOf[msg.sender];
    }

    //mint a new NFT
    function mintNFT(address _to) returns (uint256 _tokenID) {
        //only we can mint token
        //assert(msg.sender = genesisAddress);
        tokenOwners[currentTokenID] = _to;
        ownedTokens[_to].push(currentTokenID);
        currentTokenID = currentTokenID +1;
        return (currentTokenID -1);
    }

    function popToken(address _from, uint256 tokenID) {
        /* ownedTokens[_from].pop(tokenID); */
    }

    function balanceGenesis() constant returns (uint256 genesisBalance) {
        return balanceOf[0x627306090abaB3A6e1400e9345bC60c78a8BEf57];
    }

    function transfer(address _to, uint256 _tokenID) {
    	address currentOwner = msg.sender;
    	address newOwner = _to;
		assert(balanceOf[currentOwner] >= 1);
    	balanceOf[currentOwner] -= 1;
    	tokenOwners[_tokenID] = newOwner;
    	balanceOf[newOwner] += 1;
    	Transfer(currentOwner, newOwner, _tokenID);
    }

   	event Transfer(address indexed _from, address indexed _to, uint256 _tokenId);

}
