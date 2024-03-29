# HACK IT 1: 

Clasico primer nivel del hackit de la euskal. Como suele ser usual, tenemos que ir al código de la página, y dentro del HTML veremos un tag `<script>` con un código sospechoso. Lo copiamos y lo pasamos por un desmimificador de JavaScript, con lo cual conseguimos el siguiente script:

```javascript
function q(e) {
    var a = ">,------------------------------------------------------------------------------------[<+>[-]],----------------------------------------------------[<+>[-]],------------------------------------------------------------------------------------------------------------------[<+>[-]],----------------------------------------------------------------------------------------------------------------[<+>[-]],-------------------------------------------------[<+>[-]],--------------------------------------------------------------------------------------------------------------------[<+>[-]],-----------------------------------------------------------------------------------[<+>[-]],-------------------------------------------------------------------[<+>[-]],------------------------------------------------------------------------------------------------------------------[<+>[-]],-------------------------------------------------[<+>[-]],----------------------------------------------------------------------------------------------------------------[<+>[-]],------------------------------------------------------------------------------------[<+>[-]],[<+>[-]][-]+<[>>>++[>+++[>+++++++++++++++++++<-]<-]>>.-------------.-.<<<<[-]<[-]]>[>>>++[>+++[>+++++++++++++++++<-]<-]>>+.[>+>+<<-]>+++++++++++.>--..<----.<<<[-]]";
    let r = 0,
        f = 0;
    var i = a.length,
        c = new Uint8Array(3e4),
        s = "",
        b = 10240,
        k = 0;
	for (r = 0; r < i && !(b < 0); r++) 
        switch (b--, a[r]) {
            case ">":
                f++;
                break;
            case "<":
                f > 0 && f--;
                break;
            case "+":
                c[f] = c[f] + 1 & 255;
                break;
            case "-":
                c[f] = c[f] - 1 & 255;
                break;
            case ".":
                s += String.fromCharCode(c[f]);
                break;
            case ",":
                k >= e.length ? c[f] = 0 : c[f] = e.charCodeAt(k), k++;
                break;
            case "[":
                if (!c[f])
                    for (var t = 0; a[++r];)
                        if ("[" === a[r]) t++;
                        else if ("]" === a[r]) {
                    if (!(t > 0)) break;
                    t--
                    }
                break;
            case "]":
                if (c[f])
                    for (t = 0; a[--r];)
                        if ("]" === a[r]) t++;
                        else if ("[" === a[r]) {
                            if (!(t > 0)) break;
                            t--
                        }
	}
    return s
}
```

La clave de todo este hackit está claramente en el _string_ `a` del principio, ya que los caracteres de este son los que mandan que operaciones realizar sobre la contraseña que introduzcamos. Si nos centramos únicamente en dicho string podemos ver cierto patrón que resulta en trece lineas (lo que probablemente se traduzca en una contraseña de trece caracteres):

```
>,------------------------------------------------------------------------------------[<+>[-]]
,----------------------------------------------------[<+>[-]]
,------------------------------------------------------------------------------------------------------------------[<+>[-]]
,----------------------------------------------------------------------------------------------------------------[<+>[-]]
,-------------------------------------------------[<+>[-]]
,--------------------------------------------------------------------------------------------------------------------[<+>[-]]
,-----------------------------------------------------------------------------------[<+>[-]]
,-------------------------------------------------------------------[<+>[-]]
,------------------------------------------------------------------------------------------------------------------[<+>[-]]
,-------------------------------------------------[<+>[-]]
,----------------------------------------------------------------------------------------------------------------[<+>[-]]
,------------------------------------------------------------------------------------[<+>[-]]
,[<+>[-]][-]+<[>>>++[>+++[>+++++++++++++++++++<-]<-]>>.-------------.-.<<<<[-]<[-]]>[>>>++[>+++[>+++++++++++++++++<-]<-]>>+.[>+>+<<-]>+++++++++++.>--..<----.<<<[-]];
```

Como primer acercamiento, decidimos contar el número de guiones en cada linea, lo que nos da el siguiente array:
```
84 52 114 112 49 116 83 67 114 49 112 84
```

Estos valores se asemejan mucho entre si, y podemos sospechar que puede tratarse de valores ASCII. Para asegurarnos, lo pasámos por un conversor ASCII a texto, y tenemos nuestro primer nivel!
```
T4rp1tSCr1pT
```