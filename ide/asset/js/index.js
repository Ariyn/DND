var methodnames = [];
var params = [];
//메써드 이름 가져오기 밑, ul아이템 추가
function getMethods(){
	var url = "\"./" + $("#method-text").val() + ".json\"";
	$.getJSON(url, function(data){
		var test =  function(data, func){
			$.each(data, function(keys, val){
				// console.log(key + ", " + val);
				if(typeof(keys)!="object" && typeof(keys)!="number"){
					methodnames.push(data);
					// console.log(keys);
					$("#methods-ul")
						.append(
							$("<li><a href=\"#\">"+ keys +"</a></li>")
							.click(function(){
								var liobj = findObjNameis(methodnames, $(this).text());
								var valarr = findValueAtKey(methodnames, $(this).text());
								for(var i in valarr){
									var pa = valarr[i];
									$("#param-ul").append(
										$("<li><a href=\"#\">"+ pa +"</a></li>")
										.click(function(){
											var intext = $("#param-input-text").val();
											console.log(intext);
										})
									);
								}
							})
						);

					// console.log(key);
				}
				if(typeof(val)=="object"){
					test(val, test);
				} else {
					params.push(val)
					// console.log("push: " + val);
				}
			});
		}
		for(var i in data){
			test(data[i], test);
			//변수 초기화.
			// methodnames.splice(0,methodnames.length);
			params.splice(0,params.length)
		}
	});
}
function findObjNameis(param, item){
	var rt = [];
	var keys = function(data, func){
		// console.log(data);
		$.each(data, function(key, val){
			// console.log(key);
			if(typeof(key)!="object" && typeof(key)!="number"){
				if (item == key){
					rt = data;
					// console.log(rt);
				}
				if(typeof(val)=="object"){
					keys(val, keys);
				}
			}
		});
	};
	for(var i in param){
		keys(param[i], keys);
	}
	return rt;
}
function findValueAtKey(param, item){
	var rt = [];
	var keys = function(data, func){
		// console.log(data);
		$.each(data, function(key, val){
			console.log(key);
			if(typeof(key)!="object" && typeof(key)!="number"){
				if (item == key){
					rt = data[key];
					// console.log(rt);
				}
				if(typeof(val)=="object"){
					keys(val, keys);
				}
			}
		});
	};
	for(var i in param){
		keys(param[i], keys);
	}
	return rt;
}
function testfunc(){
	$(".dropdown-menu a")
}
function urlis(){
	var g_AbsoluteUrl = document.URL.substring(document.domain.length + 12, document.URL.lastIndexOf("/") + 1);
	console.log(g_AbsoluteUrl);
}
function init(){
	getMethods();
	testfunc();
}