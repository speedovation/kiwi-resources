#include <QPlainTextEdit>
#include <QDebug>
#include <QInputDialog>
#include <QLineEdit>

#include "globalfilehandler.h"

#include "Interface.h"
#include "JsBeautifyInterface.h"

using Flavours::JsBeautifyInterface;


JsBeautifyInterface::JsBeautifyInterface(): Interface()
{
//    QString scriptFileName();
//    scriptFileName = ;
//    scriptFileName = ;
    loadScriptFile(":/js/beautify_html.js");
    loadScriptFile(":/js/beautify_css.js");
    loadScriptFile(":/js/beautify_js.js");

}

void JsBeautifyInterface::test()
{
    qDebug() << currentEditor->toPlainText();
}

void JsBeautifyInterface::beautifyHtml()
{
    beautify("style_html");
}
void JsBeautifyInterface::beautifyCss()
{
    beautify("css_beautify");
}
void JsBeautifyInterface::beautifyJs()
{
    beautify("js_beautify");
}

void JsBeautifyInterface::beautify(QString functionName)
{

    QTextCursor tc = currentEditor->textCursor();

    if(!tc.hasSelection())
    {
        tc.select(QTextCursor::Document);
    }

    var text = tc.selectedText();

    var output = window[functionName](text)

    
    this.replaceSelectedText(output);

}



