#!/usr/bin/python
 
import os
import socket

print "Content-type: text/html\n\n"


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ips = (s.getsockname()[0])
s.close()

print ('<html>')
print """<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>File Directory</title>
<style>

@charset "UTF-8";
@import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);

body {
  font-family: 'Open Sans', sans-serif;
  font-weight: 300;
  line-height: 1.42em;
  color:#A7A1AE;
  background-color:#1F2739;
}

a {
  color: #4DC3FA;
}

h1 {
  font-size:3em; 
  font-weight: 300;
  line-height:1em;
  text-align: left;
  padding-top: 25px;
  color: #4DC3FA;
}

h2 {
  font-size:1em; 
  font-weight: 300;
  text-align: center;
  display: block;
  line-height:1em;
  padding-bottom: 2em;
  color: #FB667A;
}

h2 a {
  font-weight: 700;
  text-transform: uppercase;
  color: #FB667A;
  text-decoration: none;
}

td:hover.bdr {
  border-left-color: #FFF842;
  border-left-style: solid;
  border-left-width: 15px;
}

.blue { color: #185875; }
.yellow { color: #FFF842; }

.container th h1 {
	  font-weight: bold;
	  font-size: 1em;
  text-align: left;
  color: #185875;
}

.container td {
	  font-weight: normal;
	  font-size: 1em;
  -webkit-box-shadow: 0 2px 2px -2px #0E1119;
	   -moz-box-shadow: 0 2px 2px -2px #0E1119;
	        box-shadow: 0 2px 2px -2px #0E1119;
}

.container {
	  text-align: left;
	  overflow: hidden;
	  width: 80%;
	  margin: 0 auto;
  display: table;
  padding: 0 0 8em 0;
}

.container td, .container th {
	  padding-bottom: 2%;
	  padding-top: 2%;
  padding-left:2%;  
}

/* Background-color of the odd rows */
.container tr:nth-child(odd) {
	  background-color: #323C50;
}

/* Background-color of the even rows */
.container tr:nth-child(even) {
	  background-color: #2C3446;
}

.container th {
	  background-color: #1F2739;
}

.container td:first-child { color: ; }



.container td:hover {
  font-weight: bold;

  
  
  transition-delay: 0s;
	  transition-duration: 0.4s;
	  transition-property: all;
  transition-timing-function: line;
}

@media (max-width: 800px) {
.container td:nth-child(4),
.container th:nth-child(4) { display: none; }
}

#myInput {
  width: 20%;
  font-size: 14px;
  padding: 10px 10px 10px 25px;
  border: 0 solid #ddd;
  margin-bottom: 5px;
}

/*	
	search bar style
	===================

 */

input {
	outline: none;
}
input[type=search] {
	-webkit-appearance: textfield;
	-webkit-box-sizing: content-box;
	font-family: inherit;
	font-size: 100%;
}
input::-webkit-search-decoration,
input::-webkit-search-cancel-button {
	display: none; 
}


input[type=search] {
	background: #ededed url() no-repeat 9px center;
	border: solid 1px #ccc;
	padding: 9px 10px 9px 32px;
	width: 55px;
	
	-webkit-border-radius: 10em;
	-moz-border-radius: 10em;
	border-radius: 10em;
	
	-webkit-transition: all .5s;
	-moz-transition: all .5s;
	transition: all .5s;
}
input[type=search]:focus {
	width: 130px;
	background-color: #fff;
	border-color: #66CC75;
	
	-webkit-box-shadow: 0 0 5px rgba(109,207,246,.5);
	-moz-box-shadow: 0 0 5px rgba(109,207,246,.5);
	box-shadow: 0 0 5px rgba(109,207,246,.5);
}


input:-moz-placeholder {
	color: #999;
}
input::-webkit-input-placeholder {
	color: #999;
}

/* Demo 2 */
#demo-2 input[type=search] {
	width: 45px;
	padding-left: 10px;
	color: transparent;
	cursor: pointer;
}
#demo-2 input[type=search]:hover {
	background-color: #fff;
}
#demo-2 input[type=search]:focus {
	width: 250px;
	padding-left: 32px;
	color: #000;
	background-color: #fff;
	cursor: auto;
}

</style>
  
</head>


<body>

  <h1><span class="blue">&lt;</span>File<span class="blue">&gt;</span> <span class="yellow">Directory</pan> </h1>
<form align="center" id="demo-2">
	<input type="search" id="myInput" onkeyup="myFunction()" placeholder="Search for file.."></form>
	<table class="container">
    
		<thead>
			<tr>
				<th></th>

			</tr>
		</thead>
		<tbody id="myUL">"""

start_path = '/Users/murraymile/Sites/distro'
for path,dirs,files in os.walk(start_path):
    for filename in files:
        p = os.path.join(path,filename)
        #q = os.path.getsize(p)/float(1<<20))+" MB")
        q =  ('{:,.0f}'.format(os.path.getsize(p)/float(1<<20))+" MB")
        if ".app/Contents/" not in p:
            p = p.replace("/Users/murraymile/Sites","")
            print """<tr><td class="bdr"><a href="{l}">{t}</a></td><td>{q}</td></tr>""".format(t=filename,l=p,q=q)


print ('</tbody>')
print ('</table>')

print """<script>
function myFunction() {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName("tr");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}
</script>"""

 
print ('</body>')
print ('</html>')

