import React from 'react'
import ReactDOM from 'react-dom'
import Web3 from 'web3'
import './../css/index.css'


class App extends React.Component{
    constructor(props){
        super(props)
        this.
    }

    if(typeof web3 != 'undefined'){
             console.log("Using web3 detected from external source like Metamask")
             this.web3 = new Web3(web3.currentProvider)
          }else{
             console.log("No web3 detected. Falling back to http://localhost:8545. You should remove this fallback when you deploy live, as it's inherently insecure. Consider switching to Metamask for development. More info here: http://truffleframework.com/tutorials/truffle-and-metamask");
             this.web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"))
          }

          const MyContract = web3.eth.contract([{"constant":false,"inputs":[],"name":"generateNumberWinner","outputs":[],"payable":true,"type":"function"},{"constant":false,"inputs":[{"name":"myid","type":"bytes32"},{"name":"result","type":"string"}],"name":"__callback","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"numberOfBets","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_queryId","type":"bytes32"},{"name":"_result","type":"string"},{"name":"_proof","type":"bytes"}],"name":"__callback","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"player","type":"address"}],"name":"checkPlayerExists","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"resetData","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"bets","type":"uint256"}],"name":"updateMaxBets","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"number","type":"uint256"}],"name":"bet","outputs":[],"payable":true,"type":"function"},{"constant":false,"inputs":[{"name":"amountWei","type":"uint256"}],"name":"updateMinimumBet","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"distributePrizes","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"numberWinner","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"minimumBet","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"maxAmountOfBets","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"players","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalBet","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"_maxAmountOfBets","type":"uint256"}],"payable":false,"type":"constructor"},{"payable":true,"type":"fallback"}])
          this.state.ContractInstance = MyContract.at("0x430d959fa54714aca8eecd61fae2661fca900e04")

          window.a = this.state
       }

       voteNumber(number, cb){
            let bet = this.refs['ether-bet'].value

            if(!bet) bet = 0.1

            if(parseFloat(bet) < this.state.minimumBet){
               alert('You must bet more than the minimum')
               cb()
            } else {
               this.state.ContractInstance.bet(number, {
                  gas: 300000,
                  from: web3.eth.accounts[0],
                  value: web3.toWei(bet, 'ether')
               }, (err, result) => {
                  cb()
               })
            }
         }

}



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

      return App.initContract();
  },

  initContract: function() {
      $.getJSON('Adoption.json', function(data) {
        // Get the necessary contract artifact file and instantiate it with truffle-contract
        var AdoptionArtifact = data;
        App.contracts.Adoption = TruffleContract(AdoptionArtifact);

        // Set the provider for our contract
        App.contracts.Adoption.setProvider(App.web3Provider);

        // Use our contract to retrieve and mark the adopted pets
        return App.markAdopted();
      });

      return App.bindEvents();
  },

  bindEvents: function() {
    $(document).on('click', '.btn-adopt', App.handleAdopt);
  },

  markAdopted: function(adopters, account) {
      var adoptionInstance;

      App.contracts.Adoption.deployed().then(function(instance) {
        adoptionInstance = instance;

        return adoptionInstance.getAdopters.call();
      }).then(function(adopters) {
        for (i = 0; i < adopters.length; i++) {
          if (adopters[i] !== '0x0000000000000000000000000000000000000000') {
            $('.panel-pet').eq(i).find('button').text('Success').attr('disabled', true);
          }
        }
      }).catch(function(err) {
        console.log(err.message);
      });
  },

  handleAdopt: function(event) {
    event.preventDefault();

    var petId = parseInt($(event.target).data('id'));

    var adoptionInstance;

    web3.eth.getAccounts(function(error, accounts) {
      if (error) {
        console.log(error);
      }

      var account = accounts[0];

      App.contracts.Adoption.deployed().then(function(instance) {
        adoptionInstance = instance;

        // Execute adopt as a transaction by sending account
        return adoptionInstance.adopt(petId, {from: account});
      }).then(function(result) {
        return App.markAdopted();
      }).catch(function(err) {
        console.log(err.message);
      });
    });
  }

};

$(function() {
  $(window).load(function() {
    App.init();
  });
});


// App = {
//   web3Provider: null,
//   contracts: {},
//
//   init: function() {
//
//     return App.initWeb3();
//   },
//
//   initWeb3: function() {
//       // Is there an injected web3 instance?
//       if (typeof web3 !== 'undefined') {
//         App.web3Provider = web3.currentProvider;
//       } else {
//         // If no injected web3 instance is detected, fall back to Ganache
//         App.web3Provider = new Web3.providers.HttpProvider('http://localhost:7545');
//       }
//       web3 = new Web3(App.web3Provider);
//       console.log(web3)
//
//       return App.initContract();
//   }
// };
//
//
//
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
