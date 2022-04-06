function myFunction() {
    cadena = document.getElementById("input").value;
    var MensajeInvertido = reverse(cadena)

    function reverse(volteo){
        return volteo.split("").reverse().join("");
    }

    if (!cadena)
        window.alert("Ingrese una cadena a convertir")
    else
        window.alert("El texto invertido es: "+MensajeInvertido);
  }
  