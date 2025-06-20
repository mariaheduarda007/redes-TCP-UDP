const net = require('net');

const HOST = 'localhost';
const PORT = 9000;

const server = net.createServer((socket) => {
  console.log('Client on:', socket.remoteAddress, socket.remotePort);

  socket.on('data', (data) => {
    const message = data.toString('utf-8');
    console.log('Message:', message);

  });

  socket.on('end', () => {
    console.log('End of Communication');
    socket.end()
  });

  socket.on('error', (err) => {
    console.error('Error:', err.message);
  });
});

server.listen(PORT, HOST, () => {
  console.log(`Server on ${HOST}:${PORT}`);
});
