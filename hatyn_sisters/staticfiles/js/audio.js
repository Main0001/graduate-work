function soundStart() {
    document.getElementsByClassName('sound-on')[0].style.display="none";
    var audio = document.getElementById('audio');
      audio.play();
    document.getElementsByClassName('sound-off')[0].style.display="block";
}

function soundStop() {
    document.getElementsByClassName('sound-off')[0].style.display="none";
    var audio = document.getElementById('audio');
      audio.pause();
    document.getElementsByClassName('sound-on')[0].style.display="block";
}