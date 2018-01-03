
window.onload = function() {

 //counter to change the current entry record
var navCounter = 1000;
var version = "NIV";

//creating the current entry number from the number of days since Jaanuary 1, 1970 + the day of the year
var now = new Date();
var start = new Date(now.getFullYear(), 0, 0);
var diff = now - start;
var oneDay = 1000 * 60 * 60 * 24;
var currentDay = Math.floor(diff / oneDay);
currentDay = currentDay + 17166;
var d = new Date();
var n = d.getFullYear(); 
if (n = 2018){
  currentDay = currentDay + 365
}

// Turns a verse into a link to biblegateway for that verse
function verseLink(verse){
  var gatewayLinkMain = "https://www.biblegateway.com/passage/?search=";
  if (verse.includes("(")){
    verse = verse.split("(");
    link = gatewayLinkMain + verse[0] + "&version=" + version;
  }
  else {
    link = gatewayLinkMain + verse + "&version=" + version;
  }
  return link
}

// checks for a "(" which would indicate a special translation and changes the global version variable
function versionCheck(verse){
  if (verse.includes("(")){
    verse = verse.split("(");
    version = verse[1].replace(/(\))/g, "");
  }
}

//defines the main function
function main(){

//Grabs todays entry based on date and navagation number
var current_entry_log = (currentDay + navCounter)-1000;
var current_entry = myObj[(currentDay + navCounter)-1000];

// Test variables below
//var current_entry_log = (17194 + navCounter)-1000;
//var current_entry = myObj[(17194 + navCounter) - 1000];

// Splits the text from a single verse, addes the verse to the specified element as a link and returns the text of the line
function getVerse(txt, linkEle){
  verse = txt.substr(txt.lastIndexOf(".")+1);
  txt = txt.substr(0, txt.lastIndexOf(".")+1);
  versionCheck(verse);
  document.getElementById(linkEle).setAttribute("href", verseLink(verse));
  document.getElementById(linkEle).setAttribute("target", "_blank");
  document.getElementById(linkEle).innerHTML = verse;
  version = "NIV";
  return txt;
}

// Adds the remaining text lines to the correct elements and makes verse links from watch and doc lines
function finishShort(watch, doc, prayer){
  document.getElementById("watchp").innerHTML = getVerse(watch, "watcha");
  document.getElementById("docp").innerHTML = getVerse(doc, "doca");
  document.getElementById("prayer").innerHTML = prayer;
}


function addSixLines(offSet){

  // Removes the seven lines function elements
  var extraInfoDiv = document.getElementById("extraInfoD");
  var sevenLinesInfoP = document.getElementById("extraInfoP");
  if (sevenLinesInfoP != null){
    extraInfoDiv.removeChild(sevenLinesInfoP);
  }

  // Removes the eight lines function elements
  var watchWeekD = document.getElementById("watchWeekD");
  var watchWeekH = document.getElementById("watchWeekH");
  var eightLinesInfoP = document.getElementById("watchWeekP");
  var eightLinesInfoA = document.getElementById("watchWeekA")
  if (eightLinesInfoP != null){
    watchWeekD.removeChild(eightLinesInfoP);
    watchWeekD.removeChild(watchWeekH);
    watchWeekD.removeChild(eightLinesInfoA);
  }

  //Grabbing the info from the JSON file and converting it to a string
  var currentLine = JSON.stringify(current_entry["line" + (1 + offSet).toString()]);
  currentLine = currentLine.replace(/"/g,"");
  var splitCurrentLine = currentLine.split("-");
  var date = splitCurrentLine[0];
  document.getElementById("date").innerHTML = date;
  console.log("The date is : " + date);
  if (splitCurrentLine[2] != null) {
    var firstVerse = splitCurrentLine[1] + "-" + splitCurrentLine[2];
  } else
  {
    var firstVerse = splitCurrentLine[1];
  }
  //Checks for multipule verses in the date line and adds the verse if present
  if (firstVerse.includes(";")){
    var verse1Split = firstVerse.split(";");
    console.log("The verse1Split is: " + verse1Split);
    var verse1 = verse1Split[0];
    var verse2 = verse1Split[1];
    document.getElementById("script1").innerHTML = verse1;
    versionCheck(verse1);
    document.getElementById("script1").setAttribute("href", verseLink(verse1));
    document.getElementById("script1").setAttribute("target", "_blank");
    version = "NIV";
    document.getElementById("tab1").innerHTML= "<span>&emsp;</span>";
    document.getElementById("script2").innerHTML = verse2;
    versionCheck(verse2);
    document.getElementById("script2").setAttribute("href", verseLink(verse2));
    document.getElementById("script2").setAttribute("target", "_blank");
    version = "NIV";
    document.getElementById("tab2").innerHTML= "<span>&emsp;</span>";
    currentLine = JSON.stringify(current_entry["line" + (2 + offSet).toString()]);
    currentLine = currentLine.replace(/"/g,"");
    currentLineSplit = currentLine.split(";");
    console.log("The currentLineSplit in first includes ';': " + currentLineSplit);
    console.log("The current length of currentLineSplit is: " + currentLineSplit.length);
    // Adds all verses to the script elements
    for (i=0; i < currentLineSplit.length; i++){
      document.getElementById("script" + (i + 3)).innerHTML = currentLineSplit[i];
      versionCheck(currentLineSplit[i]);
      document.getElementById("script" + (i + 3)).setAttribute("href", verseLink(currentLineSplit[i]));
      document.getElementById("script" + (i + 3)).setAttribute("target", "_blank");
      version = "NIV";
      document.getElementById("tab" + (i + 3)).innerHTML= "<span>&emsp;</span>";
    }
    finishShort(current_entry["line" + (3 + offSet).toString()], current_entry["line" + (4 + offSet).toString()], current_entry["line" +(5 + offSet).toString()]);
  }
  else{
    // If date info only on this line do this
    document.getElementById("script1").innerHTML = firstVerse;
    versionCheck(firstVerse); //changes the global var for version
    document.getElementById("script1").setAttribute("href", verseLink(firstVerse));
    document.getElementById("script1").setAttribute("target", "_blank");
    version = "NIV";// changes the global version back to default
    document.getElementById("tab1").innerHTML= "<span>&emsp;</span>";
    currentLine = JSON.stringify(current_entry["line" + (2 + offSet).toString()]);
    currentLine = currentLine.replace(/"/g,"");
    currentLineSplit = currentLine.split(";");
    console.log("The currentLineSplit is: " + currentLineSplit);

    // Checks for a fourth verse and clears the script4 element if not present
    if (currentLineSplit.length < 3) {
      document.getElementById("script4").innerHTML = "";
    }

    // Adds the verses to the script elements and turns them into links
    for (i=0; i < currentLineSplit.length; i++){
      document.getElementById("script" + (i + 2)).innerHTML = currentLineSplit[i];
      versionCheck(currentLineSplit[i]);
      document.getElementById("script" + (i + 2)).setAttribute("href", verseLink(currentLineSplit[i]));
      document.getElementById("script" + (i + 2)).setAttribute("target", "_blank");
      version = "NIV";
      document.getElementById("tab" + (i + 2)).innerHTML= "<span>&emsp;</span>";
  }
  finishShort(current_entry["line" + (3 + offSet).toString()], current_entry["line" + (4 + offSet).toString()], current_entry["line" +(5 + offSet).toString()]);
}
};


function addSevenLines(offest){
  addSixLines(offest);
  firstLine = JSON.stringify(current_entry["line1"]);
  firstLine = firstLine.replace(/"/g,"");

  // Creates an h3 element for the alpha only text line
  var pElement = document.createElement("h3");
  pElement.setAttribute("id", "extraInfoP");
  pElement.setAttribute("display", "inline-block");
  var line1Text = document.createTextNode(firstLine);
  pElement.appendChild(line1Text);
  var element = document.getElementById("extraInfoD");
  element.appendChild(pElement);
}

function addEightLines(){
  addSevenLines(2);
 var currentLine = JSON.stringify(current_entry["line2"]);
 currentLine = currentLine.split("-");
 var watchWeekHeaderText = currentLine[0].replace(/"/g,"");

// Creates an h3 header for the line text up to the "-"
 var WWHeading = document.createElement("h3");
 WWHeading.setAttribute("id", "watchWeekH");
 WWHeading.style = "display : block"
 var watchWeekD = document.getElementById("watchWeekD");
 watchWeekD.appendChild(WWHeading);
 document.getElementById("watchWeekH").innerHTML = watchWeekHeaderText;

// Creates a paragraph element for the line text from "-" to the start of the verse
 var watchWeekP = document.createElement("p");
 watchWeekP.setAttribute("id", "watchWeekP");
 watchWeekD.appendChild(watchWeekP);

// Creates an anchor element for the verse
currentLine.shift();
currentLine = currentLine.join(",");
 var watchWeekBodyText = currentLine.replace(/"/g, "");
 var watchWeekA = document.createElement('a');
 watchWeekA.setAttribute("id", "watchWeekA");
 watchWeekD.appendChild(watchWeekA);
 document.getElementById("watchWeekP").innerHTML = getVerse(watchWeekBodyText, "watchWeekA");

}

// This if statment looks for the line count and calles the approprate function for that
if (current_entry["line_count"] == 6){
  addSixLines(0);
}
else if (current_entry["line_count"] == 7){
  addSevenLines(1);
}
else if (current_entry["line_count"] == 8){
  addEightLines();
}
else {
  addAllElse();
  console.log("The line_count did not match 6, 7 or 8");
}

//Hides the previous button if date entry is not found (null) This would happen if you were at the first entry
if (current_entry_log == Object.keys(myObj)[0]){
  document.getElementById("previous").style.visibility = "hidden";
}
 else {
  document.getElementById("previous").style.visibility = "visible";
};

//Hides the next button if current day is displayed
if (current_entry_log >= 17896){ //hardcoing is bad, mmkay
  document.getElementById("next").style.visibility = "hidden";
}
 else {
  document.getElementById("next").style.visibility = "visible";
};

//defines button function. when pressed-increment or decrement the navCounter and reloads the main function
document.getElementById("previous").onclick = function () {
  navCounter -= 1;
  main(); };
document.getElementById("next").onclick = function () {
  navCounter += 1;
  main();};

};

main();
}
