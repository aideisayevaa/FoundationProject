/* 
arr=[1,67,67,23,78]
 
let tekrarlananEded0 = arr[0]
for(i = 1; i < arr.length; i++){
    if(arr[i] == tekrarlananEded0){
        console.log(tekrarlananEded0)
    }
}

let tekrarlananEded1 = arr[1]
for(i = 2; i < arr.length; i++){
    if(arr[i] == tekrarlananEded1){
        console.log(tekrarlananEded1)
    }
}
let tekrarlananEded2 = arr[2]
for(i = 3; i < arr.length; i++){
    if(arr[i] == tekrarlananEded2){
        console.log(tekrarlananEded2)
    }
}

let tekrarlananEded3 = arr[3]
for(i = 4; i < arr.length; i++){
    if(arr[i] == tekrarlananEded3){
        console.log(tekrarlananEded3)
    }
} */
 
let say = 0;
for(i = 0; i < arr.length; i++){
    let tekrarSayi = 0;
    for(j = i; j < arr.length; j++){
        say = 0
        if(arr[j] == say){
            console.log(arr[i])
            say++
        }

    }

    if(say > 1){
      tekrarSayi++
    }
} 


