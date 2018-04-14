//TODO: Change this to a react framework so its easier to create html
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
      // FIXME: Need to determine what the best way of initializing contract is. This is only using the local build.
      // necessary for the
      $.getJSON($SCRIPT_ROOT+'/build', function(data) {
          var ArtArtifact = data;
          App.contracts.ArtToken = TruffleContract(ArtArtifact);

          // Set the provider for our contract
          App.contracts.ArtToken.setProvider(App.web3Provider);
     });

      return App.bindEvents();
  },

  bindEvents: function() {
    $(document).on('click', '.btn-mint', App.mintNFT);
  },

  mintNFT: function(event) {
    event.preventDefault();

    web3.eth.getAccounts(function(error, accounts) {
      if (error) {
        console.log(error);
    }
      var account = accounts[0];

      App.contracts.ArtToken.deployed().then(function(instance) {
        ArtInstance = instance;

        // Execute adopt as a transaction by sending account
        return ArtInstance.mintNFT(account);
      }).then(function(result) {
        console.log('token was minted')
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
