
# 0x06. Star Wars API project:

This script retrieves and prints all the characters of a Star Wars movie using the Star Wars API.

## Prerequisites

- Node.js (version 10 or later) installed on your system
- `request` module installed (`npm install request`)

## Usage

1. Clone the repository or create a new file for the script.
2. Open the terminal and navigate to the directory containing the script.
3. Run the script with the Movie ID as the first positional argument:

   ```
   node 0-starwars_characters.js <movie_id>
   ```

   Replace `<movie_id>` with the ID of the Star Wars movie you want to retrieve the characters for (e.g., `3` for "Return of the Jedi").

## Example

```
$ node 0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Wicket Systri Warrick
```

## How it Works

1. The script uses the `request` module to make an HTTP GET request to the Star Wars API's `/films/<movie_id>` endpoint to retrieve the movie data.
2. It then extracts the `characters` list from the movie data and makes separate requests to the `/people/<character_id>` endpoint for each character.
3. The script prints the name of each character in the order they appear in the `characters` list.

## Error Handling

- If the provided Movie ID is invalid or does not exist, the script will print an error message.
- If there is a network error or any other issue during the API requests, the script will handle the error and provide a relevant error message.

## Improvements

- Add error handling for cases where the API response data is not in the expected format.
- Implement parallel requests to the API to improve the script's performance.
- Add support for handling multiple movie IDs as arguments.
