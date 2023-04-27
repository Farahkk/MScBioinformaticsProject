<!DOCTYPE html>
<html>
<head>
	<title>JSON Table</title>
</head>
<body>
	<form id="search-form">
		<label for="search-key">Search key:</label>
		<input type="text" id="search-key" name="search-key">
		<button type="submit">Search</button>
	</form>

	<table id="data-table">
		<thead>
			<tr>
				<th>Key</th>
				<th>Value</th>
			</tr>
		</thead>
		<tbody></tbody>
	</table>

	<script>
		// Sample JSON data
		const jsonData = {
			"Request": "12054",
			"Format": "bispecific human monoclonal antibody IgM with humanized scFv-JChain-HSA fusion",
			"ID[1]": "IGM-2323",
			"Antigen[1]": "human B-lymphocyte antigen CD20, B-lymphocyte surface antigen B1, Bp35, Leukocyte surface antigen Leu-16, Membrane-spanning 4-domains subfamily A member 1, CD20 (MS4A1)"
		};

		// Parse the JSON data
		const data = JSON.parse(JSON.stringify(jsonData));

		// Populate the table with data
		const tbody = document.querySelector('#data-table tbody');
		for (const key in data) {
			const tr = document.createElement('tr');
			const td1 = document.createElement('td');
			td1.textContent = key;
			const td2 = document.createElement('td');
			td2.textContent = data[key];
			tr.appendChild(td1);
			tr.appendChild(td2);
			tbody.appendChild(tr);
		}

		// Handle form submission
		const form = document.querySelector('#search-form');
		form.addEventListener('submit', function(event) {
			event.preventDefault();
			const searchKey = document.querySelector('#search-key').value;
			const filteredData = Object.keys(data)
				.filter(key => key.includes(searchKey))
				.reduce((obj, key) => {
					obj[key] = data[key];
					return obj;
				}, {});
			tbody.innerHTML = '';
			for (const key in filteredData) {
				const tr = document.createElement('tr');
				const td1 = document.createElement('td');
				td1.textContent = key;
				const td2 = document.createElement('td');
				td2.textContent = key;
				tr.appendChild(td1);
				tr.appendChild(td2);
				tbody.appendChild(tr);
		}
	</script>
</html>
