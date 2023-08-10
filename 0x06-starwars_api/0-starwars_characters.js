#!/usr/bin/node

const process = require('process');
const request = require('request');

function fetchCharacterData (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

async function main () {
  const args = process.argv;

  if (args.length < 3) {
    console.log('Usage: node script.js <movie_id>');
    return;
  }

  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;
  request.get(movieUrl, async (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const movieData = JSON.parse(body);
    if (!movieData.characters || movieData.characters.length === 0) {
      console.log('No character data available for this movie.');
      return;
    }

    try {
      for (const characterUrl of movieData.characters) {
        const characterName = await fetchCharacterData(characterUrl);
        console.log(characterName);
      }
    } catch (err) {
      console.error(err);
    }
  });
}

main();
