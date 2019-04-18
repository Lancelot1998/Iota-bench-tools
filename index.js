let zmq = require('zeromq');
//Create a zmq socket
let sock = zmq.socket('sub');

//Connect the ZMQ socket to the IRI by passing the `connect` function the URL or the IP address of the IRI and the ZMQ port
sock.connect('47.112.194.34:14265');
//Subscribe to the confirmed transactions event
sock.subscribe('sn');

//Create a callback function to process the data that is returned from the ZMQ
sock.on('message', msg => {
//Split the data into an array
const data = msg.toString().split(' ');
console.log(`Transaction confirmed by milestone index: ${data[1]}` );
console.log(`Transaction hash: ${data[2]}` );
});
