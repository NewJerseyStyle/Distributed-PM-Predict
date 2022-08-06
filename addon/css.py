def get_css():
  return '''
  @font-face {
    font-family: SoukouMincho;
    src: url(SoukouMincho.ttf);
  }

  html, body, .body0, .body1 {
    margin: 0;
    height: calc(100% - .5em);
    overflow: hidden;
  }

  body {
    font-family: 'Azeret Mono';
    font-size: 2vh;
    border-style: solid;
    border-color: orange;
    border-width: .5em;
    background-color: #000;
    color: orange;
  }

  h2 {
    font-size: 4em;
  }

  p {
    margin: 0;
  }

  hr {
    margin: .5vh 0 .5vh 0;
    border-color: orange;
  }

  button, input[type="button"] {
    margin: 0 .2em 0 .2em;
    padding: 0 .2em 0 .2em;
    width: 4em;
    height: 4em;
    background-color: red;
    border-radius: 50%;
    border: none;
    color: white;
    box-shadow: 0 8px 0 rgb(183,9,0), 
      0 15px 20px rgba(0,0,0,.35);
    text-transform: uppercase;
    transition: .4s all ease-in;
    outline: none; 
    cursor: pointer;
    text-align: center;
    -webkit-user-select: none;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
  }

  .center {
    margin-top: 6vh;
    text-align: center;
  }

  .pos-abs {
    position: absolute;
  }

  .body0 {
    font-family: 'SoukouMincho';
    padding: 4vh 10vw 5vh 10vw;
    overflow: scroll;
  }

  .body1 {
    font-size: 1.5em;
  }

  .body0 h2 {
    font-size: 1.5em;
  }

  .titlecontainer {
    width: 100%;
    text-align: center;
    font-size: 2em;
    margin-bottom: 4vh;
  }

  #title {
    margin: 0;
    width: 60%;
    font-size: 1em;
    background: none;
    color: white;
    border: none;
    border-bottom: 1px solid orange;
  }

  .slidecontainer {
    margin: 3em 0 3em 0;
    font-size: 1.2em;
    width: 100%; /* Width of the outside container */
    text-align: right;
  }

  .slidecontainer label {
    margin-right: 1em;
    width: 9em;
  }

  .slidecontainer input {
    width: calc(95% - 10em);
    min-width: 10em;
  }

  .slidecontainer input[type="text"], .slidecontainer input[type="number"] {
    width: calc(100% - 10em);
    min-width: 10em;
    font-size: 1.2em;
    background: none;
    color: white;
    border: none;
    border-bottom: 1px solid orange;
  }

  .slidecontainer datalist {
    display: flex;
    float: right;
    justify-content: space-between;
    color: lawngreen;
    width: calc(95% - 7em);
    min-width: 10em;
  }

  #input1 .slidecontainer input {
    width: calc(100% - 10em);
  }

  #input1 .slidecontainer datalist {
    width: calc(100% - 7em);
  }

  .hazard-background {
    height: 1vh;
    color: white;
    margin: .2em 0 .2em 0;
    background-image: repeating-linear-gradient(
      -55deg,
      #000,
      #000 .5vw,
      orange .5vw,
      orange 1vw
    );
  }

  .hazard-border {
    border: 10px solid pink;
    border-image: repeating-linear-gradient(
      -55deg,
      #000,
      #000 .5vw,
      orange .5vw,
      orange 1vw
    ) 10;
  }

  .slider-green {
    -webkit-appearance: none;
    width: 50%;
    height: 15px;
    background: #000;
    outline: none;
    border: 5px solid lawngreen;
    border-radius: 8px;
  }

  /* for chrome/safari */
  .slider-green::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 60px;
    background: #000;
    cursor: pointer;
    border: 5px solid lawngreen;
    border-radius: 4px;
  }

  /*button:hover {*/
  .pressed {
    padding-top: 3px;
    transform: translateY(4px);
    box-shadow: 0 4px 0 rgb(183,0,0),
      0 8px 6px rgba(0,0,0,.45);
  }

  .hazard-btm-div {
    width: fit-content;
    display: inline-block;
    padding: 1em 2em 2em 2em;
  }

  .flap1, .flap2 {
    display: inline-block;
    position: absolute;
    width: 10em;
    height: 10em;
    margin: .5em 0 0 .5em;
    background-color: rgba(255, 255, 255, .15);
    backdrop-filter: blur(2px);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
    z-index: 1;
    transform: translateZ(1px);
    transform-origin: 0 0;
    transition: transform 1s 1.5s;
  }

  .flap2 {
    width: 7.5em;
  }

  .flap1:hover, .flap2:hover {
    transform: rotateX(170deg);
    transition: transform 1s ease;
  }

  /* for firefox */
  .slider::-moz-range-thumb {
    width: 20px;
    height: 60px;
    background: #000;
    cursor: pointer;
    border: 5px solid lawngreen;
    border-radius: 4px;
  }

  /* The slider itself */
  .slider {
    -webkit-appearance: none;  /* Override default CSS styles */
    appearance: none;
    width: 100%; /* Full-width */
    height: 25px; /* Specified height */
    background: #d3d3d3; /* Grey background */
    outline: none; /* Remove outline */
    opacity: 0.7; /* Set transparency (for mouse-over effects on hover) */
    -webkit-transition: .2s; /* 0.2 seconds transition on hover */
    transition: opacity .2s;
  }

  /* Mouse-over effects */
  .slider:hover {
    opacity: 1; /* Fully shown on mouse-over */
  }

  /* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge) and -moz- (Firefox) to override default look) */
  .slider::-webkit-slider-thumb {
    -webkit-appearance: none; /* Override default look */
    appearance: none;
    width: 25px; /* Set a specific slider handle width */
    height: 25px; /* Slider handle height */
    background: #04AA6D; /* Green background */
    cursor: pointer; /* Cursor on hover */
  }

  .slider::-moz-range-thumb {
    width: 25px; /* Set a specific slider handle width */
    height: 25px; /* Slider handle height */
    background: #04AA6D; /* Green background */
    cursor: pointer; /* Cursor on hover */
  }

  .square {
    font-family: 'Azeret Mono';
    position: absolute;
    margin: 0;
    padding: .5vh;
    height: 35vh;
    width: 35vh;
    text-align: center;
    color: black;
    background-color: #6cfeb5;
  }

  .square-flash {
    animation: blinkingBackground 1s infinite;
  }

  @keyframes blinkingBackground {
    0%    { background-color: #6cfeb5;}
    8%   { background-color: #000;}
    16%    { background-color: #6cfeb5;}
    25%   { background-color: #000;}
    33%    { background-color: #6cfeb5;}
    42%   { background-color: #000;}
    50%   { background-color: #6cfeb5;}
    60%   { background-color: #000;}
    68%    { background-color: #6cfeb5;}
    75%   { background-color: #000;}
    83%    { background-color: #6cfeb5;}
    92%   { background-color: #000;}
    100%  { background-color: #6cfeb5;}
  }

  .square h3 {
    font-size: 6vh;
    margin: 0;
  }

  .square h2 {
    font-size: 14vh;
  }

  .box {
    margin: 0;
    padding: 0;
    height: 35vh;
    width: 35vh;
    border-width: .32em;
    border-style: solid;
    border-color: orange;
  }

  .melchior {
    padding: 1vh 0 0 1vh;
    position: fixed;
    top: 50vh;
    left: calc(50vw + 12.5vh);
    transform: rotate(300deg);
  }

  .balthasar {
    padding: 0 0 0 1vh;
    position: fixed;
    top: 4vh;
    left: calc(50vw - 17.5vh);
  }

  .balthasar h2 {
    margin: 0;
    margin-bottom: calc(12vh);
  }

  .casper {
    padding: 0 0 1vh 1vh;
    position: fixed;
    top: 50vh;
    left: calc(50vw - 47.5vh);
    transform: rotate(60deg);
  }

  .circle {
    position: fixed;
    top: 20vh;
    left: calc(50vw - 30vh);
    height: 60vh;
    width: 60vh;
    border-width: .08em;
    border-radius: 50%;
    border-style: solid;
    border-color: orange;
    text-align: center;
    font-weight: bold;
    font-size: 4em;
    margin: 0;
    padding: 0;
  }

  .magi {
    /*position: absolute;*/
    margin-top: calc(30vh - .6em);
  }

  .left-col {
    position: fixed;
    left: 5vw;
    top: 4vh;
    width: calc(45vw - 17.5vh - 3vw);
  }

  .right-col {
    position: fixed;
    right: 5vw;
    top: 4vh;
    width: calc(45vw - 17.5vh - 3vw);
  }

  .t-border {
    margin: .1em;
    padding: 0;
    width: 100%;
    height: .2em;
    border-radius: 1em;
    border-style: solid;
    border-color: #6cfeb5;
  }

  .b-border {
    display: inline-block;
    margin: 0 .1em 0 .1em;
    padding: 0;
    width: .2em;
    height: 2em;
    border-radius: 1em;
    border-style: solid;
    border-color: red;
  }

  .code {
    padding-left: 1em;
  }

  .code h3 {
    margin: 0;
    margin-bottom: .2em;
    font-size: 2em;
  }

  .status {
    margin-top: 1em;
    margin-left: auto; 
    margin-right: .2vw;
    width: fit-content;
    border-color: red;
    border-radius: .1em;
    border-style: solid;
    text-align: center;
    color: red;
    font-family: 'SoukouMincho';
  }

  .status h3 {
    margin: .04em;
    padding: .2em;
    font-size: 2em;
    border-color: red;
    border-radius: .1em;
    border-style: solid;
  }

  .t1 {
    width: 100%;
    text-align: center;
  }

  .t1 h2 {
    font-family: 'SoukouMincho';
    margin: 0;
    padding-top: .1em;
  }

  .t2 {
    width: 100%;
    text-align: center;
  }

  .t2 h2 {
    font-family: 'SoukouMincho';
    margin: 0;
    padding-top: .1em;
  }

  @media only screen and (orientation:portrait) {
    .square {
      padding: .5%;
      width: 25vw;
      height: 25vw;
    }

    .square h3 {
      font-size: 4vw;
    }

    .square h2 {
      font-size: 10vw;
    }

    .box {
      height: 25vw;
      width: 25vw;
    }

    .melchior {
      padding: 1vw 0 0 1vw;
      left: 62.5vw;
    }

    .balthasar {
      top: max(calc((100vh - 60vw)/2 - 25vw + 4vh), 4vh);
      padding: 0 0 0 1vw;
      left: 37.5vw;
    }

    .balthasar h2 {
      margin-bottom: 8vw;
    }

    .casper {
      padding: 0 0 1vw 1vw;
      left: 7.5vw;
    }

    .circle {
      top: calc((100vh - 60vw)/2);
      left: 20vw;
      width:60vw;
      height: 60vw;
      font-size: 10vw;
    }

    .magi {
      margin-top: calc(30vw - .6em);
    }

    .left-col {
      width: 29.5vw;
    }

    .right-col {
        width: 28vw;
    }
  }

  .tweet-button {
    display: inline-block;
    width: 55px;
    height: 21px;
    background-image: url(http://platform.twitter.com/widgets/images/tweet.dfbf1dd98bad9f5b5addd80494650dca.png);
    background-position: 0 0;
  }
  .tweet-button:hover {
    background-position: 0 -21px;
  }
  '''
