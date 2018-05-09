var ArtToken = artifacts.require("ArtToken");

module.exports = function(deployer) {
  deployer.deploy(ArtToken, 'ArtToken', 'ART');
};
