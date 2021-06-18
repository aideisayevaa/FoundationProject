arr=[1,45,67,23,78,34,45,67,67,12,457]


//          1
//massivdəki tək ədəd sayını tapın

 let tekEdedSayi = 0;
for(i = 0; i < arr.length; i++){
    if(arr[i] % 2 != 0){
        tekEdedSayi++
    }
}

console.log(tekEdedSayi) 

//          2
//massivdəki cüt ədəd sayını tapın
arr=[1,45,67,23,78,34,45,67,67,12,457]

let cutEdedSayi = 0;
for(i = 0; i < arr.length; i++){ 
    if(arr[i] % 2 == 0){
        cutEdedSayi++ 
    }
}

console.log(cutEdedSayi) 


//          3
//massivdəki ədədlərin cəmini tapın
arr=[1,45,67,23,78,34,45,67,67,12,457]

 let cem = 0;
for(i = 0; i < arr.length; i++){
    cem = cem + arr[i]
}

console.log(cem) 

//          4
//massivdəki sondan 4 elemetin cemini tapın 

let sum = 0;
for(i = arr.length - 1; i >= arr.length - 4; i--){
    sum += arr[i]
}

console.log(sum)  

//          5
//massivdəki ən böyük ədədi tapın


 let enBoyukEded = arr[0];  
for(i = 0; i < arr.length; i++){
    if(arr[i]>=enBoyukEded){
        enBoyukEded = arr[i]
    }
}

console.log(enBoyukEded)

//          6
//massivdə təkrarlanan ədədləri ekrana çap edin
