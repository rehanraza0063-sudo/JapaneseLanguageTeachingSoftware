from flask import Flask, render_template_string

app = Flask(__name__)

# ============================================================
# JAPANESE VOCABULARY DATA
# ============================================================

vocabulary = [

    # Greetings
    ("こんにちは", "こんにちは", "konnichiwa", "Hello", "Greetings"),
    ("おはよう", "おはよう", "ohayou", "Good morning", "Greetings"),
    ("こんばんは", "こんばんは", "konbanwa", "Good evening", "Greetings"),
    ("ありがとう", "ありがとう", "arigatou", "Thank you", "Greetings"),
    ("すみません", "すみません", "sumimasen", "Excuse me / Sorry", "Greetings"),
    ("さようなら", "さようなら", "sayounara", "Goodbye", "Greetings"),
    ("おやすみ", "おやすみ", "oyasumi", "Good night", "Greetings"),
    ("はじめまして", "はじめまして", "hajimemashite", "Nice to meet you", "Greetings"),

    # People
    ("わたし", "わたし", "watashi", "I / Me", "People"),
    ("あなた", "あなた", "anata", "You", "People"),
    ("ともだち", "ともだち", "tomodachi", "Friend", "People"),
    ("せんせい", "せんせい", "sensei", "Teacher", "People"),
    ("がくせい", "がくせい", "gakusei", "Student", "People"),
    ("おとこのこ", "おとこのこ", "otokonoko", "Boy", "People"),
    ("おんなのこ", "おんなのこ", "onnanoko", "Girl", "People"),
    ("ひと", "ひと", "hito", "Person", "People"),

    # Food
    ("ごはん", "ごはん", "gohan", "Rice / Meal", "Food"),
    ("みず", "みず", "mizu", "Water", "Food"),
    ("おちゃ", "おちゃ", "ocha", "Tea", "Food"),
    ("りんご", "りんご", "ringo", "Apple", "Food"),
    ("すし", "すし", "sushi", "Sushi", "Food"),
    ("たまご", "たまご", "tamago", "Egg", "Food"),
    ("パン", "ぱん", "pan", "Bread", "Food"),
    ("さかな", "さかな", "sakana", "Fish", "Food"),

    # Places
    ("いえ", "いえ", "ie", "House / Home", "Places"),
    ("がっこう", "がっこう", "gakkou", "School", "Places"),
    ("えき", "えき", "eki", "Station", "Places"),
    ("びょういん", "びょういん", "byouin", "Hospital", "Places"),
    ("みせ", "みせ", "mise", "Shop / Store", "Places"),
    ("こうえん", "こうえん", "kouen", "Park", "Places"),
    ("としょかん", "としょかん", "toshokan", "Library", "Places"),
    ("にほん", "にほん", "nihon", "Japan", "Places"),

    # Common verbs
    ("たべる", "たべる", "taberu", "To eat", "Verbs"),
    ("のむ", "のむ", "nomu", "To drink", "Verbs"),
    ("みる", "みる", "miru", "To see / watch", "Verbs"),
    ("きく", "きく", "kiku", "To listen / ask", "Verbs"),
    ("はなす", "はなす", "hanasu", "To speak", "Verbs"),
    ("よむ", "よむ", "yomu", "To read", "Verbs"),
    ("かく", "かく", "kaku", "To write", "Verbs"),
    ("かう", "かう", "kau", "To buy", "Verbs"),
    ("いく", "いく", "iku", "To go", "Verbs"),
    ("くる", "くる", "kuru", "To come", "Verbs"),

    # Objects
    ("ほん", "ほん", "hon", "Book", "Objects"),
    ("えんぴつ", "えんぴつ", "enpitsu", "Pencil", "Objects"),
    ("つくえ", "つくえ", "tsukue", "Desk", "Objects"),
    ("いす", "いす", "isu", "Chair", "Objects"),
    ("でんわ", "でんわ", "denwa", "Telephone", "Objects"),
    ("かばん", "かばん", "kaban", "Bag", "Objects"),
    ("くるま", "くるま", "kuruma", "Car", "Objects"),
    ("じてんしゃ", "じてんしゃ", "jitensha", "Bicycle", "Objects"),

    # Useful words
    ("はい", "はい", "hai", "Yes", "Useful"),
    ("いいえ", "いいえ", "iie", "No", "Useful"),
    ("なに", "なに", "nani", "What", "Useful"),
    ("どこ", "どこ", "doko", "Where", "Useful"),
    ("いつ", "いつ", "itsu", "When", "Useful"),
    ("だれ", "だれ", "dare", "Who", "Useful"),
    ("なぜ", "なぜ", "naze", "Why", "Useful"),
    ("だいじょうぶ", "だいじょうぶ", "daijoubu", "Okay / All right", "Useful")
]


# ============================================================
# HTML
# ============================================================

HTML = """

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Japanese Vocabulary Teacher</title>


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
            #fff7ed,
            #ffedd5
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

    max-width: 1150px;

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

    background: #ea580c;

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
   VOCABULARY DISPLAY
   ============================================================ */

.japanese {

    font-size: 65px;

    margin: 20px;

    color: #111827;
}

.hiragana {

    font-size: 24px;

    color: #6b7280;

    margin-bottom: 8px;
}

.romaji {

    font-size: 25px;

    font-weight: bold;

    color: #ea580c;

    margin-bottom: 10px;
}

.meaning {

    font-size: 28px;

    font-weight: bold;

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

    background: #ea580c;

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
   CATEGORY BUTTONS
   ============================================================ */

.categories {

    display: flex;

    justify-content: center;

    gap: 8px;

    flex-wrap: wrap;

    margin-bottom: 25px;
}

.category {

    background: white;

    color: #374151;

    border: 2px solid #fed7aa;

    padding: 10px 18px;

    border-radius: 20px;

    cursor: pointer;
}

.category.active {

    background: #ea580c;

    color: white;
}


/* ============================================================
   VOCABULARY GRID
   ============================================================ */

.vocabulary-grid {

    display: grid;

    grid-template-columns:
        repeat(auto-fit, minmax(170px, 1fr));

    gap: 14px;
}

.word-card {

    background: white;

    padding: 20px;

    border-radius: 15px;

    text-align: center;

    cursor: pointer;

    box-shadow:
        0 4px 12px rgba(0,0,0,0.08);

    transition: 0.2s;
}

.word-card:hover {

    transform: translateY(-5px);

    box-shadow:
        0 8px 18px rgba(0,0,0,0.15);
}

.word-japanese {

    font-size: 35px;

    margin-bottom: 7px;
}

.word-romaji {

    color: #ea580c;

    font-weight: bold;
}

.word-meaning {

    margin-top: 5px;

    color: #4b5563;
}


/* ============================================================
   QUIZ
   ============================================================ */

.quiz-word {

    font-size: 65px;

    margin: 25px;
}

.options {

    max-width: 650px;

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

    background: #ffedd5;
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

.practice-word {

    font-size: 65px;

    margin: 25px;
}

.practice-input {

    width: 320px;

    padding: 14px;

    border: 2px solid #d1d5db;

    border-radius: 10px;

    text-align: center;

    font-size: 18px;

    outline: none;
}

.practice-input:focus {

    border-color: #ea580c;
}


/* ============================================================
   INFO
   ============================================================ */

.info {

    background: #fff7ed;

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

    .japanese,
    .quiz-word,
    .practice-word {

        font-size: 48px;
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

    <h1>🇯🇵 Japanese Vocabulary Teacher</h1>

    <p>
        Learn useful Japanese words,
        pronunciation and meanings
    </p>

</header>



<div class="container">


<!-- ============================================================
     TABS
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
     LEARN
     ============================================================ -->

<div id="learn"
     class="section active">


    <div class="card">

        <h2>📚 Learn Vocabulary</h2>

        <p>
            Select a word to learn.
        </p>


        <div id="learnJapanese"
             class="japanese">

            こんにちは

        </div>


        <div id="learnHiragana"
             class="hiragana">

            こんにちは

        </div>


        <div id="learnRomaji"
             class="romaji">

            konnichiwa

        </div>


        <div id="learnMeaning"
             class="meaning">

            Hello

        </div>


        <button onclick="speakWord()">

            🔊 Hear Japanese

        </button>


        <button
            class="secondary"
            onclick="randomWord()">

            🔄 Random Word

        </button>


        <div class="info">

            💡 Tip:
            Listen to the pronunciation and
            repeat the word aloud.

        </div>

    </div>



    <!-- CATEGORIES -->

    <div class="categories">

        <button
            class="category active"
            onclick="filterCategory('All', this)">

            All

        </button>

        <button
            class="category"
            onclick="filterCategory('Greetings', this)">

            👋 Greetings

        </button>

        <button
            class="category"
            onclick="filterCategory('People', this)">

            👤 People

        </button>

        <button
            class="category"
            onclick="filterCategory('Food', this)">

            🍱 Food

        </button>

        <button
            class="category"
            onclick="filterCategory('Places', this)">

            🏫 Places

        </button>

        <button
            class="category"
            onclick="filterCategory('Verbs', this)">

            🏃 Verbs

        </button>

        <button
            class="category"
            onclick="filterCategory('Objects', this)">

            📦 Objects

        </button>

        <button
            class="category"
            onclick="filterCategory('Useful', this)">

            ⭐ Useful

        </button>

    </div>



    <!-- VOCABULARY GRID -->

    <div id="vocabularyGrid"
         class="vocabulary-grid">

    </div>

</div>



<!-- ============================================================
     QUIZ
     ============================================================ -->

<div id="quiz"
     class="section">


    <div class="card">

        <h2>🎯 Vocabulary Quiz</h2>

        <p>
            Choose the correct English meaning.
        </p>


        <div id="quizWord"
             class="quiz-word">

            こんにちは

        </div>


        <div id="quizRomaji"
             class="romaji">

            konnichiwa

        </div>


        <div id="options"
             class="options">

        </div>


        <div id="quizResult"
             class="result">

        </div>


        <div class="score">

            🏆 Score:
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
     PRACTICE
     ============================================================ -->

<div id="practice"
     class="section">


    <div class="card">

        <h2>✍️ Practice Mode</h2>

        <p>
            Type the English meaning of the word.
        </p>


        <div id="practiceWord"
             class="practice-word">

            こんにちは

        </div>


        <div id="practiceRomaji"
             class="romaji">

            konnichiwa

        </div>


        <input
            id="practiceInput"
            class="practice-input"
            type="text"
            placeholder="Type English meaning"
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



<footer>

    🇯🇵 Japanese Vocabulary Teacher

    <br>

    Built with Python + Flask

</footer>



<script>


// ============================================================
// DATA
// ============================================================

const vocabulary = {{ vocabulary | tojson }};


// ============================================================
// VARIABLES
// ============================================================

let currentWord = vocabulary[0];

let quizWord = vocabulary[0];

let practiceWord = vocabulary[0];

let currentCategory = "All";

let score = 0;


// ============================================================
// SHOW SECTION
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
// SELECT WORD
// ============================================================

function selectWord(word) {

    currentWord = word;


    document
        .getElementById("learnJapanese")
        .innerText = word[0];


    document
        .getElementById("learnHiragana")
        .innerText = word[1];


    document
        .getElementById("learnRomaji")
        .innerText = word[2];


    document
        .getElementById("learnMeaning")
        .innerText = word[3];

}


// ============================================================
// RANDOM WORD
// ============================================================

function randomWord() {

    let available = vocabulary;


    if (currentCategory !== "All") {

        available =
            vocabulary.filter(
                word =>
                    word[4] === currentCategory
            );

    }


    const randomIndex =
        Math.floor(
            Math.random() * available.length
        );


    selectWord(
        available[randomIndex]
    );

}


// ============================================================
// CATEGORY FILTER
// ============================================================

function filterCategory(category, button) {

    currentCategory = category;


    document
        .querySelectorAll(".category")
        .forEach(function(item) {

            item.classList.remove("active");

        });


    button.classList.add("active");


    displayVocabulary();

}


// ============================================================
// DISPLAY VOCABULARY
// ============================================================

function displayVocabulary() {

    const grid =
        document.getElementById(
            "vocabularyGrid"
        );


    grid.innerHTML = "";


    let words = vocabulary;


    if (currentCategory !== "All") {

        words =
            vocabulary.filter(
                word =>
                    word[4] === currentCategory
            );

    }


    words.forEach(function(word) {

        const card =
            document.createElement("div");


        card.className = "word-card";


        card.innerHTML = `

            <div class="word-japanese">
                ${word[0]}
            </div>

            <div>
                ${word[1]}
            </div>

            <div class="word-romaji">
                ${word[2]}
            </div>

            <div class="word-meaning">
                ${word[3]}
            </div>

        `;


        card.onclick = function() {

            selectWord(word);

            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });

        };


        grid.appendChild(card);

    });

}


// ============================================================
// JAPANESE SPEECH
// ============================================================

function speakWord() {

    if (!("speechSynthesis" in window)) {

        alert(
            "Your browser does not support speech."
        );

        return;

    }


    const speech =
        new SpeechSynthesisUtterance(
            currentWord[0]
        );


    speech.lang = "ja-JP";

    speech.rate = 0.75;


    window.speechSynthesis.speak(speech);

}


// ============================================================
// QUIZ
// ============================================================

function nextQuestion() {

    const randomIndex =
        Math.floor(
            Math.random() * vocabulary.length
        );


    quizWord =
        vocabulary[randomIndex];


    document
        .getElementById("quizWord")
        .innerText =
        quizWord[0];


    document
        .getElementById("quizRomaji")
        .innerText =
        quizWord[2];


    document
        .getElementById("quizResult")
        .innerText = "";


    let answers = [
        quizWord[3]
    ];


    while (answers.length < 4) {

        const random =
            vocabulary[
                Math.floor(
                    Math.random() *
                    vocabulary.length
                )
            ][3];


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


    if (answer === quizWord[3]) {

        result.innerText =
            "✅ Correct! " +
            quizWord[0] +
            " = " +
            quizWord[3];


        score++;


        document
            .getElementById("score")
            .innerText =
            score;

    }

    else {

        result.innerText =
            "❌ Incorrect! Correct answer: " +
            quizWord[3];

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
            Math.random() * vocabulary.length
        );


    practiceWord =
        vocabulary[randomIndex];


    document
        .getElementById("practiceWord")
        .innerText =
        practiceWord[0];


    document
        .getElementById("practiceRomaji")
        .innerText =
        practiceWord[2];


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


    const correct =
        practiceWord[3]
            .toLowerCase();


    const result =
        document
            .getElementById(
                "practiceResult"
            );


    if (input === correct) {

        result.innerText =
            "🎉 Correct! " +
            practiceWord[0] +
            " = " +
            practiceWord[3];

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
// INITIALIZE
// ============================================================

displayVocabulary();

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
        vocabulary=vocabulary
    )


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 65)
    print("🇯🇵 JAPANESE VOCABULARY TEACHER")
    print("=" * 65)
    print()
    print("Server started successfully!")
    print()
    print("Open this URL in your browser:")
    print("http://localhost:8024")
    print()
    print("Press CTRL + C to stop the server.")
    print("=" * 65)
    print()

    app.run(
        host="127.0.0.1",
        port=8024,
        debug=True
    )
