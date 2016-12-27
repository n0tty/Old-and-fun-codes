//Developing a IRC bot based on node.js
//Step 1> Install node.js and npm:
//https://gist.github.com/isaacs/579814
//Step 2> Install irc module:
//npm install irc
//Step 3> Run Bot node chatur.js
// The Connection pre-requisits
var config = {
  channels: ["#channel_name"],
  server: "irc.server_name.com",
  botName: "Chatur"
};
// Load irc library
var irc = require("irc");

// Create connection
var bot = new irc.Client(config.server, config.botName, {
  channels: config.channels
});
// Listen for new joiners
bot.addListener("join", function(channel, who) {
  
  bot.say(channel, who + "...Hi n00b!");
});
// Listen for any messages in channel, spam on PM
bot.addListener("message", function(from, to, text, message) {
  bot.say(from, "¿YOLO...You Only Live Once?");
});

// Listen for any messages, spam on channel
bot.addListener("message", function(from, to, text, message) {
  bot.say(config.channels[0], "¿kkkkkk?");
});
