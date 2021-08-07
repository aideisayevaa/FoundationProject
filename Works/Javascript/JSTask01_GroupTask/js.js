let a = [1, 45, 67, 23, 78, 34, 45, 67, 67, 12, 457];

function count_duplicate(a){
 let counts = {}

 for(let i =0; i < a.length; i++){ 
     if (counts[a[i]]){
     counts[a[i]] += 1
     } else {
     counts[a[i]] = 1
     }
    }  
    for (let prop in counts){
        if (counts[prop] >= 2){
            console.log(prop + " counted: " + counts[prop] + " times.")
        }
    }
  console.log(counts)
}

count_duplicate(a)
/*  3 counted: 3 times.
    4 counted: 2 times.
    { '3': 3, '4': 2, '6': 1 }
*/