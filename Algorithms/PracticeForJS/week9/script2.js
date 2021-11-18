ededler=[1,4,3,5,7,2,6] //1+3+7+6=17   //4+5+2=11

let cem = 0
function CutEdedlerinCemi(){
    
    for(i=0;i<ededler.length;i++){
        if(ededler[i]%2==0){
            cem+=ededler[i]
        }
    }
    
    console.log("Ededler massivindeki cut ededlerin cemi: "+cem)
}

CutEdedlerinCemi()