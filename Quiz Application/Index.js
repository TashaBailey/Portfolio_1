// quiz questions, stored as a object.
const quizData = [
    {
        question: "What does HTML stand for?",
        a: "Hyper Trainer Marking Language",
        b: "Hyper Text Marketing Language",
        c: "Hyper Text Markup Language",
        d: "Hyper Text Markup Leveler",
        correct: "c",
    },
    {
        question: "What does CSS stand for?",
        a: "Central Style Sheet",
        b: "Cascading Style Sheet",
        c: "Cascading Sheet Style",
        d: "Central Sheet Style",
        correct: "b",
    },
    {
        question: "What are the two binary numbers?",
        a: "1 and 2",
        b: "0 and 2",
        c: "8 and 3",
        d: "0 and 1",
        correct: "d",
    },
    {
        question: "What is the JavaScript file extension?",
        a: ".js",
        b: ".javascript",
        c: ".jvs",
        d: ".jss",
        correct: "a",
    },
];

// get the <div> - parent element
const quiz = document.getElementById('quiz');

// get all the classes that have a class of answer - <input> all
const answer_else = document.querySelectorAll('.answer');

// h2 element
const question_else = document.getElementById('question');

// label id's
const a_text = document.getElementById('a_text');
const b_text = document.getElementById('b_text');
const c_text = document.getElementById('c_text');
const d_text = document.getElementById('d_text');

// submit button
const submitBtn = document.getElementById('submit');

// variable for how many questions currentQuiz has (4)
let currentQuiz = 0;

// how many the user got correct
let score = 0;

// activate loadQuiz function
loadQuiz();

function loadQuiz(){
    // call function
    deselectAnswers()
    
    const currentQuizData = quizData[currentQuiz];
    question_else.innerText = currentQuizData.question;
    a_text.innerText = currentQuizData.a;
    b_text.innerText = currentQuizData.b;
    c_text.innerText = currentQuizData.c;
    d_text.innerText = currentQuizData.d;
};

function deselectAnswers(){
    answer_else.forEach(answer_else => {
        return answer_else.checked = false;
    })
};

function getSelected() {
    let answer
    answer_else.forEach(answer_else => {
        if(answer_else.checked){
            answer = answer_else.id
        }
    })
    return answer;
}

submitBtn.addEventListener('click', () => {
    const answer = getSelected();
    if (answer) {
        if (answer === quizData[currentQuiz].correct) {
            score++;
        }
        currentQuiz++;
        if (currentQuiz < quizData.length) {
            loadQuiz();
        } else {
            quiz.innerHTML = `
            <h2>You answered ${score}/${quizData.length} questions correctly</h2>
            
            <button onclick="location.reload()">Reload</button>
            `
        }
    }
})