//  MODO
//
//  El modo fácil sólo se pueden leer palabras de izq. a der. o 
//  de arriba a abajo
//
//  El modo medio añade de izq. a der. en diagonal.
//
//  El modo difícil permite al revés en todo. De der. a izq., 
//  de der. a izq. en diagonal  y de abajo a arriba.

//

var MODO = '2' // 1 - Fácil, 2 - Medio, 3 - Difícil



async function cargaDatos(fichero){
  const request = new XMLHttpRequest();
  request.open("GET", 'listados_palabras/'+fichero, false); // `false` makes the request synchronous
  request.send(null);

  if (request.status === 200) {
    return request.responseText;
  }
  return null;
}

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

function getRandomChar() {
  return String.fromCharCode(0|Math.random()*26+97);
}

//






window.onload = (event) => {

  //1º Cojo los datos 
  //2º Obtengo y cuento el fichero
  //3º Genero el array del tamaño que necesitaré
  //4º Pueblo el array con los datos del fichero
  //5º Pueblo el array de nuevo con datos aleatorios

  //1º Cojo los datos
  //TODO
  //2º Obtengo y cuento el fichero
  var size = 24;
  //tamaño fijo de 24x24
  var response = cargaDatos('banco.txt');

  response.then(function(result) {
    //size = ((result.split(/\r\n|\r|\n/).length)/2)+1;

    //3ª Genero el array del tamaño que necesitaré
    var arraySopaLetras = new Array(size);

    for (var i = 0; i < arraySopaLetras.length; i++) {
      arraySopaLetras[i] = new Array(size);
    }
    //tengo el array de la tabla
   



    //4º Pueblo el array con los datos del fichero
    var datos_fichero = result.split(/\r\n|\r|\n/);

 
    for (var i = 0; i < datos_fichero.length; i++) {
      
      var palabra = datos_fichero[i];

      var arrayLetrasPalabra = Array.from(palabra);
      
      var posX;
      var posY;
      

      switch (MODO) {
        case '2':
        case '3':
        case '1':
        default:
          //calculo las letras de la palabra
          var numLetrasPalabra = arrayLetrasPalabra.length;
          //saco infinitas posiciones aleatorias hasta que consiga una en la que me quepa la palabra completa 
          var posicion = false;

          // 0->izq-drcha, 1->arriba->abajo
          // 2->drcha-abajo, 3->drcha->arriba
          var direccion = getRandomInt(4);
          console.log("d: "+direccion); 

          while(posicion == false){
            
          
            //si vamos de izq a derecha, realizamos cálculos para que los random nos quepan.
            if(direccion == 0){

              //calculamos el margenX para la palabra
              var margenX = (size - numLetrasPalabra);
              /*if(margenX == 1){
                margenX = 2;
              }*/
              posX = getRandomInt(margenX);
              posY = getRandomInt(size);

              //compruebo si en la posición y con el tamaño que hay choca
              var choca = false;
              for (var k = 0; k < numLetrasPalabra; k++) {
                if(arraySopaLetras[posX+k][posY] != undefined){
                  if(arraySopaLetras[posX+k][posY] != arrayLetrasPalabra[k]){
                    choca = true;
                  }
                }

              }
              if(!choca) posicion = true;
              

            }else if(direccion == 1){

              //calculamos el margenY para la palabra
              var margenY = (size - numLetrasPalabra);
              /*if(margenY == 1){
                margenY = 2;
              }*/
              posX = getRandomInt(size);
              posY = getRandomInt(margenY); 

              //compruebo si en la posición y con el tamaño que hay choca
              var choca = false;
              for (var k = 0; k < numLetrasPalabra; k++) {
                if(arraySopaLetras[posX][posY+k] != undefined){
                  if(arraySopaLetras[posX][posY+k] != arrayLetrasPalabra[k]){
                    choca = true;
                  }
                  
                }

              }
              if(!choca) posicion = true;
              
            }else if(direccion == 2){ //derecha hacia abajo
              //calculamos el margenY para la palabra
              var margen = (size - numLetrasPalabra);
              /*if(margenY == 1){
                margenY = 2;
              }*/
              posX = getRandomInt(margen);
              posY = getRandomInt(margen); 

              //compruebo si en la posición y con el tamaño que hay choca
              var choca = false;
              for (var k = 0; k < numLetrasPalabra; k++) {
                if(arraySopaLetras[posX+k][posY+k] != undefined){
                  if(arraySopaLetras[posX+k][posY+k] != arrayLetrasPalabra[k]){
                    choca = true;
                  }
                  
                }

              }
              if(!choca) posicion = true;

            }else if(direccion == 3){ //derecha hacia arriba
              //calculamos el margen para la palabra
              var margen = (size - numLetrasPalabra);
              
              /*if(margenY == 1){
                margenY = 2;
              }*/
              var rnd = getRandomInt(margen);
              console.log("margen"+margen);
              console.log("rnd"+rnd);
              posX = rnd + numLetrasPalabra;
            
              posY = getRandomInt(margen); 
            
              

              //compruebo si en la posición y con el tamaño que hay choca
              var choca = false;
              for (var k = 0; k < numLetrasPalabra; k++) {
                console.log(posX);
                console.log(k);
                if(arraySopaLetras[posX-k][posY+k] != undefined){
                  if(arraySopaLetras[posX-k][posY+k] != arrayLetrasPalabra[k]){
                    choca = true;
                  }
                  
                }

              }
              if(!choca) posicion = true;

            }
            
            
          }

          break;
      }


      //busco hueco
      //TODO



      //recorro la palabra y asigno la palabra
      for (var j = 0; j < arrayLetrasPalabra.length; j++) {
        if(direccion == 0){
          arraySopaLetras[posX +j][posY] = arrayLetrasPalabra[j];
        }else if(direccion == 1){
          arraySopaLetras[posX][posY+j] = arrayLetrasPalabra[j];
        }else if(direccion == 2){
          arraySopaLetras[posX+j][posY+j] = arrayLetrasPalabra[j];
        }else if(direccion == 3){
          arraySopaLetras[posX-j][posY+j] = arrayLetrasPalabra[j];
        }

      }
      
    }







    //PINTO EL ARRAY

    var tabla = document.getElementById("sopaletras");
    for (var i = 0; i < arraySopaLetras.length; i++) {
      let fila = document.createElement('tr');
      for (var j = 0; j < arraySopaLetras.length; j++) {
        let celda = document.createElement('td');
        let letra = arraySopaLetras[i][j];
        if(letra == undefined){
          celda.style.backgroundColor = "grey";
          letra = getRandomChar();
        }
        celda.innerHTML = letra.toUpperCase();
        fila.append(celda);
      }
      tabla.append(fila);
    }


    //PINTO LAS PALABRAS
    var listado1 = document.getElementById("listado1");
    var listado2 = document.getElementById("listado2");
    var listado3 = document.getElementById("listado3");
    for (var i = 0; i < datos_fichero.length; i++) {
      let elemento = document.createElement('li');
      elemento.innerHTML = datos_fichero[i];

      if(i<8){ listado1.append(elemento)
      }else if(i < 16) {listado2.append(elemento);
      }else{ listado3.append(elemento);
      }
    }
  });


};