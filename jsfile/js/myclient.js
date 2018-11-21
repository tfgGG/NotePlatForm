/*var redis = require('redis');
// subscribe
var sub = redis.createClient();
sub.subscribe('test_channel');
sub.on('message', function onSubNewMessage(channel, data) {
    console.log(channel, data);
});
// publish
var pub = redis.createClient();
pub.publish('test_channel', 'nodejs data published to test_channel');
*/ 
/*
var editing = $(function () {

  var socket = io();
  var editor = $('.CodeMirror-code')
  editor.onchange(function(){
      // mansocket.emit('note',)
      DbSave();
      socket.emit('note message', SimpleMDE.val());

  })
  socket.on('note message', function(msg){
    SimpleMDE.val(msg);
  });
  function DbSave(){
    alert("dbsave");
  }

})();*/