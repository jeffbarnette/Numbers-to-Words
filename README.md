# Numbers to Words Exercise
An code exercise in converting numbers into English words using Python and Django

## Key Features
- Dockerized container for easy setup.
- Supports any positive or negative number of any length.
- Works with both GET and POST request methods.
- Includes advanced error handling with HTTP response codes.
- Includes Postman collection for manual testing.

## Prerequisites
- [Docker Desktop](https://docs.docker.com/desktop/)
- [Postman](https://www.postman.com/downloads/) (if manually testing endpoints)

## Contents
- [Local Setup and Usage](#Local-Setup-and-Usage)
- [Using Postman](#Using-Postman)


### Local Setup and Usage

_Note: The latest Docker Desktop is required to already be installed on your system._

1. Make sure Docker is already running, then run:

```
docker-compose up
```

2. Once the container is built and running, open `http://localhost:8000`in your browser to verify everything is working. You should see a message that says ***Service is running!***

3. In the address bar, add **/num_to_english?number=100** to the URL or [click here](http://localhost:8000/num_to_english?number=100).

4. You shold see a JSON response which has the status of **OK** and the words **one hundred**. Feel free to experiment with other numbers by changing it after the **/num_to_english?number=** portion of the URL. You can enter any number of any length and get back a valid response in words.

5. Here are a few more random examples you can try:

- [150,000](http://localhost:8000/num_to_english?number=150000) should return "one hundred fifty thousand".
- [1,000,000](http://localhost:8000/num_to_english?number=1000000) should return "one million".
- [55](http://localhost:8000/num_to_english?number=55) should return "fifty five".
- [888,000](http://localhost:8000/num_to_english?number=888) should return "eight hundred eighty eight thousand".
- [-752,000,000,000](http://localhost:8000/num_to_english?number=100) should return "negative seven hundred fifity two billion".

_Note: For additional manual testing using the GET and POST methods see the Using Postman section below._


### Using Postman

You can use Postman and the included Postman collection for manual testing of both the **GET** and **POST** methods. To start, you will need to first [import the collection](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-postman-data) which is located in the **/postman** directory path.

Once you have the collection imported, you can begin experimenting with the **GET** and **POST** requests. You can change the querystring in the **GET** request (just like you might have done during the initial setup steps described above) or under Params. Then click **Send**.

For the **POST** request, you can modify the number value under the body > raw section. Then click **Send**.


### Changelog

**v1.0.0**
- Initial Release
