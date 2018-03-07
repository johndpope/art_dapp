var ArtToken = artifacts.require("./ArtToken.sol")

contract('ArtToken', function(accounts) {
  it("should put 10000 ArtToken in the first account", function() {
    return ArtToken.deployed().then(function(instance) {
      return instance.balanceOf.call(accounts[0]);
    }).then(function(balance) {
      assert.equal(balance.valueOf(), 1776, "1776 wasn't in the first account");
    });
  });
  it("should mint a token to account[5]", function() {
      return ArtToken.new(200).then(function(instance) {
        return instance.mintNFT.call(accounts[5]);
    }).then(function(_tokenID) {
        assert.equal(_tokenID.valueOf(), 0, "1776 wasn't in the first account");
      });
  });
  it("should print balance", function() {
    var balance = web3.eth.getBalance(accounts[0])
    console.log(balance.toNumber())
  });

});
