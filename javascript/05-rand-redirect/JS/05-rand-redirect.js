// rand-redirect.js

let sites = {
1: 'http://www.zoomquilt.org',
2: 'http://www.nooooooooooooooo.com',
3: 'http://cat-bounce.com',
4: 'http://www.pointerpointer.com',
5: 'http://www.bristlr.com',
6: 'http://www.flightradar24.com',
7: 'http://www.snapbubbles.com',
8: 'http://htwins.net/scale2',
9: 'http://www.sanger.dk',
10: 'http://www.patience-is-a-virtue.org',
11: 'http://www.rainymood.com',
12: 'http://www.wwwdotcom.com',
13: 'http://www.museumoftalkingboards.com/WebOuija.html',
}

function getRandomInt() {
  return Math.floor(Math.random() * Math.floor(Object.keys(sites).length));
}

console.log(sites[getRandomInt()])
