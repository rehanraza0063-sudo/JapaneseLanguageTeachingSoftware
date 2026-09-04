from flask import Flask, render_template_string

app = Flask(__name__)

# Japanese numbers
numbers = {
    1: ("一", "いち", "ichi"),
    2: ("二", "に", "ni"),
    3: ("三", "さん", "san"),
    4: ("四", "よん", "yon"),
    5: ("五", "ご", "go"),
    6: ("六", "ろく", "roku"),
    7: ("七", "なな", "nana"),
    8: ("八", "はち", "hachi"),
    9: ("九", "きゅう", "kyuu"),
    10: ("十", "じゅう", "juu"),
    11: ("十一", "じゅういち", "juu ichi"),
    12: ("十二", "じゅうに", "juu ni"),
    13: ("十三", "じゅうさん", "juu san"),
    14: ("十四", "じゅうよん", "juu yon"),
    15: ("十五", "じゅうご", "juu go"),
    16: ("十六", "じゅうろく", "juu roku"),
    17: ("十七", "じゅうなな", "juu nana"),
    18: ("十八", "じゅうはち", "juu hachi"),
    19: ("十九", "じゅうきゅう", "juu kyuu"),
    20: ("二十", "にじゅう", "ni juu"),
    30: ("三十", "さんじゅう", "san juu"),
    40: ("四十", "よんじゅう", "yon juu"),
    50: ("五十", "ごじゅう", "go juu"),
    60: ("六十", "ろくじゅう", "roku juu"),
    70: ("七十", "ななじゅう", "nana juu"),
    80: ("八十", "はちじゅう", "hachi juu"),
    90: ("九十", "きゅうじゅう", "kyuu juu"),
    100: ("百", "ひゃく", "hyaku")
}


def japanese_number(n):
    """Convert numbers from 1 to 100 into Japanese."""

    if n in numbers:
        return numbers[n]

    if n < 100:
        tens = n // 10
        ones = n % 10

        tens_kanji = {
            2: "二",
            3: "三",
            4: "四",
            5: "五",
            6: "六",
            7: "七",
            8: "八",
            9: "九"
        }

        tens_japanese = {
            2: "に",
            3: "さん",
            4: "よん",
            5: "ご",
            6: "ろく",
            7: "なな",
            8: "はち",
            9: "きゅう"
        }

        tens_romaji = {
            2: "ni",
            3: "san",
            4: "yon",
            5: "go",
            6: "roku",
            7: "nana",
            8: "hachi",
            9: "kyuu"
        }

        kanji = tens_kanji[tens] + "十"
        japanese = tens_japanese[tens] + "じゅう"
        romaji = tens_romaji[tens] + " juu"

        if ones != 0:
            kanji += numbers[ones][0]
            japanese += numbers[ones][1]
            romaji += " " + numbers[ones][2]

        return kanji, japanese, romaji

    return "百", "ひゃく", "hyaku"


# Generate all numbers from 1 to 100
all_numbers = {}

for i in range(1, 101):
    all_numbers[i] = japanese_number(i)


HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Japanese Numbers Teacher</title>

    <style>

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            min-height: 100vh;
            color: #222;
        }

        header {
            background: #111827;
            color: white;
            padding: 25px;
            text-align: center;
        }

        header h1 {
            font-size: 32px;
            margin-bottom: 8px;
        }

        header p {
            color: #d1d5db;
        }

        nav {
            background: white;
            display: flex;
            justify-content: center;
            gap: 10px;
            padding: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            flex-wrap: wrap;
        }

        nav button {
            border: none;
            padding: 11px 20px;
            border-radius: 8px;
            cursor: pointer;
            background: #e5e7eb;
            font-size: 15px;
            font-weight: bold;
        }

        nav button:hover {
            background: #d1d5db;
        }

        .section {
            display: none;
            max-width: 1100px;
            margin: 30px auto;
            padding: 20px;
        }

        .active {
            display: block;
        }

        .number-card {
            background: white;
            border-radius: 20px;
            padding: 40px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            max-width: 600px;
            margin: auto;
        }

        .number-value {
            font-size: 28px;
            color: #6b7280;
            margin-bottom: 15px;
        }

        .kanji {
            font-size: 100px;
            font-weight: bold;
            margin: 10px;
        }

        .japanese {
            font-size: 30px;
            color: #374151;
            margin: 15px;
        }

        .romaji {
            font-size: 23px;
            color: #6b7280;
            margin-bottom: 20px;
        }

        .buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
            margin-top: 20px;
        }

        .buttons button,
        .main-button {
            padding: 12px 20px;
            border: none;
            border-radius: 9px;
            cursor: pointer;
            background: #111827;
            color: white;
            font-size: 15px;
        }

        .buttons button:hover,
        .main-button:hover {
            background: #374151;
        }

        .random {
            background: #2563eb !important;
        }

        .speak {
            background: #059669 !important;
        }

        .reset {
            background: #dc2626 !important;
        }

        .table-container {
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
            padding: 12px;
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

        .quiz-card {
            background: white;
            max-width: 650px;
            margin: auto;
            padding: 35px;
            text-align: center;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        .quiz-number {
            font-size: 70px;
            font-weight: bold;
            margin: 20px;
        }

        .quiz-input {
            width: 100%;
            max-width: 400px;
            padding: 14px;
            font-size: 18px;
            border: 2px solid #d1d5db;
            border-radius: 8px;
            margin: 15px auto;
        }

        .quiz-input:focus {
            outline: none;
            border-color: #2563eb;
        }

        .result {
            margin-top: 15px;
            font-size: 18px;
            font-weight: bold;
        }

        .score {
            font-size: 20px;
            margin: 15px;
        }

        .range-box {
            margin-bottom: 20px;
            text-align: center;
        }

        select {
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
        }

        footer {
            text-align: center;
            padding: 25px;
            color: #6b7280;
        }

        @media (max-width: 600px) {

            header h1 {
                font-size: 25px;
            }

            .kanji {
                font-size: 75px;
            }

            .japanese {
                font-size: 24px;
            }

            .section {
                padding: 10px;
            }

            .number-card {
                padding: 25px 15px;
            }
        }

    </style>
</head>


<body>

<header>
    <h1>🇯🇵 Japanese Numbers Teacher</h1>
    <p>Learn Japanese numbers from 1 to 100</p>
</header>


<nav>

    <button onclick="showSection('learn')">
        📖 Learn Numbers
    </button>

    <button onclick="showSection('table')">
        📚 Number List
    </button>

    <button onclick="showSection('quiz')">
        🎯 Number Quiz
    </button>

</nav>


<!-- LEARN SECTION -->

<section id="learn" class="section active">

    <div class="number-card">

        <div class="number-value">
            Number: <span id="currentNumber">1</span>
        </div>

        <div class="kanji" id="kanji">
            一
        </div>

        <div class="japanese" id="japanese">
            いち
        </div>

        <div class="romaji" id="romaji">
            ichi
        </div>

        <div class="buttons">

            <button onclick="previousNumber()">
                ⬅ Previous
            </button>

            <button onclick="speakNumber()" class="speak">
                🔊 Listen
            </button>

            <button onclick="nextNumber()">
                Next ➡
            </button>

            <button onclick="randomNumber()" class="random">
                🎲 Random
            </button>

            <button onclick="resetNumber()" class="reset">
                🔄 Reset
            </button>

        </div>

    </div>

</section>


<!-- TABLE SECTION -->

<section id="table" class="section">

    <h2 style="text-align:center; margin-bottom:20px;">
        📚 Japanese Numbers 1–100
    </h2>

    <div class="table-container">

        <table>

            <thead>
                <tr>
                    <th>Number</th>
                    <th>Kanji</th>
                    <th>Japanese</th>
                    <th>Romaji</th>
                </tr>
            </thead>

            <tbody>

                {% for num, data in all_numbers.items() %}

                <tr>
                    <td>{{ num }}</td>
                    <td>{{ data[0] }}</td>
                    <td>{{ data[1] }}</td>
                    <td>{{ data[2] }}</td>
                </tr>

                {% endfor %}

            </tbody>

        </table>

    </div>

</section>


<!-- QUIZ SECTION -->

<section id="quiz" class="section">

    <div class="quiz-card">

        <h2>🎯 Japanese Number Quiz</h2>

        <p style="margin-top:10px;">
            Enter the Japanese reading in Romaji.
        </p>

        <div class="quiz-number" id="quizNumber">
            7
        </div>

        <input
            type="text"
            id="quizAnswer"
            class="quiz-input"
            placeholder="Example: nana"
            autocomplete="off"
        >

        <br>

        <button
            class="main-button"
            onclick="checkAnswer()">
            Check Answer
        </button>

        <button
            class="main-button random"
            onclick="newQuiz()">
            🎲 New Question
        </button>

        <div class="result" id="result"></div>

        <div class="score">
            Score: <span id="score">0</span>
        </div>

    </div>

</section>


<footer>
    Japanese Numbers Teacher • Built with Python & Flask 🇯🇵
</footer>


<script>

    const numbers = {{ all_numbers | tojson }};

    let currentNumber = 1;

    function updateNumber() {

        const data = numbers[currentNumber];

        document.getElementById("currentNumber").textContent = currentNumber;

        document.getElementById("kanji").textContent = data[0];

        document.getElementById("japanese").textContent = data[1];

        document.getElementById("romaji").textContent = data[2];
    }


    function nextNumber() {

        currentNumber++;

        if (currentNumber > 100) {
            currentNumber = 1;
        }

        updateNumber();
    }


    function previousNumber() {

        currentNumber--;

        if (currentNumber < 1) {
            currentNumber = 100;
        }

        updateNumber();
    }


    function randomNumber() {

        currentNumber =
            Math.floor(Math.random() * 100) + 1;

        updateNumber();
    }


    function resetNumber() {

        currentNumber = 1;

        updateNumber();
    }


    function speakNumber() {

        const japanese =
            numbers[currentNumber][1];

        const speech =
            new SpeechSynthesisUtterance(japanese);

        speech.lang = "ja-JP";

        speech.rate = 0.8;

        window.speechSynthesis.speak(speech);
    }


    function showSection(sectionId) {

        const sections =
            document.querySelectorAll(".section");

        sections.forEach(section => {
            section.classList.remove("active");
        });

        document
            .getElementById(sectionId)
            .classList.add("active");

        window.scrollTo(0, 0);
    }


    // QUIZ

    let quizNumber = 7;

    let score = 0;


    function newQuiz() {

        quizNumber =
            Math.floor(Math.random() * 100) + 1;

        document.getElementById("quizNumber")
            .textContent = quizNumber;

        document.getElementById("quizAnswer")
            .value = "";

        document.getElementById("result")
            .textContent = "";
    }


    function checkAnswer() {

        const input =
            document.getElementById("quizAnswer")
                .value
                .trim()
                .toLowerCase();

        const correct =
            numbers[quizNumber][2].toLowerCase();

        const result =
            document.getElementById("result");


        if (input === correct) {

            score++;

            document.getElementById("score")
                .textContent = score;

            result.textContent =
                "✅ Correct! Great job!";

        } else {

            result.textContent =
                "❌ Incorrect. Correct answer: " + correct;
        }

    }


    document
        .getElementById("quizAnswer")
        .addEventListener("keydown", function(event) {

            if (event.key === "Enter") {
                checkAnswer();
            }

        });


    updateNumber();

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HTML,
        all_numbers=all_numbers
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8026,
        debug=True
    )
