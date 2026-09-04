from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>JLPT N3 Practice</title>

<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

body {
    background: #f4f6fa;
    color: #222;
}

/* HEADER */

header {
    background: linear-gradient(135deg, #4a0e0e, #b71c1c);
    color: white;
    text-align: center;
    padding: 32px 20px;
}

header h1 {
    font-size: 36px;
    margin-bottom: 8px;
}

header p {
    opacity: 0.9;
}

/* NAVIGATION */

nav {
    background: white;
    padding: 12px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

nav button {
    border: none;
    padding: 10px 14px;
    border-radius: 20px;
    background: #eeeeee;
    cursor: pointer;
    font-weight: bold;
}

nav button:hover {
    background: #b71c1c;
    color: white;
}

/* CONTAINER */

.container {
    max-width: 1150px;
    margin: auto;
    padding: 25px;
}

.section {
    display: none;
}

.section.active {
    display: block;
}

/* HERO */

.hero {
    background: white;
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

.hero h2 {
    color: #b71c1c;
    margin-bottom: 10px;
}

/* CARDS */

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 18px;
}

.card {
    background: white;
    padding: 23px;
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

/* PRACTICE */

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
    color: #b71c1c;
    margin: 20px;
}

.meaning {
    font-size: 21px;
    margin: 15px;
}

.question {
    font-size: 22px;
    font-weight: bold;
    margin: 20px;
}

/* BUTTON */

.btn {
    border: none;
    background: #b71c1c;
    color: white;
    padding: 12px 22px;
    border-radius: 10px;
    cursor: pointer;
    font-weight: bold;
    margin: 7px;
}

.btn:hover {
    background: #7f0000;
}

/* OPTIONS */

.options {
    display: grid;
    grid-template-columns: repeat(2, minmax(150px, 1fr));
    gap: 12px;
    max-width: 700px;
    margin: 20px auto;
}

.option {
    background: #f5f5f5;
    border: 2px solid #ddd;
    padding: 15px;
    border-radius: 10px;
    cursor: pointer;
    font-size: 17px;
}

.option:hover {
    border-color: #b71c1c;
}

.option:disabled {
    cursor: default;
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
    margin: 18px;
}

/* READING */

.reading {
    background: #fafafa;
    border-left: 5px solid #b71c1c;
    padding: 22px;
    text-align: left;
    line-height: 2.1;
    border-radius: 8px;
    margin: 20px 0;
    font-size: 18px;
}

/* STATS */

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
    color: #b71c1c;
    font-size: 32px;
    margin-bottom: 8px;
}

/* PROGRESS */

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
    background: #b71c1c;
    transition: 0.4s;
}

/* FOOTER */

footer {
    text-align: center;
    padding: 30px;
    color: #777;
}

/* MOBILE */

@media(max-width:600px) {

    header h1 {
        font-size: 28px;
    }

    .options {
        grid-template-columns: 1fr;
    }

    .japanese {
        font-size: 45px;
    }

    nav button {
        font-size: 11px;
        padding: 8px 10px;
    }

}

</style>

</head>


<body>


<header>

<h1>🇯🇵 JLPT N3 Practice</h1>

<p>Build stronger Japanese reading, grammar and vocabulary skills</p>

</header>


<nav>

<button onclick="showSection('home')">🏠 Home</button>

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

<h2>JLPT N3 Learning Dashboard</h2>

<p>
Practice intermediate Japanese vocabulary, Kanji,
grammar, reading and listening.
</p>

</div>


<div class="cards">


<div class="card" onclick="showSection('kanji')">

<div class="icon">漢</div>

<h3>N3 Kanji</h3>

<p>Practice commonly used intermediate Kanji.</p>

</div>


<div class="card" onclick="showSection('vocabulary')">

<div class="icon">📚</div>

<h3>N3 Vocabulary</h3>

<p>Expand your Japanese vocabulary.</p>

</div>


<div class="card" onclick="showSection('grammar')">

<div class="icon">📝</div>

<h3>N3 Grammar</h3>

<p>Practice intermediate grammar patterns.</p>

</div>


<div class="card" onclick="showSection('reading')">

<div class="icon">📖</div>

<h3>Reading</h3>

<p>Practice reading longer Japanese passages.</p>

</div>


<div class="card" onclick="showSection('listening')">

<div class="icon">🔊</div>

<h3>Listening</h3>

<p>Practice Japanese sentences using speech.</p>

</div>


<div class="card" onclick="showSection('quiz')">

<div class="icon">🎯</div>

<h3>Quiz</h3>

<p>Test your N3 knowledge.</p>

</div>


<div class="card" onclick="showSection('mock')">

<div class="icon">🏆</div>

<h3>Mock Test</h3>

<p>Take a 10-question N3-style test.</p>

</div>


<div class="card" onclick="showSection('progress')">

<div class="icon">📊</div>

<h3>Progress</h3>

<p>Track your learning performance.</p>

</div>


</div>

</section>


<!-- KANJI -->

<section id="kanji" class="section">

<div class="hero">

<h2>漢 N3 Kanji Practice</h2>

<p>Learn useful intermediate Kanji.</p>

</div>


<div class="practice-box">

<div class="japanese" id="kanjiChar">
経験
</div>

<div class="meaning" id="kanjiMeaning">
Experience
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

<h2>📚 N3 Vocabulary</h2>

<p>Learn intermediate Japanese vocabulary.</p>

</div>


<div class="practice-box">

<div class="japanese" id="vocabWord">
経験
</div>

<div class="meaning" id="vocabMeaning">
Experience
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

<h2>📝 N3 Grammar Practice</h2>

<p>Practice important intermediate grammar structures.</p>

</div>


<div class="practice-box">

<div class="question" id="grammarQuestion">

日本に行った ___ がありません。

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

<h2>📖 N3 Reading Practice</h2>

<p>Read the passage and answer the question.</p>

</div>


<div class="practice-box">


<div class="reading">

最近、日本では健康のために運動を始める人が増えています。

特に、仕事の前や仕事の後にウォーキングをする人が多いです。

運動をすると体が健康になるだけでなく、
気分もよくなると言われています。

しかし、毎日長い時間運動する必要はありません。

短い時間でも、続けることが大切です。

</div>


<div class="question">

健康のために大切なことは何ですか？

</div>


<div class="options" id="readingOptions"></div>


<div id="readingResult"></div>


</div>

</section>


<!-- LISTENING -->

<section id="listening" class="section">

<div class="hero">

<h2>🔊 N3 Listening Practice</h2>

<p>
Use your browser's Japanese text-to-speech system.
</p>

</div>


<div class="practice-box">


<div class="japanese">

最近、日本語を勉強する時間が増えました。

</div>


<div class="meaning">

Recently, the amount of time I study Japanese has increased.

</div>


<button class="btn"
onclick="speakJapanese('最近、日本語を勉強する時間が増えました。')">

🔊 Play

</button>


<br>


<button class="btn"
onclick="speakJapanese('来週、友達と京都へ旅行する予定です。')">

🔊 Sentence 2

</button>


<button class="btn"
onclick="speakJapanese('毎日少しずつ練習することが大切です。')">

🔊 Sentence 3

</button>


</div>

</section>


<!-- QUIZ -->

<section id="quiz" class="section">

<div class="hero">

<h2>🎯 N3 Quiz</h2>

<p>Test your vocabulary and grammar.</p>

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


<!-- MOCK -->

<section id="mock" class="section">

<div class="hero">

<h2>🏆 N3-Style Mini Mock Test</h2>

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
🇯🇵 JLPT N3 Practice Website | Built with Python + Flask
</p>

</footer>


<script>


/* ==========================
   N3 KANJI
========================== */


const kanji = [

["経験","Experience"],
["必要","Necessary"],
["問題","Problem / Question"],
["理由","Reason"],
["意味","Meaning"],
["場合","Case / Situation"],
["関係","Relationship"],
["社会","Society"],
["世界","World"],
["生活","Life / Living"],
["文化","Culture"],
["教育","Education"],
["経済","Economy"],
["政治","Politics"],
["自然","Nature"],
["環境","Environment"],
["情報","Information"],
["技術","Technology"],
["研究","Research"],
["結果","Result"],
["原因","Cause"],
["方法","Method"],
["意見","Opinion"],
["準備","Preparation"],
["予定","Plan / Schedule"],
["約束","Promise"],
["説明","Explanation"],
["注意","Attention / Caution"],
["参加","Participation"],
["成功","Success"],
["失敗","Failure"],
["変化","Change"],
["増加","Increase"],
["減少","Decrease"],
["確認","Confirmation"],
["連絡","Contact"],
["利用","Use / Utilization"],
["選択","Choice"],
["決定","Decision"],
["比較","Comparison"]

];


/* ==========================
   N3 VOCABULARY
========================== */


const vocabulary = [

["経験","Experience"],
["必要","Necessary"],
["便利","Convenient"],
["複雑","Complicated"],
["簡単","Simple"],
["危険","Dangerous"],
["安全","Safe"],
["特別","Special"],
["普通","Normal / Ordinary"],
["十分","Enough"],
["急に","Suddenly"],
["特に","Especially"],
["最近","Recently"],
["将来","Future"],
["最初","First"],
["最後","Last"],
["途中","Middle / On the way"],
["場合","Case"],
["理由","Reason"],
["目的","Purpose"],
["方法","Method"],
["結果","Result"],
["原因","Cause"],
["意見","Opinion"],
["社会","Society"],
["生活","Life"],
["環境","Environment"],
["情報","Information"],
["技術","Technology"],
["文化","Culture"],
["研究","Research"],
["準備","Preparation"],
["予定","Plan"],
["約束","Promise"],
["参加","Participation"],
["確認","Confirmation"],
["連絡","Contact"],
["利用","Use"],
["選ぶ","Choose"],
["決める","Decide"]

];


/* ==========================
   N3 GRAMMAR
========================== */


const grammar = [

{
q:"日本に行った ___ がありません。",
options:["こと","もの","ため","ところ"],
answer:"こと"
},

{
q:"雨が降っている ___、出かけます。",
options:["のに","ので","から","まで"],
answer:"のに"
},

{
q:"この問題は難し ___ ます。",
options:["すぎ","すぎる","すぎて","すぎた"],
answer:"すぎ"
},

{
q:"健康のために、毎日運動する ___ にしています。",
options:["よう","こと","ため","もの"],
answer:"よう"
},

{
q:"忘れない ___ に、メモしてください。",
options:["よう","こと","ため","もの"],
answer:"よう"
},

{
q:"日本語を勉強すれば ___ ほど上手になります。",
options:["する","した","して","しない"],
answer:"する"
},

{
q:"彼は来る ___ 言っていました。",
options:["と","を","に","が"],
answer:"と"
},

{
q:"電車に乗り遅れない ___ 早く家を出ました。",
options:["ように","ために","ので","のに"],
answer:"ように"
},

{
q:"この店は駅から近い ___、とても便利です。",
options:["ので","のに","ほど","しか"],
answer:"ので"
},

{
q:"日本へ行く ___、日本語を勉強しています。",
options:["ために","ように","のに","ので"],
answer:"ために"
}

];


/* ==========================
   QUIZ
========================== */


const quizData = [

{
q:"「経験」の意味は？",
options:["Experience","Reason","Result","Problem"],
answer:"Experience"
},

{
q:"「必要」の意味は？",
options:["Necessary","Convenient","Dangerous","Special"],
answer:"Necessary"
},

{
q:"「最近」の意味は？",
options:["Recently","Future","Usually","Finally"],
answer:"Recently"
},

{
q:"「理由」の意味は？",
options:["Reason","Method","Result","Culture"],
answer:"Reason"
},

{
q:"「環境」の意味は？",
options:["Environment","Economy","Society","Technology"],
answer:"Environment"
},

{
q:"「失敗」の反対の意味は？",
options:["成功","変化","減少","原因"],
answer:"成功"
},

{
q:"「予定」の意味は？",
options:["Plan / Schedule","Promise","Research","Opinion"],
answer:"Plan / Schedule"
},

{
q:"「利用する」の意味は？",
options:["Use","Choose","Forget","Explain"],
answer:"Use"
},

{
q:"日本に行った ___ がありません。",
options:["こと","もの","ため","ところ"],
answer:"こと"
},

{
q:"忘れない ___ にメモしてください。",
options:["よう","こと","ので","ほど"],
answer:"よう"
}

];


/* ==========================
   MOCK TEST
========================== */


const mockQuestions = [

{
q:"「経験」の意味は？",
options:["Experience","Information","Culture","Environment"],
answer:"Experience"
},

{
q:"「必要」の意味は？",
options:["Necessary","Special","Dangerous","Normal"],
answer:"Necessary"
},

{
q:"日本に行った ___ がありません。",
options:["こと","もの","ため","ところ"],
answer:"こと"
},

{
q:"「最近」の意味は？",
options:["Recently","Future","First","Last"],
answer:"Recently"
},

{
q:"忘れない ___ にしてください。",
options:["よう","こと","ので","ほど"],
answer:"よう"
},

{
q:"「成功」の反対は？",
options:["失敗","原因","結果","変化"],
answer:"失敗"
},

{
q:"「環境」の意味は？",
options:["Environment","Society","Economy","Research"],
answer:"Environment"
},

{
q:"日本語を勉強すればする ___ 上手になります。",
options:["ほど","ので","ため","こと"],
answer:"ほど"
},

{
q:"「予定」の意味は？",
options:["Plan / Schedule","Promise","Reason","Result"],
answer:"Plan / Schedule"
},

{
q:"彼は来る ___ 言いました。",
options:["と","を","に","が"],
answer:"と"
}

];


/* ==========================
   PROGRESS
========================== */


let progress =
JSON.parse(localStorage.getItem("jlptN3Progress"))
|| {
    answered: 0,
    correct: 0,
    bestMock: 0
};


function saveProgress(){

    localStorage.setItem(
        "jlptN3Progress",
        JSON.stringify(progress)
    );

    updateProgress();

}


function updateProgress(){

    document.getElementById("totalAnswered")
        .innerText = progress.answered;

    document.getElementById("correctAnswers")
        .innerText = progress.correct;


    let accuracy =
        progress.answered === 0
        ? 0
        : Math.round(
            (progress.correct /
            progress.answered) * 100
        );


    document.getElementById("accuracy")
        .innerText = accuracy + "%";


    document.getElementById("mockScore")
        .innerText =
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
        percentage +
        "% learning progress completed.";

}


/* ==========================
   NAVIGATION
========================== */


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
        top: 0,
        behavior: "smooth"
    });


    if(id === "progress"){
        updateProgress();
    }

}


/* ==========================
   SHUFFLE
========================== */


function shuffle(array){

    return [...array]
    .sort(() => Math.random() - 0.5);

}


/* ==========================
   OPTIONS
========================== */


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


/* ==========================
   KANJI
========================== */


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


/* ==========================
   VOCABULARY
========================== */


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


/* ==========================
   GRAMMAR
========================== */


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


/* ==========================
   READING
========================== */


function setupReading(){

    createOptions(

        document.getElementById("readingOptions"),

        [
            "毎日長い時間運動すること",
            "短い時間でも運動を続けること",
            "運動をしないこと",
            "仕事の前だけ運動すること"
        ],

        "短い時間でも運動を続けること",

        document.getElementById("readingResult")

    );

}


/* ==========================
   SPEECH
========================== */


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


/* ==========================
   QUIZ
========================== */


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


/* ==========================
   MOCK TEST
========================== */


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

            progress.bestMock =
                mockScore;

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


/* ==========================
   RESET
========================== */


function resetProgress(){

    if(confirm("Reset all N3 progress?")){


        progress = {

            answered: 0,

            correct: 0,

            bestMock: 0

        };


        saveProgress();


        alert("Progress reset.");

    }

}


/* ==========================
   INITIALIZE
========================== */


updateProgress();

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
        "app": "JLPT N3 Practice",
        "port": 8031
    })


if __name__ == "__main__":

    print("=" * 55)
    print("🇯🇵 JLPT N3 Practice Website")
    print("Running on http://127.0.0.1:8031")
    print("=" * 55)

    app.run(
        host="127.0.0.1",
        port=8031,
        debug=True
    )
