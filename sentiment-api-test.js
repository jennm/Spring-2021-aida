var axios = require("axios").default;

var options = {
  method: 'GET',
  url: 'https://socialsentiment-io.p.rapidapi.com/stocks/MCD/sentiment/daily/',
  headers: {
    'x-rapidapi-host': 'socialsentiment-io.p.rapidapi.com',
    'x-rapidapi-key': '0ccd37de99msh0a70f7730e4db59p13e996jsn3c6203252024'
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});