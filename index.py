<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <div style="color:blue">
        <form action="{{ url_for('predict')}}" method="post">
            <h2>Predictive analysis</h2>
            <h3>OverallQual?(1-10)</h3>
            <input id="first" name="OverallQual" type="number ">
            <h3>Year?(YYYY)</h3><br><input id="second" name="YearBuilt" required="required">
            <h3>ExterQual?(0-3)</h3><input id="third" name="ExterQual" required="required">
            <h3>GrLivArea?(334-5642)</h3><br><input id="fourth" name="GrLivArea" required="required">
            <!--<h3>GarageCars?(0-4)</h3><br><input id="fifth" name="GarageCars" required="required">-->
            <h3>GarageCars?</h3><br><select name="GarageCars" id="Number" required="required">
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
            </select>
            <br><br><button id="sub" type="submit ">Calculate the Selling Price</button>
            <br>




        </form>



        <br><br><h3>{{ prediction_text }}<h3>
    </div>




    <style>
        body {
            background-color: lightslategray;
            text-align: center;
            padding: 0px;
        }
        
        #research {
            font-size: 18px;
            width: 100px;
            height: 23px;
            top: 23px;
        }
        
        #box {
            border-radius: 60px;
            border-color: 45px;
            border-style: solid;
            font-family: cursive;
            text-align: center;
            background-color: rgb(168, 131, 61);
            font-size: medium;
            position: absolute;
            width: 700px;
            bottom: 9%;
            height: 850px;
            right: 30%;
            padding: 0px;
            margin: 0px;
            font-size: 14px;
        }
        
        #Number {
            width: 83px;
            height: 43px;
            text-align: center;
            border-radius: 14px;
            font-size: 20px;
        }
        
        #Number:hover {
            background-color: coral;
        }
        
        <!--
        #fifth {
            border-radius: 14px;
            height: 25px;
            font-size: 20px;
            text-align: center;
        }
        -->
        
        #sub {
            width: 120px;
            height: 43px;
            text-align: center;
            border-radius: 14px;
            font-size: 18px;
        }
        
        #sub:hover {
            background-color: darkcyan;
        }
        
        #first {
            border-radius: 14px;
            height: 25px;
            font-size: 20px;
            text-align: center;
        }
        
        #second {
            border-radius: 14px;
            height: 25px;
            font-size: 20px;
            text-align: center;
        }
        
        #third {
            border-radius: 14px;
            height: 25px;
            font-size: 20px;
            text-align: center;
        }
        
        #fourth {
            border-radius: 14px;
            height: 25px;
            font-size: 20px;
            text-align: center;
        }
    </style>
</body>

</html>