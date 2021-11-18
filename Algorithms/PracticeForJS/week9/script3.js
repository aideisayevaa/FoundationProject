ededler=[1,4,3,5,7,2,6] 

let cem=0;
function TekYerdeDuranEdedlerinCemi(){
    
    for(i=0;i<ededler.length;i++){
        if(i%2==0){
            cem+=ededler[i]
        }
    }
    
    console.log("Tek yerde duran ededlerin cemi: "+cem)
}

TekYerdeDuranEdedlerinCemi()