#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const endpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
let characters = [];
const names = [];

function getCharacters () {
  return new Promise((resolve, reject) => {
    request(endpoint, async (err, res, body) => {
      if (err || res.statusCode !== 200) {
        reject(err);
      } else {
        const movieData = JSON.parse(body);
        characters = movieData.characters;
        resolve();
      }
    });
  });
}

async function getCharNames () {
  try {
    await getCharacters();
    if (characters.length > 0) {
      for (const character of characters) {
        await new Promise((resolve, reject) => {
          request(character, (err, res, body) => {
            if (err || res.statusCode !== 200) {
              reject(err);
            } else {
              const characterData = JSON.parse(body);
              names.push(characterData.name);
              resolve();
            }
          });
        });
      }
    } else {
      console.error('Error No Characters found');
    }

    for (const name of names) {
      if (name === names[names.length - 1]) {
        process.stdout.write(name);
      } else {
        process.stdout.write(name + '\n');
      }
    }
  } catch (error) {
    console.error('Error fetching characters:', error);
  }
}

getCharNames();
