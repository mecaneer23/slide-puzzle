const BOARD_SIZE = 3; // any int, > 2
var moves = null;
var board = null;

async function move(event) {
    let k = event.key;
    let openSpaceLocation = board.indexOf(" ");
    let moveLocation = null;
    if (k == "w" || k == "ArrowUp") {
        if (!(openSpaceLocation + BOARD_SIZE < BOARD_SIZE * BOARD_SIZE)) {
            return;
        }
        moveLocation = openSpaceLocation + BOARD_SIZE;
    } else if (k == "s" || k == "ArrowDown") {
        if (!(openSpaceLocation - BOARD_SIZE >= 0)) {
            return;
        }
        moveLocation = openSpaceLocation - BOARD_SIZE;
    } else if (k == "a" || k == "ArrowLeft") {
        if (!(
            (openSpaceLocation + 1) % BOARD_SIZE != 0
            && openSpaceLocation + 1 < BOARD_SIZE * BOARD_SIZE
        )) {
            return;
        }
        moveLocation = openSpaceLocation + 1;
    } else if (k == "d" || k == "ArrowRight") {
        if (!(openSpaceLocation % BOARD_SIZE != 0 && openSpaceLocation - 1 >= 0)) {
            return;
        }
        moveLocation = openSpaceLocation - 1;
    } else if (k == "x") {
        // continue
        moveLocation = openSpaceLocation;
    } else {
        return;
    }
    [board[openSpaceLocation], board[moveLocation]] = [board[moveLocation], board[openSpaceLocation]];
    setTimeout(() => {
        moves++;
        document.getElementById("move-counter").innerHTML = "Moves: " + moves;
        let children = document.getElementById("grid-container").children;
        for (let i = 0; i < children.length; i++) {
            children[i].innerHTML = board[i];
        }
        let sorted = [...board].sort();
        sorted.shift();
        sorted.push(" ")
        if (
            (JSON.stringify(board) === JSON.stringify([...board].sort())
            || JSON.stringify(board) === JSON.stringify(sorted))
            && moves > 0
        ) {
            setTimeout(() => {
                alert("You got it in " + moves + " moves!");
            }, 0);
            reset();
        }
    }, 0);
    return;
}

function reset() {
    document.getElementById("move-counter").innerHTML = "Moves: 0";
    let container = document.getElementById("grid-container");
    container.innerHTML = "";
    board = new Array();
    for (let i = 0; i < BOARD_SIZE * BOARD_SIZE; i++) {
        let elem = document.createElement("div");
        elem.classList.add("grid-item");
        elem.innerHTML = i == 0 ? " " : i;
        board[i] = elem.innerHTML;
        container.appendChild(elem);
    }
    let items = ["w", "a", "s", "d"];
    for (i = 0; i < 1000; i++) {
        move({key: items[items.length * Math.random() | 0]});
    }
    setTimeout(() => {
        moves = -1;
        move({key: "x"});
    }, 0);
    return;
}

window.addEventListener("keyup", move);
reset();