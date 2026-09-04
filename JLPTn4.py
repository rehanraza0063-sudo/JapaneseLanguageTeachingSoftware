from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>JLPT N4 Practice</title>

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
    background: linear-gradient(135deg, #7b1e1e, #c62828);
    color: white;
    text-align: center;
    padding: 30px 20px;
}

header h1 {
    font-size: 34px;
    margin-bottom: 8px;
}

header p {
    opacity: 0.9;
}

nav {
    background: white;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;
    padding: 12px;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

nav button {
    border: none;
    padding: 10px 15px;
    border-radius: 20px;
    cursor: pointer;
    background: #eeeeee;
    font-weight: bold;
}

nav button:hover {
    background: #c62828;
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
    margin-bottom: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

.hero h2 {
    color: #c62828;
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
    transform: translateY(-5px);
}

.card h3 {
    margin-bottom: 8px;
}

.icon {
    font-size: 40px;
    margin-bottom: 10px;
}

.practice-box {
    background: white;
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

.japanese {
    font-size: 55px;
    font-weight: bold;
    color: #c62828;
    margin: 20px;
}

.question {
    font-size: 22px;
    font-weight: bold;
    margin: 20px;
}

.meaning {
    font-size: 21px;
    margin: 15px;
}

.btn {
    border: none;
    padding: 12px 22px;
    margin: 7px;
    border-radius: 10px;
    cursor: pointer;
    background: #c62828;
    color: white;
    font-weight: bold;
}

.btn:hover {
    background: #8e1b1b;
}

.options {
    display: grid;
    grid-template-columns: repeat(2, minmax(150px, 1fr));
    gap: 12px;
    max-width: 650px;
    margin: 20px auto;
}

.option {
    border: 2px solid #ddd;
    background: #f5f5f5;
    padding: 15px;
    border-radius: 10px;
    cursor: pointer;
    font-size: 17px;
}

.option:hover {
    border-color: #c62828;
}

.correct {
    background: #b9f6ca !important;
    border-color: green !important;
}

.wrong {
    background: #ffcdd2 !important;
    border-color: red !important;
}

.result {
    font-size: 20px;
    font-weight: bold;
    margin: 15px;
}

.reading {
    background: #fafafa;
    border-left: 5px solid #c62828;
    padding: 22px;
    text-align: left;
    line-height: 2.1;
    border-radius: 8px;
    margin: 20px 0;
    font-size: 18px;
}

.stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 15px;
}

.stat {
    background: white;
    padding: 22px;
    text-align: center;
    border-radius: 15px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
}

.stat h2 {
    color: #c62828;
    font-size: 32px;
    margin-bottom: 8px;
}

.progress-container {
    height: 22px;
    background: #ddd;
    border-radius: 20px;
    overflow: hidden;
    margin: 20px 0;
}

.progress-bar {
    height: 100%;
    width: 0%;
    background: #c62828;
    transition: 0.4s;
}

footer {
    text-align: center;
    padding: 30px;
    color: #777;
}

@media(max-width:600px) {

    header h1 {
        font-size: 27px;
    }

    .options {
        grid-template-columns: 1fr;
    }

    .japanese {
        font-size: 45px;
    }

    nav button {
        font-size: 11px;
    }
}

</style>
</head>

<body>

<header>

<h1>🇯🇵 JLPT N4 Practice</h1>

<p>Japanese Intermediate Beginner Practice Platform</p>

</header>


<nav>

<button onclick="showSection('home')">🏠 Home</button>

<button onclick="showSection('hiragana')">あ Hiragana</button>

<button onclick="showSection('katakana')">カ Katakana</button>

<button onclick="showSection('kanji')">漢 Kanji</button>

<button onclick="showSection('vocabulary')">📚 Vocabulary</button>

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

<h2>JLPT N4 Learning Dashboard</h2>

<p>
Improve your Japanese vocabulary, Kanji, grammar,
reading and listening skills.
</p>

</div>


<div class="cards">

<div class="card" onclick="showSection('hiragana')">

<div class="icon">あ</div>

<h3>Hiragana Review</h3>

<p>Review basic Hiragana characters.</p>

</div>


<div class="card" onclick="showSection('katakana')">

<div class="icon">カ</div>

<h3>Katakana Review</h3>

<p>Review Katakana pronunciation.</p>

</div>


<div class="card" onclick="showSection('kanji')">

<div class="icon">漢</div>

<h3>N4 Kanji</h3>

<p>Practice common intermediate Kanji.</p>

</div>


<div class="card" onclick="showSection('vocabulary')">

<div class="icon">📚</div>

<h3>N4 Vocabulary</h3>

<p>Learn useful Japanese vocabulary.</p>

</div>


<div class="card" onclick="showSection('grammar')">

<div class="icon">📝</div>

<h3>N4 Grammar</h3>

<p>Practice important N4 grammar patterns.</p>

</div>


<div class="card" onclick="showSection('reading')">

<div class="icon">📖</div>

<h3>Reading</h3>

<p>Read simple N4-level passages.</p>

</div>


<div class="card" onclick="showSection('listening')">

<div class="icon">🔊</div>

<h3>Listening</h3>

<p>Practice Japanese pronunciation.</p>

</div>


<div class="card" onclick="showSection('quiz')">

<div class="icon">🎯</div>

<h3>Quiz</h3>

<p>Test your Japanese knowledge.</p>

</div>


<div class="card" onclick="showSection('mock')">

<div class="icon">🏆</div>

<h3>Mock Test</h3>

<p>Take a mini N4-style test.</p>

</div>


<div class="card" onclick="showSection('progress')">

<div class="icon">📊</div>

<h3>Progress</h3>

<p>Track your learning progress.</p>

</div>

</div>

</section>


<!-- HIRAGANA -->

<section id="hiragana" class="section">

<div class="hero">

<h2>あ Hiragana Review</h2>

<p>Review Japanese Hiragana pronunciation.</p>

</div>

<div class="practice-box">

<div class="japanese" id="hiraChar">あ</div>

<div class="question">
What is the pronunciation?
</div>

<div class="options" id="hiraOptions"></div>

<div id="hiraResult"></div>

<button class="btn" onclick="newHiragana()">
Next
</button>

</div>

</section>


<!-- KATAKANA -->

<section id="katakana" class="section">

<div class="hero">

<h2>カ Katakana Review</h2>

<p>Review Katakana pronunciation.</p>

</div>

<div class="practice-box">

<div class="japanese" id="kataChar">ア</div>

<div class="question">
What is the pronunciation?
</div>

<div class="options" id="kataOptions"></div>

<div id="kataResult"></div>

<button class="btn" onclick="newKatakana()">
Next
</button>

</div>

</section>


<!-- KANJI -->

<section id="kanji" class="section">

<div class="hero">

<h2>漢 N4 Kanji</h2>

<p>Learn common Kanji and their meanings.</p>

</div>

<div class="practice-box">

<div class="japanese" id="kanjiChar">
会
</div>

<div class="meaning" id="kanjiMeaning">
Meet / Meeting
</div>

<button class="btn"
onclick="speakJapanese(document.getElementById('kanjiChar').innerText)">
🔊 Listen
</button>

<button class="btn" onclick="newKanji()">
Next Kanji
</button>

</div>

</section>


<!-- VOCABULARY -->

<section id="vocabulary" class="section">

<div class="hero">

<h2>📚 N4 Vocabulary</h2>

<p>Learn useful N4 vocabulary.</p>

</div>

<div class="practice-box">

<div class="japanese" id="vocabWord">
りょこう
</div>

<div class="meaning" id="vocabMeaning">
Travel
</div>

<button class="btn"
onclick="speakJapanese(document.getElementById('vocabWord').innerText)">
🔊 Listen
</button>

<button class="btn" onclick="newVocabulary()">
Next Word
</button>

</div>

</section>


<!-- GRAMMAR -->

<section id="grammar" class="section">

<div class="hero">

<h2>📝 N4 Grammar Practice</h2>

<p>Practice common N4 grammar patterns.</p>

</div>

<div class="practice-box">

<div class="question" id="grammarQuestion">
あした、雨が ___ と思います。
</div>

<div class="options" id="grammarOptions"></div>

<div id="grammarResult"></div>

<button class="btn" onclick="newGrammar()">
Next Question
</button>

</div>

</section>


<!-- READING -->

<section id="reading" class="section">

<div class="hero">

<h2>📖 N4 Reading Practice</h2>

<p>Read the passage and answer the question.</p>

</div>

<div class="practice-box">

<div class="reading">

先週の日曜日、私は友達と一緒に映画を見に行きました。

映画の後で、近くのレストランで昼ご飯を食べました。

とても楽しい一日でした。

</div>

<div class="question">

先週の日曜日、何をしましたか？

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
Practice Japanese pronunciation using your browser.
</p>

</div>

<div class="practice-box">

<div class="japanese">
今日はいい天気ですね。
</div>

<div class="meaning">
The weather is nice today, isn't it?
</div>

<button class="btn"
onclick="speakJapanese('今日はいい天気ですね')">
🔊 Play
</button>

<br>

<button class="btn"
onclick="speakJapanese('明日学校へ行きます')">
🔊 Sentence 2
</button>

<button class="btn"
onclick="speakJapanese('昨日友達と映画を見ました')">
🔊 Sentence 3
</button>

</div>

</section>


<!-- QUIZ -->

<section id="quiz" class="section">

<div class="hero">

<h2>🎯 N4 Quiz</h2>

<p>Test your Japanese knowledge.</p>

</div>

<div class="practice-box">

<div class="question" id="quizQuestion">
Click Start Quiz
</div>

<div class="options" id="quizOptions"></div>

<div class="result" id="quizResult"></div>

<button class="btn" onclick="newQuiz()">
Start / Next Question
</button>

</div>

</section>


<!-- MOCK TEST -->

<section id="mock" class="section">

<div class="hero">

<h2>🏆 N4-Style Mini Mock Test</h2>

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

<h2>📊 Learning Progress</h2>

<p>Your progress is saved in your browser.</p>

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

<h2 id="mockScore">0/10</h2>

<p>Best Mock Score</p>

</div>

</div>


<div class="practice-box" style="margin-top:20px;">

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

<p>
🇯🇵 JLPT N4 Practice Website | Python + Flask
</p>

</footer>


<script>


/* =========================
   DATA
========================= */


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

["会","Meet / Meeting"],
["同","Same"],
["事","Thing / Matter"],
["自","Self"],
["発","Departure / Start"],
["者","Person"],
["地","Ground / Place"],
["業","Business / Work"],
["度","Degree / Time"],
["持","Hold / Have"],
["思","Think"],
["知","Know"],
["使","Use"],
["作","Make"],
["住","Live / Reside"],
["始","Begin"],
["終","Finish"],
["習","Learn / Practice"],
["考","Think / Consider"],
["教","Teach"],
["働","Work"],
["楽","Fun / Comfortable"],
["強","Strong"],
["弱","Weak"],
["近","Near"],
["遠","Far"],
["早","Early / Fast"],
["遅","Late / Slow"],
["新","New"],
["古","Old"],
["多","Many"],
["少","Few"],
["長","Long"],
["短","Short"],
["高","High / Expensive"],
["安","Cheap / Safe"],
["明","Bright"],
["暗","Dark"]

];


const vocabulary = [

["りょこう","Travel"],
["しゅくだい","Homework"],
["せいかつ","Daily life"],
["けいけん","Experience"],
["やくそく","Promise / Appointment"],
["じゅんび","Preparation"],
["せつめい","Explanation"],
["れんしゅう","Practice"],
["しゅみ","Hobby"],
["しごと","Work"],
["かいしゃ","Company"],
["びょういん","Hospital"],
["やくにたつ","Be useful"],
["わすれる","Forget"],
["おぼえる","Remember"],
["つかう","Use"],
["つくる","Make"],
["あつめる","Collect"],
["えらぶ","Choose"],
["なおす","Fix / Correct"]

];


const grammar = [

{
q:"あした、雨が ___ と思います。",
options:["ふる","ふった","ふって","ふります"],
answer:"ふる"
},

{
q:"日本へ行った ___ があります。",
options:["こと","もの","ため","ところ"],
answer:"こと"
},

{
q:"この本は子ども ___ 読めます。",
options:["でも","しか","だけ","ほど"],
answer:"でも"
},

{
q:"宿題をして ___ テレビを見ます。",
options:["から","まで","だけ","しか"],
answer:"から"
},

{
q:"日本語を話す ___ ができます。",
options:["こと","もの","ところ","ため"],
answer:"こと"
},

{
q:"駅まで歩いて ___ 10分かかります。",
options:["約","全部","特別","十分"],
answer:"約"
},

{
q:"この料理は簡単 ___ 作れます。",
options:["に","で","な","を"],
answer:"に"
},

{
q:"もっと日本語を勉強 ___ なりたいです。",
options:["して","する","した","し"],
answer:"して"
}

];


const quizData = [

{
q:"「りょこう」の意味は？",
options:["Travel","Homework","Company","Hospital"],
answer:"Travel"
},

{
q:"「経験」の読み方は？",
options:["けいけん","けいかん","きょうけん","けんけい"],
answer:"けいけん"
},

{
q:"「新しい」の反対は？",
options:["古い","高い","長い","強い"],
answer:"古い"
},

{
q:"「しゅくだい」の意味は？",
options:["Homework","Holiday","Travel","Meeting"],
answer:"Homework"
},

{
q:"「強い」の反対は？",
options:["弱い","短い","安い","暗い"],
answer:"弱い"
},

{
q:"「会社」の意味は？",
options:["Company","School","Hospital","Station"],
answer:"Company"
},

{
q:"「忘れる」の意味は？",
options:["Forget","Remember","Learn","Teach"],
answer:"Forget"
},

{
q:"「使う」の意味は？",
options:["Use","Make","Choose","Fix"],
answer:"Use"
}

];


const mockQuestions = [

{
q:"「りょこう」の意味は？",
options:["Travel","Work","Study","Hospital"],
answer:"Travel"
},

{
q:"「経験」の読み方は？",
options:["けいけん","けいせん","きょうけん","けんこう"],
answer:"けいけん"
},

{
q:"日本へ行った ___ があります。",
options:["こと","もの","ため","ところ"],
answer:"こと"
},

{
q:"「古い」の反対は？",
options:["新しい","強い","短い","安い"],
answer:"新しい"
},

{
q:"「会社」の意味は？",
options:["Company","School","House","Station"],
answer:"Company"
},

{
q:"「忘れる」の意味は？",
options:["Forget","Remember","Practice","Teach"],
answer:"Forget"
},

{
q:"宿題をして ___ テレビを見ます。",
options:["から","まで","しか","ほど"],
answer:"から"
},

{
q:"「弱い」の反対は？",
options:["強い","長い","高い","新しい"],
answer:"強い"
},

{
q:"「使う」の意味は？",
options:["Use","Choose","Forget","Finish"],
answer:"Use"
},

{
q:"日本語を話す ___ ができます。",
options:["こと","もの","ため","ところ"],
answer:"こと"
}

];


/* =========================
   PROGRESS
========================= */


let progress =
JSON.parse(localStorage.getItem("jlptN4Progress"))
|| {
    answered:0,
    correct:0,
    bestMock:0
};


function saveProgress(){

    localStorage.setItem(
        "jlptN4Progress",
        JSON.stringify(progress)
    );

    updateProgress();
}


function updateProgress(){

    document.getElementById("totalAnswered").innerText =
        progress.answered;

    document.getElementById("correctAnswers").innerText =
        progress.correct;

    let accuracy =
        progress.answered === 0
        ? 0
        : Math.round(
            (progress.correct / progress.answered) * 100
        );

    document.getElementById("accuracy").innerText =
        accuracy + "%";

    document.getElementById("mockScore").innerText =
        progress.bestMock + "/10";

    let percentage =
        Math.min(
            100,
            Math.round(
                (progress.answered / 50) * 100
            )
        );

    document.getElementById("progressBar")
        .style.width = percentage + "%";

    document.getElementById("progressText")
        .innerText =
        percentage + "% learning progress completed.";
}


/* =========================
   NAVIGATION
========================= */


function showSection(id){

    document
    .querySelectorAll(".section")
    .forEach(section => {

        section.classList.remove("active");

    });

    document
    .getElementById(id)
    .classList.add("active");

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });

    if(id === "progress"){
        updateProgress();
    }

}


/* =========================
   UTILITIES
========================= */


function shuffle(array){

    return [...array]
        .sort(() => Math.random() - 0.5);

}


function createOptions(
    container,
    options,
    answer,
    resultElement
){

    container.innerHTML = "";

    shuffle(options).forEach(option => {

        let button =
            document.createElement("button");

        button.className = "option";

        button.innerText = option;

        button.onclick = function(){

            let all =
                container.querySelectorAll(".option");

            all.forEach(btn => {

                btn.disabled = true;

                if(btn.innerText === answer){
                    btn.classList.add("correct");
                }

            });


            if(option === answer){

                button.classList.add("correct");

                resultElement.innerHTML =
                "<p style='color:green;'>✓ Correct!</p>";

                progress.correct++;

            }
            else{

                button.classList.add("wrong");

                resultElement.innerHTML =
                "<p style='color:red;'>✗ Correct answer: "
                + answer +
                "</p>";

            }

            progress.answered++;

            saveProgress();

        };

        container.appendChild(button);

    });

}


/* =========================
   HIRAGANA
========================= */


function newHiragana(){

    let item =
        hiragana[
            Math.floor(
                Math.random() *
                hiragana.length
            )
        ];

    document.getElementById("hiraChar")
        .innerText = item[0];

    let wrong =
        shuffle(
            hiragana.filter(
                x => x[1] !== item[1]
            )
        )
        .slice(0,3)
        .map(x => x[1]);

    document.getElementById("hiraResult")
        .innerHTML = "";

    createOptions(
        document.getElementById("hiraOptions"),
        [item[1],...wrong],
        item[1],
        document.getElementById("hiraResult")
    );

}


/* =========================
   KATAKANA
========================= */


function newKatakana(){

    let item =
        katakana[
            Math.floor(
                Math.random() *
                katakana.length
            )
        ];

    document.getElementById("kataChar")
        .innerText = item[0];

    let wrong =
        shuffle(
            katakana.filter(
                x => x[1] !== item[1]
            )
        )
        .slice(0,3)
        .map(x => x[1]);

    document.getElementById("kataResult")
        .innerHTML = "";

    createOptions(
        document.getElementById("kataOptions"),
        [item[1],...wrong],
        item[1],
        document.getElementById("kataResult")
    );

}


/* =========================
   KANJI
========================= */


function newKanji(){

    let item =
        kanji[
            Math.floor(
                Math.random() *
                kanji.length
            )
        ];

    document.getElementById("kanjiChar")
        .innerText = item[0];

    document.getElementById("kanjiMeaning")
        .innerText = item[1];

}


/* =========================
   VOCABULARY
========================= */


function newVocabulary(){

    let item =
        vocabulary[
            Math.floor(
                Math.random() *
                vocabulary.length
            )
        ];

    document.getElementById("vocabWord")
        .innerText = item[0];

    document.getElementById("vocabMeaning")
        .innerText = item[1];

}


/* =========================
   GRAMMAR
========================= */


let grammarIndex = 0;


function newGrammar(){

    let item =
        grammar[grammarIndex];

    document.getElementById("grammarQuestion")
        .innerText = item.q;

    document.getElementById("grammarResult")
        .innerHTML = "";

    createOptions(
        document.getElementById("grammarOptions"),
        item.options,
        item.answer,
        document.getElementById("grammarResult")
    );

    grammarIndex++;

    if(grammarIndex >= grammar.length){
        grammarIndex = 0;
    }

}


/* =========================
   READING
========================= */


function setupReading(){

    createOptions(

        document.getElementById("readingOptions"),

        [
            "映画を見ました。",
            "学校へ行きました。",
            "買い物をしました。",
            "勉強しました。"
        ],

        "映画を見ました。",

        document.getElementById("readingResult")

    );

}


/* =========================
   SPEECH
========================= */


function speakJapanese(text){

    if(!("speechSynthesis" in window)){

        alert(
            "Your browser does not support speech synthesis."
        );

        return;

    }

    let speech =
        new SpeechSynthesisUtterance(text);

    speech.lang = "ja-JP";

    speech.rate = 0.8;

    window.speechSynthesis.cancel();

    window.speechSynthesis.speak(speech);

}


/* =========================
   QUIZ
========================= */


let quizIndex = 0;


function newQuiz(){

    let item =
        quizData[quizIndex];

    document.getElementById("quizQuestion")
        .innerText = item.q;

    document.getElementById("quizResult")
        .innerHTML = "";

    createOptions(
        document.getElementById("quizOptions"),
        item.options,
        item.answer,
        document.getElementById("quizResult")
    );

    quizIndex++;

    if(quizIndex >= quizData.length){
        quizIndex = 0;
    }

}


/* =========================
   MOCK TEST
========================= */


let mockIndex = 0;

let mockScore = 0;


function startMock(){

    mockIndex = 0;

    mockScore = 0;

    showMockQuestion();

}


function showMockQuestion(){

    if(mockIndex >= mockQuestions.length){

        document.getElementById("mockQuestion")
            .innerText =
            "🎉 Mock Test Completed!";

        document.getElementById("mockOptions")
            .innerHTML = "";

        document.getElementById("mockResult")
            .innerText =
            "Your Score: "
            + mockScore
            + " / 10";

        if(mockScore > progress.bestMock){

            progress.bestMock = mockScore;

            saveProgress();

        }

        return;

    }


    let item =
        mockQuestions[mockIndex];


    document.getElementById("mockQuestion")
        .innerText =
        "Question "
        + (mockIndex + 1)
        + ": "
        + item.q;


    document.getElementById("mockResult")
        .innerText = "";


    let container =
        document.getElementById("mockOptions");

    container.innerHTML = "";


    shuffle(item.options)
    .forEach(option => {

        let button =
            document.createElement("button");

        button.className = "option";

        button.innerText = option;


        button.onclick = function(){

            let all =
                container.querySelectorAll(".option");

            all.forEach(btn => {

                btn.disabled = true;

                if(btn.innerText === item.answer){

                    btn.classList.add("correct");

                }

            });


            if(option === item.answer){

                button.classList.add("correct");

                mockScore++;

            }
            else{

                button.classList.add("wrong");

            }


            mockIndex++;


            setTimeout(
                showMockQuestion,
                700
            );

        };


        container.appendChild(button);

    });

}


/* =========================
   RESET
========================= */


function resetProgress(){

    if(confirm("Reset all N4 progress?")){

        progress = {
            answered:0,
            correct:0,
            bestMock:0
        };

        saveProgress();

        alert("Progress reset.");

    }

}


/* =========================
   INITIALIZATION
========================= */


updateProgress();

newHiragana();

newKatakana();

newKanji();

newVocabulary();

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
        "app": "JLPT N4 Practice",
        "port": 8030
    })


if __name__ == "__main__":

    print("=" * 50)
    print("JLPT N4 Practice Website")
    print("Running on http://127.0.0.1:8030")
    print("=" * 50)

    app.run(
        host="127.0.0.1",
        port=8030,
        debug=True
    )
