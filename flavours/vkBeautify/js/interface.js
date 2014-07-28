function beautify(mode,text) {

	var value;

		
	cp = cp.replace(/\'/g,'').replace(/\"/g,'');
	
	if ( !isNaN(parseInt(cp)) ) {  // argument is integer
		cp = parseInt(cp);
	} else {
		cp = cp ? cp : 4;
	}
	
	if(mode == 'XML') 
	{
		return vkbeautify.xml(text,cp);
	} else 
	if(mode == 'JSON') {
		return  vkbeautify.json(text,cp);
	} else 
	if(mode == 'CSS') {
		return  vkbeautify.css(text,cp);
	} 
	if(mode == 'SQL') {
		return  vkbeautify.sql(text,cp);
	} 

}

function minify(mode,text) {
	
	var preservecomm = document.getElementById('preservews').checked;
	
	if(mode == 'XML') {
		return preservecomm ? vkbeautify.xmlmin(text,true) : vkbeautify.xmlmin(text);
	} else 
	if(mode == 'JSON') {
		return  preservecomm ? vkbeautify.jsonmin(text) : vkbeautify.jsonmin(text);
	} else 
	if(mode == 'CSS') {
		return  preservecomm ? vkbeautify.cssmin(text,true) : vkbeautify.cssmin(text);
	}  else 
	if(mode == 'SQL') {
		return  vkbeautify.sqlmin(text);
	} 
	
}
