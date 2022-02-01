const realFileBtn = document.getElementById('real-file');
const customBtn = document.getElementById('custom-button');
const customTxt = document.getElementById('custom-text');
const audio = document.getElementById('audio-control');
const shortaudio = document.getElementById('shortaudio');
const audios = document.getElementById('audio-short')
const source = document.getElementById('src');
const result = document.getElementById('result-text');
const button1 = document.getElementById('button-1');
const button2 = document.getElementById('button-2');
const dropArea = document.querySelector(".drag-area"),
dragText = dropArea.querySelector("header"),
orText = document.getElementById("or"),
button = dropArea.querySelector("button");
const title = document.getElementById("title"); 

let file; 

const model = await tf.loadLayersModel('https://adrian-alu0101024363.github.io/SoundDeepWeb/model.json');
//console.log(model);
function bounceEffect() {
  title.style.fontSize = "0";
  gsap.to(title, 2, {fontSize: 30, ease: "bounce.out"});
}

function fadeIn(element) {
  let opacity = 0.1;
  element.style.display = 'block';
  let timer = setInterval(() => {
    if (opacity >= 1) {
      clearInterval(timer);
    }
    element.style.opacity = opacity;
    element.style.filter = 'alpha(opacity=' + opacity * 100 + ")";
    opacity += opacity * 0.1;
  }, 50);
}
fadeIn(title);
//bounceEffect();

customBtn.addEventListener('click', function() {
  realFileBtn.click();
});

realFileBtn.addEventListener('change', function() {
  let filePath = realFileBtn.value;
  dropArea.classList.add("active");
  let allowedExtensions = /(\.mp3|\.wav|\.m4a)$/i;
  if (allowedExtensions.exec(filePath)) {
    customTxt.innerHTML = realFileBtn.files[0].name;
    source.setAttribute('src', URL.createObjectURL(realFileBtn.files[0]));
    audio.load();
  } else {
    customTxt.innerHTML = "No file chosen yet";
  }
});

dropArea.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload File";
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("active");
  dragText.textContent = "Drop file to upload";
});

dropArea.addEventListener("drop", (event) => {
  event.preventDefault();
  file = event.dataTransfer.files[0];
  showFile();
});

function showFile() {
  let fileType = file.type;
  let allowedTypes = ["audio/mpeg", "audio/wav"];
  if (allowedTypes.includes(fileType)) {
    customTxt.innerHTML = file.name;
    source.setAttribute('src', URL.createObjectURL(file));
    audio.load();
    dragText.textContent = "File Uploaded";
    dragText.style.color = "#a58555";
    orText.textContent = "Drop new file to upload or";
  } else {
    alert("Please drop a mp3 , wav or m4a file");
    dropArea.classList.remove("active");
    dragText.textContent = "Drop file to upload";
  }
}

button1.addEventListener('click', function() {

});

button2.addEventListener('click', function() {

});
//Testo no tame
shortaudio.src = 'poli.mp3';
audios.load();