function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function receiveMessage(event) {
    var message = event.data;
    console.log(message);
    switch (message.messageType) {
        case "SCORE":
            saveGamescore(message);
            break;
        case "SAVE":
            saveGamestate(message);
            break;
        case "LOAD_REQUEST":
            requestGamestate(message);
            break;
        case "LOAD":
            loadGamestate(message);
            break;
        case "ERROR":
            throwError(message);
            break;
        case "SETTING":
            setSettings(message);
            break;
        default:
            console.log("MessageType not recognized.");
    }
}

function saveGamescore(message) {

}

function saveGamestate(message) {

}


function requestGamestate(message) {

}


function loadGamestate(message) {

}


function throwError(message) {

}


function setSettings(message) {

}
