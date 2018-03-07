pragma solidity ^0.4.17;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/ArtToken.sol";

contract TestArtToken {
    ArtToken art = ArtToken(DeployedAddresses.ArtToken());

    function test_get_initial_balance() public{

        address address_1 = msg.sender;
        address address_2 = 0x821aEa9a577a9b44299B9c15c88cf3087F3b5544;

        uint256 balance_1 = art.balanceOf(address_1);
        uint256 expected_1 = 1776;

        uint256 balance_2 = art.balanceOf(address_2);
        uint256 expected_2 = 0;

        Assert.equal(balance_1, expected_1, "There should be 1776 tokens");
        Assert.equal(balance_2, expected_2, "There should be 0 tokens");
    }

    function test_minting() public{

        address address_1 = msg.sender;

        uint256 tokenid_2 = art.mintNFT(address_1);
        uint256 first_coin_id = 0;

        Assert.equal(tokenid_2, first_coin_id, "Should create coin with id 2");

        uint256 tokenid_1 = art.mintNFT(address_1);
        uint256 second_coin_id = 1;

        Assert.equal(tokenid_1, second_coin_id, "Should create coin with id 1");

        uint256 balance_1 = art.balanceOf(address_1);
        uint256 expected_1 = 1776;
        Assert.equal(balance_1, expected_1, "There should be 1776 tokens still");

        address owner = art.ownerOf(1);

        Assert.equal(address_1, owner, "The owner should be the OG address");

    }

    function test_transfer() public{

        address address_1 = 0x627306090abaB3A6e1400e9345bC60c78a8BEf57;
        address address_2 = 0x821aEa9a577a9b44299B9c15c88cf3087F3b5544;

        uint256 tokenid_1 = art.mintNFT(address_1);
        uint256 first_coin_id = 2;

        Assert.equal(tokenid_1, first_coin_id, "Should create coin with id 0");

        address owner = art.ownerOf(2);
        Assert.equal(address_1, owner, "The owner should be the OG address");

        art.transfer(address_2, tokenid_1);

        address new_owner = art.ownerOf(2);
        Assert.equal(address_2, new_owner, "The owner should be the OG address");


    }

}
