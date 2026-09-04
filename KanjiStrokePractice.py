from flask import Flask, render_template_string

app = Flask(__name__)

# ============================================================
# KANJI DATA
# ============================================================
# Each Kanji contains:
# character, meaning, reading, romaji, stroke count
#
# The stroke visualization uses a simple educational animation.
# ============================================================

kanji_data = [
    ("一", "One", "いち", "ichi", 1),
    ("二", "Two", "に", "ni", 2),
    ("三", "Three", "さん", "san", 3),
    ("十", "Ten", "じゅう", "juu", 2),
    ("人", "Person", "ひと", "hito", 2),
    ("大", "Big", "おお", "oo", 3),
    ("小", "Small", "ちい", "chii", 3),
    ("上", "Up / Above", "うえ", "ue", 3),
    ("下", "Down / Below", "した", "shita", 3),
    ("中", "Middle", "なか", "naka", 4),
    ("山", "Mountain", "やま", "yama", 3),
    ("川", "River", "かわ", "kawa", 3),
    ("日", "Sun / Day", "ひ", "hi", 4),
    ("月", "Moon / Month", "つき", "tsuki", 4),
    ("木", "Tree / Wood", "き", "ki", 4),
    ("水", "Water", "みず", "mizu", 4),
    ("火", "Fire", "ひ", "hi", 4),
    ("金", "Gold / Money", "かね", "kane", 8),
    ("土", "Earth / Soil", "つち", "tsuchi", 3),
    ("本", "Book / Origin", "ほん", "hon", 5)
]


# ============================================================
# HTML PAGE
# ============================================================

HTML = r"""

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Kanji Stroke Order Practice</title>


<style>

/* ============================================================
   GENERAL
   ============================================================ */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

body {

    min-height: 100vh;

    background:
        linear-gradient(
            135deg,
            #eff6ff,
            #dbeafe
        );

    color: #1f2937;
}


/* ============================================================
   HEADER
   ============================================================ */

header {

    background: #111827;

    color: white;

    text-align: center;

    padding: 30px 20px;

    box-shadow:
        0 4px 15px rgba(0,0,0,0.2);
}

header h1 {

    font-size: 36px;

    margin-bottom: 8px;
}

header p {

    color: #d1d5db;

    font-size: 16px;
}


/* ============================================================
   CONTAINER
   ============================================================ */

.container {

    max-width: 1100px;

    margin: 30px auto;

    padding: 20px;
}


/* ============================================================
   NAVIGATION
   ============================================================ */

.tabs {

    display: flex;

    justify-content: center;

    gap: 12px;

    margin-bottom: 25px;

    flex-wrap: wrap;
}

.tab {

    border: none;

    background: white;

    color: #111827;

    padding: 12px 25px;

    border-radius: 25px;

    cursor: pointer;

    font-size: 16px;

    box-shadow:
        0 4px 12px rgba(0,0,0,0.1);

    transition: 0.2s;
}

.tab:hover {

    transform: translateY(-2px);
}

.tab.active {

    background: #2563eb;

    color: white;
}


/* ============================================================
   SECTIONS
   ============================================================ */

.section {

    display: none;
}

.section.active {

    display: block;
}


/* ============================================================
   MAIN CARD
   ============================================================ */

.card {

    background: white;

    border-radius: 20px;

    padding: 35px;

    text-align: center;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.12);

    margin-bottom: 25px;
}

.card h2 {

    margin-bottom: 10px;
}


/* ============================================================
   KANJI DISPLAY
   ============================================================ */

.kanji {

    font-family:
        "Yu Mincho",
        "Meiryo",
        serif;

    font-size: 150px;

    line-height: 1;

    margin: 25px;

    color: #111827;
}

.meaning {

    font-size: 28px;

    font-weight: bold;

    color: #2563eb;

    margin-bottom: 8px;
}

.reading {

    font-size: 20px;

    color: #6b7280;

    margin-bottom: 5px;
}

.romaji {

    font-size: 18px;

    color: #374151;

    margin-bottom: 10px;
}

.strokes {

    font-size: 18px;

    color: #4b5563;

    margin: 15px;
}


/* ============================================================
   BUTTONS
   ============================================================ */

button {

    border: none;

    padding: 13px 22px;

    border-radius: 10px;

    cursor: pointer;

    font-size: 16px;

    margin: 6px;

    background: #2563eb;

    color: white;

    transition: 0.2s;
}

button:hover {

    transform: translateY(-2px);

    opacity: 0.9;
}

.secondary {

    background: #374151;
}

.green {

    background: #059669;
}


/* ============================================================
   STROKE CANVAS
   ============================================================ */

.stroke-area {

    width: 320px;

    height: 320px;

    margin: 25px auto;

    border: 3px solid #bfdbfe;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            transparent 49.7%,
            #dbeafe 50%,
            transparent 50.3%
        ),
        linear-gradient(
            transparent 49.7%,
            #dbeafe 50%,
            transparent 50.3%
        );

    display: flex;

    align-items: center;

    justify-content: center;

    position: relative;

    overflow: hidden;
}

.stroke-kanji {

    font-family:
        "Yu Mincho",
        "Meiryo",
        serif;

    font-size: 220px;

    color: #111827;

    transition: 0.4s;

    user-select: none;
}


/* ============================================================
   STROKE NUMBER
   ============================================================ */

.stroke-number {

    font-size: 22px;

    font-weight: bold;

    color: #2563eb;

    margin: 10px;
}


/* ============================================================
   GRID
   ============================================================ */

.kanji-grid {

    display: grid;

    grid-template-columns:
        repeat(auto-fit, minmax(130px, 1fr));

    gap: 12px;
}

.kanji-card {

    background: white;

    padding: 18px;

    border-radius: 15px;

    text-align: center;

    cursor: pointer;

    box-shadow:
        0 4px 12px rgba(0,0,0,0.08);

    transition: 0.2s;
}

.kanji-card:hover {

    transform: translateY(-5px);

    box-shadow:
        0 8px 18px rgba(0,0,0,0.15);
}

.small-kanji {

    font-size: 48px;

    font-family:
        "Yu Mincho",
        "Meiryo",
        serif;
}

.small-meaning {

    color: #2563eb;

    font-weight: bold;

    margin-top: 6px;
}


/* ============================================================
   QUIZ
   ============================================================ */

.quiz-character {

    font-family:
        "Yu Mincho",
        "Meiryo",
        serif;

    font-size: 130px;

    margin: 25px;
}

.quiz-question {

    font-size: 20px;

    margin-bottom: 15px;
}

.options {

    max-width: 600px;

    margin: 20px auto;

    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: 12px;
}

.option {

    background: #f3f4f6;

    color: #111827;

    border: 2px solid #e5e7eb;

    margin: 0;
}

.option:hover {

    background: #dbeafe;
}

.result {

    min-height: 30px;

    font-size: 20px;

    font-weight: bold;

    margin: 15px;
}

.score {

    font-size: 20px;

    margin: 15px;
}


/* ============================================================
   INFORMATION
   ============================================================ */

.info {

    background: #eff6ff;

    padding: 18px;

    border-radius: 12px;

    margin-top: 20px;

    line-height: 1.6;

    color: #374151;
}


/* ============================================================
   FOOTER
   ============================================================ */

footer {

    text-align: center;

    padding: 25px;

    color: #6b7280;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 600px) {

    header h1 {

        font-size: 28px;
    }

    .kanji {

        font-size: 110px;
    }

    .stroke-area {

        width: 270px;

        height: 270px;
    }

    .stroke-kanji {

        font-size: 180px;
    }

    .quiz-character {

        font-size: 90px;
    }

    .options {

        grid-template-columns: 1fr;
    }

}

</style>

</head>


<body>


<!-- ============================================================
     HEADER
     ============================================================ -->

<header>

    <h1>🇯🇵 Kanji Stroke Order Practice</h1>

    <p>
        Learn the correct order of Kanji strokes
        step by step
    </p>

</header>



<div class="container">


<!-- ============================================================
     TABS
     ============================================================ -->

<div class="tabs">

    <button
        class="tab active"
        onclick="showSection('practice', this)">

        ✍️ Stroke Practice

    </button>


    <button
        class="tab"
        onclick="showSection('learn', this)">

        📚 Kanji List

    </button>


    <button
        class="tab"
        onclick="showSection('quiz', this)">

        🎯 Stroke Quiz

    </button>

</div>



<!-- ============================================================
     PRACTICE SECTION
     ============================================================ -->

<div id="practice"
     class="section active">


    <div class="card">

        <h2>✍️ Practice Stroke Order</h2>

        <p>
            Watch the Kanji build up stroke by stroke.
        </p>


        <div class="stroke-area">

            <div id="strokeKanji"
                 class="stroke-kanji">

                一

            </div>

        </div>


        <div id="strokeNumber"
             class="stroke-number">

            Stroke 1 / 1

        </div>


        <div id="practiceMeaning"
             class="meaning">

            One

        </div>


        <div id="practiceReading"
             class="reading">

            いち

        </div>


        <div id="practiceRomaji"
             class="romaji">

            ichi

        </div>


        <div id="practiceButtons">

            <button onclick="previousStroke()">

                ← Previous

            </button>


            <button
                class="green"
                onclick="playStrokes()">

                ▶ Play Strokes

            </button>


            <button onclick="nextStroke()">

                Next →

            </button>


            <button
                class="secondary"
                onclick="resetStrokes()">

                🔄 Reset

            </button>

        </div>


        <button onclick="speakKanji()">

            🔊 Pronunciation

        </button>


        <div class="info">

            <strong>How to practice:</strong>

            <br>

            1. Watch the stroke animation.

            <br>

            2. Notice the direction of each stroke.

            <br>

            3. Try writing the Kanji yourself.

            <br>

            4. Repeat until you can write it
            without looking.

        </div>

    </div>

</div>



<!-- ============================================================
     LEARN SECTION
     ============================================================ -->

<div id="learn"
     class="section">


    <div class="card">

        <h2>📚 Beginner Kanji</h2>

        <p>
            Select a Kanji to practice its strokes.
        </p>

    </div>


    <div class="kanji-grid">

        {% for item in kanji_data %}

        <div
            class="kanji-card"
            onclick="selectKanji({{ loop.index0 }})">

            <div class="small-kanji">

                {{ item[0] }}

            </div>

            <div class="small-meaning">

                {{ item[1] }}

            </div>

        </div>

        {% endfor %}

    </div>

</div>



<!-- ============================================================
     QUIZ SECTION
     ============================================================ -->

<div id="quiz"
     class="section">


    <div class="card">

        <h2>🎯 Kanji Stroke Quiz</h2>

        <p class="quiz-question">

            How many strokes does this Kanji have?

        </p>


        <div id="quizCharacter"
             class="quiz-character">

            一

        </div>


        <div id="quizOptions"
             class="options">

        </div>


        <div id="quizResult"
             class="result">

        </div>


        <div class="score">

            🏆 Score:
            <span id="score">0</span>

        </div>


        <button onclick="nextQuiz()">

            Next Question →

        </button>


        <button
            class="secondary"
            onclick="resetScore()">

            Reset Score

        </button>

    </div>

</div>


</div>



<footer>

    🇯🇵 Kanji Stroke Order Practice

    <br>

    Built with Python + Flask

</footer>



<script>


// ============================================================
// KANJI DATA
// ============================================================

const kanjiData =
    {{ kanji_data | tojson }};


// ============================================================
// VARIABLES
// ============================================================

let currentIndex = 0;

let currentStroke = 1;

let quizItem = kanjiData[0];

let score = 0;


// ============================================================
// SECTION SWITCH
// ============================================================

function showSection(sectionName, button) {

    document
        .querySelectorAll(".section")
        .forEach(function(section) {

            section.classList.remove("active");

        });


    document
        .querySelectorAll(".tab")
        .forEach(function(tab) {

            tab.classList.remove("active");

        });


    document
        .getElementById(sectionName)
        .classList.add("active");


    button.classList.add("active");


    if (sectionName === "quiz") {

        nextQuiz();

    }

}


// ============================================================
// LOAD KANJI
// ============================================================

function loadKanji(index) {

    currentIndex = index;

    currentStroke = 1;


    const item =
        kanjiData[currentIndex];


    document
        .getElementById("strokeKanji")
        .innerText = item[0];


    document
        .getElementById("practiceMeaning")
        .innerText = item[1];


    document
        .getElementById("practiceReading")
        .innerText = item[2];


    document
        .getElementById("practiceRomaji")
        .innerText = item[3];


    updateStrokeDisplay();

}


// ============================================================
// SELECT KANJI
// ============================================================

function selectKanji(index) {

    loadKanji(index);


    showSectionDirect("practice");

}


// ============================================================
// DIRECT SECTION
// ============================================================

function showSectionDirect(sectionName) {

    document
        .querySelectorAll(".section")
        .forEach(function(section) {

            section.classList.remove("active");

        });


    document
        .getElementById(sectionName)
        .classList.add("active");


    document
        .querySelectorAll(".tab")
        .forEach(function(tab) {

            tab.classList.remove("active");

        });


    document
        .querySelector(".tab")
        .classList.add("active");

}


// ============================================================
// UPDATE STROKE
// ============================================================

function updateStrokeDisplay() {

    const item =
        kanjiData[currentIndex];


    const total =
        item[4];


    document
        .getElementById("strokeNumber")
        .innerText =
            "Stroke " +
            currentStroke +
            " / " +
            total;


    const character =
        document
            .getElementById("strokeKanji");


    character.style.opacity =
        0.35 +
        (
            currentStroke /
            total
        ) * 0.65;

}


// ============================================================
// NEXT STROKE
// ============================================================

function nextStroke() {

    const total =
        kanjiData[currentIndex][4];


    if (currentStroke < total) {

        currentStroke++;

        updateStrokeDisplay();

    }

}


// ============================================================
// PREVIOUS STROKE
// ============================================================

function previousStroke() {

    if (currentStroke > 1) {

        currentStroke--;

        updateStrokeDisplay();

    }

}


// ============================================================
// RESET
// ============================================================

function resetStrokes() {

    currentStroke = 1;

    updateStrokeDisplay();

}


// ============================================================
// PLAY STROKES
// ============================================================

function playStrokes() {

    resetStrokes();


    const total =
        kanjiData[currentIndex][4];


    let step = 1;


    const interval =
        setInterval(function() {

            if (step >= total) {

                clearInterval(interval);

                currentStroke = total;

                updateStrokeDisplay();

                return;

            }


            step++;

            currentStroke = step;

            updateStrokeDisplay();

        }, 700);

}


// ============================================================
// SPEECH
// ============================================================

function speakKanji() {

    if (!("speechSynthesis" in window)) {

        alert(
            "Your browser does not support speech."
        );

        return;

    }


    const item =
        kanjiData[currentIndex];


    const speech =
        new SpeechSynthesisUtterance(
            item[0]
        );


    speech.lang = "ja-JP";

    speech.rate = 0.7;


    window.speechSynthesis.speak(speech);

}


// ============================================================
// QUIZ
// ============================================================

function nextQuiz() {

    const randomIndex =
        Math.floor(
            Math.random() *
            kanjiData.length
        );


    quizItem =
        kanjiData[randomIndex];


    document
        .getElementById("quizCharacter")
        .innerText =
        quizItem[0];


    document
        .getElementById("quizResult")
        .innerText = "";


    let answers = [
        quizItem[4]
    ];


    while (answers.length < 4) {

        const random =
            kanjiData[
                Math.floor(
                    Math.random() *
                    kanjiData.length
                )
            ][4];


        if (!answers.includes(random)) {

            answers.push(random);

        }

    }


    answers.sort(
        () => Math.random() - 0.5
    );


    const options =
        document.getElementById(
            "quizOptions"
        );


    options.innerHTML = "";


    answers.forEach(function(answer) {

        const button =
            document.createElement("button");


        button.className = "option";


        button.innerText =
            answer + " strokes";


        button.onclick =
            function() {

                checkQuiz(answer);

            };


        options.appendChild(button);

    });

}


// ============================================================
// CHECK QUIZ
// ============================================================

function checkQuiz(answer) {

    const result =
        document.getElementById(
            "quizResult"
        );


    if (answer === quizItem[4]) {

        result.innerText =
            "✅ Correct! " +
            quizItem[0] +
            " has " +
            quizItem[4] +
            " strokes.";


        score++;


        document
            .getElementById("score")
            .innerText =
            score;

    }

    else {

        result.innerText =
            "❌ Incorrect! " +
            quizItem[0] +
            " has " +
            quizItem[4] +
            " strokes.";

    }

}


// ============================================================
// RESET SCORE
// ============================================================

function resetScore() {

    score = 0;


    document
        .getElementById("score")
        .innerText = "0";


    document
        .getElementById("quizResult")
        .innerText =
        "Score reset.";

}


// ============================================================
// INITIALIZE
// ============================================================

loadKanji(0);

nextQuiz();


</script>


</body>

</html>

"""


# ============================================================
# HOME ROUTE
# ============================================================

@app.route("/")
def home():

    return render_template_string(
        HTML,
        kanji_data=kanji_data
    )


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 65)
    print("🇯🇵 KANJI STROKE ORDER PRACTICE")
    print("=" * 65)
    print()
    print("Server started successfully!")
    print()
    print("Open this URL in your browser:")
    print("http://localhost:8025")
    print()
    print("Press CTRL + C to stop the server.")
    print("=" * 65)
    print()

    app.run(
        host="127.0.0.1",
        port=8025,
        debug=True
    )
