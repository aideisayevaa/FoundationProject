/* var findElement = document.getElementById('result');
alert(findElement.innerText); */
//-------------------------------------------------

/* var findElement = document.getElementsByName('resultName');
alert(findElement[3].innerText); *///innerHTML de yaza bilerik
//bu bir array verdiyi ucun [3] yazdiq
//-------------------------------------------------

//for ile de yaza bilerik birbir yazmayaq deye
/* var findElement = document.getElementsByName('resultName');

    var message="",i;
    for(i=0;i<findElement.length;i++){
        message+=findElement[i].innerHTML+'\n';
    }
    alert(message); */


//-------------------------------------------------
/* var findElement = document.getElementsByTagName('h5');
alert(findElement[0].innerHTML) */

//-------------------------------------------------
/* 
var findElement = document.getElementsByTagName('p');
var message="",i;
    for(i=0;i<findElement.length;i++){
        message+=findElement[i].innerHTML+'\n';
    }
    alert(message); */



//---------------------------------------

/* var findElement = document.getElementsByClassName('color');
alert(findElement[0].innerHTML) */

//---------------------------------------
//color clasina aid butun hamisini getirir
/* var findElement = document.getElementsByClassName('color');
var message="",i;
    for(i=0;i<findElement.length;i++){
        message+=findElement[i].innerHTML+'\n';
    }
    alert(message); */


//--------------------------------
/* var findElement = document.querySelector('.color');
alert(findElement.innerHTML)
 */
//--------------------------------
/* var findElement = document.querySelectorAll('.color');
var message="",i;
    for(i=0;i<findElement.length;i++){
        message+=findElement[i].innerHTML+'\n';
    }
    alert(message); */


//---------------------
// eger bir class meselen hem p daxilinde hem span daxilindedi ve biz span daxilindekini cagirmaliyiqsa onda:
/* var findElement = document.querySelector('span.color'); */


//----------------------------------
//attribute cagirma
/* 
var findElement = document.querySelectorAll("[name]");
var message="",i;
    for(i=0;i<findElement.length;i++){
        message+=findElement[i].innerHTML+'\n';
    }
    alert(message); */


/* 

var findElement = document.querySelector("[name=resaultName2]");//name-ler arasinda daxilinde resaultName2 yazilani getirir
alert(findElement.innerHTML) */


