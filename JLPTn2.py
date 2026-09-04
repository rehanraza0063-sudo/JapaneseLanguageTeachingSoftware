from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# ============================================================
# JLPT N2 DATA
# ============================================================

KANJI = [
    {"kanji": "影響", "reading": "えいきょう", "meaning": "influence / effect"},
    {"kanji": "環境", "reading": "かんきょう", "meaning": "environment"},
    {"kanji": "状況", "reading": "じょうきょう", "meaning": "situation / condition"},
    {"kanji": "原因", "reading": "げんいん", "meaning": "cause"},
    {"kanji": "結果", "reading": "けっか", "meaning": "result"},
    {"kanji": "解決", "reading": "かいけつ", "meaning": "solution / resolution"},
    {"kanji": "複雑", "reading": "ふくざつ", "meaning": "complicated"},
    {"kanji": "重要", "reading": "じゅうよう", "meaning": "important"},
    {"kanji": "必要", "reading": "ひつよう", "meaning": "necessary"},
    {"kanji": "可能", "reading": "かのう", "meaning": "possible"},
    {"kanji": "技術", "reading": "ぎじゅつ", "meaning": "technology / technique"},
    {"kanji": "情報", "reading": "じょうほう", "meaning": "information"},
    {"kanji": "経験", "reading": "けいけん", "meaning": "experience"},
    {"kanji": "経済", "reading": "けいざい", "meaning": "economy"},
    {"kanji": "社会", "reading": "しゃかい", "meaning": "society"},
    {"kanji": "政治", "reading": "せいじ", "meaning": "politics"},
    {"kanji": "文化", "reading": "ぶんか", "meaning": "culture"},
    {"kanji": "教育", "reading": "きょういく", "meaning": "education"},
    {"kanji": "研究", "reading": "けんきゅう", "meaning": "research"},
    {"kanji": "発展", "reading": "はってん", "meaning": "development"},
    {"kanji": "改善", "reading": "かいぜん", "meaning": "improvement"},
    {"kanji": "増加", "reading": "ぞうか", "meaning": "increase"},
    {"kanji": "減少", "reading": "げんしょう", "meaning": "decrease"},
    {"kanji": "選択", "reading": "せんたく", "meaning": "selection / choice"},
    {"kanji": "判断", "reading": "はんだん", "meaning": "judgment"},
    {"kanji": "決定", "reading": "けってい", "meaning": "decision"},
    {"kanji": "説明", "reading": "せつめい", "meaning": "explanation"},
    {"kanji": "確認", "reading": "かくにん", "meaning": "confirmation"},
    {"kanji": "連絡", "reading": "れんらく", "meaning": "contact"},
    {"kanji": "参加", "reading": "さんか", "meaning": "participation"},
    {"kanji": "成功", "reading": "せいこう", "meaning": "success"},
    {"kanji": "失敗", "reading": "しっぱい", "meaning": "failure"},
    {"kanji": "努力", "reading": "どりょく", "meaning": "effort"},
    {"kanji": "責任", "reading": "せきにん", "meaning": "responsibility"},
    {"kanji": "関係", "reading": "かんけい", "meaning": "relationship"},
    {"kanji": "条件", "reading": "じょうけん", "meaning": "condition"},
    {"kanji": "目的", "reading": "もくてき", "meaning": "purpose"},
    {"kanji": "方法", "reading": "ほうほう", "meaning": "method"},
    {"kanji": "意識", "reading": "いしき", "meaning": "awareness / consciousness"},
    {"kanji": "価値", "reading": "かち", "meaning": "value"},
]

VOCAB = [
    ("あらかじめ", "in advance"),
    ("あまりにも", "too much / excessively"),
    ("いずれ", "eventually / either"),
    ("おそらく", "probably"),
    ("かなり", "considerably"),
    ("必ずしも", "not necessarily"),
    ("たまたま", "by chance"),
    ("つまり", "in other words"),
    ("とうとう", "finally"),
    ("なかなか", "quite / not easily"),
    ("ほとんど", "almost"),
    ("まもなく", "soon"),
    ("わざわざ", "go out of one's way"),
    ("一応", "for the time being"),
    ("実際", "actually"),
    ("当然", "naturally / of course"),
    ("特に", "especially"),
    ("突然", "suddenly"),
    ("十分", "enough / sufficiently"),
    ("一般的", "general / common"),
    ("具体的", "specific / concrete"),
    ("基本的", "fundamental / basic"),
    ("積極的", "positive / proactive"),
    ("消極的", "negative / passive"),
    ("適切", "appropriate"),
    ("正確", "accurate"),
    ("豊か", "rich / abundant"),
    ("重大", "serious / important"),
    ("有効", "effective / valid"),
    ("明確", "clear"),
    ("不可能", "impossible"),
    ("不安", "anxiety / uneasiness"),
    ("満足", "satisfaction"),
    ("不足", "shortage / insufficiency"),
    ("余裕", "room / margin"),
    ("傾向", "tendency"),
    ("特徴", "characteristic"),
    ("対象", "target / subject"),
    ("影響", "influence"),
    ("維持", "maintenance"),
]

GRAMMAR = [
    {
        "q": "この問題は難しい＿＿＿、解決できないわけではない。",
        "options": ["ものの", "ところで", "ばかり", "ほど"],
        "answer": 0,
        "explanation": "ものの = although / even though"
    },
    {
        "q": "健康のために、毎日運動する＿＿＿している。",
        "options": ["ように", "ことに", "ために", "ばかり"],
        "answer": 0,
        "explanation": "ようにしている = make an effort to / make it a practice to"
    },
    {
        "q": "彼は忙しい＿＿＿、いつも手伝ってくれる。",
        "options": ["にもかかわらず", "にしたがって", "につれて", "に対して"],
        "answer": 0,
        "explanation": "にもかかわらず = despite / nevertheless"
    },
    {
        "q": "日本へ行く＿＿＿、日本語をもっと勉強したい。",
        "options": ["からには", "ところが", "ばかりに", "わけで"],
        "answer": 0,
        "explanation": "からには = now that / since"
    },
    {
        "q": "この薬は医者の指示＿＿＿飲んでください。",
        "options": ["に従って", "につれて", "に比べて", "において"],
        "answer": 0,
        "explanation": "に従って = according to / following"
    },
    {
        "q": "駅に着いた＿＿＿、電車が出てしまった。",
        "options": ["とたんに", "うちに", "たびに", "ほど"],
        "answer": 0,
        "explanation": "とたんに = just as / immediately after"
    },
    {
        "q": "忙しい＿＿＿、友達に連絡する時間もない。",
        "options": ["あまり", "ほど", "わけで", "ところで"],
        "answer": 0,
        "explanation": "あまり = so much that / excessively"
    },
    {
        "q": "彼は学生＿＿＿、会社を経営している。",
        "options": ["でありながら", "につれて", "にしては", "ばかりか"],
        "answer": 0,
        "explanation": "でありながら = despite being"
    },
    {
        "q": "この店は安い＿＿＿、料理もおいしい。",
        "options": ["ばかりか", "ところで", "わけで", "ために"],
        "answer": 0,
        "explanation": "ばかりか = not only...but also"
    },
    {
        "q": "雨が降った＿＿＿、試合は予定通り行われた。",
        "options": ["にもかかわらず", "に対して", "にしたがって", "につれて"],
        "answer": 0,
        "explanation": "にもかかわらず = despite"
    },
]

QUIZ = [
    {
        "q": "「影響」の意味は？",
        "options": ["Influence", "Experience", "Decision", "Method"],
        "answer": 0
    },
    {
        "q": "「維持」の意味は？",
        "options": ["Maintenance", "Increase", "Failure", "Research"],
        "answer": 0
    },
    {
        "q": "「あらかじめ」の意味は？",
        "options": ["In advance", "Suddenly", "Eventually", "By chance"],
        "answer": 0
    },
    {
        "q": "「責任」の読み方は？",
        "options": ["せきにん", "せつめい", "せんたく", "せいじ"],
        "answer": 0
    },
    {
        "q": "「豊か」の意味は？",
        "options": ["Rich / abundant", "Difficult", "Accurate", "Serious"],
        "answer": 0
    },
    {
        "q": "「判断」の意味は？",
        "options": ["Judgment", "Contact", "Participation", "Environment"],
        "answer": 0
    },
    {
        "q": "「必ずしも」の意味は？",
        "options": ["Not necessarily", "Definitely", "Suddenly", "Usually"],
        "answer": 0
    },
    {
        "q": "「改善」の意味は？",
        "options": ["Improvement", "Decrease", "Cause", "Target"],
        "answer": 0
    },
    {
        "q": "「対象」の意味は？",
        "options": ["Target / subject", "Condition", "Culture", "Society"],
        "answer": 0
    },
    {
        "q": "「突然」の意味は？",
        "options": ["Suddenly", "Finally", "Actually", "Enough"],
        "answer": 0
    },
]

MOCK = [
    {
        "q": "この研究は社会に大きな＿＿＿を与えた。",
        "options": ["影響", "責任", "余裕", "不足"],
        "answer": 0
    },
    {
        "q": "彼は忙しい＿＿＿、毎日日本語を勉強している。",
        "options": ["にもかかわらず", "ばかりに", "ところで", "ほど"],
        "answer": 0
    },
    {
        "q": "「おそらく」の意味として正しいものは？",
        "options": ["Probably", "Certainly", "Immediately", "Rarely"],
        "answer": 0
    },
    {
        "q": "環境問題を＿＿＿ためには、社会全体の協力が必要だ。",
        "options": ["解決する", "失敗する", "参加する", "連絡する"],
        "answer": 0
    },
    {
        "q": "彼は学生＿＿＿、会社を経営している。",
        "options": ["でありながら", "につれて", "に従って", "ところが"],
        "answer": 0
    },
    {
        "q": "「傾向」の意味は？",
        "options": ["Tendency", "Value", "Result", "Technology"],
        "answer": 0
    },
    {
        "q": "駅に着いた＿＿＿、電車が出発した。",
        "options": ["とたんに", "ばかりか", "からには", "ものの"],
        "answer": 0
    },
    {
        "q": "「正確」の意味は？",
        "options": ["Accurate", "Rich", "Possible", "General"],
        "answer": 0
    },
    {
        "q": "健康を＿＿＿ために、毎日運動している。",
        "options": ["維持する", "比較する", "決定する", "説明する"],
        "answer": 0
    },
    {
        "q": "「一応」の意味は？",
        "options": ["For the time being", "Suddenly", "Not necessarily", "In other words"],
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
<title>JLPT N2 Practice</title>

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
    background: linear-gradient(135deg, #8e0e00, #d83a00);
    color: white;
    padding: 30px 20px;
    text-align: center;
}

header h1 {
    font-size: 36px;
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
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    font-weight: bold;
}

.nav button:hover {
    background: #ffe8e2;
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
    padding: 22px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
}

.card h3 {
    margin-bottom: 10px;
}

.stat {
    font-size: 32px;
    font-weight: bold;
    color: #b42318;
}

.practice-card {
    max-width: 750px;
    margin: 20px auto;
    text-align: center;
}

.japanese {
    font-size: 52px;
    margin: 20px;
}

.reading {
    font-size: 26px;
    color: #b42318;
    margin: 10px;
}

.meaning {
    font-size: 20px;
    margin: 10px;
}

button.action {
    background: #b42318;
    color: white;
    border: none;
    padding: 12px 22px;
    border-radius: 8px;
    cursor: pointer;
    margin: 7px;
}

button.action:hover {
    background: #8f1c14;
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
}

.option:hover {
    border-color: #b42318;
    background: #fff5f3;
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
    background: #b42318;
    transition: 0.3s;
}

textarea {
    width: 100%;
    min-height: 130px;
    padding: 12px;
    border-radius: 10px;
    border: 1px solid #ccc;
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
    <h1>🇯🇵 JLPT N2 Practice</h1>
    <p>Intermediate Japanese Learning & Practice</p>
</header>

<div class="container">

<div class="nav">
    <button onclick="showSection('home')">🏠 Home</button>
    <button onclick="showSection('kanji')">漢字 Kanji</button>
    <button onclick="showSection('vocab')">📚 Vocabulary</button>
    <button onclick="showSection('grammar')">📝 Grammar</button>
    <button onclick="showSection('reading')">📖 Reading</button>
    <button onclick="showSection('listening')">🔊 Listening</button>
    <button onclick="showSection('quiz')">❓ Quiz</button>
    <button onclick="showSection('mock')">🧪 Mock Test</button>
</div>


<!-- HOME -->

<div id="home" class="section active">

<h2>JLPT N2 Dashboard</h2>
<br>

<div class="dashboard">

<div class="card">
<h3>漢字 Kanji</h3>
<p class="stat">{{ kanji_count }}</p>
<p>N2-style kanji practice</p>
</div>

<div class="card">
<h3>Vocabulary</h3>
<p class="stat">{{ vocab_count }}</p>
<p>Useful N2 vocabulary</p>
</div>

<div class="card">
<h3>Grammar</h3>
<p class="stat">{{ grammar_count }}</p>
<p>Grammar questions</p>
</div>

<div class="card">
<h3>Mock Test</h3>
<p class="stat">10</p>
<p>Questions</p>
</div>

</div>

<br>

<div class="card">
<h3>📊 Your Progress</h3>
<p>Completed questions:</p>
<h2 id="progressText">0</h2>

<div class="progress">
<div class="progress-bar" id="progressBar"></div>
</div>

<br>

<button class="action" onclick="resetProgress()">Reset Progress</button>
</div>

<br>

<div class="info">
<strong>Note:</strong> This is an original JLPT N2-style practice tool.
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

<button class="action" onclick="showKanjiAnswer()">Show Answer</button>
<button class="action" onclick="nextKanji()">Next</button>

</div>

</div>


<!-- VOCAB -->

<div id="vocab" class="section">

<h2>📚 Vocabulary Practice</h2>

<div class="card practice-card">

<div id="vocabWord" class="japanese"></div>
<div id="vocabMeaning" class="meaning"></div>

<button class="action" onclick="showVocabAnswer()">Show Meaning</button>
<button class="action" onclick="nextVocab()">Next</button>

</div>

</div>


<!-- GRAMMAR -->

<div id="grammar" class="section">

<h2>📝 Grammar Practice</h2>

<div class="card practice-card">

<h3 id="grammarQuestion"></h3>

<div id="grammarOptions" class="options"></div>

<p id="grammarResult"></p>

<button class="action" onclick="nextGrammar()">Next Question</button>

</div>

</div>


<!-- READING -->

<div id="reading" class="section">

<h2>📖 Reading Practice</h2>

<div class="card">

<h3>日本語を勉強する理由</h3>

<br>

<p>
日本語を勉強する理由は人によって違います。
日本の文化に興味がある人もいれば、
日本で働くために勉強している人もいます。
また、日本の映画や音楽が好きで、
日本語を理解したいと思う人もいます。
外国語を勉強すると、新しい文化や考え方を
知ることができます。
</p>

<br>

<h3>Question</h3>

<p>日本語を勉強する理由について、本文で述べられていないものはどれですか。</p>

<div class="options">

<button class="option" onclick="readingAnswer(this, false)">
日本の文化に興味がある
</button>

<button class="option" onclick="readingAnswer(this, false)">
日本で働きたい
</button>

<button class="option" onclick="readingAnswer(this, true)">
日本のスポーツ選手になりたい
</button>

<button class="option" onclick="readingAnswer(this, false)">
映画や音楽が好き
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
明日は雨が降るかもしれません。
</p>

<br>

<button class="action" onclick="speakJapanese()">
🔊 Play Japanese
</button>

<p>
Meaning: It may rain tomorrow.
</p>

</div>

</div>


<!-- QUIZ -->

<div id="quiz" class="section">

<h2>❓ N2 Quiz</h2>

<div class="card practice-card">

<h3 id="quizQuestion"></h3>

<div id="quizOptions" class="options"></div>

<p id="quizResult"></p>

<button class="action" onclick="nextQuiz()">Next Question</button>

</div>

</div>


<!-- MOCK TEST -->

<div id="mock" class="section">

<h2>🧪 N2 Mock Test</h2>

<div class="card practice-card">

<p id="mockCounter"></p>

<h3 id="mockQuestion"></h3>

<div id="mockOptions" class="options"></div>

<p id="mockResult"></p>

<button class="action" onclick="nextMock()">Next</button>

</div>

</div>

</div>

<footer>
JLPT N2 Practice Website • Python + Flask
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
    parseInt(localStorage.getItem("jlptN2Progress") || "0");

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

    localStorage.setItem("jlptN2Progress", progress);

    document.getElementById("progressText").innerText = progress;

    let percentage = Math.min(progress * 5, 100);

    document.getElementById("progressBar").style.width =
        percentage + "%";
}

function resetProgress() {

    progress = 0;

    localStorage.setItem("jlptN2Progress", "0");

    document.getElementById("progressText").innerText = "0";
    document.getElementById("progressBar").style.width = "0%";
}


// ================= KANJI =================

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


// ================= VOCAB =================

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


// ================= GRAMMAR =================

function loadGrammar() {

    let item = grammarData[grammarIndex];

    document.getElementById("grammarQuestion").innerText =
        item.q;

    let box = document.getElementById("grammarOptions");

    box.innerHTML = "";

    document.getElementById("grammarResult").innerText = "";

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


// ================= READING =================

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


// ================= LISTENING =================

function speakJapanese() {

    let text =
        "明日は雨が降るかもしれません。";

    let speech =
        new SpeechSynthesisUtterance(text);

    speech.lang = "ja-JP";

    speech.rate = 0.8;

    speechSynthesis.speak(speech);

    updateProgress();
}


// ================= QUIZ =================

function loadQuiz() {

    let item = quizData[quizIndex];

    document.getElementById("quizQuestion").innerText =
        item.q;

    document.getElementById("quizResult").innerText = "";

    let box = document.getElementById("quizOptions");

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


// ================= MOCK TEST =================

function loadMock() {

    let item = mockData[mockIndex];

    document.getElementById("mockCounter").innerText =
        "Question " + (mockIndex + 1) +
        " / " + mockData.length;

    document.getElementById("mockQuestion").innerText =
        item.q;

    document.getElementById("mockResult").innerText = "";

    let box = document.getElementById("mockOptions");

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


// ================= INITIALIZE =================

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
        "project": "JLPT N2 Practice",
        "level": "N2",
        "port": 8032,
        "kanji": len(KANJI),
        "vocabulary": len(VOCAB),
        "grammar": len(GRAMMAR),
        "quiz": len(QUIZ),
        "mock_questions": len(MOCK)
    })


# ============================================================
# RUN SERVER
# ============================================================

if __name__ == "__main__":
    print("=" * 55)
    print("🇯🇵 JLPT N2 Practice Website")
    print("=" * 55)
    print("Server running at:")
    print("http://127.0.0.1:8032")
    print("http://localhost:8032")
    print("=" * 55)

    app.run(
        host="127.0.0.1",
        port=8032,
        debug=True
    )
