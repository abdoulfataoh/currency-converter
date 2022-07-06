HTML_INDEX_TREMPLATE = """
<!Doctype html>
<html>
	<head>
		<title> Currency converter </title>
		<meta charset="utf-8">
		<link rel="stylesheet"	type="text/css" href="style.css" />
		<link rel="stylesheet"	type="text/css" href="w3.css" />
		<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia">

	</head>

	<body>
		<div style="width: 50%%;" class="w3-amber w3-card-2 w3-padding-16" id="main-div">
			<form action="treatment.py">

				<div class="w3-row-padding w3-padding-16">
					<div class="w3-half">
						<h3 id="title">Currency Converter</h3>
					</div>
				</div>
             
				<div class="w3-row-padding">
			  		<div class="w3-half">
			    		<label>Ammount</label>
			    		<input class="w3-input w3-border w3-border-red w3-hover-border-green" type="number" placeholder="ammount" name="ammount" min="1">
			  		</div>

			  		<div class="w3-half">
			    		<label>From currency</label>
			    		<select class="w3-select w3-border"  name="from-currency" >
			    			
							%s
			    			
			    		</select>
			  		</div>
				</div>

				<div class="w3-row-padding">
					<div class="w3-half">
			    		<label>To currency</label>
			    		<select class="w3-select w3-border" name="to-currency">
			    			
			    			%s
			    		
			    		</select>
			  		</div>
			  		
			  		<div class="w3-half">
			    		<label>To ammount</label>
			    		<button type="submit" class="w3-button w3-input w3-white w3-border">Process</button>
			  		</div>

			  		
				</div>

			</form>

		</div>

	</body>
</html>
"""

HTML_RESULT_TREMPLATE = """
<!Doctype html>
<html>
	<head>
		<title> Currency converter </title>
		<meta charset="utf-8">
		<style type="text/css">
			.center {
					  padding: 70px 0;
					  /*border: 3px solid green;*/
					  text-align: center;
					  font-size: 150px;
					}
			body{background-color: orange;}
		</style>
	</head>

	<body>
		<p class="center"> %s %s </p>
	</body>		
</html>

"""

