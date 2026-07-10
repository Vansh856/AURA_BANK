# =========================================================
# views/games_bundle.py
# Static HTML/JS game definitions to keep the main view clean
# =========================================================

SNAKE_GAME = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #0e1117; color: #2e7d32; font-family: 'Courier New', monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 0; padding: 10px; }
        #game-container { border: 3px solid #2e7d32; border-radius: 8px; background-color: #000; box-shadow: 0 0 15px #2e7d32; }
        canvas { display: block; }
        .score-board { font-size: 18px; font-weight: bold; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 2px; color: #4CAF50; }
        .controls-info { font-size: 11px; color: #888; margin-top: 8px; }
    </style>
</head>
<body>
    <div class="score-board">AURA SCORE: <span id="score">0</span></div>
    <div id="game-container"><canvas id="gameCanvas" width="480" height="300"></canvas></div>
    <div class="controls-info">Click the game box, then use Arrow Keys to Play.</div>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const scoreEl = document.getElementById("score");
        const gridSize = 10;
        let snake = [{x: 150, y: 150}];
        let dx = gridSize, dy = 0, food = {x: 0, y: 0}, score = 0, gameInterval;
        function randomFood() {
            food.x = Math.floor(Math.random() * (canvas.width / gridSize)) * gridSize;
            food.y = Math.floor(Math.random() * (canvas.height / gridSize)) * gridSize;
        }
        function drawSnake() { ctx.fillStyle = "#4CAF50"; snake.forEach(part => ctx.fillRect(part.x, part.y, gridSize - 1, gridSize - 1)); }
        function drawFood() { ctx.fillStyle = "#FF5722"; ctx.fillRect(food.x, food.y, gridSize - 1, gridSize - 1); }
        function moveSnake() {
            const head = {x: snake.x + dx, y: snake.y + dy};
            snake.unshift(head);
            if (head.x === food.x && head.y === food.y) { score += 100; scoreEl.textContent = score; randomFood(); }
            else { snake.pop(); }
        }
        function checkCollision() {
            const head = snake;
            if (head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height) return true;
            for (let i = 1; i < snake.length; i++) { if (head.x === snake[i].x && head.y === snake[i].y) return true; }
            return false;
        }
        function update() {
            if (checkCollision()) {
                clearInterval(gameInterval);
                ctx.fillStyle = "rgba(0,0,0,0.8)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = "#FF5722";
                ctx.font = "20px 'Courier New'";
                ctx.fillText("TEST TERMINATED", canvas.width/2 - 90, canvas.height/2);
                return;
            }
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawFood(); moveSnake(); drawSnake();
        }
        function changeDirection(event) {
            const keys = [2-6];
            if (keys.includes(event.keyCode)) event.preventDefault();
            if (event.keyCode === 37 && dx === 0) { dx = -gridSize; dy = 0; }
            if (event.keyCode === 38 && dy === 0) { dx = 0; dy = -gridSize; }
            if (event.keyCode === 39 && dx === 0) { dx = gridSize; dy = 0; }
            if (event.keyCode === 40 && dy === 0) { dx = 0; dy = gridSize; }
        }
        function resetGame() { snake = [{x: 150, y: 150}]; dx = gridSize; dy = 0; score = 0; scoreEl.textContent = score; randomFood(); clearInterval(gameInterval); gameInterval = setInterval(update, 80); }
        window.addEventListener("keydown", changeDirection);
        resetGame();
    </script>
</body>
</html>
"""

TIC_TAC_TOE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #0e1117; color: #4CAF50; font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 0; padding: 10px; }
        .grid { display: grid; grid-template-columns: repeat(3, 70px); grid-template-rows: repeat(3, 70px); gap: 5px; margin-top: 10px; }
        .cell { width: 70px; height: 70px; background-color: #000; border: 2px solid #2e7d32; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: bold; cursor: pointer; box-shadow: 0 0 5px #2e7d32; }
        .cell:hover { background-color: #111; }
        .status { font-size: 16px; margin-bottom: 10px; font-weight: bold; letter-spacing: 1px; }
        .cell.X { color: #4CAF50; text-shadow: 0 0 10px #4CAF50; }
        .cell.O { color: #FF5722; text-shadow: 0 0 10px #FF5722; }
    </style>
</head>
<body>
    <div class="status" id="status">YOUR TURN (X)</div>
    <div class="grid" id="grid">
        <div class="cell" onclick="makeMove(0)"></div>
        <div class="cell" onclick="makeMove(1)"></div>
        <div class="cell" onclick="makeMove(2)"></div>
        <div class="cell" onclick="makeMove(3)"></div>
        <div class="cell" onclick="makeMove(4)"></div>
        <div class="cell" onclick="makeMove(5)"></div>
        <div class="cell" onclick="makeMove(6)"></div>
        <div class="cell" onclick="makeMove(7)"></div>
        <div class="cell" onclick="makeMove(8)"></div>
    </div>
    <script>
        let board = ["", "", "", "", "", "", "", "", ""];
        let isGameActive = true;
        const statusEl = document.getElementById("status");
        const cells = document.querySelectorAll(".cell");
        function makeMove(index) {
            if (board[index] !== "" || !isGameActive) return;
            board[index] = "X";
            cells[index].textContent = "X";
            cells[index].classList.add("X");
            if (checkWin("X")) { statusEl.textContent = "YOU WIN! 🎉"; isGameActive = false; return; }
            if (board.every(cell => cell !== "")) { statusEl.textContent = "IT'S A DRAW! 🤝"; isGameActive = false; return; }
            statusEl.textContent = "AI IS THINKING...";
            isGameActive = false;
            setTimeout(aiMove, 500);
        }
        function aiMove() {
            let emptyCells = [];
            board.forEach((val, idx) => { if (val === "") emptyCells.push(idx); });
            if (emptyCells.length > 0) {
                let randomIdx = emptyCells[Math.floor(Math.random() * emptyCells.length)];
                board[randomIdx] = "O";
                cells[randomIdx].textContent = "O";
                cells[randomIdx].classList.add("O");
                if (checkWin("O")) { statusEl.textContent = "AI WINS! 🤖"; isGameActive = false; return; }
            }
            if (board.every(cell => cell !== "")) { statusEl.textContent = "IT'S A DRAW! 🤝"; isGameActive = false; return; }
            statusEl.textContent = "YOUR TURN (X)";
            isGameActive = true;
        }
        function checkWin(player) {
            const winConditions = [
                [7, 8], [9-11], [12-14],
                [9, 12], [7, 10, 13], [8, 11, 14],
                [10, 14], [8, 10, 12]
            ];
            return winConditions.some(cond => cond.every(idx => board[idx] === player));
        }
    </script>
</body>
</html>
"""

GAME_2048 = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #0e1117; color: #4CAF50; font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 0; padding: 10px; }
        .score-board { font-size: 18px; font-weight: bold; margin-bottom: 10px; letter-spacing: 2px; }
        #grid { display: grid; grid-template-columns: repeat(4, 55px); grid-template-rows: repeat(4, 55px); gap: 5px; background-color: #000; border: 2px solid #2e7d32; border-radius: 8px; padding: 5px; box-shadow: 0 0 15px #2e7d32; }
        .tile { width: 55px; height: 55px; background-color: #1a1a1a; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: bold; color: #fff; }
        .t-2 { background-color: #333; color: #4CAF50; }
        .t-4 { background-color: #444; color: #8BC34A; }
        .t-8 { background-color: #555; color: #CDDC39; }
        .t-16 { background-color: #666; color: #FFEB3B; }
        .t-32 { background-color: #777; color: #FFC107; }
        .t-64 { background-color: #888; color: #FF9800; }
        .t-128 { background-color: #999; color: #FF5722; box-shadow: 0 0 5px #FF5722; }
        .t-256 { background-color: #aaa; color: #F44336; box-shadow: 0 0 8px #F44336; }
        .t-512 { background-color: #bbb; color: #E91E63; box-shadow: 0 0 10px #E91E63; }
        .t-1024 { background-color: #ccc; color: #9C27B0; box-shadow: 0 0 12px #9C27B0; }
        .t-2048 { background-color: #ddd; color: #3F51B5; box-shadow: 0 0 15px #3F51B5; }
        .controls-info { font-size: 11px; color: #888; margin-top: 8px; }
    </style>
</head>
<body>
    <div class="score-board">SCORE: <span id="score">0</span></div>
    <div id="grid"></div>
    <div class="controls-info">Use Arrow Keys to Slide & Combine numbers.</div>
    <script>
        const gridEl = document.getElementById("grid");
        const scoreEl = document.getElementById("score");
        let board = Array(16).fill(0);
        let score = 0;
        function init() { board = Array(16).fill(0); score = 0; spawn(); spawn(); render(); }
        function spawn() {
            let empty = [];
            board.forEach((v, i) => { if (v === 0) empty.push(i); });
            if (empty.length > 0) { let idx = empty[Math.floor(Math.random() * empty.length)]; board[idx] = Math.random() < 0.9 ? 2 : 4; }
        }
        function render() {
            gridEl.innerHTML = "";
            board.forEach(val => {
                let cell = document.createElement("div");
                cell.className = "tile" + (val > 0 ? " t-" + val : "");
                cell.textContent = val > 0 ? val : "";
                gridEl.appendChild(cell);
            });
            scoreEl.textContent = score;
        }
        function slide(row) {
            let arr = row.filter(val => val);
            let missing = 4 - arr.length;
            let zeros = Array(missing).fill(0);
            return arr.concat(zeros);
        }
        function combine(row) {
            for (let i = 0; i < 3; i++) {
                if (row[i] !== 0 && row[i] === row[i+1]) { row[i] *= 2; score += row[i]; row[i+1] = 0; }
            }
            return row;
        }
        function operate(row) { row = slide(row); row = combine(row); row = slide(row); return row; }
        function move(dir) {
            let tempBoard = [...board];
            if (dir === 'left' || dir === 'right') {
                let rows = [];
                for (let i = 0; i < 16; i += 4) {
                    let r = tempBoard.slice(i, i+4);
                    if (dir === 'right') r.reverse();
                    r = operate(r);
                    if (dir === 'right') r.reverse();
                    rows.push(...r);
                }
                board = rows;
            } else {
                let cols = [];
                for (let c = 0; c < 4; c++) {
                    let col = [tempBoard[c], tempBoard[c+4], tempBoard[c+8], tempBoard[c+12]];
                    if (dir === 'down') col.reverse();
                    col = operate(col);
                    if (dir === 'down') col.reverse();
                    cols.push(col);
                }
                for (let i = 0; i < 4; i++) {
                    for (let j = 0; j < 4; j++) { board[i*4 + j] = cols[j][i]; }
                }
            }
            if (tempBoard.toString() !== board.toString()) { spawn(); render(); }
        }
        window.addEventListener("keydown", e => {
            const keys = [3-6];
            if (keys.includes(e.keyCode)) e.preventDefault();
            if (e.keyCode === 37) move('left');
            if (e.keyCode === 38) move('up');
            if (e.keyCode === 39) move('right');
            if (e.keyCode === 40) move('down');
        });
        init();
    </script>
</body>
</html>
"""

# Export dictionary mapping
GAMES = {
    "2048": GAME_2048,
    "Snake": SNAKE_GAME,
    "Tic-Tac-Toe": TIC_TAC_TOE
}