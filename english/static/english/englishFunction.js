function vocaContentsChanger(){
    vocaEng = document.querySelectorAll('.voca_eng')
    vocaKor = document.querySelectorAll('.voca_kor')
    vocaSen = document.querySelectorAll('.voca_sentence')
    vocaTra = document.querySelectorAll('.voca_translate')

    vocaEng[0].innerHTML = hypeDocument.customData.voca[0]['word']
    vocaEng[1].innerHTML = hypeDocument.customData.voca[1]['word']

    vocaKor[0].innerHTML = hypeDocument.customData.voca[0]['mean']
    vocaKor[1].innerHTML = hypeDocument.customData.voca[1]['mean']

    vocaSen[0].innerHTML = hypeDocument.customData.voca[0]['sentence']
    vocaSen[1].innerHTML = hypeDocument.customData.voca[1]['sentence']

    vocaTra[0].innerHTML = hypeDocument.customData.voca[0]['translate']
    vocaTra[1].innerHTML = hypeDocument.customData.voca[1]['translate']
}
//ajax crsf 토큰 함수
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
