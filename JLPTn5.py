from flask import Flask, render_template_string, request, jsonify
import random

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JLPT N5 Practice</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background: #f4f7fb;
            color: #222;
        }

        header {
            background: linear-gradient(135deg, #d62828, #8e0000);
            color: white;
            padding: 25px;
            text-align: center;
        }

        header h1 {
            font-size: 32px;
            margin-bottom: 8px;
        }

        header p {
            opacity: 0.9;
        }

        nav {
            background: white;
            padding: 12px;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            position: sticky;
            top: 0;
            z-index: 10;
        }

        nav button {
            border: none;
            background: #eeeeee;
            padding: 10px 15px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
        }

        nav button:hover {
            background: #d62828;
            color: white;
        }

        .container {
            max-width: 1100px;
            margin: auto;
            padding: 25px;
        }

        .section {
            display: none;
        }

        .section.active {
            display: block;
        }

        .hero {
            background: white;
            padding: 30px;
            border-radius: 18px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            margin-bottom: 25px;
        }

        .hero h2 {
            color: #d62828;
            margin-bottom: 10px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 18px;
        }

        .card {
            background: white;
            padding: 22px;
            border-radius: 16px;
            box-shadow: 0 3px 12px rgba(0,0,0,0.08);
            cursor: pointer;
            transition: 0.2s;
        }

        .card:hover {
            transform: translateY(-4px);
        }

        .card h3 {
            margin-bottom: 8px;
            color: #333;
        }

        .icon {
            font-size: 38px;
            margin-bottom: 10px;
        }

        .practice-box {
            background: white;
            padding: 30px;
            border-radius: 18px;
            margin-top: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            text-align: center;
        }

        .japanese {
            font-size: 70px;
            margin: 20px;
            color: #d62828;
            font-weight: bold;
        }

        .meaning {
            font-size: 22px;
            margin: 15px;
        }

        .btn {
            background: #d62828;
            color: white;
            border: none;
            padding: 12px 22px;
            margin: 7px;
            border-radius: 10px;
            cursor: pointer;
            font-weight: bold;
        }

        .btn:hover {
            background: #a51d1d;
        }

        .btn.secondary {
            background: #333;
        }

        .options {
            display: grid;
            grid-template-columns: repeat(2, minmax(150px, 1fr));
            gap: 12px;
            max-width: 600px;
            margin: 20px auto;
        }

        .option {
            background: #f0f0f0;
            border: 2px solid #ddd;
            padding: 15px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 18px;
        }

        .option:hover {
            border-color: #d62828;
        }

        .correct {
            background: #b7efc5 !important;
            border-color: green !important;
        }

        .wrong {
            background: #ffb3b3 !important;
            border-color: red !important;
        }

        .progress-container {
            background: #ddd;
            border-radius: 20px;
            height: 20px;
            margin: 15px 0;
            overflow: hidden;
        }

        .progress-bar {
            height: 100%;
            background: #d62828;
            width: 0%;
            transition: 0.4s;
        }

        .stat {
            background: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        }

        .stat h2 {
            color: #d62828;
            font-size: 32px;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .question {
            font-size: 22px;
            margin: 20px;
            font-weight: bold;
        }

        .reading-text {
            background: #fafafa;
            border-left: 5px solid #d62828;
            padding: 20px;
            text-align: left;
            line-height: 2;
            margin: 20px 0;
            border-radius: 8px;
        }

        .result {
            font-size: 24px;
            font-weight: bold;
            margin: 20px;
        }

        footer {
            text-align: center;
            padding: 30px;
            margin-top: 30px;
            color: #777;
        }

        @media(max-width:600px) {
            .options {
                grid-template-columns: 1fr;
            }

            .japanese {
                font-size: 55px;
            }

            nav button {
                font-size: 12px;
            }
        }
    </style>
</head>

<body>

<header>
    <h1>🇯🇵 JLPT N5 Practice</h1>
    <p>Learn Japanese • Practice • Test Yourself</p>
</header>

<nav>
    <button onclick="showSection('home')">🏠 Home</button>
    <button onclick="showSection('hiragana')">あ Hiragana</button>
    <button onclick="showSection('katakana')">カ Katakana</button>
    <button onclick="showSection('kanji')">漢 Kanji</button>
    <button onclick="showSection('vocabulary')">📚 Vocabulary</button>
    <button onclick="showSection('numbers')">🔢 Numbers</button>
    <button onclick="showSection('grammar')">📝 Grammar</button>
    <button onclick="showSection('reading')">📖 Reading</button>
    <button onclick="showSection('listening')">🔊 Listening</button>
    <button onclick="showSection('quiz')">🎯 Quiz</button>
    <button onclick="showSection('mock')">🏆 Mock Test</button>
    <button onclick="showSection('progress')">📊 Progress</button>
</nav>

<div class="container">

    <!-- HOME -->
    <section id="home" class="section active">

        <div class="hero">
            <h2>JLPT N5 Learning Dashboard</h2>
            <p>
                Build your Japanese fundamentals through vocabulary,
                grammar, kanji, reading and quizzes.
            </p>
        </div>

        <div class="cards">

            <div class="card" onclick="showSection('hiragana')">
                <div class="icon">あ</div>
                <h3>Hiragana</h3>
                <p>Practice basic Japanese sounds.</p>
            </div>

            <div class="card" onclick="showSection('katakana')">
                <div class="icon">カ</div>
                <h3>Katakana</h3>
                <p>Practice words written in Katakana.</p>
            </div>

            <div class="card" onclick="showSection('kanji')">
                <div class="icon">漢</div>
                <h3>Kanji</h3>
                <p>Learn common N5 Kanji.</p>
            </div>

            <div class="card" onclick="showSection('vocabulary')">
                <div class="icon">📚</div>
                <h3>Vocabulary</h3>
                <p>Learn useful Japanese words.</p>
            </div>

            <div class="card" onclick="showSection('grammar')">
                <div class="icon">📝</div>
                <h3>Grammar</h3>
                <p>Practice beginner grammar.</p>
            </div>

            <div class="card" onclick="showSection('reading')">
                <div class="icon">📖</div>
                <h3>Reading</h3>
                <p>Read simple Japanese passages.</p>
            </div>

            <div class="card" onclick="showSection('listening')">
                <div class="icon">🔊</div>
                <h3>Listening</h3>
                <p>Listen to browser-generated Japanese pronunciation.</p>
            </div>

            <div class="card" onclick="showSection('quiz')">
                <div class="icon">🎯</div>
                <h3>Quiz</h3>
                <p>Test your Japanese knowledge.</p>
            </div>

            <div class="card" onclick="showSection('mock')">
                <div class="icon">🏆</div>
                <h3>Mock Test</h3>
                <p>Try a mini N5-style test.</p>
            </div>

            <div class="card" onclick="showSection('progress')">
                <div class="icon">📊</div>
                <h3>Progress</h3>
                <p>Check your learning progress.</p>
            </div>

        </div>
    </section>


    <!-- HIRAGANA -->
    <section id="hiragana" class="section">
        <div class="hero">
            <h2>あ Hiragana Practice</h2>
            <p>Identify the Hiragana character.</p>
        </div>

        <div class="practice-box">
            <div class="japanese" id="hiraChar">あ</div>
            <div class="question">What is the pronunciation?</div>
            <div class="options" id="hiraOptions"></div>
            <div id="hiraResult"></div>
            <button class="btn" onclick="newHiragana()">Next</button>
        </div>
    </section>


    <!-- KATAKANA -->
    <section id="katakana" class="section">
        <div class="hero">
            <h2>カ Katakana Practice</h2>
            <p>Identify the Katakana character.</p>
        </div>

        <div class="practice-box">
            <div class="japanese" id="kataChar">ア</div>
            <div class="question">What is the pronunciation?</div>
            <div class="options" id="kataOptions"></div>
            <div id="kataResult"></div>
            <button class="btn" onclick="newKatakana()">Next</button>
        </div>
    </section>


    <!-- KANJI -->
    <section id="kanji" class="section">
        <div class="hero">
            <h2>漢 Kanji Practice</h2>
            <p>Learn common beginner Kanji.</p>
        </div>

        <div class="practice-box">
            <div class="japanese" id="kanjiChar">日</div>
            <div class="meaning" id="kanjiMeaning">Day / Sun</div>
            <button class="btn" onclick="speakJapanese(document.getElementById('kanjiChar').innerText)">
                🔊 Listen
            </button>
            <button class="btn" onclick="newKanji()">Next Kanji</button>
        </div>
    </section>


    <!-- VOCABULARY -->
    <section id="vocabulary" class="section">
        <div class="hero">
            <h2>📚 Vocabulary Practice</h2>
            <p>Learn useful N5 vocabulary.</p>
        </div>

        <div class="practice-box">
            <div class="japanese" id="vocabWord">ねこ</div>
            <div class="meaning" id="vocabMeaning">Cat</div>

            <button class="btn" onclick="speakJapanese(document.getElementById('vocabWord').innerText)">
                🔊 Listen
            </button>

            <button class="btn" onclick="newVocabulary()">Next Word</button>
        </div>
    </section>


    <!-- NUMBERS -->
    <section id="numbers" class="section">
        <div class="hero">
            <h2>🔢 Japanese Numbers</h2>
            <p>Practice Japanese numbers.</p>
        </div>

        <div class="practice-box">
            <div class="japanese" id="numberJapanese">いち</div>
            <div class="meaning" id="numberMeaning">1</div>

            <button class="btn" onclick="speakJapanese(document.getElementById('numberJapanese').innerText)">
                🔊 Listen
            </button>

            <button class="btn" onclick="newNumber()">Next Number</button>
        </div>
    </section>


    <!-- GRAMMAR -->
    <section id="grammar" class="section">

        <div class="hero">
            <h2>📝 Grammar Practice</h2>
            <p>Practice basic Japanese grammar patterns.</p>
        </div>

        <div class="practice-box">

            <div class="question" id="grammarQuestion">
                わたし ___ がくせいです。
            </div>

            <div class="options" id="grammarOptions"></div>

            <div id="grammarResult"></div>

            <button class="btn" onclick="newGrammar()">Next Question</button>

        </div>
    </section>


    <!-- READING -->
    <section id="reading" class="section">

        <div class="hero">
            <h2>📖 Reading Practice</h2>
            <p>Read a simple Japanese passage.</p>
        </div>

        <div class="practice-box">

            <div class="reading-text">
                わたしは たなかです。<br>
                20さいです。<br>
                まいにち がっこうへ いきます。<br>
                がっこうで にほんごを べんきょうします。
            </div>

            <div class="question">
                たなかさんは なんさいですか？
            </div>

            <div class="options" id="readingOptions"></div>

            <div id="readingResult"></div>

        </div>
    </section>


    <!-- LISTENING -->
    <section id="listening" class="section">

        <div class="hero">
            <h2>🔊 Listening Practice</h2>
            <p>
                Use your browser's Japanese text-to-speech feature.
            </p>
        </div>

        <div class="practice-box">

            <div class="japanese">
                こんにちは
            </div>

            <p class="meaning">
                Hello
            </p>

            <button class="btn" onclick="speakJapanese('こんにちは')">
                🔊 Play Japanese
            </button>

            <button class="btn" onclick="speakJapanese('おはようございます')">
                🔊 Good Morning
            </button>

            <button class="btn" onclick="speakJapanese('ありがとうございます')">
                🔊 Thank You
            </button>

        </div>
    </section>


    <!-- QUIZ -->
    <section id="quiz" class="section">

        <div class="hero">
            <h2>🎯 N5 Quiz</h2>
            <p>Test your Japanese knowledge.</p>
        </div>

        <div class="practice-box">

            <div class="question" id="quizQuestion">
                Start the quiz!
            </div>

            <div class="options" id="quizOptions"></div>

            <div class="result" id="quizResult"></div>

            <button class="btn" onclick="newQuiz()">Start / Next Question</button>

        </div>
    </section>


    <!-- MOCK TEST -->
    <section id="mock" class="section">

        <div class="hero">
            <h2>🏆 JLPT N5-Style Mini Mock Test</h2>
            <p>Complete 10 original practice questions.</p>
        </div>

        <div class="practice-box">

            <div class="question" id="mockQuestion">
                Click Start Mock Test
            </div>

            <div class="options" id="mockOptions"></div>

            <div class="result" id="mockResult"></div>

            <button class="btn" onclick="startMock()">
                Start Mock Test
            </button>

        </div>
    </section>


    <!-- PROGRESS -->
    <section id="progress" class="section">

        <div class="hero">
            <h2>📊 Your Progress</h2>
            <p>Your browser stores your practice statistics.</p>
        </div>

        <div class="stats">

            <div class="stat">
                <h2 id="totalAnswered">0</h2>
                <p>Questions Answered</p>
            </div>

            <div class="stat">
                <h2 id="correctAnswers">0</h2>
                <p>Correct Answers</p>
            </div>

            <div class="stat">
                <h2 id="accuracy">0%</h2>
                <p>Accuracy</p>
            </div>

            <div class="stat">
                <h2 id="mockScore">0</h2>
                <p>Best Mock Score</p>
            </div>

        </div>

        <div class="practice-box">

            <h3>Overall Progress</h3>

            <div class="progress-container">
                <div class="progress-bar" id="progressBar"></div>
            </div>

            <p id="progressText">
                Start practicing to increase your progress.
            </p>

            <button class="btn" onclick="resetProgress()">
                Reset Progress
            </button>

        </div>

    </section>

</div>

<footer>
    <p>🇯🇵 JLPT N5 Practice Website | Built with Python + Flask</p>
</footer>


<script>

const hiragana = [
    ["あ","a"],["い","i"],["う","u"],["え","e"],["お","o"],
    ["か","ka"],["き","ki"],["く","ku"],["け","ke"],["こ","ko"],
    ["さ","sa"],["し","shi"],["す","su"],["せ","se"],["そ","so"],
    ["た","ta"],["ち","chi"],["つ","tsu"],["て","te"],["と","to"],
    ["な","na"],["に","ni"],["ぬ","nu"],["ね","ne"],["の","no"],
    ["は","ha"],["ひ","hi"],["ふ","fu"],["へ","he"],["ほ","ho"],
    ["ま","ma"],["み","mi"],["む","mu"],["め","me"],["も","mo"],
    ["や","ya"],["ゆ","yu"],["よ","yo"],
    ["ら","ra"],["り","ri"],["る","ru"],["れ","re"],["ろ","ro"],
    ["わ","wa"],["を","wo"],["ん","n"]
];

const katakana = [
    ["ア","a"],["イ","i"],["ウ","u"],["エ","e"],["オ","o"],
    ["カ","ka"],["キ","ki"],["ク","ku"],["ケ","ke"],["コ","ko"],
    ["サ","sa"],["シ","shi"],["ス","su"],["セ","se"],["ソ","so"],
    ["タ","ta"],["チ","chi"],["ツ","tsu"],["テ","te"],["ト","to"],
    ["ナ","na"],["ニ","ni"],["ヌ","nu"],["ネ","ne"],["ノ","no"],
    ["ハ","ha"],["ヒ","hi"],["フ","fu"],["ヘ","he"],["ホ","ho"],
    ["マ","ma"],["ミ","mi"],["ム","mu"],["メ","me"],["モ","mo"],
    ["ヤ","ya"],["ユ","yu"],["ヨ","yo"],
    ["ラ","ra"],["リ","ri"],["ル","ru"],["レ","re"],["ロ","ro"],
    ["ワ","wa"],["ヲ","wo"],["ン","n"]
];

const kanji = [
    ["日","Day / Sun"],
    ["月","Moon / Month"],
    ["火","Fire"],
    ["水","Water"],
    ["木","Tree"],
    ["金","Gold / Money"],
    ["土","Earth"],
    ["山","Mountain"],
    ["川","River"],
    ["田","Rice field"],
    ["人","Person"],
    ["口","Mouth"],
    ["目","Eye"],
    ["耳","Ear"],
    ["手","Hand"],
    ["足","Foot"],
    ["上","Up"],
    ["下","Down"],
    ["中","Middle"],
    ["大","Big"],
    ["小","Small"],
    ["本","Book"],
    ["学","Study"],
    ["校","School"],
    ["先","Previous / Ahead"],
    ["生","Life / Student"],
    ["名","Name"],
    ["年","Year"],
    ["時","Time"]
];

const vocabulary = [
    ["ねこ","Cat"],
    ["いぬ","Dog"],
    ["みず","Water"],
    ["ごはん","Rice / Meal"],
    ["ほん","Book"],
    ["がっこう","School"],
    ["せんせい","Teacher"],
    ["がくせい","Student"],
    ["ともだち","Friend"],
    ["でんしゃ","Train"],
    ["くるま","Car"],
    ["やま","Mountain"],
    ["かわ","River"],
    ["おちゃ","Tea"],
    ["たべもの","Food"]
];

const numbers = [
    ["いち","1"],
    ["に","2"],
    ["さん","3"],
    ["よん","4"],
    ["ご","5"],
    ["ろく","6"],
    ["なな","7"],
    ["はち","8"],
    ["きゅう","9"],
    ["じゅう","10"]
];

const grammar = [
    {
        q: "わたし ___ がくせいです。",
        options: ["は","を","に","で"],
        answer: "は"
    },
    {
        q: "これ ___ ほんです。",
        options: ["は","を","が","へ"],
        answer: "は"
    },
    {
        q: "みず ___ のみます。",
        options: ["を","は","に","で"],
        answer: "を"
    },
    {
        q: "がっこう ___ いきます。",
        options: ["へ","を","が","は"],
        answer: "へ"
    },
    {
        q: "ともだち ___ べんきょうします。",
        options: ["と","を","が","へ"],
        answer: "と"
    }
];

const quizData = [
    {
        q: "「ねこ」の意味は？",
        options: ["Dog","Cat","Bird","Fish"],
        answer: "Cat"
    },
    {
        q: "「みず」の意味は？",
        options: ["Fire","Water","Tree","Mountain"],
        answer: "Water"
    },
    {
        q: "「山」の意味は？",
        options: ["River","Mountain","School","Person"],
        answer: "Mountain"
    },
    {
        q: "「いち」は何ですか？",
        options: ["1","2","3","4"],
        answer: "1"
    },
    {
        q: "「せんせい」の意味は？",
        options: ["Student","Teacher","Friend","Doctor"],
        answer: "Teacher"
    }
];

let progress = JSON.parse(localStorage.getItem("jlptProgress")) || {
    answered: 0,
    correct: 0,
    bestMock: 0
};

function saveProgress() {
    localStorage.setItem("jlptProgress", JSON.stringify(progress));
    updateProgress();
}

function updateProgress() {

    document.getElementById("totalAnswered").innerText =
        progress.answered;

    document.getElementById("correctAnswers").innerText =
        progress.correct;

    let accuracy = progress.answered === 0
        ? 0
        : Math.round((progress.correct / progress.answered) * 100);

    document.getElementById("accuracy").innerText =
        accuracy + "%";

    document.getElementById("mockScore").innerText =
        progress.bestMock + "/10";

    let percentage = Math.min(100, Math.round(
        (progress.answered / 50) * 100
    ));

    document.getElementById("progressBar").style.width =
        percentage + "%";

    document.getElementById("progressText").innerText =
        percentage + "% learning progress completed.";
}

function showSection(id) {

    document.querySelectorAll(".section").forEach(section => {
        section.classList.remove("active");
    });

    document.getElementById(id).classList.add("active");

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

    if (id === "progress") {
        updateProgress();
    }
}

function shuffle(array) {
    return [...array].sort(() => Math.random() - 0.5);
}

function createOptions(container, options, answer, resultElement) {

    container.innerHTML = "";

    shuffle(options).forEach(option => {

        let button = document.createElement("button");

        button.className = "option";
        button.innerText = option;

        button.onclick = function() {

            let all = container.querySelectorAll(".option");

            all.forEach(btn => {
                btn.disabled = true;

                if (btn.innerText === answer) {
                    btn.classList.add("correct");
                }
            });

            if (option === answer) {

                button.classList.add("correct");

                resultElement.innerHTML =
                    "<p style='color:green;font-weight:bold;'>✓ Correct!</p>";

                progress.correct++;

            } else {

                button.classList.add("wrong");

                resultElement.innerHTML =
                    "<p style='color:red;font-weight:bold;'>✗ Correct answer: "
                    + answer + "</p>";
            }

            progress.answered++;

            saveProgress();
        };

        container.appendChild(button);
    });
}


function newHiragana() {

    let item =
        hiragana[Math.floor(Math.random() * hiragana.length)];

    document.getElementById("hiraChar").innerText = item[0];

    let wrong = shuffle(
        hiragana.filter(x => x[1] !== item[1])
    ).slice(0,3).map(x => x[1]);

    createOptions(
        document.getElementById("hiraOptions"),
        [item[1], ...wrong],
        item[1],
        document.getElementById("hiraResult")
    );

    document.getElementById("hiraResult").innerHTML = "";
}


function newKatakana() {

    let item =
        katakana[Math.floor(Math.random() * katakana.length)];

    document.getElementById("kataChar").innerText = item[0];

    let wrong = shuffle(
        katakana.filter(x => x[1] !== item[1])
    ).slice(0,3).map(x => x[1]);

    createOptions(
        document.getElementById("kataOptions"),
        [item[1], ...wrong],
        item[1],
        document.getElementById("kataResult")
    );

    document.getElementById("kataResult").innerHTML = "";
}


function newKanji() {

    let item =
        kanji[Math.floor(Math.random() * kanji.length)];

    document.getElementById("kanjiChar").innerText = item[0];

    document.getElementById("kanjiMeaning").innerText =
        item[1];
}


function newVocabulary() {

    let item =
        vocabulary[Math.floor(Math.random() * vocabulary.length)];

    document.getElementById("vocabWord").innerText =
        item[0];

    document.getElementById("vocabMeaning").innerText =
        item[1];
}


function newNumber() {

    let item =
        numbers[Math.floor(Math.random() * numbers.length)];

    document.getElementById("numberJapanese").innerText =
        item[0];

    document.getElementById("numberMeaning").innerText =
        item[1];
}


let grammarIndex = 0;

function newGrammar() {

    let item =
        grammar[grammarIndex];

    document.getElementById("grammarQuestion").innerText =
        item.q;

    document.getElementById("grammarResult").innerHTML = "";

    createOptions(
        document.getElementById("grammarOptions"),
        item.options,
        item.answer,
        document.getElementById("grammarResult")
    );

    grammarIndex++;

    if (grammarIndex >= grammar.length) {
        grammarIndex = 0;
    }
}


function setupReading() {

    createOptions(
        document.getElementById("readingOptions"),
        ["20さい","18さい","25さい","30さい"],
        "20さい",
        document.getElementById("readingResult")
    );
}


let quizIndex = 0;

function newQuiz() {

    let item =
        quizData[quizIndex];

    document.getElementById("quizQuestion").innerText =
        item.q;

    document.getElementById("quizResult").innerHTML = "";

    createOptions(
        document.getElementById("quizOptions"),
        item.options,
        item.answer,
        document.getElementById("quizResult")
    );

    quizIndex++;

    if (quizIndex >= quizData.length) {
        quizIndex = 0;
    }
}


function speakJapanese(text) {

    if (!("speechSynthesis" in window)) {
        alert("Your browser does not support speech synthesis.");
        return;
    }

    let speech = new SpeechSynthesisUtterance(text);

    speech.lang = "ja-JP";
    speech.rate = 0.8;

    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(speech);
}


/* MOCK TEST */

const mockQuestions = [
    {
        q: "「いぬ」は何ですか？",
        options: ["Cat","Dog","Bird","Fish"],
        answer: "Dog"
    },
    {
        q: "「水」の読み方は？",
        options: ["みず","ひ","き","つち"],
        answer: "みず"
    },
    {
        q: "「さん」は何ですか？",
        options: ["1","2","3","4"],
        answer: "3"
    },
    {
        q: "わたし ___ がくせいです。",
        options: ["は","を","へ","で"],
        answer: "は"
    },
    {
        q: "「先生」の意味は？",
        options: ["Teacher","Student","Friend","Doctor"],
        answer: "Teacher"
    },
    {
        q: "「山」の意味は？",
        options: ["River","Mountain","School","Book"],
        answer: "Mountain"
    },
    {
        q: "「ほん」の意味は？",
        options: ["Book","Car","Food","Water"],
        answer: "Book"
    },
    {
        q: "がっこう ___ いきます。",
        options: ["へ","を","が","と"],
        answer: "へ"
    },
    {
        q: "「ねこ」の意味は？",
        options: ["Dog","Cat","Bird","Horse"],
        answer: "Cat"
    },
    {
        q: "「十」は何ですか？",
        options: ["5","8","10","20"],
        answer: "10"
    }
];

let mockIndex = 0;
let mockScore = 0;
let mockRunning = false;

function startMock() {

    mockIndex = 0;
    mockScore = 0;
    mockRunning = true;

    showMockQuestion();
}

function showMockQuestion() {

    if (mockIndex >= mockQuestions.length) {

        document.getElementById("mockQuestion").innerText =
            "🎉 Mock Test Completed!";

        document.getElementById("mockOptions").innerHTML = "";

        document.getElementById("mockResult").innerText =
            "Your Score: " + mockScore + " / 10";

        if (mockScore > progress.bestMock) {
            progress.bestMock = mockScore;
            saveProgress();
        }

        mockRunning = false;

        return;
    }

    let item = mockQuestions[mockIndex];

    document.getElementById("mockQuestion").innerText =
        "Question " + (mockIndex + 1) + ": " + item.q;

    document.getElementById("mockResult").innerText = "";

    let container =
        document.getElementById("mockOptions");

    container.innerHTML = "";

    shuffle(item.options).forEach(option => {

        let button = document.createElement("button");

        button.className = "option";
        button.innerText = option;

        button.onclick = function() {

            let all = container.querySelectorAll(".option");

            all.forEach(btn => {
                btn.disabled = true;

                if (btn.innerText === item.answer) {
                    btn.classList.add("correct");
                }
            });

            if (option === item.answer) {
                button.classList.add("correct");
                mockScore++;
            } else {
                button.classList.add("wrong");
            }

            mockIndex++;

            setTimeout(showMockQuestion, 700);
        };

        container.appendChild(button);
    });
}


function resetProgress() {

    if (confirm("Reset all JLPT progress?")) {

        progress = {
            answered: 0,
            correct: 0,
            bestMock: 0
        };

        saveProgress();

        alert("Progress reset.");
    }
}


/* INITIALIZE */

updateProgress();
newHiragana();
newKatakana();
newKanji();
newVocabulary();
newNumber();
newGrammar();
setupReading();

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/api/status")
def status():
    return jsonify({
        "status": "running",
        "app": "JLPT N5 Practice",
        "port": 8029
    })


if __name__ == "__main__":
    print("=" * 50)
    print("JLPT N5 Practice Website")
    print("Running on http://127.0.0.1:8029")
    print("=" * 50)

    app.run(
        host="127.0.0.1",
        port=8029,
        debug=True
    )
