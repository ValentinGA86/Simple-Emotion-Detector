function RunSentimentAnalysis() {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        } else if (this.readyState == 4 && this.status == 400) {
            document.getElementById("system_response").innerHTML = "Invalid text! Please try again.";
        }
    };
    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("text=" + textToAnalyze);
}
