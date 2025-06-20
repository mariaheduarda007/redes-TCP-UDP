const net = require('net');
const prompt = require('prompt-sync')();

const client = new net.Socket();

const HOST = 'localhost'; 
const PORT = 9000;

client.connect(PORT, HOST, () => {
  console.log('Connected');
  const message = prompt('Message: ');
  client.write(message);
  client.end()
});

client.on('end', () => {
  console.log('End of Communication');
});

client.on('error', (err) => {
  console.error('Error:', err.message);
});
