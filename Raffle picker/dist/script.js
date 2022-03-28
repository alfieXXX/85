let data;
let colors = [
"#9B3D47",
"#5CA7A7",
"#E24B6B",
"#BBC6D1",
"#BBA180",
"#ECAE81",
"#021243",
"#055591",
"#D5250E",
"#2D242B",
"#78676B",
"#C7C293"];


// function getQuotes() {
//   return $.ajax({
//     headers: {
//       Accept: 'application/json' },

//     url: 'https://gist.githubusercontent.com/camperbot/5a022b72e96c4c9585c32bf6a75f62d9/raw/e3c6895ce42069f0ee7e991229064f167fe8ccdc/quotes.json',
//     success: jsonQoutes => {
//       if (typeof jsonQoutes === 'string') {
//         data = JSON.parse(jsonQoutes);
//         console.log('data');
//         console.log(data);
//       }
//     } });

// };

function getQuotes() {
  return $.ajax({
    type: 'GET',
    hearders: {
      accept:'application/json' 
    },
    url: 'http://127.0.0.1:8000/apidet/list/',
    success: jsonQoutes => {
      console.log(jsonQoutes)
    } 
  });

};

function rmQuotes() {
  return data.quotes[Math.floor(Math.random() * data.quotes.length)];
};

function quote() {
  let rQuote = rmQuotes();

  let currentQuote = rQuote.quote;
  let currentAuthor = rQuote.author;

  $('#tweet-quote').attr(
  'href',
  'https://twitter.com/intent/tweet?hashtags=quotes&related=freecodecamp&text=' +
  encodeURIComponent('"' + currentQuote + '" ' + currentAuthor));


  $('#text').animate({ opacity: 0 }, 500, function () {
    $(this).animate({ opacity: 1 }, 500);
    $('#text').text(rQuote.quote);
  });
  $('#author').animate({ opacity: 0 }, 500, function () {
    $(this).animate({ opacity: 1 }, 500);
    $('#author').text(rQuote.author);
  });

  changeColor();
}

function changeColor() {
  let colorC = Math.floor(Math.random() * colors.length);
  let color = colors[colorC];
  $('body').animate({
    backgroundColor: color,
    color: color }, 1000);
  $('.colorChange').animate({ backgroundColor: color }, 1000);
}

$(document).ready(() => {
  // getQuotes().then(() => {
  //   quote();
  // });
  getQuotes()

  $('#new-quote').click(() => {
    quote();
  });
});