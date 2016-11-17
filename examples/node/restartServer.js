'use strict';

const https = require('https');
const path = require('path');

// Constants
const API_HOSTNAME = 'prisma.cubedhost.com';
const API_PATH = '/api/';

// Your authentication details
const API_KEY = 'example_api_key';
const API_USER = 'me@example.com';

/**
 * General purpose API function
 *
 * @param  {String}   endpoint API endpoint to request
 * @param  {String}   method   HTTP method (GET, POST, PUT, DELETE)
 * @param  {Mixed}    body     Data to send with request, can be an object
 * @return {Promise}           Resolved with response object
 */
function send(endpoint, method, body) {
  if (!method) method = 'GET';

  let requestPath = path.join(API_PATH, endpoint);

  if (body && typeof body !== 'string') {
    body = JSON.stringify(body);
  }

  let options = {
    hostname: API_HOSTNAME,
    path: requestPath,
    method: method,
    headers: {
      'Content-Type': 'application/json',
      'X-Api-Key': API_KEY,
      'X-Api-User': API_USER
    }
  };

  return new Promise((resolve, reject) => {
    // Perform our HTTP request
    let req = https.request(options, res => {
      let output = '';

      // Set UTF-8 encoding to receive strings from the stream
      res.setEncoding('utf8');

      // Append output to a single string until there's none left
      res.on('data', chunk => output += chunk);

      // Parse JSON response and check for error
      res.on('end', () => {
        output = JSON.parse(output);

        // If the request was not successful, create an error and reject
        if (!output.success) {
          let err = new Error(output.error);

          // Grab HTTP status code from response
          err.status = res.statusCode;

          return reject(err);
        }

        // If successful, resolve with API response object
        resolve(output);
      });
    });

    // Reject the promise immediately on error
    req.on('error', reject);

    // Send request body
    req.end(body);
  });
}

// Restart a server
let id = 123;

send(`/server/${id}/restart`, 'POST')
  .then(data => console.log('Output:', data))
  .catch(err => console.error('Error!', err));
