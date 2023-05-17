function myFunction(elem) {
    elem = String(elem)
    document.getElementById(elem).classList.toggle("show");
}

function filterFunction(drop) {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    drop = String(drop)
    div = document.getElementById(drop);
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}

function filterFunction1(drop) {
    var input, filter, ul, li, a, i, chapter;
    chapter = document.querySelector('.events-input-filter');
    filter = chapter.value.toUpperCase();
    drop = String(drop)
    div = document.getElementById(drop);
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}