const consoleDiv = document.querySelector('#console')
const filepath = '/javascript/07-hackertyper/uchess2.txt'
let text
const getText = async () => {
  const res = await fetch(filepath)
  const data = await res.text()
  text = data
}

getText()
let textdex = 0;
document.addEventListener('keypress', (evt) => {
  consoleDiv.innertext += text.charAt(textdex;
  textdex++;
}
