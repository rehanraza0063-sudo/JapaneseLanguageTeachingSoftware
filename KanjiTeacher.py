from flask import Flask, render_template_string

app = Flask(__name__)

# ============================================================
# KANJI DATA
# ============================================================

kanji = [
    ("日", "Sun / Day", "にち / ひ", "nichi / hi"),
    ("月", "Moon / Month", "げつ / つき", "getsu / tsuki"),
    ("火", "Fire", "か / ひ", "ka / hi"),
    ("水", "Water", "すい / みず", "sui / mizu"),
    ("木", "Tree / Wood", "もく / き", "moku / ki"),
    ("金", "Gold / Money", "きん / かね", "kin / kane"),
    ("土", "Earth / Soil", "ど / つち", "do / tsuchi"),
    ("山", "Mountain", "さん / やま", "san / yama"),
    ("川", "River", "せん / かわ", "sen / kawa"),
    ("人", "Person", "じん / ひと", "jin / hito"),

    ("大", "Big", "だい / おお", "dai / oo"),
    ("小", "Small", "しょう / ちい", "shou / chii"),
    ("上", "Up / Above", "じょう / うえ", "jou / ue"),
    ("下", "Down / Below", "か / した", "ka / shita"),
    ("中", "Middle / Inside", "ちゅう / なか", "chuu / naka"),

    ("左", "Left", "さ / ひだり", "sa / hidari"),
    ("右", "Right", "う / みぎ", "u / migi"),
    ("前", "Front / Before", "ぜん / まえ", "zen / mae"),
    ("後", "Behind / After", "ご / あと", "go / ato"),
    ("外", "Outside", "がい / そと", "gai / soto"),

    ("学", "Study / Learning", "がく / まな", "gaku / mana"),
    ("校", "School", "こう", "kou"),
    ("先", "Previous / Ahead", "せん / さき", "sen / saki"),
    ("生", "Life / Student", "せい / い", "sei / i"),
    ("年", "Year", "ねん / とし", "nen / toshi"),

    ("時", "Time / Hour", "じ / とき", "ji / toki"),
    ("間", "Interval / Between", "かん / あいだ", "kan / aida"),
    ("今", "Now", "こん / いま", "kon / ima"),
    ("毎", "Every", "まい", "mai"),
    ("週", "Week", "しゅう", "shuu"),

    ("何", "What", "なに / なん", "nani / nan"),
    ("名", "Name", "めい / な", "mei / na"),
    ("友", "Friend", "ゆう / とも", "yuu / tomo"),
    ("男", "Man / Male", "だん / おとこ", "dan / otoko"),
    ("女", "Woman / Female", "じょ / おんな", "jo / onna"),

    ("子", "Child", "し / こ", "shi / ko"),
    ("父", "Father", "ふ / ちち", "fu / chichi"),
    ("母", "Mother", "ぼ / はは", "bo / haha"),
    ("家", "House / Home", "か / いえ", "ka / ie"),
    ("国", "Country", "こく / くに", "koku / kuni"),

    ("食", "Eat / Food", "しょく / た", "shoku / ta"),
    ("飲", "Drink", "いん / の", "in / no"),
    ("見", "See / Look", "けん / み", "ken / mi"),
    ("聞", "Hear / Listen", "ぶん / き", "bun / ki"),
    ("話", "Talk / Speak", "わ / はな", "wa / hana"),

    ("読", "Read", "どく / よ", "doku / yo"),
    ("書", "Write", "しょ / か", "sho / ka"),
    ("買", "Buy", "ばい / か", "bai / ka"),
    ("行", "Go", "こう / い", "kou / i"),
    ("来", "Come", "らい / く", "rai / ku")
]


# ============================================================
# HTML PAGE
# ============================================================

HTML = """

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Kanji Teacher</title>


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
            #f5f3ff,
            #ede9fe
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

    background: #7c3aed;

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
   KANJI CHARACTER
   ============================================================ */

.main-kanji {

    font-size: 140px;

    margin: 20px;

    color: #111827;

    font-family:
        "Yu Mincho",
        "Meiryo",
        serif;
}

.meaning {

    font-size: 28px;

    font-weight: bold;

    color: #7c3aed;

    margin-bottom: 10px;
}

.reading {

    font-size: 18px;

    color: #4b5563;

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

    background: #7c3aed;

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
   KANJI GRID
   ============================================================ */

.kanji-grid {

    display: grid;

    grid-template-columns:
        repeat(auto-fit, minmax(140px, 1fr));

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

.kanji-symbol {

    font-size: 48px;

    font-family:
        "Yu Mincho",
        "Meiryo",
        serif;
}

.kanji-meaning {

    color: #7c3aed;

    font-weight: bold;

    margin-top: 7px;
}


/* ============================================================
   QUIZ
   ============================================================ */

.quiz-kanji {

    font-size: 130px;

    margin: 20px;

    font-family:
        "Yu Mincho",
        "Meiryo",
        serif;
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

    background: #ede9fe;
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

.practice-kanji {

    font-size: 130px;

    margin: 20px;

    font-family:
        "Yu Mincho",
        "Meiryo",
        serif;
}

.practice-input {

    width: 300px;

    padding: 14px;

    border: 2px solid #d1d5db;

    border-radius: 10px;

    text-align: center;

    font-size: 18px;

    outline: none;
}

.practice-input:focus {

    border-color: #7c3aed;
}


/* ============================================================
   INFO
   ============================================================ */

.info {

    background: #f5f3ff;

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

    .main-kanji,
    .quiz-kanji,
    .practice-kanji {

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

    <h1>🇯🇵 Kanji Teacher</h1>

    <p>
        Learn Japanese Kanji through
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

        <h2>Learn Kanji</h2>

        <p>
            Select a Kanji to learn its meaning
            and pronunciation.
        </p>


        <div id="learnKanji"
             class="main-kanji">

            日

        </div>


        <div id="learnMeaning"
             class="meaning">

            Sun / Day

        </div>


        <div id="learnReading"
             class="reading">

            にち / ひ
            <br>
            nichi / hi

        </div>


        <button onclick="speakKanji()">

            🔊 Hear Pronunciation

        </button>


        <button
            class="secondary"
            onclick="randomKanji()">

            🔄 Random Kanji

        </button>


        <div class="info">

            Kanji are Japanese characters
            that carry meanings.
            Start with these beginner-friendly characters.

        </div>

    </div>



    <!-- KANJI GRID -->

    <div class="kanji-grid">

        {% for character, meaning, reading, romaji in kanji %}

        <div
            class="kanji-card"
            onclick="selectKanji(
                '{{ character }}',
                '{{ meaning }}',
                '{{ reading }}',
                '{{ romaji }}'
            )">

            <div class="kanji-symbol">

                {{ character }}

            </div>

            <div class="kanji-meaning">

                {{ meaning }}

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

        <h2>🎯 Kanji Quiz</h2>

        <p>
            Choose the correct meaning.
        </p>


        <div id="quizKanji"
             class="quiz-kanji">

            日

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
            Type the English meaning of the Kanji.
        </p>


        <div id="practiceKanji"
             class="practice-kanji">

            日

        </div>


        <input
            id="practiceInput"
            class="practice-input"
            type="text"
            placeholder="Example: Sun"
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

    🇯🇵 Kanji Teacher

    <br>

    Built with Python + Flask

</footer>



<script>


// ============================================================
// KANJI DATA
// ============================================================

const kanji = {{ kanji | tojson }};


// ============================================================
// VARIABLES
// ============================================================

let currentKanji = kanji[0];

let quizKanji = kanji[0];

let practiceKanji = kanji[0];

let score = 0;


// ============================================================
// SECTION SWITCH
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
// SELECT KANJI
// ============================================================

function selectKanji(
    character,
    meaning,
    reading,
    romaji
) {

    currentKanji = [
        character,
        meaning,
        reading,
        romaji
    ];


    document
        .getElementById("learnKanji")
        .innerText = character;


    document
        .getElementById("learnMeaning")
        .innerText = meaning;


    document
        .getElementById("learnReading")
        .innerHTML =
            reading +
            "<br>" +
            romaji;

}


// ============================================================
// RANDOM KANJI
// ============================================================

function randomKanji() {

    const randomIndex =
        Math.floor(
            Math.random() * kanji.length
        );


    const item =
        kanji[randomIndex];


    selectKanji(
        item[0],
        item[1],
        item[2],
        item[3]
    );

}


// ============================================================
// PRONUNCIATION
// ============================================================

function speakKanji() {

    if (!("speechSynthesis" in window)) {

        alert(
            "Your browser does not support speech."
        );

        return;

    }


    const speech =
        new SpeechSynthesisUtterance(
            currentKanji[0]
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
            Math.random() * kanji.length
        );


    quizKanji =
        kanji[randomIndex];


    document
        .getElementById("quizKanji")
        .innerText =
        quizKanji[0];


    document
        .getElementById("quizResult")
        .innerText = "";


    let answers = [
        quizKanji[1]
    ];


    while (answers.length < 4) {

        const random =
            kanji[
                Math.floor(
                    Math.random() * kanji.length
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
// CHECK QUIZ
// ============================================================

function checkAnswer(answer) {

    const result =
        document.getElementById(
            "quizResult"
        );


    if (answer === quizKanji[1]) {

        result.innerText =
            "✅ Correct! " +
            quizKanji[0] +
            " = " +
            quizKanji[1];


        score++;


        document
            .getElementById("score")
            .innerText = score;

    }

    else {

        result.innerText =
            "❌ Incorrect! Correct answer: " +
            quizKanji[1];

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
            Math.random() * kanji.length
        );


    practiceKanji =
        kanji[randomIndex];


    document
        .getElementById("practiceKanji")
        .innerText =
        practiceKanji[0];


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


    const correctAnswer =
        practiceKanji[1]
            .split("/")[0]
            .trim()
            .toLowerCase();


    if (
        input === correctAnswer ||
        practiceKanji[1]
            .toLowerCase()
            .includes(input)
    ) {

        result.innerText =
            "🎉 Correct! " +
            practiceKanji[0] +
            " = " +
            practiceKanji[1];

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
# HOME ROUTE
# ============================================================

@app.route("/")
def home():

    return render_template_string(
        HTML,
        kanji=kanji
    )


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("🇯🇵 KANJI TEACHER")
    print("=" * 60)
    print()
    print("Server started successfully!")
    print()
    print("Open this URL in your browser:")
    print("http://localhost:8023")
    print()
    print("Press CTRL + C to stop the server.")
    print("=" * 60)
    print()

    app.run(
        host="127.0.0.1",
        port=8023,
        debug=True
    )
