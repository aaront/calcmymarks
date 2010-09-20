var counter = 1;
var limit = 20;
var min = 0;
function addInput(divName){
     if (counter == limit)  {
          alert("You have reached the limit of adding " + counter + " term marks.");
     }
     else {
          var newdiv = document.createElement('div');
          newdiv.className = "curr_array";
          newdiv.innerHTML = "\
				<div class='span-2'>\
					<p>I have <input type='text' name='curr' class='percentage' size='3'>%</p>\
				</div>\
				<div class='span-2'>\
					<p>\
						on <input type='text' name='eval' class='percentage' size='10'>\
					</p>\
				</div>\
				<div class='span-3 last'>\
					<p>worth <input type='text' name='tally' class='percentage' size='3'>% of the course</p>\
				</div>";
          document.getElementById(divName).appendChild(newdiv);
          counter++;
     }
}

function removeInput(divName) {
    if (counter <= 1)  {
          alert("You have to at least have 1 term mark!");
    }
    else {
        var d = document.getElementById(divName);
        d.removeChild(d.lastChild);
        counter--;
    }
}

function clickclear(thisfield, defaulttext) {
    if (thisfield.value == defaulttext) {
        thisfield.value = "";
    }
}

function clickrecall(thisfield, defaulttext) {
    if (thisfield.value == "") {
        thisfield.value = defaulttext;
    }
}