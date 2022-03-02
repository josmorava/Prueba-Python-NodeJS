const fs= require('fs')

fs.readFile('./ejemplo3.txt','utf-8',(error,data)=>{
  if(error){
    console.log('Se a detectado un error', error)
  }

  //Contenido en el archivo de texto
  var cambio = [1,5,10,25,50]
  var numeros = data.split('\n')
  var numbers = []
  let addNumbers = numeros.forEach((numero)=>{
    numbers.push(Number(numero))
  })

  numbers.forEach((numero)=>{
    cambio.forEach((moneda)=>{
      if((numero/moneda) > 0.9){
        console.log(`Para ${numero} se puede dar cambio de ${moneda}`)
      }
    })
  })
  

})