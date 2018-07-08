var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);


io.on('connection', function(socket){
    socket.on('note message', function(msg){
        io.emit('note message', msg);
    });
});


http.listen(8000, function(){
  console.log('listening on *:8000 mana');
});