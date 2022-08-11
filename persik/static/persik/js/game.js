let container = document.querySelector("#container");
let cat = document.querySelector("#cat");
let block = document.querySelector("#block");
let road = document.querySelector("#road");
let cloud = document.querySelector("#cloud");
let score = document.querySelector("#score");
let gameOver = document.querySelector("#gameOver");

//declaring variable for score
let interval = null;
let playerScore = 0;


//function for score
let scoreCounter = () => {
    playerScore++;
    score.innerHTML = `Score <b>${playerScore}</b>`;
}


//start Game
window.addEventListener("keydown", (start) => {
    //    console.log(start);
    if (start.code == "Space") {
        gameOver.style.display = "none";
        block.classList.add("blockActive");
        road.firstElementChild.style.animation = "roadAnimate 1.5s linear infinite";
        cloud.firstElementChild.style.animation = "cloudAnimate 20s linear infinite";

        //score
        let playerScore = 0;
        interval = setInterval(scoreCounter, 200);
    }
});


//jump Your Character
window.addEventListener("keydown", (e) => {
    //    console.log(e);

    if (e.key == "ArrowUp")
        if (cat.classList != "catActive") {
            cat.classList.add("catActive");

            //                remove class after 0.5 seconds
            setTimeout(() => {
                cat.classList.remove("catActive");
            }, 500);
        }
});

//'Game Over' if 'Character' hit The 'Block'
let result = setInterval(() => {
    let catBottom = parseInt(getComputedStyle(cat).getPropertyValue("bottom"));
    //    console.log("dinoBottom" + dinoBottom);

    let blockLeft = parseInt(getComputedStyle(block).getPropertyValue("left"));
    //    console.log("BlockLeft" + blockLeft);

    if (catBottom <= 90 && blockLeft >= 20 && blockLeft <= 100) {
        //        console.log("Game Over");

        gameOver.style.display = "block";
        block.classList.remove("blockActive");
        road.firstElementChild.style.animation = "none";
        cloud.firstElementChild.style.animation = "none";
        clearInterval(interval);
        playerScore = 0;
    }
}, 10);