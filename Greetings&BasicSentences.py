from flask import Flask, render_template_string

app = Flask(__name__)

# Japanese Greetings and Basic Sentences
sentences = [
    {
        "japanese": "おはようございます",
        "romaji": "Ohayou gozaimasu",
        "english": "Good morning",
        "category": "Greetings"
    },
    {
        "japanese": "こんにちは",
        "romaji": "Konnichiwa",
        "english": "Hello / Good afternoon",
        "category": "Greetings"
    },
    {
        "japanese": "こんばんは",
        "romaji": "Konbanwa",
        "english": "Good evening",
        "category": "Greetings"
    },
    {
        "japanese": "おやすみなさい",
        "romaji": "Oyasuminasai",
        "english": "Good night",
        "category": "Greetings"
    },
    {
        "japanese": "さようなら",
        "romaji": "Sayounara",
        "english": "Goodbye",
        "category": "Greetings"
    },
    {
        "japanese": "またね",
        "romaji": "Mata ne",
        "english": "See you later",
        "category": "Greetings"
    },
    {
        "japanese": "ありがとう",
        "romaji": "Arigatou",
        "english": "Thank you",
        "category": "Basic"
    },
    {
        "japanese": "ありがとうございます",
        "romaji": "Arigatou gozaimasu",
        "english": "Thank you very much",
        "category": "Basic"
    },
    {
        "japanese": "どういたしまして",
        "romaji": "Dou itashimashite",
        "english": "You're welcome",
        "category": "Basic"
    },
    {
        "japanese": "すみません",
        "romaji": "Sumimasen",
        "english": "Excuse me / Sorry",
        "category": "Basic"
    },
    {
        "japanese": "ごめんなさい",
        "romaji": "Gomen nasai",
        "english": "I'm sorry",
        "category": "Basic"
    },
    {
        "japanese": "はい",
        "romaji": "Hai",
        "english": "Yes",
        "category": "Basic"
    },
    {
        "japanese": "いいえ",
        "romaji": "Iie",
        "english": "No",
        "category": "Basic"
    },
    {
        "japanese": "お願いします",
        "romaji": "Onegaishimasu",
        "english": "Please",
        "category": "Basic"
    },
    {
        "japanese": "元気ですか？",
        "romaji": "Genki desu ka?",
        "english": "How are you?",
        "category": "Conversation"
    },
    {
        "japanese": "元気です",
        "romaji": "Genki desu",
        "english": "I am fine",
        "category": "Conversation"
    },
    {
        "japanese": "はじめまして",
        "romaji": "Hajimemashite",
        "english": "Nice to meet you",
        "category": "Introduction"
    },
    {
        "japanese": "よろしくお願いします",
        "romaji": "Yoroshiku onegaishimasu",
        "english": "Nice to meet you / Please treat me well",
        "category": "Introduction"
    },
    {
        "japanese": "私の名前はレハンです",
        "romaji": "Watashi no namae wa Rehan desu",
        "english": "My name is Rehan",
        "category": "Introduction"
    },
    {
        "japanese": "お名前は何ですか？",
        "romaji": "Onamae wa nan desu ka?",
        "english": "What is your name?",
        "category": "Introduction"
    },
    {
        "japanese": "これは何ですか？",
        "romaji": "Kore wa nan desu ka?",
        "english": "What is this?",
        "category": "Conversation"
    },
    {
        "japanese": "どこですか？",
        "romaji": "Doko desu ka?",
        "english": "Where is it?",
        "category": "Conversation"
    },
    {
        "japanese": "わかりません",
        "romaji": "Wakarimasen",
        "english": "I don't understand",
        "category": "Conversation"
    },
    {
        "japanese": "わかりました",
        "romaji": "Wakarimashita",
        "english": "I understand",
        "category": "Conversation"
    },
    {
        "japanese": "日本語を話しますか？",
        "romaji": "Nihongo o hanashimasu ka?",
        "english": "Do you speak Japanese?",
        "category": "Conversation"
    },
    {
        "japanese": "英語を話せますか？",
        "romaji": "Eigo o hanasemasu ka?",
        "english": "Can you speak English?",
        "category": "Conversation"
    },
    {
        "japanese": "大丈夫です",
        "romaji": "Daijoubu desu",
        "english": "It's okay / I'm fine",
        "category": "Basic"
    },
    {
        "japanese": "ちょっと待ってください",
        "romaji": "Chotto matte kudasai",
        "english": "Please wait a moment",
        "category": "Conversation"
    },
    {
        "japanese": "助けてください",
        "romaji": "Tasukete kudasai",
        "english": "Please help me",
        "category": "Useful"
    },
    {
        "japanese": "いくらですか？",
        "romaji": "Ikura desu ka?",
        "english": "How much is it?",
        "category": "Useful"
    }
]


HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Japanese Greetings & Basic Sentences</title>

    <style>

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(
                135deg,
                #f8f9fa,
                #e5e7eb
            );
            min-height: 100vh;
            color: #222;
        }

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
            font-size: 16px;
        }

        nav {
            background: white;
            display: flex;
            justify-content: center;
            gap: 10px;
            padding: 15px;
            flex-wrap: wrap;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        nav button {
            border: none;
            background: #e5e7eb;
            padding: 11px 18px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            font-size: 14px;
        }

        nav button:hover {
            background: #d1d5db;
        }

        .section {
            display: none;
            max-width: 1100px;
            margin: 30px auto;
            padding: 15px;
        }

        .active {
            display: block;
        }

        /* LEARNING CARD */

        .learning-card {
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 45px 30px;
            text-align: center;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        .category {
            display: inline-block;
            background: #e5e7eb;
            padding: 7px 15px;
            border-radius: 20px;
            font-size: 14px;
            margin-bottom: 20px;
        }

        .counter {
            color: #6b7280;
            margin-bottom: 15px;
        }

        .japanese {
            font-size: 48px;
            font-weight: bold;
            margin: 20px 0;
        }

        .romaji {
            font-size: 25px;
            color: #374151;
            margin-bottom: 15px;
        }

        .english {
            font-size: 21px;
            color: #6b7280;
            margin-bottom: 25px;
        }

        .buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .buttons button,
        .main-button {
            border: none;
            padding: 12px 20px;
            border-radius: 9px;
            cursor: pointer;
            color: white;
            background: #111827;
            font-size: 15px;
        }

        .buttons button:hover,
        .main-button:hover {
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

        /* LIST */

        .list-container {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th,
        td {
            padding: 13px;
            text-align: center;
            border-bottom: 1px solid #ddd;
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
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        .quiz-question {
            font-size: 25px;
            margin: 20px 0;
        }

        .quiz-japanese {
            font-size: 45px;
            font-weight: bold;
            margin: 20px;
        }

        .quiz-input {
            width: 100%;
            max-width: 400px;
            padding: 14px;
            border: 2px solid #d1d5db;
            border-radius: 8px;
            font-size: 17px;
            margin: 15px auto;
        }

        .quiz-input:focus {
            outline: none;
            border-color: #2563eb;
        }

        .result {
            margin-top: 18px;
            font-size: 18px;
            font-weight: bold;
        }

        .score {
            margin-top: 15px;
            font-size: 20px;
        }

        footer {
            text-align: center;
            padding: 25px;
            color: #6b7280;
        }

        @media(max-width: 600px) {

            header h1 {
                font-size: 25px;
            }

            .japanese {
                font-size: 36px;
            }

            .romaji {
                font-size: 21px;
            }

            .learning-card {
                padding: 30px 15px;
            }

        }

    </style>

</head>


<body>


<header>

    <h1>🇯🇵 Japanese Greetings & Basic Sentences</h1>

    <p>
        Learn useful Japanese expressions for everyday conversation
    </p>

</header>


<nav>

    <button onclick="showSection('learn')">
        📖 Learn
    </button>

    <button onclick="showSection('list')">
        📚 Sentence List
    </button>

    <button onclick="showSection('quiz')">
        🎯 Quiz
    </button>

</nav>


<!-- LEARN -->

<section id="learn" class="section active">

    <div class="learning-card">

        <div class="category"
             id="category">
            Greetings
        </div>

        <div class="counter">

            Sentence
            <span id="current">
                1
            </span>
            /
            <span id="total">
                30
            </span>

        </div>

        <div class="japanese"
             id="japanese">

            おはようございます

        </div>

        <div class="romaji"
             id="romaji">

            Ohayou gozaimasu

        </div>

        <div class="english"
             id="english">

            Good morning

        </div>


        <div class="buttons">

            <button onclick="previousSentence()">
                ⬅ Previous
            </button>

            <button onclick="speakSentence()"
                    class="speak">

                🔊 Listen

            </button>

            <button onclick="nextSentence()">
                Next ➡
            </button>

            <button onclick="randomSentence()"
                    class="random">

                🎲 Random

            </button>

            <button onclick="resetSentence()"
                    class="reset">

                🔄 Reset

            </button>

        </div>

    </div>

</section>


<!-- LIST -->

<section id="list" class="section">

    <h2 style="text-align:center; margin-bottom:20px;">

        📚 Japanese Greetings & Sentences

    </h2>


    <div class="list-container">

        <table>

            <thead>

                <tr>

                    <th>#</th>
                    <th>Category</th>
                    <th>Japanese</th>
                    <th>Romaji</th>
                    <th>English</th>

                </tr>

            </thead>


            <tbody>

                {% for sentence in sentences %}

                <tr>

                    <td>
                        {{ loop.index }}
                    </td>

                    <td>
                        {{ sentence.category }}
                    </td>

                    <td>
                        {{ sentence.japanese }}
                    </td>

                    <td>
                        {{ sentence.romaji }}
                    </td>

                    <td>
                        {{ sentence.english }}
                    </td>

                </tr>

                {% endfor %}

            </tbody>

        </table>

    </div>

</section>


<!-- QUIZ -->

<section id="quiz" class="section">

    <div class="quiz-card">

        <h2>
            🎯 Japanese Sentence Quiz
        </h2>

        <p class="quiz-question">

            Translate the Japanese sentence
            into English.

        </p>


        <div class="quiz-japanese"
             id="quizJapanese">

            こんにちは

        </div>


        <input
            type="text"
            id="quizAnswer"
            class="quiz-input"
            placeholder="Type English meaning..."
            autocomplete="off"
        >


        <br>


        <button class="main-button"
                onclick="checkAnswer()">

            Check Answer

        </button>


        <button class="main-button random"
                onclick="newQuiz()">

            🎲 New Question

        </button>


        <div class="result"
             id="result">
        </div>


        <div class="score">

            Score:
            <span id="score">
                0
            </span>

        </div>

    </div>

</section>


<footer>

    Japanese Greetings Teacher
    •
    Built with Python & Flask 🇯🇵

</footer>


<script>


const sentences = {{ sentences | tojson }};


let currentIndex = 0;


/* UPDATE SENTENCE */

function updateSentence() {

    const sentence =
        sentences[currentIndex];


    document.getElementById("current")
        .textContent =
        currentIndex + 1;


    document.getElementById("total")
        .textContent =
        sentences.length;


    document.getElementById("category")
        .textContent =
        sentence.category;


    document.getElementById("japanese")
        .textContent =
        sentence.japanese;


    document.getElementById("romaji")
        .textContent =
        sentence.romaji;


    document.getElementById("english")
        .textContent =
        sentence.english;

}


/* NEXT */

function nextSentence() {

    currentIndex++;

    if (currentIndex >= sentences.length) {

        currentIndex = 0;

    }

    updateSentence();

}


/* PREVIOUS */

function previousSentence() {

    currentIndex--;

    if (currentIndex < 0) {

        currentIndex =
            sentences.length - 1;

    }

    updateSentence();

}


/* RANDOM */

function randomSentence() {

    currentIndex =
        Math.floor(
            Math.random() *
            sentences.length
        );

    updateSentence();

}


/* RESET */

function resetSentence() {

    currentIndex = 0;

    updateSentence();

}


/* JAPANESE SPEECH */

function speakSentence() {

    const japanese =
        sentences[currentIndex].japanese;


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


/* SECTIONS */

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


/* QUIZ */

let quizIndex = 0;

let score = 0;


function newQuiz() {

    quizIndex =
        Math.floor(
            Math.random() *
            sentences.length
        );


    document.getElementById(
        "quizJapanese"
    ).textContent =
        sentences[quizIndex].japanese;


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
        sentences[quizIndex].english
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
            + sentences[quizIndex].english;

    }

}


/* ENTER KEY FOR QUIZ */

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

updateSentence();

newQuiz();


</script>


</body>

</html>
"""


@app.route("/")
def home():

    return render_template_string(
        HTML,
        sentences=sentences
    )


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=8027,
        debug=True
    )
