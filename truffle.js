var HDWalletProvider = require("truffle-hdwallet-provider");
var infura_apikey = "LaHsmpJShSJIEAQiI0bg";
var mnemonic = "stock improve rough range dutch syrup trust horse drastic involve moral film";

// TODO: Create a configuration file that doesn't get pushed to cache this

module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 7545,
      network_id: "*"
  },
    ropsten: {
      provider: new HDWalletProvider(mnemonic, "https://ropsten.infura.io/"+infura_apikey),
      network_id: 3,
      gas: 4612388
    }
  }
};
