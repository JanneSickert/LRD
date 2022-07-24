<p style="font-size: 20pt;">LRD</p>
<u><p>Datenhaltung mit NumPy in Matrizen.</p></u>

-------------------------

<div width="33%" style="margin-left: 20px; padding-bottom: 10px; margin-right:33%; font-size: 18pt;">
   <a style="color: #FFF; width: 100%; background-color: #221; margin-top: 10px; padding-right: 42px" href="https://github.com/jannikwiessler/pythonDHBW/blob/main/Lineare_Regression/Lineare_Regression_py.pptx">Erklärung des LRD</a><br>
   <a style="20px; color: #FFF; width:100%; background-color: #221; margin-top: 10px;" href="https://www.crashkurs-statistik.de/einfache-lineare-regression/">Erklärung der Formeln</a>
</div>
<div style="margin-left: 20px">
    <img src="pics/b.PNG" alt="Bild existiert nicht mehr" width="33%" height="100px"></img>
    <img src="pics/a.PNG" alt="Bild existiert nicht mehr" width="33%" height="100px"></img>
    <img src="pics/y.PNG" alt="Bild existiert nicht mehr" width="32%" height="100px"></img>
</div>

-------------------------

<font color="#00AA00" style="font-size: 18pt">MATRIX IS:<font color="#000">AAAAAAAAAAAA</font>
numpy.float64</font><br>
<font color= #00AA00 style = "font-size: 14pt">avg(xy) ist der Durchschnittswert.</font><br>
<font color= #00AA00 style = "font-size: 14pt">
   <ul>
   	<li>matrix[0][0][1] -> input: y</li>
      <li>matrix[0][1][2] -> avg(y)</li>
   </ul>
</font>
<div>
   <div style="margin-left: 20px">
      <font color= #00AA00 style = "font-size: 14pt">Dimension 0</font>
         <table width=570px border = "3">
            <tr>
               <td>input: x</td>
               <td>input: y</td>
            </tr>
            <tr>
               <td>∑ (x)</td>
               <td>∑ (y)</td>
            </tr>
            <tr>
               <td>avg(x)</td>
               <td>avg(y)</td>
            </tr>
         </table>
   </div>
   <div style="margin-left: 20px">
   <font color= #00AA00 style = "font-size: 14pt">Dimension 1</font>
      <table width="570px" border = "3">
         <tr>
            <td>x[i] - (∑ (x) / length)</td>
            <td>y[i] - (∑ (y) / length)</td>
         </tr>
         <tr>
            <td>x[i] - avg(x)</td>
            <td>y[i] - avg(y)</td>
         </tr>
         <tr>
            <td>(x[i] - avg(x)) * (y[i] - avg(y))</td>
            <td>(x[i] - avg(x)) * (x[i] - avg(x))</td>
         </tr>
      </table>
   </div>
   <div style="margin-left: 20px">
   <font color= #00AA00 style = "font-size: 14pt">Dimension 2</font>
      <table width="570px" border = "3">
         <tr>
            <td>b * avg(x)</td>
            <td>∑ (x[i] - avg(x)) * (y[i] - avg(y))</td>
         </tr>
         <tr>
            <td>a = avg(y) - (b * avg(x))</td>
            <td>∑ (x[i] - avg(x)) * (x[i] - avg(x))</td>
         </tr>
         <tr>
            <td>y = a + b * x <font color="#000">AAAAAAAAAAAA</font></td>
            <td>b = Zähler - Nenner</td>
         </tr>
      </table>
   </div>
</div>