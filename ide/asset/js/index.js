function getMethods(){
	var items;
	$.getJSON("../../settigs/methods.json", function(data){
		items = data.items
		$.each(data, function(key, val){
			console.log(key + ": " + val);
		});
	});
}
function init(){
	getMethods();
}