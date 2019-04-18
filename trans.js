const Iota = require('@iota/core');
const Converter = require('@iota/converter');
// Create a new instance of the IOTA object
// Use the `provider` field to specify which IRI node to connect to
const iota = Iota.composeAPI({
provider: 'http://localhost:14265'
});
// Call the `getNodeInfo()` method for information about the IRI node
iota.getNodeInfo()
// Convert the returned object to JSON to make the output more readable
//.then(info => console.log(JSON.stringify(info, null, 1)))
//.then(info => )
.catch(err => {
    // Catch any errors
    console.log(err);
});
const address =
'FJHSSHBZTAKQNDTIKJYCZBOZDGSZANCZSWCNWUOCZXFADNOQSYAHEJPXRLOVPNOQFQXXGEGVDGICLMOXX';
const seed =
'FJHSSHBZTAKQNDTIKJYCZBOZDGSZANCZSWCNWUOCZXFADNOQSYAHEJPXRLOVPNOQFQXXGEGVDGICLMOXM';
const message = Converter.asciiToTrytes('Hello World!');

const transfers = [
{
    value: 0,
    address: address,
    message: message
}
];

iota.prepareTransfers(seed, transfers)
    .then(trytes => {
        return iota.sendTrytes(trytes, 3, 9)
    })
    .then(bundle => {
    console.log(`Published transaction with tail hash: ${bundle[0].hash}`)
    console.log(`Bundle: ${JSON.stringify(bundle, null, 1)}`)
        console.log(`send right`)
})
.catch(err => {
        // Catch any errors
    console.log(err);
});
