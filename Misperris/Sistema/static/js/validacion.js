$(function(){
	var error_message = "";
    //variables que indican valor de estado validacion

	var error_email = false;
	var error_rut = false;
	var error_nombre = false;
	var error_fecnac = false;
	var error_telefono = false;
	var error_region = false;
	var error_ciudad = false;
	var error_tipo = false;
	var error_password = false
	var error_retype_password = false;
	
	//SOLO NUMEROS EN TELEFONO
	$('#id_telefono').on('input', function () { 
		
		this.value = this.value.replace(/[^0-9]/g,'');
	});

	//Solo letras, tildes y espacios en el nombre
$("#id_nombrePersona").keypress(function (key) {
	if ((key.charCode < 97 || key.charCode > 122)//letras mayusculas
	&& (key.charCode < 65 || key.charCode > 90) //letras minusculas
	&& (key.charCode != 241) //ñ
	&& (key.charCode != 209) //Ñ
	&& (key.charCode != 32) //espacio
	&& (key.charCode != 225) //á
	&& (key.charCode != 233) //é
	&& (key.charCode != 237) //í
	&& (key.charCode != 243) //ó
	&& (key.charCode != 250) //ú
	&& (key.charCode != 193) //Á
	&& (key.charCode != 201) //É
	&& (key.charCode != 205) //Í
	&& (key.charCode != 211) //Ó
	&& (key.charCode != 218) //Ú
	)
		return false;
	});

	//Solo numeros, puntos, guión y K
$("#id_codigoPersona").keypress(function (key) {
	if ((key.charCode < 48 || key.charCode > 57) //Numeros
	&& (key.charCode != 45) //-
	&& (key.charCode != 46)//.
	&& (key.charCode != 75)//k
	&& (key.charCode != 107)//K
	)
		return false;
	});
	
//Cambiar ciudad según región
	$("#id_region").change(function() {
		
		if($("#id_region").val()=="--Región--"){
			$("#id_ciudad").html("<option>--Ciudad--</option>")
		}
		if($("#id_region").val()=="Arica y Parinacota"){
			$("#id_ciudad").html("<option>--Ciudad--</option><option>Arica</option><option>Putre</option><option>General Lagos</option><option>Camarones</option>")
		}
		if($("#id_region").val()=="Coquimbo"){
			$("#id_ciudad").html("<option>--Ciudad--</option><option>La Serena</option><option>Ovalle</option><option>Vicuña</option><option>Illapel</option>")
		}
		if($("#id_region").val()=="Metropolitana"){
			$("#id_ciudad").html("<option>--Ciudad--</option><option>Santiago</option><option>Providencia</option><option>Colina</option><option>Melipilla</option>")
		}
	});

		//[VALIDACIONES AL MOMENTO DEL ENVIO]//


	//Validar estructura del email
	function check_email() {

		var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);
	
		if(pattern.test($("#id_correoPersona").val())) {

		} else {
			error_message = "DIRECCIÓN DE CORREO INVÁLIDO";
			error_email = true;
		}
	
	}
	
	//Validar estructura de Run
	function check_rut(){

	var campo = $("#id_codigoPersona").val();

	if ( campo.length == 0 ){
		error_message ="RUN INVÁLIDO";
		error_rut=true;
	}else{
		if ( campo.length < 8 ){
			error_message = "RUT INVÁLIDO";
			error_rut=true;
		} else{

			campo = campo.replace('-','')
			campo = campo.replace(/\./g,'')

			var suma = 0;
			var caracteres = "1234567890kK";
			var contador = 0;    
			for (var i=0; i < campo.length; i++){
				u = campo.substring(i, i + 1);
				if (caracteres.indexOf(u) != -1)
				contador ++;
			}
			if ( contador==0 ) {
				error_message = "RUN INVÁLIDO";
				error_rut=true;
			} else{
			
				var rut = campo.substring(0,campo.length-1)
				var drut = campo.substring( campo.length-1 )
				var dvr = '0';
				var mul = 2;
				
				for (i= rut.length -1 ; i >= 0; i--) {
					suma = suma + rut.charAt(i) * mul
			                if (mul == 7) 	mul = 2
					        else	mul++
				}
				res = suma % 11
				if (res==1)		dvr = 'k'
			                else if (res==0) dvr = '0'
				else {
					dvi = 11-res
					dvr = dvi + ""
				}
				if ( dvr != drut.toLowerCase() ) {
					error_message = "RUN INVÁLIDO";
					error_rut=true;
				}
			}
		}
	}
}
	//Validación largo del nombre 
	function check_nombre() {
	
		var username_length = $("#id_nombrePersona").val().length;
		
		if(username_length < 5 || username_length > 50) {
			error_message = "NOMBRE INVÁLIDO:Debe tener entre 5 y 50 ";
			error_nombre = true;
		}
	
	}
	//Validación largo de contraseña
	function check_passwd(){
	
		var passwd_length = $("#id_passwd").val().length;
		
		if(passwd_length < 4) {
			error_message = "CONTRASEÑA INVÁLIDA:Debe tener 4 o mas de caracteres";
			error_password = true;
		}
	
	}	

		//Validación reingreso de contraseña
		function check_passwd2(){
		
			var passwd1 = $("#id_passwd").val();
			var passwd2 = $("#id_passwd2").val();
			
			if(passwd1 != passwd2) {
				error_message = "LAS CONTRASEÑAS NO COINCIDEN";
				error_nombre = true;
			}
		}

		//Validacion cantidad de digitos del teléfono
		function check_telefono(){
			
			var tel_length = $("#id_telefono").val().length;
			
			if(tel_length !=8 && tel_length != 0) {
				error_message = "TELEFONO DEBE TENER 8 DIGITOS";
				error_nombre = true;
			}
		}

		//Validacion región seleccionada
		function check_region(){
			var region=$("#id_region").val();
			
			if(region=="--Región--"){
				error_message = "DEBE SELECCIONAR UNA REGIÓN";
				error_region = true;
			}
		}
		
		//Validacion ciudad seleccionada
		function check_ciudad(){
			var ciudad=$("#id_ciudad").val();
			
			if(ciudad=="--Ciudad--"){
				error_message = "DEBE SELECCIONAR UNA CIUDAD";
				error_ciudad = true;
			}
		}
		
		//Validacion tipo de vivienda seleccionada
		function check_tipo(){
		var tipo=$("#id_tipoVivienda").val();
			
			if(tipo=="--Tipo--"){
				error_message = "DEBE SELECCIONAR UN TIPO DE VIVIENDA";
				error_tipo = true;
			}
		}

	$("#registro").submit(function() {
	
		error_message = "";
		error_email = false;		
		error_rut = false;
		error_nombre = false;		
		error_fecnac = false;
		error_telefono = false;
		error_region = false;
		error_ciudad = false;
		error_tipo = false;
		error_password = false;
		error_retype_password = false;
		
		
		//check_tipo();
		//check_ciudad();
		check_region();
		check_telefono();
		check_email();
		check_passwd2();
		check_passwd();
		check_nombre();
		check_rut();
		


		
		if(error_password == false && error_retype_password == false && error_email == false && error_rut == false && error_nombre == false && error_fecnac == false
		&& error_telefono == false && error_region == false && error_ciudad == false && error_tipo == false) {
			$( "#registro" ).submit();
		} else {
			alert(error_message);
			return false;
		}

	});


});