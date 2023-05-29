function myFunction(elem) {
    elem = String(elem)
    document.getElementById(elem).classList.toggle("show");
}

function filterFunction(drop) {
    var filter, a, i, chapter;
    chapter = document.querySelector('#' + drop + ' .events-input-filter');
    filter = chapter.value.toUpperCase();
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