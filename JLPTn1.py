from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# ============================================================
# JLPT N1 DATA
# ============================================================

KANJI = [
    {"kanji": "抽象", "reading": "ちゅうしょう", "meaning": "abstract"},
    {"kanji": "概念", "reading": "がいねん", "meaning": "concept"},
    {"kanji": "傾向", "reading": "けいこう", "meaning": "tendency"},
    {"kanji": "根拠", "reading": "こんきょ", "meaning": "basis / grounds"},
    {"kanji": "妥当", "reading": "だとう", "meaning": "valid / appropriate"},
    {"kanji": "矛盾", "reading": "むじゅん", "meaning": "contradiction"},
    {"kanji": "曖昧", "reading": "あいまい", "meaning": "ambiguous"},
    {"kanji": "顕著", "reading": "けんちょ", "meaning": "remarkable"},
    {"kanji": "著しい", "reading": "いちじるしい", "meaning": "remarkable / significant"},
    {"kanji": "促進", "reading": "そくしん", "meaning": "promotion / acceleration"},
    {"kanji": "抑制", "reading": "よくせい", "meaning": "suppression / restraint"},
    {"kanji": "排除", "reading": "はいじょ", "meaning": "elimination / exclusion"},
    {"kanji": "導入", "reading": "どうにゅう", "meaning": "introduction"},
    {"kanji": "普及", "reading": "ふきゅう", "meaning": "spread / diffusion"},
    {"kanji": "維持", "reading": "いじ", "meaning": "maintenance"},
    {"kanji": "克服", "reading": "こくふく", "meaning": "overcome"},
    {"kanji": "遂げる", "reading": "とげる", "meaning": "accomplish / achieve"},
    {"kanji": "携わる", "reading": "たずさわる", "meaning": "be involved in"},
    {"kanji": "著作", "reading": "ちょさく", "meaning": "written work"},
    {"kanji": "考慮", "reading": "こうりょ", "meaning": "consideration"},
    {"kanji": "配慮", "reading": "はいりょ", "meaning": "consideration / care"},
    {"kanji": "措置", "reading": "そち", "meaning": "measure / action"},
    {"kanji": "措定", "reading": "そてい", "meaning": "postulation"},
    {"kanji": "余儀ない", "reading": "よぎない", "meaning": "unavoidable"},
    {"kanji": "免れる", "reading": "まぬがれる", "meaning": "escape / avoid"},
    {"kanji": "伴う", "reading": "ともなう", "meaning": "accompany"},
    {"kanji": "及ぼす", "reading": "およぼす", "meaning": "exert / cause"},
    {"kanji": "著しく", "reading": "いちじるしく", "meaning": "remarkably"},
    {"kanji": "一概に", "reading": "いちがいに", "meaning": "unconditionally / generally"},
    {"kanji": "必然", "reading": "ひつぜん", "meaning": "inevitability"},
    {"kanji": "偶然", "reading": "ぐうぜん", "meaning": "coincidence"},
    {"kanji": "普遍", "reading": "ふへん", "meaning": "universal"},
    {"kanji": "相互", "reading": "そうご", "meaning": "mutual"},
    {"kanji": "獲得", "reading": "かくとく", "meaning": "acquisition"},
    {"kanji": "喪失", "reading": "そうしつ", "meaning": "loss"},
    {"kanji": "適応", "reading": "てきおう", "meaning": "adaptation"},
    {"kanji": "独自", "reading": "どくじ", "meaning": "original / unique"},
    {"kanji": "革新", "reading": "かくしん", "meaning": "innovation"},
    {"kanji": "変革", "reading": "へんかく", "meaning": "reform / transformation"},
    {"kanji": "是正", "reading": "ぜせい", "meaning": "correction / rectification"},
]

VOCAB = [
    ("あえて", "dare to / intentionally"),
    ("あらかじめ", "in advance"),
    ("おおむね", "generally / roughly"),
    ("かえって", "on the contrary"),
    ("ことごとく", "entirely / completely"),
    ("さほど", "not so much"),
    ("もっぱら", "solely / exclusively"),
    ("ひとえに", "entirely / solely"),
    ("ひいては", "and consequently"),
    ("おのずから", "naturally / spontaneously"),
    ("およそ", "approximately / generally"),
    ("かろうじて", "barely"),
    ("ことさら", "deliberately / especially"),
    ("しいて", "forcefully / insistently"),
    ("すでに", "already"),
    ("せっかく", "with effort / specially"),
    ("たとえ", "even if"),
    ("ともすれば", "apt to / tend to"),
    ("とかく", "apt to / tend to"),
    ("ひとまず", "for the moment"),
    ("まんざら", "not entirely"),
    ("あくまで", "to the very end"),
    ("一挙に", "at one stroke"),
    ("一切", "entirely / without exception"),
    ("一向に", "not at all"),
    ("概して", "generally"),
    ("極めて", "extremely"),
    ("相当", "considerably"),
    ("著しく", "remarkably"),
    ("必然的", "inevitable"),
    ("合理的", "rational"),
    ("客観的", "objective"),
    ("主観的", "subjective"),
    ("普遍的", "universal"),
    ("抽象的", "abstract"),
    ("具体的", "concrete"),
    ("柔軟", "flexible"),
    ("強硬", "hard-line / uncompromising"),
    ("膨大", "enormous"),
    ("微妙", "subtle / delicate"),
]

GRAMMAR = [
    {
        "q": "彼の説明は、事実に基づいている＿＿＿、説得力に欠ける。",
        "options": ["ものの", "ばかりか", "ことから", "に伴って"],
        "answer": 0,
        "explanation": "ものの = although / even though"
    },
    {
        "q": "この問題は、政府だけでなく国民全体が取り組む＿＿＿だ。",
        "options": ["べきもの", "わけではない", "ところだ", "ものではない"],
        "answer": 0,
        "explanation": "べきものだ = should be done / ought to be"
    },
    {
        "q": "彼は何度失敗しても、あきらめる＿＿＿努力を続けた。",
        "options": ["ことなく", "わけなく", "ほどなく", "ものなく"],
        "answer": 0,
        "explanation": "ことなく = without doing"
    },
    {
        "q": "この結果は、長年の研究の成果＿＿＿ほかならない。",
        "options": ["に", "を", "が", "で"],
        "answer": 0,
        "explanation": "〜にほかならない = nothing other than"
    },
    {
        "q": "彼の成功は、本人の努力＿＿＿、周囲の支援も大きかった。",
        "options": ["はもちろん", "に限らず", "ばかりに", "どころか"],
        "answer": 0,
        "explanation": "はもちろん = not to mention / of course"
    },
    {
        "q": "十分な証拠がない＿＿＿、彼を責めることはできない。",
        "options": ["以上", "からには", "ばかりか", "につれて"],
        "answer": 0,
        "explanation": "〜ない以上 = as long as / since"
    },
    {
        "q": "環境問題を解決する＿＿＿、一人一人の意識改革が必要だ。",
        "options": ["には", "ばかり", "ところ", "わけ"],
        "answer": 0,
        "explanation": "〜には = in order to"
    },
    {
        "q": "彼は責任者＿＿＿、最後まで計画を成功させようとした。",
        "options": ["として", "に対して", "につれて", "に応じて"],
        "answer": 0,
        "explanation": "として = as / in the role of"
    },
    {
        "q": "この研究結果は、従来の理論を覆す＿＿＿ものだ。",
        "options": ["に値する", "にあたる", "にすぎない", "に限る"],
        "answer": 0,
        "explanation": "〜に値する = worthy of"
    },
    {
        "q": "彼の発言は、問題をさらに複雑にする＿＿＿だった。",
        "options": ["きらいがある", "わけがある", "ものがある", "ところがある"],
        "answer": 0,
        "explanation": "きらいがある = have a tendency to"
    },
]

QUIZ = [
    {
        "q": "「矛盾」の意味は？",
        "options": ["Contradiction", "Improvement", "Innovation", "Adaptation"],
        "answer": 0
    },
    {
        "q": "「顕著」の意味は？",
        "options": ["Remarkable", "Ordinary", "Flexible", "Temporary"],
        "answer": 0
    },
    {
        "q": "「克服」の意味は？",
        "options": ["Overcome", "Exclude", "Maintain", "Introduce"],
        "answer": 0
    },
    {
        "q": "「携わる」の意味は？",
        "options": ["Be involved in", "Escape", "Increase", "Compare"],
        "answer": 0
    },
    {
        "q": "「妥当」の意味は？",
        "options": ["Valid / appropriate", "Impossible", "Ambiguous", "Universal"],
        "answer": 0
    },
    {
        "q": "「おおむね」の意味は？",
        "options": ["Generally", "Suddenly", "Barely", "Deliberately"],
        "answer": 0
    },
    {
        "q": "「あえて」の意味は？",
        "options": ["Dare to / intentionally", "Naturally", "Already", "Almost"],
        "answer": 0
    },
    {
        "q": "「一概に」の意味は？",
        "options": ["Unconditionally / generally", "Exactly", "Immediately", "Rarely"],
        "answer": 0
    },
    {
        "q": "「普遍」の意味は？",
        "options": ["Universal", "Unique", "Temporary", "Personal"],
        "answer": 0
    },
    {
        "q": "「革新」の意味は？",
        "options": ["Innovation", "Loss", "Judgment", "Suppression"],
        "answer": 0
    },
]

MOCK = [
    {
        "q": "この問題を解決するには、抜本的な＿＿＿が必要だ。",
        "options": ["改革", "偶然", "喪失", "矛盾"],
        "answer": 0
    },
    {
        "q": "彼は何度失敗しても、あきらめる＿＿＿努力を続けた。",
        "options": ["ことなく", "わけなく", "ほどなく", "ものなく"],
        "answer": 0
    },
    {
        "q": "「かろうじて」の意味は？",
        "options": ["Barely", "Completely", "Naturally", "Generally"],
        "answer": 0
    },
    {
        "q": "この制度には改善すべき点がある＿＿＿、廃止する必要はない。",
        "options": ["ものの", "ばかりか", "ところで", "につれて"],
        "answer": 0
    },
    {
        "q": "彼の成功は努力の結果＿＿＿ほかならない。",
        "options": ["に", "を", "が", "で"],
        "answer": 0
    },
    {
        "q": "「独自」の意味は？",
        "options": ["Original / unique", "Universal", "Objective", "Abstract"],
        "answer": 0
    },
    {
        "q": "問題の原因を＿＿＿する必要がある。",
        "options": ["究明", "普及", "維持", "導入"],
        "answer": 0
    },
    {
        "q": "「ひいては」の意味は？",
        "options": ["And consequently", "Not at all", "Barely", "Deliberately"],
        "answer": 0
    },
    {
        "q": "環境への影響を＿＿＿しながら開発を進めるべきだ。",
        "options": ["考慮", "克服", "喪失", "排除"],
        "answer": 0
    },
    {
        "q": "「おのずから」の意味は？",
        "options": ["Naturally / spontaneously", "Forcefully", "Approximately", "Especially"],
        "answer": 0
    },
]


# ============================================================
# HTML
# ============================================================

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>JLPT N1 Practice</title>

<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background: #f5f6fa;
    color: #222;
}

header {
    background: linear-gradient(135deg, #4a0000, #b30000);
    color: white;
    text-align: center;
    padding: 32px 20px;
}

header h1 {
    font-size: 38px;
    margin-bottom: 8px;
}

header p {
    opacity: 0.9;
}

.container {
    max-width: 1150px;
    margin: auto;
    padding: 25px;
}

.nav {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 25px;
}

.nav button {
    border: none;
    background: white;
    padding: 12px 18px;
    border-radius: 10px;
    cursor: pointer;
    font-weight: bold;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.nav button:hover {
    background: #ffe3e3;
}

.section {
    display: none;
}

.section.active {
    display: block;
}

.dashboard {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 18px;
}

.card {
    background: white;
    border-radius: 15px;
    padding: 23px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
}

.card h3 {
    margin-bottom: 10px;
}

.stat {
    font-size: 32px;
    font-weight: bold;
    color: #a00000;
}

.practice-card {
    max-width: 780px;
    margin: 20px auto;
    text-align: center;
}

.japanese {
    font-size: 50px;
    margin: 20px;
}

.reading {
    font-size: 26px;
    color: #a00000;
    margin: 10px;
}

.meaning {
    font-size: 20px;
    margin: 10px;
}

button.action {
    background: #a00000;
    color: white;
    border: none;
    padding: 12px 22px;
    border-radius: 8px;
    cursor: pointer;
    margin: 7px;
}

button.action:hover {
    background: #720000;
}

.options {
    display: grid;
    gap: 10px;
    margin-top: 20px;
}

.option {
    padding: 14px;
    border: 2px solid #ddd;
    background: white;
    border-radius: 10px;
    cursor: pointer;
    text-align: left;
    font-size: 16px;
}

.option:hover {
    border-color: #a00000;
    background: #fff4f4;
}

.correct {
    background: #d4edda !important;
    border-color: #28a745 !important;
}

.wrong {
    background: #f8d7da !important;
    border-color: #dc3545 !important;
}

.progress {
    width: 100%;
    height: 18px;
    background: #ddd;
    border-radius: 20px;
    overflow: hidden;
    margin-top: 10px;
}

.progress-bar {
    height: 100%;
    width: 0%;
    background: #a00000;
    transition: 0.3s;
}

.info {
    padding: 15px;
    background: #fff3cd;
    border-radius: 10px;
    margin: 15px 0;
}

footer {
    text-align: center;
    padding: 30px;
    color: #777;
}

@media(max-width:600px) {

    header h1 {
        font-size: 28px;
    }

    .japanese {
        font-size: 40px;
    }

}

</style>

</head>

<body>

<header>

<h1>🇯🇵 JLPT N1 Practice</h1>

<p>Advanced Japanese Learning & Practice</p>

</header>


<div class="container">


<div class="nav">

<button onclick="showSection('home')">
🏠 Home
</button>

<button onclick="showSection('kanji')">
漢字 Kanji
</button>

<button onclick="showSection('vocab')">
📚 Vocabulary
</button>

<button onclick="showSection('grammar')">
📝 Grammar
</button>

<button onclick="showSection('reading')">
📖 Reading
</button>

<button onclick="showSection('listening')">
🔊 Listening
</button>

<button onclick="showSection('quiz')">
❓ Quiz
</button>

<button onclick="showSection('mock')">
🧪 Mock Test
</button>

</div>


<!-- HOME -->

<div id="home" class="section active">

<h2>JLPT N1 Dashboard</h2>

<br>

<div class="dashboard">

<div class="card">

<h3>漢字 Kanji</h3>

<p class="stat">{{ kanji_count }}</p>

<p>Advanced kanji practice</p>

</div>


<div class="card">

<h3>Vocabulary</h3>

<p class="stat">{{ vocab_count }}</p>

<p>N1-level vocabulary</p>

</div>


<div class="card">

<h3>Grammar</h3>

<p class="stat">{{ grammar_count }}</p>

<p>Advanced grammar questions</p>

</div>


<div class="card">

<h3>Mock Test</h3>

<p class="stat">10</p>

<p>Practice questions</p>

</div>

</div>


<br>


<div class="card">

<h3>📊 Your Progress</h3>

<p>Completed activities:</p>

<h2 id="progressText">0</h2>

<div class="progress">

<div class="progress-bar" id="progressBar"></div>

</div>

<br>

<button class="action" onclick="resetProgress()">
Reset Progress
</button>

</div>


<br>


<div class="info">

<strong>Note:</strong>

This is an original JLPT N1-style practice tool.
It is not official JLPT exam material.

</div>

</div>


<!-- KANJI -->

<div id="kanji" class="section">

<h2>漢字 Kanji Practice</h2>

<div class="card practice-card">

<div id="kanjiChar" class="japanese"></div>

<div id="kanjiReading" class="reading"></div>

<div id="kanjiMeaning" class="meaning"></div>

<button class="action" onclick="showKanjiAnswer()">
Show Answer
</button>

<button class="action" onclick="nextKanji()">
Next
</button>

</div>

</div>


<!-- VOCABULARY -->

<div id="vocab" class="section">

<h2>📚 Advanced Vocabulary</h2>

<div class="card practice-card">

<div id="vocabWord" class="japanese"></div>

<div id="vocabMeaning" class="meaning"></div>

<button class="action" onclick="showVocabAnswer()">
Show Meaning
</button>

<button class="action" onclick="nextVocab()">
Next
</button>

</div>

</div>


<!-- GRAMMAR -->

<div id="grammar" class="section">

<h2>📝 N1 Grammar</h2>

<div class="card practice-card">

<h3 id="grammarQuestion"></h3>

<div id="grammarOptions" class="options"></div>

<p id="grammarResult"></p>

<button class="action" onclick="nextGrammar()">
Next Question
</button>

</div>

</div>


<!-- READING -->

<div id="reading" class="section">

<h2>📖 N1 Reading Practice</h2>

<div class="card">

<h3>技術の発展と社会</h3>

<br>

<p>

科学技術の発展は、私たちの生活を大きく変化させてきた。
情報通信技術の普及によって、世界中の人々が
瞬時に情報を共有できるようになった。

しかし、技術の発展が常に社会にとって
良い結果をもたらすとは限らない。
便利さの一方で、個人情報の保護や
情報の信頼性など、新たな問題も生じている。

そのため、技術を利用する際には、
その利点だけでなく、社会に与える影響についても
十分に考慮する必要がある。

</p>

<br>

<h3>Question</h3>

<p>

本文によると、技術を利用する際に
重要なことは何ですか。

</p>

<div class="options">

<button class="option"
onclick="readingAnswer(this, false)">

技術の便利さだけを考えること

</button>

<button class="option"
onclick="readingAnswer(this, true)">

利点と社会への影響の両方を考えること

</button>

<button class="option"
onclick="readingAnswer(this, false)">

技術を利用しないこと

</button>

<button class="option"
onclick="readingAnswer(this, false)">

情報を共有しないこと

</button>

</div>

<p id="readingResult"></p>

</div>

</div>


<!-- LISTENING -->

<div id="listening" class="section">

<h2>🔊 Listening Practice</h2>

<div class="card practice-card">

<p class="japanese">

社会の変化に対応するためには、
柔軟な考え方が必要です。

</p>

<button class="action" onclick="speakJapanese()">

🔊 Play Japanese

</button>

<br><br>

<p>

Meaning:
A flexible way of thinking is necessary
to adapt to changes in society.

</p>

</div>

</div>


<!-- QUIZ -->

<div id="quiz" class="section">

<h2>❓ N1 Quiz</h2>

<div class="card practice-card">

<h3 id="quizQuestion"></h3>

<div id="quizOptions" class="options"></div>

<p id="quizResult"></p>

<button class="action" onclick="nextQuiz()">

Next Question

</button>

</div>

</div>


<!-- MOCK -->

<div id="mock" class="section">

<h2>🧪 N1 Mock Test</h2>

<div class="card practice-card">

<p id="mockCounter"></p>

<h3 id="mockQuestion"></h3>

<div id="mockOptions" class="options"></div>

<p id="mockResult"></p>

<button class="action" onclick="nextMock()">

Next

</button>

</div>

</div>


</div>


<footer>

JLPT N1 Practice Website • Python + Flask

</footer>


<script>

const kanjiData = {{ kanji|tojson }};

const vocabData = {{ vocab|tojson }};

const grammarData = {{ grammar|tojson }};

const quizData = {{ quiz|tojson }};

const mockData = {{ mock|tojson }};


let kanjiIndex = 0;

let vocabIndex = 0;

let grammarIndex = 0;

let quizIndex = 0;

let mockIndex = 0;

let mockScore = 0;


let progress =
parseInt(localStorage.getItem("jlptN1Progress") || "0");


function showSection(id) {

document.querySelectorAll(".section").forEach(section => {

section.classList.remove("active");

});

document.getElementById(id).classList.add("active");


if (id === "kanji") loadKanji();

if (id === "vocab") loadVocab();

if (id === "grammar") loadGrammar();

if (id === "quiz") loadQuiz();

if (id === "mock") loadMock();

}


function updateProgress() {

progress++;

localStorage.setItem("jlptN1Progress", progress);

document.getElementById("progressText").innerText =
progress;

let percentage = Math.min(progress * 5, 100);

document.getElementById("progressBar").style.width =
percentage + "%";

}


function resetProgress() {

progress = 0;

localStorage.setItem("jlptN1Progress", "0");

document.getElementById("progressText").innerText = "0";

document.getElementById("progressBar").style.width = "0%";

}


// ============================================================
// KANJI
// ============================================================

function loadKanji() {

let item = kanjiData[kanjiIndex];

document.getElementById("kanjiChar").innerText =
item.kanji;

document.getElementById("kanjiReading").innerText =
"••••";

document.getElementById("kanjiMeaning").innerText =
"Click Show Answer";

}


function showKanjiAnswer() {

let item = kanjiData[kanjiIndex];

document.getElementById("kanjiReading").innerText =
item.reading;

document.getElementById("kanjiMeaning").innerText =
item.meaning;

updateProgress();

}


function nextKanji() {

kanjiIndex++;

if (kanjiIndex >= kanjiData.length)
kanjiIndex = 0;

loadKanji();

}


// ============================================================
// VOCABULARY
// ============================================================

function loadVocab() {

let item = vocabData[vocabIndex];

document.getElementById("vocabWord").innerText =
item[0];

document.getElementById("vocabMeaning").innerText =
"Click Show Meaning";

}


function showVocabAnswer() {

document.getElementById("vocabMeaning").innerText =
vocabData[vocabIndex][1];

updateProgress();

}


function nextVocab() {

vocabIndex++;

if (vocabIndex >= vocabData.length)
vocabIndex = 0;

loadVocab();

}


// ============================================================
// GRAMMAR
// ============================================================

function loadGrammar() {

let item = grammarData[grammarIndex];

document.getElementById("grammarQuestion").innerText =
item.q;

document.getElementById("grammarResult").innerText = "";

let box =
document.getElementById("grammarOptions");

box.innerHTML = "";


item.options.forEach((option, index) => {

let btn = document.createElement("button");

btn.className = "option";

btn.innerText = option;


btn.onclick = function() {

if (index === item.answer) {

btn.classList.add("correct");

document.getElementById("grammarResult").innerText =
"✅ Correct! " + item.explanation;

updateProgress();

} else {

btn.classList.add("wrong");

document.getElementById("grammarResult").innerText =
"❌ Incorrect. Correct answer: " +
item.options[item.answer];

}

};


box.appendChild(btn);

});

}


function nextGrammar() {

grammarIndex++;

if (grammarIndex >= grammarData.length)
grammarIndex = 0;

loadGrammar();

}


// ============================================================
// READING
// ============================================================

function readingAnswer(button, correct) {

if (correct) {

button.classList.add("correct");

document.getElementById("readingResult").innerText =
"✅ Correct!";

updateProgress();

} else {

button.classList.add("wrong");

document.getElementById("readingResult").innerText =
"❌ Incorrect. Try again.";

}

}


// ============================================================
// LISTENING
// ============================================================

function speakJapanese() {

let text =
"社会の変化に対応するためには、柔軟な考え方が必要です。";

let speech =
new SpeechSynthesisUtterance(text);

speech.lang = "ja-JP";

speech.rate = 0.75;

speechSynthesis.speak(speech);

updateProgress();

}


// ============================================================
// QUIZ
// ============================================================

function loadQuiz() {

let item = quizData[quizIndex];

document.getElementById("quizQuestion").innerText =
item.q;

document.getElementById("quizResult").innerText = "";

let box =
document.getElementById("quizOptions");

box.innerHTML = "";


item.options.forEach((option, index) => {

let btn = document.createElement("button");

btn.className = "option";

btn.innerText = option;


btn.onclick = function() {

if (index === item.answer) {

btn.classList.add("correct");

document.getElementById("quizResult").innerText =
"✅ Correct!";

updateProgress();

} else {

btn.classList.add("wrong");

document.getElementById("quizResult").innerText =
"❌ Incorrect. Correct answer: " +
item.options[item.answer];

}

};


box.appendChild(btn);

});

}


function nextQuiz() {

quizIndex++;

if (quizIndex >= quizData.length)
quizIndex = 0;

loadQuiz();

}


// ============================================================
// MOCK TEST
// ============================================================

function loadMock() {

let item = mockData[mockIndex];

document.getElementById("mockCounter").innerText =
"Question " + (mockIndex + 1) +
" / " + mockData.length;

document.getElementById("mockQuestion").innerText =
item.q;

document.getElementById("mockResult").innerText = "";

let box =
document.getElementById("mockOptions");

box.innerHTML = "";


item.options.forEach((option, index) => {

let btn = document.createElement("button");

btn.className = "option";

btn.innerText = option;


btn.onclick = function() {

if (index === item.answer) {

btn.classList.add("correct");

mockScore++;

document.getElementById("mockResult").innerText =
"✅ Correct!";

updateProgress();

} else {

btn.classList.add("wrong");

document.getElementById("mockResult").innerText =
"❌ Incorrect. Correct answer: " +
item.options[item.answer];

}

};


box.appendChild(btn);

});

}


function nextMock() {

mockIndex++;


if (mockIndex >= mockData.length) {

alert(
"Mock Test Finished! Your score: " +
mockScore + " / " + mockData.length
);

mockIndex = 0;

mockScore = 0;

}


loadMock();

}


// ============================================================
// INITIALIZE
// ============================================================

document.getElementById("progressText").innerText =
progress;

document.getElementById("progressBar").style.width =
Math.min(progress * 5, 100) + "%";

loadKanji();

</script>

</body>
</html>
"""


# ============================================================
# ROUTES
# ============================================================

@app.route("/")
def home():

    return render_template_string(
        HTML,
        kanji=KANJI,
        vocab=VOCAB,
        grammar=GRAMMAR,
        quiz=QUIZ,
        mock=MOCK,
        kanji_count=len(KANJI),
        vocab_count=len(VOCAB),
        grammar_count=len(GRAMMAR)
    )


@app.route("/api/status")
def status():

    return jsonify({
        "project": "JLPT N1 Practice",
        "level": "N1",
        "port": 8033,
        "kanji": len(KANJI),
        "vocabulary": len(VOCAB),
        "grammar": len(GRAMMAR),
        "quiz": len(QUIZ),
        "mock_questions": len(MOCK)
    })


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print("=" * 55)
    print("🇯🇵 JLPT N1 Practice Website")
    print("=" * 55)
    print("Server running at:")
    print("http://127.0.0.1:8033")
    print("http://localhost:8033")
    print("=" * 55)

    app.run(
        host="127.0.0.1",
        port=8033,
        debug=True
    )
