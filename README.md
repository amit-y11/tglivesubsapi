# tglivesubsapi
Simple Flask App to get live subscribers count of telegram channels along with channel logo and description.

You can get channel or group name, its description , its current subcribers/members , and its profile picture
```json
{"channel_name":"Bots By Amit",
"description":"Get all updates regarding bots made by @amit_y11 in this channel",
"image":"https://cdn5.telesco.pe/file/nyOdKkOjx6434MW6wUwW02iFbl0EGyihrXkkVIVB4uUQN9dMcUUuQU8B9N66LfX6TSE8iT_yUcJ1B7QPhwzjOItdzMlkwpkptFn7KN1_gXMZUolvAc11wr7xR4oG2866fYK6jrT8bMVinyOW8m9jfsz3Mi3kqSs0I5fisejx3lqbuC1zdUc6naBII_Dun4FUlwuVZIRZKIoYzdh-0B5zxRDcqptcGMt4uCg_2j-U8XjdzKZFJB2PHwAT5A3XwjOLoRG3S5JUZMP8wde9tHXKBF4upIFoj5EdQLogU1QpcJy4wy5xcfERPbEX589K_XXoMNo3yDVwlbzatTN37fI71Q.jpg",
"subs":"9481"}
```
---
## Installation : 
Clone this repository using
```sh
$ git clone https://github.com/amit-y11/tglivesubsapi
```
Enter the directory and install all the requirements using
```sh
$ pip3 install -r requirements.txt
```
Run the app using
```sh
$ python3 app.py
```
Now the app is running on 127.0.0.1:5000

## Usage : 
```sh
https://127.0.0.1:5000/getsubs/<Enter name of the channel or Group Here>
```
You can check out this api here [tglivesubsapi.vercel.app](https://tglivesubsapi.vercel.app/).
