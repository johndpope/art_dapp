


App = {
  web3Provider: null,
  contracts: {},

  init: function() {

    return App.initWeb3();
  },

  initWeb3: function() {
      // Is there an injected web3 instance?
      if (typeof web3 !== 'undefined') {
        App.web3Provider = web3.currentProvider;
      } else {
        // If no injected web3 instance is detected, fall back to Ganache
        App.web3Provider = new Web3.providers.HttpProvider('http://localhost:7545');
      }
      web3 = new Web3(App.web3Provider);
      console.log(web3)

      return App.initContract();
  }
};



// exports.init = function() {
//     if (typeof web3 !== 'undefined') {
//       web3 = new Web3(web3.currentProvider);
//     } else {
//       // set the provider you want from Web3.providers
//       web3 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:7545"));
//     }
//     return web3
// }
//
// exports.get_addresses = function() {
//     return web3.eth.accounts
// }


// class Jello {
//     constructor(provider) {
//         this.web3Provider = provider,
//         this.contracts = {}
//     }
//
//     init() {
//         return this.initWeb3();
//     };
//
//   initWeb3() {
//       // Is there an injected web3 instance?
//       if (typeof web3 !== 'undefined') {
//         this.web3Provider = web3.currentProvider;
//       } else {
//         // If no injected web3 instance is detected, fall back to Ganache
//         this.web3Provider = new Web3.providers.HttpProvider('http://127.0.0.1:7545');
//       }
//       web3 = new Web3(this.web3Provider);
//
//       return this.initContract();
//   };
//
//   initContract() {
//       $.getJSON('ArtToken.json', function(data) {
//         // Get the necessary contract artifact file and instantiate it with truffle-contract
//         var ArtTokenArtifact = data;
//         this.contracts.ArtToken = TruffleContract(ArtTokenArtifact);
//
//         // Set the provider for our contract
//         this.contracts.ArtToken.setProvider(this.web3Provider);
//
//       });
//   };
//
//   getbalanceOf(account) {
//         this.contracts.ArtToken.deployed().then(function(instance) {
//           return instance.balanceOf.call(account);
//         }).then(function(balance) {
//             return balance.valueOf()
//         }).catch(function(err) {
//           console.log(err.message);
//     });
//    }
// }
