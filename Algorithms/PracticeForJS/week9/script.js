telebeler=[
    {
        ad:'Nurlan',
        soyad:'Heseneliyev',
        yas:45
    },
    {
        ad:'Elekber',
        soyad:'Tagiyev',
        yas:23,
    },
    {
        ad:'Seda',
        soyad:'Babayeva',
        yas:29
    }

]

function AdaGoreTelebeTap(yas){
    for(i=0;i<telebeler.length;i++){
        if(telebeler[i].yas>yas){
            console.log(telebeler[i].ad,telebeler[i].soyad)
        }
    }
}

AdaGoreTelebeTap(25)