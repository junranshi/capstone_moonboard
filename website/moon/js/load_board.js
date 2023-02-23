function random_climb() {
    // find grade selected by the user
    var grade = document.querySelector('input[name="grade"]:checked').value;
    // if random: randomly choose grade from 0 to 6
    if (grade == "random") {
        grade = Math.floor(Math.random() * 7);
    }
    // find index of route based on the grade chosen
    var index = Math.floor(Math.random() * 19) + grade * 19;
    // load route image
    var background = document.querySelector('[title="MoonBoard Wall"]');
    background.style.backgroundImage = "url(../img/routes/"+String(grade)+"/"+String(index)+".jpeg)";
    // find and display classified grade
    display_grades(index);
}


function display_grades(index) {
    var container = document.getElementsByClassName("grade");
    // display grade
    for (var i = 0; i < container.length; i++) {
        if (generated_climbs[index][container.item(i).id] == 6) {
            container.item(i).innerText = "V"+String(generated_climbs[index][container.item(i).id]+4)+"+";
        }
        else {
            container.item(i).innerText = "V"+String(generated_climbs[index][container.item(i).id]+4);
        }
    }
}
