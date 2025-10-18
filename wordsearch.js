const canvas = document.getElementById('wordCanvas');
const ctx = canvas.getContext('2d');
canvas.width = 300;
canvas.height = 300;

ctx.fillStyle = '#fff5f9';
ctx.fillRect(0, 0, canvas.width, canvas.height);
ctx.fillStyle = '#ff6f91';
ctx.font = '20px Poppins';

const words = ['MONEY', 'SAVE', 'CASH', 'BUDGET'];
for (let i = 0; i < 10; i++) {
  let y = 30 + i * 25;
  let randomWord = words[Math.floor(Math.random() * words.length)];
  ctx.fillText(randomWord, 20, y);
}
