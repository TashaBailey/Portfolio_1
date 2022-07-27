// Change the image of bird depending on the button state.

// If button pressed is pardalote.

document.getElementById('pardalote').addEventListener('click', pardaloteImg);

function pardaloteImg() {
    // Change the image.
    document.getElementById('imageBird').src = 'http://www.outgrabe.net/bird00.jpg';
    // Change the paragraph.
    document.getElementById('paraBird').innerText = 'Pardalote by fir0002 (CC-by-NC)';
}

// If button pressed is Purple Swamp Hen.

document.getElementById('hen').addEventListener('click', henImg);

function henImg() {
    // Change the image.
    document.getElementById('imageBird').src = 'http://www.outgrabe.net/bird01.jpg';
    // Change the paragraph.
    document.getElementById('paraBird').innerText = 'Purple swamp hen by Toby Hudson (CC-by-SA)';
}

// If button pressed is White-headed Stilt.

document.getElementById('stilt').addEventListener('click', stiltImg);

function stiltImg() {
    // Change the image.
    document.getElementById('imageBird').src = 'http://www.outgrabe.net/bird02.jpg';
    // Change the paragraph.
    document.getElementById('paraBird').innerText = 'White-headed Stilt by JJ Harrison (CC-by-SA)';
}

// If button pressed is Inland Thornbill.

document.getElementById('thornbill').addEventListener('click', thornbillImg);

function thornbillImg() {
    // Change the image.
    document.getElementById('imageBird').src = 'http://www.outgrabe.net/bird03.jpg	';
    // Change the paragraph.
    document.getElementById('paraBird').innerText = 'Inland Thornbill by Peter Jacobs (CC-by-SA)';
}

// If button pressed is Rose Robin.

document.getElementById('robin').addEventListener('click', robinImg);

function robinImg() {
    // Change the image.
    document.getElementById('imageBird').src = 'http://www.outgrabe.net/bird04.jpg';
    // Change the paragraph.
    document.getElementById('paraBird').innerText = 'Rose Robin by JJ Harrison (CC-by-SA)';
}

// If button pressed is Change Theme.
// Dark and light mode activated.

function themeChange() {
    var themeChange = document.body;
    themeChange.classList.toggle('dark-mode')

    var colorChange = document.getElementById('paraBird');
    colorChange.classList.toggle('dark-mode')
}