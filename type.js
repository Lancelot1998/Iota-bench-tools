var request = require('request');

var command = {
  "command": "getTrytes",
  "hashes": [
    "GIIVWOG9CVECAZKRTTIUXVEGXDERNFDNPYTCPBDEWPESJGYPZKBJRMAC9NLAOJMWBAFCFGKNWXMTPL999"
  ]
}

var options = {
  url: 'http://localhost:14265',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
		'X-IOTA-API-Version': '1',
    'Content-Length': Buffer.byteLength(JSON.stringify(command))
  },
  json: command
};

request(options, function (error, response, data) {
  if (!error && response.statusCode == 200) {
    console.log(data);
  }
});
