from flask import Flask, render_template_string

app = Flask(__name__)


# ============================================================
# JAPANESE VOCABULARY
# ============================================================

vocabulary = [
    {
        "japanese": "猫",
        "reading": "ねこ",
        "romaji": "neko",
        "english": "Cat",
        "category": "Animals"
    },
    {
        "japanese": "犬",
        "reading": "いぬ",
        "romaji": "inu",
        "english": "Dog",
        "category": "Animals"
    },
    {
        "japanese": "鳥",
        "reading": "とり",
        "romaji": "tori",
        "english": "Bird",
        "category": "Animals"
    },
    {
        "japanese": "魚",
        "reading": "さかな",
        "romaji": "sakana",
        "english": "Fish",
        "category": "Animals"
    },
    {
        "japanese": "学校",
        "reading": "がっこう",
        "romaji": "gakkou",
        "english": "School",
        "category": "Places"
    },
    {
        "japanese": "大学",
        "reading": "だいがく",
        "romaji": "daigaku",
        "english": "University",
        "category": "Places"
    },
    {
        "japanese": "病院",
        "reading": "びょういん",
        "romaji": "byouin",
        "english": "Hospital",
        "category": "Places"
    },
    {
        "japanese": "駅",
        "reading": "えき",
        "romaji": "eki",
        "english": "Station",
        "category": "Places"
    },
    {
        "japanese": "家",
        "reading": "いえ",
        "romaji": "ie",
        "english": "House / Home",
        "category": "Places"
    },
    {
        "japanese": "水",
        "reading": "みず",
        "romaji": "mizu",
        "english": "Water",
        "category": "Food & Drinks"
    },
    {
        "japanese": "お茶",
        "reading": "おちゃ",
        "romaji": "ocha",
        "english": "Tea",
        "category": "Food & Drinks"
    },
    {
        "japanese": "ご飯",
        "reading": "ごはん",
        "romaji": "gohan",
        "english": "Rice / Meal",
        "category": "Food & Drinks"
    },
    {
        "japanese": "魚",
        "reading": "さかな",
        "romaji": "sakana",
        "english": "Fish",
        "category": "Food & Drinks"
    },
    {
        "japanese": "肉",
        "reading": "にく",
        "romaji": "niku",
        "english": "Meat",
        "category": "Food & Drinks"
    },
    {
        "japanese": "りんご",
        "reading": "りんご",
        "romaji": "ringo",
        "english": "Apple",
        "category": "Food & Drinks"
    },
    {
        "japanese": "本",
        "reading": "ほん",
        "romaji": "hon",
        "english": "Book",
        "category": "Objects"
    },
    {
        "japanese": "電話",
        "reading": "でんわ",
        "romaji": "denwa",
        "english": "Telephone",
        "category": "Objects"
    },
    {
        "japanese": "時計",
        "reading": "とけい",
        "romaji": "tokei",
        "english": "Clock / Watch",
        "category": "Objects"
    },
    {
        "japanese": "車",
        "reading": "くるま",
        "romaji": "kuruma",
        "english": "Car",
        "category": "Transportation"
    },
    {
        "japanese": "電車",
        "reading": "でんしゃ",
        "romaji": "densha",
        "english": "Train",
        "category": "Transportation"
    },
    {
        "japanese": "自転車",
        "reading": "じてんしゃ",
        "romaji": "jitensha",
        "english": "Bicycle",
        "category": "Transportation"
    },
    {
        "japanese": "先生",
        "reading": "せんせい",
        "romaji": "sensei",
        "english": "Teacher",
        "category": "People"
    },
    {
        "japanese": "学生",
        "reading": "がくせい",
        "romaji": "gakusei",
        "english": "Student",
        "category": "People"
    },
    {
        "japanese": "友達",
        "reading": "ともだち",
        "romaji": "tomodachi",
        "english": "Friend",
        "category": "People"
    },
    {
        "japanese": "家族",
        "reading": "かぞく",
        "romaji": "kazoku",
        "english": "Family",
        "category": "People"
    },
    {
        "japanese": "今日",
        "reading": "きょう",
        "romaji": "kyou",
        "english": "Today",
        "category": "Time"
    },
    {
        "japanese": "明日",
        "reading": "あした",
        "romaji": "ashita",
        "english": "Tomorrow",
        "category": "Time"
    },
    {
        "japanese": "昨日",
        "reading": "きのう",
        "romaji": "kinou",
        "english": "Yesterday",
        "category": "Time"
    },
    {
        "japanese": "朝",
        "reading": "あさ",
        "romaji": "asa",
        "english": "Morning",
        "category": "Time"
    },
    {
        "japanese": "夜",
        "reading": "よる",
        "romaji": "yoru",
        "english": "Night",
        "category": "Time"
    },
    {
        "japanese": "大きい",
        "reading": "おおきい",
        "romaji": "ookii",
        "english": "Big",
        "category": "Adjectives"
    },
    {
        "japanese": "小さい",
        "reading": "ちいさい",
        "romaji": "chiisai",
        "english": "Small",
        "category": "Adjectives"
    },
    {
        "japanese": "新しい",
        "reading": "あたらしい",
        "romaji": "atarashii",
        "english": "New",
        "category": "Adjectives"
    },
    {
        "japanese": "古い",
        "reading": "ふるい",
        "romaji": "furui",
        "english": "Old",
        "category": "Adjectives"
    },
    {
        "japanese": "良い",
        "reading": "いい",
        "romaji": "ii",
        "english": "Good",
        "category": "Adjectives"
    },
    {
        "japanese": "悪い",
        "reading": "わるい",
        "romaji": "warui",
        "english": "Bad",
        "category": "Adjectives"
    },
    {
        "japanese": "食べる",
        "reading": "たべる",
        "romaji": "taberu",
        "english": "To eat",
        "category": "Verbs"
    },
    {
        "japanese": "飲む",
        "reading": "のむ",
        "romaji": "nomu",
        "english": "To drink",
        "category": "Verbs"
    },
    {
        "japanese": "見る",
        "reading": "みる",
        "romaji": "miru",
        "english": "To see / watch",
        "category": "Verbs"
    },
    {
        "japanese": "行く",
        "reading": "いく",
        "romaji": "iku",
        "english": "To go",
        "category": "Verbs"
    },
    {
        "japanese": "来る",
        "reading": "くる",
        "romaji": "kuru",
        "english": "To come",
        "category": "Verbs"
    },
    {
        "japanese": "読む",
        "reading": "よむ",
        "romaji": "yomu",
        "english": "To read",
        "category": "Verbs"
    },
    {
        "japanese": "書く",
        "reading": "かく",
        "romaji": "kaku",
        "english": "To write",
        "category": "Verbs"
    }
]


# ============================================================
# HTML
# ============================================================

HTML = r"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Japanese Vocabulary Flashcards</title>


<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}


body {

    font-family: Arial, sans-serif;

    background:
        linear-gradient(
            135deg,
            #f8f9fa,
            #e5e7eb
        );

    min-height: 100vh;

    color: #222;
}


/* HEADER */

header {

    background: #111827;

    color: white;

    text-align: center;

    padding: 28px 15px;

}


header h1 {

    font-size: 32px;

    margin-bottom: 8px;

}


header p {

    color: #d1d5db;

}


/* NAVIGATION */

nav {

    background: white;

    display: flex;

    justify-content: center;

    gap: 10px;

    padding: 15px;

    flex-wrap: wrap;

    box-shadow:
        0 2px 8px
        rgba(0,0,0,0.08);

}


nav button {

    border: none;

    padding: 11px 18px;

    border-radius: 8px;

    cursor: pointer;

    background: #e5e7eb;

    font-weight: bold;

    font-size: 14px;

}


nav button:hover {

    background: #d1d5db;

}


/* SECTIONS */

.section {

    display: none;

    max-width: 1100px;

    margin: 30px auto;

    padding: 15px;

}


.active {

    display: block;

}


/* FLASHCARD */

.flashcard-container {

    max-width: 700px;

    margin: auto;

    perspective: 1000px;

}


.flashcard {

    background: white;

    min-height: 430px;

    border-radius: 25px;

    box-shadow:
        0 15px 40px
        rgba(0,0,0,0.12);

    display: flex;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    text-align: center;

    padding: 40px;

    transition: 0.3s;

}


.flashcard:hover {

    transform:
        translateY(-5px);

}


.category {

    background: #e5e7eb;

    padding: 7px 16px;

    border-radius: 20px;

    font-size: 14px;

    margin-bottom: 15px;

}


.counter {

    color: #6b7280;

    margin-bottom: 15px;

}


.word {

    font-size: 80px;

    font-weight: bold;

    margin: 15px;

}


.reading {

    font-size: 28px;

    margin-bottom: 10px;

    color: #374151;

}


.romaji {

    font-size: 22px;

    color: #6b7280;

}


.meaning {

    margin-top: 20px;

    font-size: 25px;

    font-weight: bold;

    color: #2563eb;

}


.hidden {

    display: none;

}


.buttons {

    display: flex;

    justify-content: center;

    gap: 10px;

    flex-wrap: wrap;

    margin-top: 25px;

}


.buttons button {

    border: none;

    padding: 12px 19px;

    border-radius: 9px;

    cursor: pointer;

    background: #111827;

    color: white;

    font-size: 15px;

}


.buttons button:hover {

    opacity: 0.85;

}


.speak {

    background: #059669 !important;

}


.random {

    background: #2563eb !important;

}


.reset {

    background: #dc2626 !important;

}


.show {

    background: #7c3aed !important;

}


/* LIST */

.list-container {

    background: white;

    padding: 20px;

    border-radius: 15px;

    overflow-x: auto;

    box-shadow:
        0 5px 20px
        rgba(0,0,0,0.08);

}


table {

    width: 100%;

    border-collapse: collapse;

}


th,
td {

    padding: 13px;

    text-align: center;

    border-bottom:
        1px solid #ddd;

}


th {

    background: #111827;

    color: white;

}


tr:hover {

    background: #f3f4f6;

}


/* QUIZ */

.quiz-card {

    max-width: 650px;

    margin: auto;

    background: white;

    padding: 35px;

    text-align: center;

    border-radius: 20px;

    box-shadow:
        0 10px 30px
        rgba(0,0,0,0.1);

}


.quiz-word {

    font-size: 70px;

    font-weight: bold;

    margin: 25px;

}


.quiz-question {

    color: #6b7280;

    margin-bottom: 15px;

}


.quiz-input {

    width: 100%;

    max-width: 400px;

    padding: 14px;

    font-size: 17px;

    border: 2px solid #d1d5db;

    border-radius: 8px;

}


.quiz-input:focus {

    outline: none;

    border-color: #2563eb;

}


.main-button {

    border: none;

    padding: 12px 20px;

    border-radius: 9px;

    cursor: pointer;

    color: white;

    background: #111827;

    margin: 10px 5px;

    font-size: 15px;

}


.result {

    margin-top: 15px;

    font-weight: bold;

    font-size: 18px;

}


.score {

    margin-top: 15px;

    font-size: 20px;

}


/* FOOTER */

footer {

    text-align: center;

    padding: 25px;

    color: #6b7280;

}


/* MOBILE */

@media(max-width:600px) {

    header h1 {

        font-size: 25px;

    }


    .word {

        font-size: 60px;

    }


    .reading {

        font-size: 23px;

    }


    .flashcard {

        padding: 25px 15px;

    }

}

</style>

</head>


<body>


<header>

<h1>
🇯🇵 Japanese Vocabulary Flashcards
</h1>

<p>
Learn Japanese words through interactive flashcards
</p>

</header>


<nav>

<button onclick="showSection('flashcards')">
🃏 Flashcards
</button>

<button onclick="showSection('list')">
📚 Vocabulary List
</button>

<button onclick="showSection('quiz')">
🎯 Quiz
</button>

</nav>


<!-- =====================================================
     FLASHCARDS
====================================================== -->

<section id="flashcards"
         class="section active">


<div class="flashcard-container">


<div class="flashcard">


<div class="category"
     id="category">

Animals

</div>


<div class="counter">

Word
<span id="current">1</span>
/
<span id="total">45</span>

</div>


<div class="word"
     id="word">

猫

</div>


<div class="reading"
     id="reading">

ねこ

</div>


<div class="romaji"
     id="romaji">

neko

</div>


<div id="meaning"
     class="meaning hidden">

Cat

</div>


<div class="buttons">


<button onclick="previousWord()">

⬅ Previous

</button>


<button onclick="showMeaning()"
        class="show">

👀 Show Answer

</button>


<button onclick="speakWord()"
        class="speak">

🔊 Listen

</button>


<button onclick="nextWord()">

Next ➡

</button>


<button onclick="randomWord()"
        class="random">

🎲 Random

</button>


<button onclick="resetWord()"
        class="reset">

🔄 Reset

</button>


</div>


</div>

</div>

</section>


<!-- =====================================================
     VOCABULARY LIST
====================================================== -->

<section id="list"
         class="section">


<h2 style="text-align:center;
           margin-bottom:20px;">

📚 Japanese Vocabulary List

</h2>


<div class="list-container">


<table>


<thead>

<tr>

<th>#</th>

<th>Category</th>

<th>Japanese</th>

<th>Reading</th>

<th>Romaji</th>

<th>English</th>

</tr>

</thead>


<tbody>


{% for word in vocabulary %}


<tr>

<td>
{{ loop.index }}
</td>

<td>
{{ word.category }}
</td>

<td>
{{ word.japanese }}
</td>

<td>
{{ word.reading }}
</td>

<td>
{{ word.romaji }}
</td>

<td>
{{ word.english }}
</td>

</tr>


{% endfor %}


</tbody>

</table>

</div>

</section>


<!-- =====================================================
     QUIZ
====================================================== -->

<section id="quiz"
         class="section">


<div class="quiz-card">


<h2>
🎯 Vocabulary Quiz
</h2>


<p class="quiz-question">

What is the English meaning of:

</p>


<div class="quiz-word"
     id="quizWord">

猫

</div>


<input
    type="text"
    id="quizAnswer"
    class="quiz-input"
    placeholder="Type English meaning..."
    autocomplete="off"
>


<div>

<button class="main-button"
        onclick="checkAnswer()">

Check Answer

</button>


<button class="main-button random"
        onclick="newQuiz()">

🎲 New Question

</button>

</div>


<div class="result"
     id="result">
</div>


<div class="score">

Score:
<span id="score">0</span>

</div>


</div>

</section>


<footer>

Japanese Vocabulary Flashcards
•
Python + Flask 🇯🇵

</footer>


<script>


const vocabulary =
    {{ vocabulary | tojson }};


let currentIndex = 0;


/* =====================================================
   UPDATE FLASHCARD
====================================================== */

function updateCard() {

    const word =
        vocabulary[currentIndex];


    document.getElementById(
        "current"
    ).textContent =
        currentIndex + 1;


    document.getElementById(
        "total"
    ).textContent =
        vocabulary.length;


    document.getElementById(
        "category"
    ).textContent =
        word.category;


    document.getElementById(
        "word"
    ).textContent =
        word.japanese;


    document.getElementById(
        "reading"
    ).textContent =
        word.reading;


    document.getElementById(
        "romaji"
    ).textContent =
        word.romaji;


    document.getElementById(
        "meaning"
    ).textContent =
        word.english;


    document.getElementById(
        "meaning"
    ).classList.add(
        "hidden"
    );

}


/* NEXT */

function nextWord() {

    currentIndex++;

    if (
        currentIndex >=
        vocabulary.length
    ) {

        currentIndex = 0;

    }

    updateCard();

}


/* PREVIOUS */

function previousWord() {

    currentIndex--;

    if (currentIndex < 0) {

        currentIndex =
            vocabulary.length - 1;

    }

    updateCard();

}


/* RANDOM */

function randomWord() {

    currentIndex =
        Math.floor(
            Math.random() *
            vocabulary.length
        );

    updateCard();

}


/* RESET */

function resetWord() {

    currentIndex = 0;

    updateCard();

}


/* SHOW ANSWER */

function showMeaning() {

    document.getElementById(
        "meaning"
    ).classList.toggle(
        "hidden"
    );

}


/* SPEECH */

function speakWord() {

    const japanese =
        vocabulary[currentIndex]
        .reading;


    window.speechSynthesis.cancel();


    const speech =
        new SpeechSynthesisUtterance(
            japanese
        );


    speech.lang = "ja-JP";

    speech.rate = 0.8;

    speech.pitch = 1;


    window.speechSynthesis.speak(
        speech
    );

}


/* =====================================================
   NAVIGATION
====================================================== */

function showSection(sectionId) {

    const sections =
        document.querySelectorAll(
            ".section"
        );


    sections.forEach(
        section => {

            section.classList.remove(
                "active"
            );

        }
    );


    document
        .getElementById(sectionId)
        .classList.add("active");


    window.scrollTo(0, 0);

}


/* =====================================================
   QUIZ
====================================================== */

let quizIndex = 0;

let score = 0;


function newQuiz() {

    quizIndex =
        Math.floor(
            Math.random() *
            vocabulary.length
        );


    document.getElementById(
        "quizWord"
    ).textContent =
        vocabulary[quizIndex]
        .japanese;


    document.getElementById(
        "quizAnswer"
    ).value = "";


    document.getElementById(
        "result"
    ).textContent = "";

}


function checkAnswer() {

    const answer =
        document.getElementById(
            "quizAnswer"
        ).value
        .trim()
        .toLowerCase();


    const correct =
        vocabulary[quizIndex]
        .english
        .toLowerCase();


    const result =
        document.getElementById(
            "result"
        );


    if (
        answer === correct ||
        answer.includes(correct) ||
        correct.includes(answer)
    ) {

        score++;


        document.getElementById(
            "score"
        ).textContent =
            score;


        result.textContent =
            "✅ Correct! Great job!";

    }

    else {

        result.textContent =
            "❌ Incorrect! Correct answer: "
            + vocabulary[quizIndex].english;

    }

}


/* ENTER KEY */

document
    .getElementById("quizAnswer")
    .addEventListener(
        "keydown",
        function(event) {

            if (event.key === "Enter") {

                checkAnswer();

            }

        }
    );


/* INITIALIZE */

updateCard();

newQuiz();

</script>


</body>

</html>
"""


# ============================================================
# ROUTE
# ============================================================

@app.route("/")
def home():

    return render_template_string(
        HTML,
        vocabulary=vocabulary
    )


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=8028,
        debug=True
    )
