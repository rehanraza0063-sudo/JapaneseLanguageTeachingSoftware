from flask import Flask, render_template_string

app = Flask(__name__)

# ============================================================
# KATAKANA DATA - 46 BASIC CHARACTERS
# ============================================================

katakana = [
    ("ア", "a"),
    ("イ", "i"),
    ("ウ", "u"),
    ("エ", "e"),
    ("オ", "o"),

    ("カ", "ka"),
    ("キ", "ki"),
    ("ク", "ku"),
    ("ケ", "ke"),
    ("コ", "ko"),

    ("サ", "sa"),
    ("シ", "shi"),
    ("ス", "su"),
    ("セ", "se"),
    ("ソ", "so"),

    ("タ", "ta"),
    ("チ", "chi"),
    ("ツ", "tsu"),
    ("テ", "te"),
    ("ト", "to"),

    ("ナ", "na"),
    ("ニ", "ni"),
    ("ヌ", "nu"),
    ("ネ", "ne"),
    ("ノ", "no"),

    ("ハ", "ha"),
    ("ヒ", "hi"),
    ("フ", "fu"),
    ("ヘ", "he"),
    ("ホ", "ho"),

    ("マ", "ma"),
    ("ミ", "mi"),
    ("ム", "mu"),
    ("メ", "me"),
    ("モ", "mo"),

    ("ヤ", "ya"),
    ("ユ", "yu"),
    ("ヨ", "yo"),

    ("ラ", "ra"),
    ("リ", "ri"),
    ("ル", "ru"),
    ("レ", "re"),
    ("ロ", "ro"),

    ("ワ", "wa"),
    ("ヲ", "wo"),
    ("ン", "n")
]


# ============================================================
# HTML + CSS + JAVASCRIPT
# ============================================================

HTML = """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Katakana Teacher</title>


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

    background: linear-gradient(
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
   TABS
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
   CARD
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
   MAIN CHARACTER
   ============================================================ */

.main-character {
    font-size: 130px;

    margin: 20px;

    color: #111827;
}

.main-romaji {
    font-size: 32px;

    font-weight: bold;

    color: #2563eb;

    margin-bottom: 15px;
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


/* ============================================================
   KATAKANA GRID
   ============================================================ */

.katakana-grid {
    display: grid;

    grid-template-columns:
        repeat(auto-fit, minmax(110px, 1fr));

    gap: 12px;
}

.kana-card {
    background: white;

    padding: 15px;

    border-radius: 15px;

    text-align: center;

    cursor: pointer;

    box-shadow:
        0 4px 12px rgba(0,0,0,0.08);

    transition: 0.2s;
}

.kana-card:hover {
    transform: translateY(-5px);

    box-shadow:
        0 8px 18px rgba(0,0,0,0.15);
}

.kana {
    font-size: 48px;
}

.kana-romaji {
    color: #2563eb;

    font-weight: bold;

    margin-top: 5px;
}


/* ============================================================
   QUIZ
   ============================================================ */

.quiz-character {
    font-size: 120px;

    margin: 20px;
}

.options {
    max-width: 500px;

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
   PRACTICE
   ============================================================ */

.practice-input {
    width: 250px;

    padding: 14px;

    border: 2px solid #d1d5db;

    border-radius: 10px;

    text-align: center;

    font-size: 18px;

    outline: none;
}

.practice-input:focus {
    border-color: #2563eb;
}


/* ============================================================
   INFORMATION
   ============================================================ */

.info {
    background: #eff6ff;

    padding: 15px;

    border-radius: 12px;

    margin-top: 20px;

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

    .main-character {
        font-size: 90px;
    }

    .quiz-character {
        font-size: 90px;
    }

    .options {
        grid-template-columns: 1fr;
    }

    .practice-input {
        width: 90%;
    }

}

</style>

</head>


<body>


<!-- ============================================================
     HEADER
     ============================================================ -->

<header>

    <h1>🇯🇵 Katakana Teacher</h1>

    <p>
        Learn Japanese Katakana through
        learning, quizzes and practice
    </p>

</header>



<div class="container">


<!-- ============================================================
     NAVIGATION
     ============================================================ -->

<div class="tabs">

    <button
        class="tab active"
        onclick="showSection('learn', this)">

        📚 Learn

    </button>


    <button
        class="tab"
        onclick="showSection('quiz', this)">

        🎯 Quiz

    </button>


    <button
        class="tab"
        onclick="showSection('practice', this)">

        ✍️ Practice

    </button>

</div>



<!-- ============================================================
     LEARN SECTION
     ============================================================ -->

<div id="learn"
     class="section active">


    <div class="card">

        <h2>Learn Katakana</h2>

        <p>
            Select a character to learn its pronunciation.
        </p>


        <div id="learnCharacter"
             class="main-character">

            ア

        </div>


        <div id="learnRomaji"
             class="main-romaji">

            a

        </div>


        <button onclick="speakCharacter()">

            🔊 Hear Pronunciation

        </button>


        <button
            class="secondary"
            onclick="randomCharacter()">

            🔄 Random Character

        </button>


        <div class="info">

            Katakana is commonly used for
            foreign words, names and loanwords.

        </div>

    </div>



    <!-- KATAKANA GRID -->

    <div class="katakana-grid">

        {% for char, romaji in katakana %}

        <div
            class="kana-card"
            onclick="selectCharacter('{{ char }}', '{{ romaji }}')">

            <div class="kana">

                {{ char }}

            </div>

            <div class="kana-romaji">

                {{ romaji }}

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

        <h2>🎯 Katakana Quiz</h2>

        <p>
            Choose the correct Romaji pronunciation.
        </p>


        <div id="quizCharacter"
             class="quiz-character">

            ア

        </div>


        <div id="options"
             class="options">

        </div>


        <div id="quizResult"
             class="result">

        </div>


        <div class="score">

            Score:
            <span id="score">0</span>

        </div>


        <button onclick="nextQuestion()">

            Next Question →

        </button>


        <button
            class="secondary"
            onclick="resetScore()">

            Reset Score

        </button>

    </div>

</div>



<!-- ============================================================
     PRACTICE SECTION
     ============================================================ -->

<div id="practice"
     class="section">


    <div class="card">

        <h2>✍️ Practice Mode</h2>

        <p>
            Type the Romaji pronunciation of the character.
        </p>


        <div id="practiceCharacter"
             class="quiz-character">

            ア

        </div>


        <input
            id="practiceInput"
            class="practice-input"
            type="text"
            placeholder="Type Romaji"
            autocomplete="off"
        >


        <br>


        <button onclick="checkPractice()">

            Check Answer

        </button>


        <button
            class="secondary"
            onclick="nextPractice()">

            Next →

        </button>


        <div id="practiceResult"
             class="result">

        </div>

    </div>

</div>


</div>



<!-- ============================================================
     FOOTER
     ============================================================ -->

<footer>

    🇯🇵 Katakana Teacher

    <br>

    Built with Python + Flask

</footer>



<!-- ============================================================
     JAVASCRIPT
     ============================================================ -->

<script>


// ============================================================
// KATAKANA DATA
// ============================================================

const katakana = {{ katakana | tojson }};


// ============================================================
// VARIABLES
// ============================================================

let currentCharacter = katakana[0];

let quizCharacter = katakana[0];

let practiceCharacter = katakana[0];

let score = 0;


// ============================================================
// CHANGE SECTION
// ============================================================

function showSection(sectionName, button) {

    const sections =
        document.querySelectorAll(".section");

    sections.forEach(function(section) {

        section.classList.remove("active");

    });


    const tabs =
        document.querySelectorAll(".tab");

    tabs.forEach(function(tab) {

        tab.classList.remove("active");

    });


    document
        .getElementById(sectionName)
        .classList.add("active");


    button.classList.add("active");


    if (sectionName === "quiz") {

        nextQuestion();

    }


    if (sectionName === "practice") {

        nextPractice();

    }

}


// ============================================================
// SELECT CHARACTER
// ============================================================

function selectCharacter(character, romaji) {

    currentCharacter = [
        character,
        romaji
    ];


    document
        .getElementById("learnCharacter")
        .innerText = character;


    document
        .getElementById("learnRomaji")
        .innerText = romaji;

}


// ============================================================
// RANDOM CHARACTER
// ============================================================

function randomCharacter() {

    const randomIndex =
        Math.floor(
            Math.random() * katakana.length
        );


    const random =
        katakana[randomIndex];


    selectCharacter(
        random[0],
        random[1]
    );

}


// ============================================================
// JAPANESE PRONUNCIATION
// ============================================================

function speakCharacter() {

    if (!("speechSynthesis" in window)) {

        alert(
            "Your browser does not support speech."
        );

        return;

    }


    const speech =
        new SpeechSynthesisUtterance(
            currentCharacter[0]
        );


    speech.lang = "ja-JP";

    speech.rate = 0.7;


    window.speechSynthesis.speak(speech);

}


// ============================================================
// QUIZ
// ============================================================

function nextQuestion() {

    const randomIndex =
        Math.floor(
            Math.random() * katakana.length
        );


    quizCharacter =
        katakana[randomIndex];


    document
        .getElementById("quizCharacter")
        .innerText =
        quizCharacter[0];


    document
        .getElementById("quizResult")
        .innerText = "";


    let answers = [
        quizCharacter[1]
    ];


    while (answers.length < 4) {

        const random =
            katakana[
                Math.floor(
                    Math.random() *
                    katakana.length
                )
            ][1];


        if (!answers.includes(random)) {

            answers.push(random);

        }

    }


    answers.sort(
        () => Math.random() - 0.5
    );


    const options =
        document.getElementById("options");


    options.innerHTML = "";


    answers.forEach(function(answer) {

        const button =
            document.createElement("button");


        button.className = "option";

        button.innerText = answer;


        button.onclick = function() {

            checkAnswer(answer);

        };


        options.appendChild(button);

    });

}


// ============================================================
// CHECK QUIZ ANSWER
// ============================================================

function checkAnswer(answer) {

    const result =
        document.getElementById(
            "quizResult"
        );


    if (answer === quizCharacter[1]) {

        result.innerText =
            "✅ Correct! " +
            quizCharacter[0] +
            " = " +
            quizCharacter[1];


        score++;


        document
            .getElementById("score")
            .innerText = score;

    }

    else {

        result.innerText =
            "❌ Incorrect! Correct answer: " +
            quizCharacter[1];

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
        "Score has been reset.";

}


// ============================================================
// PRACTICE
// ============================================================

function nextPractice() {

    const randomIndex =
        Math.floor(
            Math.random() * katakana.length
        );


    practiceCharacter =
        katakana[randomIndex];


    document
        .getElementById("practiceCharacter")
        .innerText =
        practiceCharacter[0];


    document
        .getElementById("practiceInput")
        .value = "";


    document
        .getElementById("practiceResult")
        .innerText = "";


    document
        .getElementById("practiceInput")
        .focus();

}


// ============================================================
// CHECK PRACTICE
// ============================================================

function checkPractice() {

    const input =
        document
            .getElementById("practiceInput")
            .value
            .trim()
            .toLowerCase();


    const result =
        document
            .getElementById("practiceResult");


    if (input === practiceCharacter[1]) {

        result.innerText =
            "🎉 Correct! " +
            practiceCharacter[0] +
            " = " +
            practiceCharacter[1];

    }

    else {

        result.innerText =
            "❌ Incorrect! Try again.";

    }

}


// ============================================================
// ENTER KEY
// ============================================================

document
    .getElementById("practiceInput")
    .addEventListener(
        "keypress",
        function(event) {

            if (event.key === "Enter") {

                checkPractice();

            }

        }
    );


// ============================================================
// START
// ============================================================

nextQuestion();

nextPractice();

</script>


</body>

</html>
"""


# ============================================================
# FLASK ROUTE
# ============================================================

@app.route("/")
def home():

    return render_template_string(
        HTML,
        katakana=katakana
    )


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 55)
    print("🇯🇵 KATAKANA TEACHER")
    print("=" * 55)
    print()
    print("Server started successfully!")
    print()
    print("Open this URL in your browser:")
    print("http://localhost:8022")
    print()
    print("Press CTRL + C to stop the server.")
    print("=" * 55)
    print()

    app.run(
        host="127.0.0.1",
        port=8022,
        debug=True
    )
