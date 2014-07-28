function expandAbbreviation()
{
	var profile_name = 'xhtml';
	var syntax = 'html';
    var abbr = this.selectedText();
	var content = zen_coding.expandAbbreviation(abbr, syntax, profile_name);

    this.replaceSelectedText(content);

}

function wrapWithAbbreviation()
{

    var profile_name = 'xhtml';
    var syntax = 'html';
    var text = this.selectedText();
    var abbr = this.getInputText();

    var content = zen_coding.wrapWithAbbreviation(abbr, text, syntax, profile_name);

    this.replaceSelectedText(content);
}


/* Somewhere: * /
window.settings = {
  /* [..] Other settings * /
  functionName: 'clickedOnItem'
  /* , [..] More settings * /
};

/* Later * /
function clickedOnItem (nodeId) {
  /* Some cool event handling code here * /
}

/* Even later * /
var fn = window[settings.functionName]; 
/* note that settings.functionName could also be written
   as window.settings.functionName. In this case, we use the fact that window
   is the implied scope of global variables. * /
if(typeof fn === 'function') {
    fn(t.parentNode.id);
}`	
*/
