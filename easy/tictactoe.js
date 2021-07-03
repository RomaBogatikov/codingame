/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

 function analyze(arr) {
  let numOfZeroes = 0;
  let isEmpty, isX;
  for (let char of arr) {
      if (char === 'O') numOfZeroes++;
      if (char === '.') isEmpty = true;
      if (char === 'X') isX = true;
  }

  return {numOfZeroes, isEmpty, isX};
}

function printBoard() {
  for (let line of board) {
      let str = line.join('');
      console.log(str);
  }
  didPrint = true;
}

function checkLine(line) {
  const {numOfZeroes, isEmpty, isX} = analyze(line);
  if (numOfZeroes === 2 && isEmpty) {
      for (let i = 0; i < 3; i++) {
          if (line[i] === '.') line[i] = 'O'
      }
      return printBoard();
  }
}

function checkColumn(column, i) {
  const {numOfZeroes, isEmpty, isX} = analyze(column);

  if (numOfZeroes === 2 && isEmpty) {
      for (let j = 0; j < 3; j++) {
          if (column[j] === '.') {
              board[j][i] = 'O'
          }
      }
      return printBoard();
  }
}

function readInput() {
  let board = [];
  for (let i = 0; i < 3; i++) {
      const line = readline();
      board.push(line.split(''))
  }
  return board;
}

function checkDiagonal1(diagonal1) {
  const {numOfZeroes, isEmpty, isX} = analyze(diagonal1);
  if (numOfZeroes === 2 && isEmpty) {
      for (let j = 0; j < 3; j++) {
          if (diagonal1[j] === '.') {
              board[j][j] = 'O';
          }
      }
      return printBoard();
  }
}

function checkDiagonal2(diagonal2) {
  const {numOfZeroes, isEmpty, isX} = analyze(diagonal2);
  if (numOfZeroes === 2 && isEmpty) {
      for (let j = 0; j < 3; j++) {
          if (diagonal2[j] === '.') {
              board[j][2-j] = 'O';
          }
      }
      return printBoard();
  }

}



let board = readInput();
let didPrint = false;

for (let i = 0; i < 3; i++) {
  const line = board[i];
  checkLine(line);
  if (didPrint) break;
  const column = [board[0][i], board[1][i], board[2][i]];
  checkColumn(column, i);
  if (didPrint) break;
}


let diagonal1 = [board[0][0], board[1][1], board[2][2]];
checkDiagonal1(diagonal1);

let diagonal2 = [board[0][2], board[1][1], board[2][0]]
checkDiagonal2(diagonal2);

!didPrint && console.log("false");