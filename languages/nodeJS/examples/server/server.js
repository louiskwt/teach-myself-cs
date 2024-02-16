const http = require("http"); // holding the label interface for network capability

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.end("Bye now!");
});

const port = 3000;

server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
