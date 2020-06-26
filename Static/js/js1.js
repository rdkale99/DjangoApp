
  function autoFill() {
    document.getElementById('1').value = 1028;
    document.getElementById('2').value = 350;
    document.getElementById('3').value = 69789;
    document.getElementById('4').value = 6000;
    document.getElementById('5').value = 1;
    document.getElementById('6').value = 0;
    document.getElementById('7').value = 0;
    document.getElementById('8').value = 0;
    document.getElementById('9').value = 0;
    document.getElementById('10').value =0;
    document.getElementById('11').value =20;
    document.getElementById('12').value =1179;
    document.getElementById('13').value =0;
    document.getElementById('14').value =0;
    document.getElementById('15').value =350;
    document.getElementById('16').value =100;
    document.getElementById('17').value =1.15;
    document.getElementById('18').value =1.15;
    document.getElementById('19').value =1.15;
    document.getElementById('20').value =1.15;
    document.getElementById('21').value =0.07;
    document.getElementById('22').value =0.07;
    document.getElementById('23').value =0.05;
    document.getElementById('24').value =225;
    document.getElementById('25').value =20;
    document.getElementById('26').value =20;
    document.getElementById('27').value =20;
    document.getElementById('28').value =0;
    document.getElementById('29').value =0;
    document.getElementById('30').value =0;
    document.getElementById('31').value =0.3;
    document.getElementById('32').value =0.3;
    document.getElementById('33').value =0.3;
    document.getElementById('34').value =0.3;
    document.getElementById('35').value =0;
    document.getElementById('36').value =0;
    document.getElementById('37').value =0;
    document.getElementById('38').value =0.2;
    document.getElementById('39').value =0.2;
    document.getElementById('40').value =0.2;
    document.getElementById('41').value =0.2;
    document.getElementById('42').value =0;
    document.getElementById('43').value =0;
    document.getElementById('44').value =0;
    document.getElementById('45').value =0;
    document.getElementById('46').value =0;
    document.getElementById('47').value =0;
    document.getElementById('48').value =0;
    document.getElementById('49').value =0;
    document.getElementById('50').value =0;
    document.getElementById('51').value =2000;
    document.getElementById('52').value =500;
    document.getElementById('53').value =500;
    document.getElementById('54').value =500;
    document.getElementById('55').value =500;
    document.getElementById('56').value =500;
    document.getElementById('57').value =38;
    document.getElementById('58').value =40;
    document.getElementById('59').value =0;
    document.getElementById('60').value =0;
    document.getElementById('61').value =0;
    document.getElementById('62').value =0;
    document.getElementById('63').value =30;
    document.getElementById('64').value =25;
    document.getElementById('65').value =77;
    document.getElementById('66').value =60;
    document.getElementById('67').value =100;
    document.getElementById('68').value =30;
    document.getElementById('69').value =5;
    document.getElementById('70').value =5;
    document.getElementById('71').value =12;
    document.getElementById('72').value =12;
    document.getElementById('73').value =0;
    document.getElementById('74').value =0;
    document.getElementById('75').value =10;
    document.getElementById('76').value =10;
    document.getElementById('77').value =10;
    document.getElementById('78').value =10;
    document.getElementById('79').value =0;
    document.getElementById('80').value =0;
    document.getElementById('81').value =3;
    document.getElementById('82').value =3;
    document.getElementById('83').value =0;
    document.getElementById('84').value =0;
    document.getElementById('85').value =0;
    document.getElementById('86').value =0;
    document.getElementById('87').value =3;
    document.getElementById('88').value =3;
    document.getElementById('89').value =4.5;
    document.getElementById('90').value =4.5;
    document.getElementById('91').value =0;
    document.getElementById('92').value =0;
    document.getElementById('93').value =0;
    document.getElementById('94').value =0;
    document.getElementById('95').value =0;
    document.getElementById('96').value =0;
    document.getElementById('97').value =0;
    document.getElementById('98').value =0;
    document.getElementById('99').value =0;
    document.getElementById('100').value =0;
    document.getElementById('101').value =0;
    document.getElementById('102').value =0;
    document.getElementById('103').value =0;
    document.getElementById('104').value =0;



    }

	function change(id_val){

					 var checkbox_val=document.getElementById(id_val).checked;
					 if(checkbox_val==true)
					 {
          			switch(id_val){
          			case "process2_col":

          					document.getElementById("17").addEventListener("change", P2);
          					document.getElementById("24").addEventListener("change", P2);
          					document.getElementById("31").addEventListener("change", P2);
          					document.getElementById("38").addEventListener("change", P2);

          					document.getElementById("51").addEventListener("change", P2);

							break;
          			case "process3_col":

          					document.getElementById("18").addEventListener("change", P3);
          					document.getElementById("25").addEventListener("change", P3);
          					document.getElementById("32").addEventListener("change", P3);
          					document.getElementById("39").addEventListener("change", P3);

          					document.getElementById("52").addEventListener("change", P3);

          					break;
          			case "process4_col":

          					document.getElementById("19").addEventListener("change", P4);
          					document.getElementById("26").addEventListener("change", P4);
          					document.getElementById("33").addEventListener("change", P4);
          					document.getElementById("40").addEventListener("change", P4);

          					document.getElementById("53").addEventListener("change", P4);

          					break;
          			case "process5_col":

          					document.getElementById("20").addEventListener("change", P5);
          					document.getElementById("27").addEventListener("change", P5);
          					document.getElementById("34").addEventListener("change", P5);
          					document.getElementById("41").addEventListener("change", P5);

          					document.getElementById("54").addEventListener("change", P5);

          					break;
          			case "process6_col":
							document.getElementById("21").addEventListener("change", P6);
          					document.getElementById("28").addEventListener("change", P6);
          					document.getElementById("35").addEventListener("change", P6);
          					document.getElementById("42").addEventListener("change", P6);

          					document.getElementById("55").addEventListener("change", P6);
          					break;
          				}
				}

            }



            function P2(){
					var p=document.getElementById("process3_col").checked;
					if(p==false){
					document.getElementById("18").value=document.getElementById("17").value;
					document.getElementById("25").value=document.getElementById("24").value;
					document.getElementById("32").value=document.getElementById("31").value;
					document.getElementById("39").value=document.getElementById("38").value;

					document.getElementById("52").value=document.getElementById("51").value;
					document.getElementById("59").value=0;
					document.getElementById("60").value=0;
					document.getElementById("71").value=0;
					document.getElementById("72").value=0;
					document.getElementById("83").value=0;
					document.getElementById("84").value=0;
					document.getElementById("95").value=0;
					document.getElementById("96").value=0;
					}
					else{

					document.getElementById("18").value=document.getElementById("17").value;
					document.getElementById("25").value=document.getElementById("24").value;
					document.getElementById("32").value=document.getElementById("31").value;
					document.getElementById("39").value=document.getElementById("38").value;

					document.getElementById("52").value=document.getElementById("51").value;
					document.getElementById("59").value=0;
					document.getElementById("60").value=0;
					document.getElementById("71").value=0;
					document.getElementById("72").value=0;
					document.getElementById("83").value=0;
					document.getElementById("84").value=0;
					document.getElementById("95").value=0;
					document.getElementById("96").value=0;
					P3();

					}
					}
				function P3(){
					var q=document.getElementById("process4_col").checked;
					if(q==false){
					document.getElementById("19").value=document.getElementById("18").value;
					document.getElementById("26").value=document.getElementById("25").value;
					document.getElementById("33").value=document.getElementById("32").value;
					document.getElementById("40").value=document.getElementById("39").value;

					document.getElementById("53").value=document.getElementById("52").value;
					document.getElementById("61").value=0;
					document.getElementById("62").value=0;
					document.getElementById("73").value=0;
					document.getElementById("74").value=0;
					document.getElementById("85").value=0;
					document.getElementById("86").value=0;
					document.getElementById("97").value=0;
					document.getElementById("98").value=0;
					}
					else{
					document.getElementById("19").value=document.getElementById("18").value;
					document.getElementById("26").value=document.getElementById("25").value;
					document.getElementById("33").value=document.getElementById("32").value;
					document.getElementById("40").value=document.getElementById("39").value;

					document.getElementById("53").value=document.getElementById("52").value;
					document.getElementById("61").value=0;
					document.getElementById("62").value=0;
					document.getElementById("73").value=0;
					document.getElementById("74").value=0;
					document.getElementById("85").value=0;
					document.getElementById("86").value=0;
					document.getElementById("97").value=0;
					document.getElementById("98").value=0;
					P4();

					}
					}

				function P4(){
						var r=document.getElementById("process5_col").checked;
							if(r==false){
					document.getElementById("20").value=document.getElementById("19").value;
					document.getElementById("27").value=document.getElementById("26").value;
					document.getElementById("34").value=document.getElementById("33").value;
					document.getElementById("41").value=document.getElementById("40").value;

					document.getElementById("54").value=document.getElementById("53").value;
					document.getElementById("63").value=0;
					document.getElementById("64").value=0;
					document.getElementById("75").value=0;
					document.getElementById("76").value=0;
					document.getElementById("87").value=0;
					document.getElementById("88").value=0;
					document.getElementById("99").value=0;
					document.getElementById("100").value=0;
					}
					else{

					document.getElementById("20").value=document.getElementById("19").value;
					document.getElementById("27").value=document.getElementById("26").value;
					document.getElementById("34").value=document.getElementById("33").value;
					document.getElementById("41").value=document.getElementById("40").value;

					document.getElementById("54").value=document.getElementById("53").value;
					document.getElementById("63").value=0;
					document.getElementById("64").value=0;
					document.getElementById("75").value=0;
					document.getElementById("76").value=0;
					document.getElementById("87").value=0;
					document.getElementById("88").value=0;
					document.getElementById("99").value=0;
					document.getElementById("100").value=0;
					P5();

					}
					}
				function P5(){
						var s=document.getElementById("process6_col").checked;
						if(s==false){
					document.getElementById("21").value=document.getElementById("20").value;
					document.getElementById("28").value=document.getElementById("27").value;
					document.getElementById("35").value=document.getElementById("34").value;
					document.getElementById("42").value=document.getElementById("41").value;

					document.getElementById("55").value=document.getElementById("54").value;
					document.getElementById("65").value=0;
					document.getElementById("66").value=0;
					document.getElementById("77").value=0;
					document.getElementById("78").value=0;
					document.getElementById("89").value=0;
					document.getElementById("90").value=0;
					document.getElementById("101").value=0;
					document.getElementById("102").value=0;
					}
					else{

					document.getElementById("21").value=document.getElementById("20").value;
					document.getElementById("28").value=document.getElementById("27").value;
					document.getElementById("35").value=document.getElementById("34").value;
					document.getElementById("42").value=document.getElementById("41").value;

					document.getElementById("55").value=document.getElementById("54").value;
					document.getElementById("65").value=0;
					document.getElementById("66").value=0;
					document.getElementById("77").value=0;
					document.getElementById("78").value=0;
					document.getElementById("89").value=0;
					document.getElementById("90").value=0;
					document.getElementById("101").value=0;
					document.getElementById("102").value=0;
					P6();
					}
					}
				function P6(){
					document.getElementById("22").value=document.getElementById("21").value;
					document.getElementById("29").value=document.getElementById("28").value;
					document.getElementById("36").value=document.getElementById("35").value;
					document.getElementById("43").value=document.getElementById("42").value;

					document.getElementById("56").value=document.getElementById("55").value;
					document.getElementById("67").value=0;
					document.getElementById("68").value=0;
					document.getElementById("79").value=0;
					document.getElementById("80").value=0;
					document.getElementById("91").value=0;
					document.getElementById("92").value=0;
					document.getElementById("103").value=0;
					document.getElementById("104").value=0;
					}



function hide_show_table(col_name)
{
change(col_name);
    getidpo(col_name);
 var x=col_name;

 var checkbox_val=document.getElementById(col_name).checked;
 if(checkbox_val==true)
 {

  var all_col=document.getElementsByClassName(col_name);
  for(var i=0;i<all_col.length;i++)
  {
   all_col[i].style.display="none";
  }
  document.getElementById(col_name+"_head").style.display="none";
  document.getElementById(col_name).value="show";
 }

 else
 {
  var all_col=document.getElementsByClassName(col_name);
  for(var i=0;i<all_col.length;i++)
  {
   all_col[i].style.display="table-cell";
  }
  document.getElementById(col_name+"_head").style.display="table-cell";
  document.getElementById(col_name).value="hide";
 }

}
		function refresh(){
		        localStorage.clear();

				var val_check2=document.getElementById("process2_col").checked;
				if(val_check2==true)
					{document.getElementById("process2_col").checked = false;
					 hide_show_table("process2_col");}
				var val_check3=document.getElementById("process3_col").checked;
				if(val_check3==true)
					{document.getElementById("process3_col").checked = false;
					 hide_show_table("process3_col");}
				var val_check4=document.getElementById("process4_col").checked;
				if(val_check4==true)
					{document.getElementById("process4_col").checked = false;
					 hide_show_table("process4_col");}
				var val_check5=document.getElementById("process5_col").checked;
				if(val_check5==true)
					{document.getElementById("process5_col").checked = false;
					 hide_show_table("process5_col");}
				var val_check6=document.getElementById("process6_col").checked;
				if(val_check6==true)
					{document.getElementById("process6_col").checked = false;
					 hide_show_table("process6_col");}



	}

	function oilfn(id_val) {
			refresh();
			localStorage.clear();
			document.getElementById("proil").value=document.getElementById(id_val).value;
			getidpo("Oil");
			switch(id_val) {
				  case "Oil_1":
				    checkboxhidehide();

					break;
				  case Oil_2:
				  checkboxhidehide();
					process2_col.click();
					process3_col.click();
					break;
				  case Oil_3:
				  checkboxhidehide();

					break;
				  case "Oil_4":
				  checkboxhidehide();
					process2_col.click();
					process3_col.click();

					break;
				  case "Oil_5":
				  checkboxhidehide();
					process3_col.click();
					break;
				  case "Oil_6":
				  checkboxhidehide();
				  process2_col.click();
				  process4_col.click();
				  process6_col.click();
					break;
				  case "Oil_7":
				  checkboxhidehide();
				   process2_col.click();
				   process4_col.click();
				   process6_col.click();
					break;
				  case "Oil_8":
				  checkboxhidehide();
					process4_col.click();
				   process6_col.click();
					break;
				  case "Oil_9":
				  checkboxhidehide();
					process2_col.click();
				   process4_col.click();
				   process6_col.click();
					break;
				  case "Oil_10":
				  checkboxhidehide();
					process4_col.click();
				   process6_col.click();
					break;
				  case "Oil_11":
				  checkboxhidehide();
					process4_col.click();
				   process6_col.click();
					break;
				  case "Oil_12":
				  checkboxhidehide();
					process4_col.click();
				   process6_col.click();
					break;
				  case "Oil_13":
				  checkboxhidehide();
					process4_col.click();
				   process6_col.click();
					break;
				  case "Oil_14":
				  checkboxhidehide();
					process4_col.click();
				   process6_col.click();
					break;
				  case "Oil_15":
 					checkboxhidehide();
 					process4_col.click();
				   process6_col.click();
					break;
				  case "Oil_16":
				  	checkboxhidehide();
					process4_col.click();
				   process6_col.click();
					break;
				  case "Oil_17":
					checkboxhide();
				  	break;


				}


	}


function checkboxhidehide() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "block") {
    x.style.display = "none";
  }

}
function checkboxhide() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
function resetinput(){
localStorage.clear();
window.location = '/';
}

function getidpo(id_name){
switch(id_name){
	case "process2_col":
			localStorage.setItem("ddvalue2",id_name);
			break;
	case "process3_col":
			localStorage.setItem("ddvalue3",id_name);
			break;
	case "process4_col":
			localStorage.setItem("ddvalue4",id_name);
			break;
	case "process5_col":
			localStorage.setItem("ddvalue5",id_name);
			break;
	case "process6_col":
			localStorage.setItem("ddvalue6",id_name);
			break;
	case "Oil":
			output=document.getElementById(id_name).value;
			localStorage.setItem("ddvalue7",output);
			return true;
			break;
		}


}

function getdata(){
if (localStorage.getItem("ddvalue2") === null)
	{}
	else{id_val2=localStorage.getItem("ddvalue2");
	document.getElementById(id_val2).checked=true;
	hide_show_table(id_val2);					 }
if (localStorage.getItem("ddvalue3") === null)
	{}
	else{id_val3=localStorage.getItem("ddvalue3");
	document.getElementById(id_val3).checked=true;
	hide_show_table(id_val3);					 }
if (localStorage.getItem("ddvalue4") === null)
	{}
	else{id_val4=localStorage.getItem("ddvalue4");
	document.getElementById(id_val4).checked=true;
	hide_show_table(id_val4);					 }
if (localStorage.getItem("ddvalue5") === null)
	{}
	else{id_val5=localStorage.getItem("ddvalue5");
	document.getElementById(id_val5).checked=true;
	hide_show_table(id_val5);					 }
if (localStorage.getItem("ddvalue6") === null)
	{}
	else{id_val6=localStorage.getItem("ddvalue6");
	document.getElementById(id_val6).checked=true;
	hide_show_table(id_val6);					 }
if (localStorage.getItem("ddvalue7") === null)
	{}
	else{id_val7=localStorage.getItem("ddvalue7");

		document.getElementById("Oil").value = id_val7;
						 }


}


