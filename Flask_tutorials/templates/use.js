
const url = 'https://swapi-api.alx-tools.com/api/films/' + 3;
const connect = require('request');

const myList = [];
connect(url, function (err, response, body) {
  if (!err) {
    const content = JSON.parse(body);
    const actors = content.characters;
    for (let i = 0; i <= actors.length - 1; i++) {
      myList.push(actors[i]);
    }
  } else {
    console.log(err);
  }
  for (x in myList) {
    const newurl = myList[x];
    const charactersconnect = require('request');
    charactersconnect(newurl, function (err, resp, body) {
      if (!err) {
        const charactersconnect = JSON.parse(body);
        console.log(charactersconnect.name);
      }
    });
  }
});
