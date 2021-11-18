function getDOM(){
    var findElement,i,message="",result;
    findElement=document.forms["frmDOM"];
    for(i=0;i<findElement.length;i++){
        message+=findElement[i].value; //formdaki elementlerin deyeri -> value
    }
    result=document.querySelector("#result")
    result.innerHTML=findElement.length; //bunu yazandan sonra 2 cixir cunki form daxilinde 
    // 2 input var eger butonu da form daxilinde yazmis olsaydiq onda 3 cixardi

}