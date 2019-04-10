const consoleDiv = document.querySelector('#console')
const filepath = '/javascript/07-hackertyper/uchess2.txt'
let text
const getText = async () => {
  const res = await fetch(filepath)
  const data = await res.text()
  text = data
}
getText()
document.addEventListener('keypress', (evt) => {
  consoleDiv.innerText = text
})
